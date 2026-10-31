# Growfinix Task 1 — AI Visual Prompt Studio

## Overview
A Python desktop application that constructs detailed prompts for:
- Professional DSLR portraits
- Cinematic promotional posters

Users can customize the subject, setting, lighting, camera angle/composition, and visual style. The app generates a structured prompt, copies it to the clipboard, saves it as a text file, and opens a free SDXL demo.

## Technology
- Python 3
- Tkinter (included with most standard Python installations)
- No paid API key required

## Run
1. Install Python 3 from https://www.python.org/downloads/
2. Save `prompt_studio.py`.
3. Run in Command Prompt:
   ```bash
   python prompt_studio.py
   ```
4. Choose settings and click **Generate Prompt**.
5. Click **Copy Prompt**, open the SDXL demo, paste the prompt, and generate the image.

## Important implementation note
This application performs prompt construction locally. The linked SDXL demo performs the actual image generation. The project does not claim to run an image-generation model locally or call a paid API.

## Suggested demonstration
1. Open the Python app.
2. Select Professional DSLR Portrait and generate a prompt.
3. Change lighting or camera angle and generate a second prompt.
4. Select Cinematic Promotional Poster and generate another prompt.
5. Copy one prompt and demonstrate image generation in the SDXL demo.
6. Show the saved prompt text file.

## Project files
- `prompt_studio.py` — application source code
- `README.md` — project documentation
