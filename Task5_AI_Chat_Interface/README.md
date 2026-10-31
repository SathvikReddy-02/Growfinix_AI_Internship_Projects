\# Growfinix Task 5 — AI Chat Interface



\## Overview

A web-based AI chatbot application that allows users to communicate with an AI assistant through a simple and user-friendly chat interface.



The frontend sends user messages to a Python Flask backend, which communicates with the Groq API and returns AI-generated responses.



\## Features

\- Interactive chat interface.

\- Send messages and receive AI responses.

\- Real-time request handling.

\- Display user and assistant messages separately.

\- Loading indicator while waiting for responses.

\- Error handling for failed requests.



\## Technologies Used

\- HTML

\- CSS

\- JavaScript

\- Python 3

\- Flask

\- Flask-CORS

\- Groq API

\- Python-dotenv



\## Installation

Install the required packages:



```bash

pip install flask flask-cors groq python-dotenv

```



\## Configuration

Create a `.env` file in the project folder:



```text

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



Never upload your actual API key or `.env` file to GitHub.



\## How to Run



1\. Open the project folder in VS Code.

2\. Start the Flask backend:



```bash

python app.py

```



3\. Open `index.html` using VS Code Live Server.

4\. Enter a message in the chat box.

5\. Click Send to receive an AI-generated response.



\## AI Model

The backend uses the Groq API with the `openai/gpt-oss-20b` model to generate conversational responses.



\## Project Files

\- `index.html` — Chat interface structure.

\- `style.css` — Application styling.

\- `script.js` — Frontend interaction and API requests.

\- `app.py` — Flask backend and Groq API integration.

\- `.env` — Private API configuration.

\- `.gitignore` — Excludes sensitive files.



\## Outcome

Successfully developed a web-based AI chatbot with a frontend interface and Python backend integration.



\*\*Organization:\*\* Growfinix Technology  

\*\*Task:\*\* Frontend AI Chat Interface



