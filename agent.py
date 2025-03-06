# Standard library imports
import os
import time
from typing import List, Dict, Callable, Tuple
import logging

# Third-party imports
from flask import Flask, render_template, request, jsonify
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv
from azure.identity import AzureCliCredential

# Local application imports
from llm_interface import LLMInterface
from memory import Memory

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Agent class definition
class Agent:
    def __init__(self, llm: LLMInterface, memory: Memory):
        self.llm = llm
        self.memory = memory

    def run(self, input: str) -> str:
        # 1. Add input to memory
        self.memory.add(f"User: {input}")

        # 2. Construct prompt for LLM
        prompt = self.construct_prompt()

        # 3. Get LLM response
        llm_response = self.llm.generate_response(prompt)

        # 4. Add LLM response to memory
        self.memory.add(f"Agent: {llm_response}")

        # 5. Return the response directly (no tools to execute)
        return llm_response

    def construct_prompt(self) -> str:
        # Simplified prompt without tools
        prompt = "Here is your memory:\n"
        prompt += self.memory.get_memory() + "\n"
        prompt += "Respond with either:\n"
        prompt += "1. a question to guide the user to think by himself.\n"
        prompt += "2. a direct answer to the user.\n"
        prompt += "What do you do?"
        return prompt

# OpenAI LLM implementation
class OpenAILLM(LLMInterface):
    def __init__(self, model="gpt-4o"):
        self.model = model
        # Setup Azure OpenAI with AAD authentication
        # Create Azure CLI credential
        cli_credential = AzureCliCredential()
        
        # Initialize the AzureOpenAI client with proper configuration
        self.client = AzureOpenAI(
            api_version='2023-05-15',
            api_key=cli_credential.get_token("https://cognitiveservices.azure.com/.default").token,
            azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT')
        )

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful AI psychological counselor that guides the user to think."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,  # Increase token limit
                temperature=0.7,
                stop=["\n\n"]  # Prevent truncation in the middle of paragraphs
            )
            
            content = response.choices[0].message.content.strip()
            
            # Check if the response might be truncated (by checking if the last sentence is complete)
            if content and not content[-1] in {'.', '?', '!', '。', '？', '！'}:
                # If potentially truncated, add a notice
                content += " [...Response may be incomplete, try shortening your input...]"
                
            return content
            
        except Exception as e:
            # Handle potential API errors
            error_msg = f"Error generating response: {str(e)}"
            print(error_msg)  # Log the error
            return "I apologize, but I cannot provide a complete response at the moment. Please try again later or rephrase your question."

# Simple in-memory implementation
class SimpleMemory(Memory):
    def __init__(self):
        self.memory = []

    def add(self, item: str):
        self.memory.append(item)

    def get_memory(self) -> str:
        return "\n".join(self.memory)
        
    def clear(self):
        self.memory = []

# Flask app
app = Flask(__name__)

# Initialize agent components and create agent
llm = OpenAILLM()
memory = SimpleMemory()
agent = Agent(llm, memory)  # No tools parameter needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    start_time = time.time()
    logger.info("Request started")
    
    user_input = request.json.get('message')
    # Use the agent to process the user's message
    response = agent.run(user_input)
    
    # Return the full conversation history
    result = jsonify({
        'response': response,
        'history': memory.get_memory().split('\n')
    })
    
    logger.info("Request ended")
    logger.info(f"Request duration: {time.time() - start_time} seconds")
    
    return result

@app.route('/history', methods=['GET'])
def history():
    start_time = time.time()
    logger.info("History request started")
    
    # Return the current conversation history
    messages = []
    history = memory.get_memory().split('\n')
    
    for item in history:
        if item.startswith('User: '):
            messages.append({
                'text': item[6:],
                'sender': 'user'
            })
        elif item.startswith('Agent: '):
            messages.append({
                'text': item[7:],
                'sender': 'agent'
            })
    
    result = jsonify({'messages': messages})
    
    logger.info("History request ended")
    logger.info(f"History request duration: {time.time() - start_time} seconds")
    
    return result

@app.route('/new_chat', methods=['POST'])
def new_chat():
    start_time = time.time()
    logger.info("New chat request started")
    
    # Clear the memory
    memory.clear()
    
    logger.info("New chat request ended")
    logger.info(f"New chat request duration: {time.time() - start_time} seconds")
    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
