
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import asyncio
import edge_tts
import os
import subprocess
import sys

async def generate_speech(text, voice, filename):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def create_audio():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    voice = voice_box.get()
    filename = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 Audio", "*.mp3")],
        initialfile="generated_speech.mp3"
    )

    if not filename:
        return

    try:
        asyncio.run(generate_speech(text, voice, filename))
        messagebox.showinfo("Success", "Speech generated successfully!")
        if sys.platform == "win32":
            os.startfile(filename)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", filename])
        else:
            subprocess.Popen(["xdg-open", filename])
    except Exception as error:
        messagebox.showerror("Error", str(error))

root = tk.Tk()
root.title("Growfinix AI Text-to-Speech")
root.geometry("600x450")

tk.Label(
    root, text="AI Text-to-Speech Generator",
    font=("Arial", 20, "bold")
).pack(pady=15)

tk.Label(root, text="Enter your text:").pack()

text_box = tk.Text(root, height=10, width=65)
text_box.pack(pady=10)

tk.Label(root, text="Select Voice:").pack()

voice_box = ttk.Combobox(
    root,
    values=[
        "en-US-AriaNeural",
        "en-US-GuyNeural",
        "en-GB-SoniaNeural",
        "en-IN-NeerjaNeural",
        "en-IN-PrabhatNeural"
    ],
    state="readonly",
    width=35
)
voice_box.set("en-US-AriaNeural")
voice_box.pack(pady=10)

tk.Button(
    root,
    text="Generate Speech",
    command=create_audio,
    bg="#2878D0",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=20)

root.mainloop()
