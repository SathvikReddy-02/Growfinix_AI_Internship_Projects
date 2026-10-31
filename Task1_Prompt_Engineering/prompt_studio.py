"""
Growfinix Internship - Task 1
AI-Based Advanced Prompt Engineering System
Python GUI built with Tkinter (standard library only).

This application constructs detailed prompts. Actual image generation is
performed by pasting the prompt into the linked free SDXL demo.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
from datetime import datetime

SDXL_URL = "https://huggingface.co/spaces/radames/Real-Time-Text-to-Image-SDXL-Lightning"


class PromptStudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Growfinix | AI Visual Prompt Studio")
        self.root.geometry("900x720")
        self.root.minsize(760, 620)
        self.root.configure(bg="#101729")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#17233b", foreground="#edf2ff",
                        font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("TCombobox", padding=6)
        style.configure("TLabelframe", background="#17233b",
                        foreground="#bcb5ff")
        style.configure("TLabelframe.Label", background="#17233b",
                        foreground="#bcb5ff", font=("Segoe UI", 11, "bold"))

        header = tk.Frame(root, bg="#101729", padx=24, pady=18)
        header.pack(fill="x")
        tk.Label(header, text="GROWFINIX • ARTIFICIAL INTELLIGENCE INTERNSHIP",
                 bg="#101729", fg="#9b91ff",
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        tk.Label(header, text="AI Visual Prompt Studio", bg="#101729",
                 fg="#ffffff", font=("Segoe UI", 23, "bold")).pack(anchor="w", pady=(5, 0))
        tk.Label(header, text="Build detailed prompts for realistic portraits and cinematic posters.",
                 bg="#101729", fg="#b8c4dc",
                 font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 0))

        body = tk.Frame(root, bg="#101729", padx=24, pady=8)
        body.pack(fill="both", expand=True)

        controls = ttk.LabelFrame(body, text=" 1. Prompt settings ", padding=14)
        controls.pack(fill="x")

        self.project = tk.StringVar(value="Professional DSLR Portrait")
        self.subject = tk.StringVar(value="a professional male fashion model wearing a black formal suit")
        self.setting = tk.StringVar(value="modern photography studio")
        self.lighting = tk.StringVar(value="cinematic soft lighting")
        self.angle = tk.StringVar(value="eye-level medium portrait shot")
        self.style = tk.StringVar(value="photorealistic professional photography")

        self.add_combo(controls, "Project type", self.project,
                       ["Professional DSLR Portrait", "Cinematic Promotional Poster"])
        self.add_entry(controls, "Subject / main idea", self.subject)
        self.add_combo(controls, "Background / setting", self.setting, [
            "modern photography studio", "urban city at night",
            "mountain landscape at golden hour", "minimal dark studio",
            "futuristic technology environment"
        ])
        self.add_combo(controls, "Lighting", self.lighting, [
            "cinematic soft lighting", "dramatic low-key lighting",
            "warm golden-hour lighting", "bright natural window lighting",
            "neon rim lighting"
        ])
        self.add_combo(controls, "Camera angle / composition", self.angle, [
            "eye-level medium portrait shot", "low-angle dramatic shot",
            "close-up head-and-shoulders shot", "wide cinematic composition",
            "three-quarter view"
        ])
        self.add_combo(controls, "Visual style", self.style, [
            "photorealistic professional photography",
            "premium luxury advertising aesthetic",
            "cinematic movie-poster aesthetic",
            "editorial fashion photography"
        ])

        button_row = tk.Frame(controls, bg="#17233b")
        button_row.pack(fill="x", pady=(12, 2))
        ttk.Button(button_row, text="Generate Prompt",
                   command=self.generate_prompt).pack(side="left", padx=(0, 8))
        ttk.Button(button_row, text="Reset",
                   command=self.reset).pack(side="left")

        output_frame = ttk.LabelFrame(body, text=" 2. Generated advanced prompt ", padding=12)
        output_frame.pack(fill="both", expand=True, pady=14)

        self.output = tk.Text(output_frame, height=8, wrap="word",
                              bg="#0b1221", fg="#e8edff", insertbackground="white",
                              relief="flat", padx=12, pady=12,
                              font=("Consolas", 10))
        self.output.pack(fill="both", expand=True)
        self.output.insert("1.0", "Click Generate Prompt to build your prompt.")

        actions = tk.Frame(output_frame, bg="#17233b")
        actions.pack(fill="x", pady=(10, 0))
        ttk.Button(actions, text="Copy Prompt", command=self.copy_prompt).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Save Prompt as TXT", command=self.save_prompt).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Open Free SDXL Demo", command=self.open_sdxl).pack(side="left")

        self.status = tk.StringVar(value="Ready. Choose settings and generate a prompt.")
        tk.Label(root, textvariable=self.status, bg="#101729", fg="#72ddc5",
                 anchor="w", padx=24, pady=10, font=("Segoe UI", 9)).pack(fill="x")

        self.generate_prompt()

    def add_combo(self, parent, label, variable, values):
        row = tk.Frame(parent, bg="#17233b")
        row.pack(fill="x", pady=4)
        tk.Label(row, text=label, width=25, anchor="w",
                 bg="#17233b", fg="#edf2ff",
                 font=("Segoe UI", 10)).pack(side="left")
        combo = ttk.Combobox(row, textvariable=variable, values=values,
                             state="readonly")
        combo.pack(side="left", fill="x", expand=True)

    def add_entry(self, parent, label, variable):
        row = tk.Frame(parent, bg="#17233b")
        row.pack(fill="x", pady=4)
        tk.Label(row, text=label, width=25, anchor="w",
                 bg="#17233b", fg="#edf2ff",
                 font=("Segoe UI", 10)).pack(side="left")
        entry = tk.Entry(row, textvariable=variable, bg="#243451",
                         fg="#ffffff", insertbackground="white",
                         relief="flat", font=("Segoe UI", 10))
        entry.pack(side="left", fill="x", expand=True, ipady=7)

    def generate_prompt(self):
        project = self.project.get()
        subject = self.subject.get().strip() or "a professional visual subject"
        setting = self.setting.get()
        lighting = self.lighting.get()
        angle = self.angle.get()
        visual_style = self.style.get()

        if project == "Professional DSLR Portrait":
            prompt = (
                f"{visual_style} of {subject}, in a {setting}, {lighting}, "
                f"{angle}, natural realistic skin texture, detailed facial features, "
                "85mm portrait lens look, f/1.8 shallow depth of field, softly "
                "blurred background, balanced composition, realistic colors, "
                "professional studio quality, high detail."
            )
        else:
            prompt = (
                f"{visual_style} featuring {subject}, set in a {setting}, "
                f"{lighting}, {angle}, striking focal point, dramatic atmosphere, "
                "rich visual textures, professional advertising art direction, "
                "balanced negative space for headline placement, crisp details, "
                "polished color grading, high-resolution finish."
            )

        self.output.delete("1.0", "end")
        self.output.insert("1.0", prompt)
        self.status.set("Prompt generated successfully. Copy it into the SDXL demo.")

    def get_prompt(self):
        return self.output.get("1.0", "end").strip()

    def copy_prompt(self):
        prompt = self.get_prompt()
        if not prompt:
            messagebox.showwarning("No prompt", "Generate a prompt first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(prompt)
        self.status.set("Prompt copied to clipboard.")

    def save_prompt(self):
        prompt = self.get_prompt()
        if not prompt:
            messagebox.showwarning("No prompt", "Generate a prompt first.")
            return
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="growfinix_advanced_prompt.txt",
            filetypes=[("Text files", "*.txt")]
        )
        if filename:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("Growfinix Task 1 - Advanced Prompt Engineering\n")
                file.write(f"Created: {datetime.now():%Y-%m-%d %H:%M}\n\n")
                file.write(prompt + "\n")
            self.status.set("Prompt saved successfully.")

    def open_sdxl(self):
        webbrowser.open(SDXL_URL)
        self.status.set("Opened the SDXL demo in your browser. Paste the copied prompt there.")

    def reset(self):
        self.project.set("Professional DSLR Portrait")
        self.subject.set("a professional male fashion model wearing a black formal suit")
        self.setting.set("modern photography studio")
        self.lighting.set("cinematic soft lighting")
        self.angle.set("eye-level medium portrait shot")
        self.style.set("photorealistic professional photography")
        self.generate_prompt()
        self.status.set("Settings reset.")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = PromptStudio(app_root)
    app_root.mainloop()
