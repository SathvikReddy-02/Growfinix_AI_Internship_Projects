import os
import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
from dotenv import load_dotenv
from groq import Groq

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

def extract_data():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    if not API_KEY:
        messagebox.showerror(
            "API Error",
            "API key not found. Please check your .env file."
        )
        return

    extract_button.config(state=tk.DISABLED, text="Extracting...")
    root.update()

    try:
        client = Groq(api_key=API_KEY)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract important information from the user's text. "
                        "Return valid JSON only. Use suitable keys such as "
                        "name, age, email, phone, city, profession and date. "
                        "Include only information present in the text. "
                        "Use null for missing values."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.2
        )

        result = response.choices[0].message.content
        data = json.loads(result)

        output_box.delete("1.0", tk.END)
        output_box.insert(
            tk.END,
            json.dumps(data, indent=4, ensure_ascii=False)
        )

    except Exception as error:
        messagebox.showerror("Error", str(error))

    finally:
        extract_button.config(state=tk.NORMAL, text="Extract Data")

# Main application window
root = tk.Tk()
root.title("Growfinix AI - Data Extraction")
root.geometry("750x650")
root.configure(bg="#f0f4f8")

# Heading
heading = tk.Label(
    root,
    text="AI-Powered Data Extraction",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#17365D"
)
heading.pack(pady=15)

# Input label
tk.Label(
    root,
    text="Enter Unstructured Text:",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
).pack(anchor="w", padx=25)

# Input area
input_box = scrolledtext.ScrolledText(
    root,
    height=9,
    font=("Arial", 11),
    wrap=tk.WORD
)
input_box.pack(fill="x", padx=25, pady=10)

# Example text
input_box.insert(
    tk.END,
    "John Smith is 22 years old. He lives in Hyderabad. "
    "His email is john@gmail.com and he works as a software engineer."
)

# Extract button
extract_button = tk.Button(
    root,
    text="Extract Data",
    command=extract_data,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=8
)
extract_button.pack(pady=12)

# Output label
tk.Label(
    root,
    text="Extracted JSON Output:",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
).pack(anchor="w", padx=25)

# Output area
output_box = scrolledtext.ScrolledText(
    root,
    height=12,
    font=("Consolas", 11),
    wrap=tk.WORD
)
output_box.pack(fill="both", expand=True, padx=25, pady=10)

# Run application
root.mainloop()