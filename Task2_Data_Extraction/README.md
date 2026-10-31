\# Growfinix Task 2 — AI-Powered Data Extraction



\## Overview

A Python desktop application that uses AI to extract structured information from unstructured text and convert it into JSON format.



Users can enter plain-text information, and the application identifies important details and displays them in a structured JSON response.



\## Features

\- Extract information from unstructured text.

\- Identify names, age, city, profession, email and phone number.

\- Convert extracted information into JSON format.

\- Display the generated JSON in the application.

\- Simple graphical user interface.



\## Technologies Used

\- Python 3

\- Tkinter

\- Groq API

\- Groq Python SDK

\- Python-dotenv



\## Installation

Install the required packages:



```bash

pip install groq python-dotenv

```



\## Configuration

Create a `.env` file in the project folder and add your Groq API key:



```text

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



Never upload the actual `.env` file or API key to GitHub.



\## How to Run

Run the following command:



```bash

python data\_extractor.py

```



1\. Enter unstructured text.

2\. Click the extraction button.

3\. Wait for the AI response.

4\. View the extracted information in JSON format.



\## Project Files

\- `data\_extractor.py` — Main Python application.

\- `.env` — Private API configuration.

\- `.gitignore` — Excludes sensitive files.

\- `README.md` — Project information.



\## AI Model

The application uses the Groq API with the `openai/gpt-oss-20b` model to process text and generate structured JSON output.



\## Outcome

Successfully developed an AI-powered application that converts unstructured text into structured JSON data.



\*\*Organization:\*\* Growfinix Technology  

\*\*Task:\*\* AI-Powered Data Extraction



