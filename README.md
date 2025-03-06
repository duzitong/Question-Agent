# Question Agent

A conversational AI agent built with Flask and Azure OpenAI designed to guide users through their thought process rather than simply providing answers.

## Purpose

Question Agent is designed as a psychological counselor that encourages critical thinking by asking guiding questions rather than providing immediate answers. The agent uses conversational techniques to help users:

- Develop their own problem-solving skills
- Explore their thoughts more deeply
- Reach conclusions through guided self-reflection
- Build independent thinking capabilities

## Overview

Question Agent is a web application that creates an interactive chat interface where users can engage with an AI assistant. The agent is designed to:

1. Maintain conversation history
2. Process user inputs
3. Generate contextually relevant responses
4. Provide guiding questions that lead users toward their own insights

## Use Cases

Question Agent can be particularly valuable in several scenarios:

### Personal Growth & Self-Reflection
- Working through personal decisions or dilemmas
- Exploring career choices and professional development
- Understanding emotional responses to situations
- Developing better self-awareness

### Learning & Education
- Breaking down complex problems into manageable steps
- Developing critical thinking skills
- Exploring different perspectives on academic topics
- Strengthening analytical reasoning

### Problem-Solving
- Analyzing business challenges
- Working through technical issues
- Developing project strategies
- Evaluating different solution approaches

### Professional Development
- Preparing for important conversations or presentations
- Developing leadership skills
- Improving decision-making processes
- Enhancing communication strategies

The agent achieves these by:
- Asking open-ended questions that promote deeper thinking
- Encouraging users to examine assumptions
- Helping users identify patterns in their thinking
- Guiding users to develop their own solutions

## Architecture

The application follows a modular design with the following components:

- `agent.py`: Main agent implementation and Flask web server
- `llm_interface.py`: Abstract interface for language model interactions
- `memory.py`: Abstract interface for memory storage
- `templates/index.html`: Frontend chat interface

## Installation

### Prerequisites

- Python 3.6+
- Azure OpenAI API access
- Azure CLI configured with appropriate permissions

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/question-agent.git
   cd question-agent
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables by creating a `.env` file:
   ```
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   ```

## Usage

1. Start the Flask application:
   ```
   python agent.py
   ```

2. Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Begin interacting with the Question Agent through the chat interface.

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
