\# Growfinix Task 3 — Semantic Sentiment and Urgency Analyzer



\## Overview

A Python desktop application that analyzes text and identifies its sentiment and urgency level.



The application uses a pretrained Hugging Face sentiment-analysis model to classify text as positive or negative. It also applies keyword-based rules to estimate urgency.



\## Features

\- Analyze user-entered text.

\- Identify positive and negative sentiment.

\- Estimate urgency as High, Medium or Low.

\- Display analysis results through a graphical interface.

\- Provide confidence scores from the sentiment model.



\## Technologies Used

\- Python 3

\- Tkinter

\- Hugging Face Transformers

\- PyTorch

\- DistilBERT sentiment-analysis model



\## Installation

Install the required packages:



```bash

pip install transformers torch

```



\## How to Run

Run the following command:



```bash

python sentiment\_analyzer.py

```



1\. Open the application.

2\. Enter a sentence or message.

3\. Click the Analyze button.

4\. View the sentiment and urgency results.



\## AI Model

The application uses the pretrained model:



`distilbert/distilbert-base-uncased-finetuned-sst-2-english`



The model performs sentiment classification locally after downloading the required model files.



\## Implementation Note

Sentiment classification is performed using the Hugging Face model locally, not through the Hugging Face Inference API. Urgency estimation is based on predefined keyword rules, rather than a separate AI urgency model. Emotion labels are derived using simple application logic.



\## Outcome

Successfully developed a text-analysis application that combines pretrained AI sentiment classification with rule-based urgency estimation.



\*\*Organization:\*\* Growfinix Technology  

\*\*Task:\*\* Semantic Sentiment and Urgency Analyzer



