import tkinter as tk
from tkinter import messagebox, scrolledtext
from transformers import pipeline

# Load local AI sentiment model
analyzer = None

def load_model():
    global analyzer
    status_label.config(text="Loading AI model... Please wait")
    root.update()

    try:
        analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        )
        status_label.config(text="AI Model Ready!")
        analyze_button.config(state=tk.NORMAL)

    except Exception as error:
        status_label.config(text="Model loading failed")
        messagebox.showerror("Model Error", str(error))

def analyze_message():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Enter a message!")
        return

    try:
        result = analyzer(text[:512])[0]

        if result["label"] == "POSITIVE":
            sentiment = "Positive"
            emotion = "Happy / Satisfied"
        else:
            sentiment = "Negative"
            emotion = "Frustrated / Unhappy"

        words = [
            "immediately", "urgent", "emergency",
            "asap", "critical", "right now"
        ]

        medium_words = [
            "soon", "quickly", "today",
            "important", "waiting", "delay"
        ]

        lower_text = text.lower()

        if any(word in lower_text for word in words):
            urgency = "High"
        elif any(word in lower_text for word in medium_words):
            urgency = "Medium"
        else:
            urgency = "Low"

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "ANALYSIS RESULTS\n")
        output_box.insert(tk.END, "-" * 35 + "\n\n")
        output_box.insert(tk.END, f"Sentiment: {sentiment}\n")
        output_box.insert(tk.END, f"Urgency: {urgency}\n")
        output_box.insert(tk.END, f"Emotion: {emotion}\n")
        output_box.insert(
            tk.END,
            f"Confidence: {result['score'] * 100:.2f}%\n"
        )

    except Exception as error:
        messagebox.showerror("Analysis Error", str(error))

# Create application window
root = tk.Tk()
root.title("Growfinix AI - Sentiment & Urgency Analyzer")
root.geometry("750x620")
root.configure(bg="#f0f4f8")

heading = tk.Label(
    root,
    text="Semantic Sentiment & Urgency Analyzer",
    font=("Arial", 19, "bold"),
    bg="#f0f4f8",
    fg="#17365D"
)
heading.pack(pady=20)

tk.Label(
    root,
    text="Enter Your Message:",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
).pack(anchor="w", padx=25)

input_box = scrolledtext.ScrolledText(
    root, height=9, font=("Arial", 11), wrap=tk.WORD
)
input_box.pack(fill="x", padx=25, pady=10)

input_box.insert(
    tk.END,
    "I have been waiting for my order for 10 days. "
    "Please resolve this immediately!"
)

analyze_button = tk.Button(
    root,
    text="Analyze Message",
    command=analyze_message,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=8,
    state=tk.DISABLED
)
analyze_button.pack(pady=15)

tk.Label(
    root,
    text="Analysis Output:",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
).pack(anchor="w", padx=25)

output_box = scrolledtext.ScrolledText(
    root, height=10, font=("Consolas", 12), wrap=tk.WORD
)
output_box.pack(fill="both", expand=True, padx=25, pady=10)

status_label = tk.Label(
    root,
    text="Preparing AI model...",
    font=("Arial", 10),
    bg="#f0f4f8"
)
status_label.pack(pady=5)

# Load the model after creating the interface
root.after(100, load_model)

root.mainloop()