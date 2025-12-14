
# 🧞 genzAi: The AI Wingman

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![API](https://img.shields.io/badge/Powered%20By-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> **"Don't just text. Perform."**

**genzAi** is a Python-based "Digital Copilot" designed for introverts, dating app warriors, and anyone who runs out of things to say. It sits quietly in the background, reads the text you copy to your clipboard, and uses **Google's Gemini LLM** to generate the perfect reply instantly.

Whether you need to be charming, savage, or just friendly, genzAi has a mode for it.

---

## 📂 Project Structure

This repository contains the evolution of the Wingman bot. You can use whichever version suits your needs:

| File Name | Version | Description | Best For |
| :--- | :--- | :--- | :--- |
| `wingman.py` | **V1.0 (Basic)** | Single hotkey (`Alt+G`). Generates one generic "helpful" reply. | Quick testing. |
| `wingman_v2.py` | **V2.0 (Moods)** | Adds **Personas** (Friendly, Flirty, Roast) via specific hotkeys. | Dating apps, group chats. |
| `wingman_v3_memory.py` | **V3.0 (Memory)** | **The Ultimate Version.** Remembers conversation history for context-aware replies. | **Deep conversations**, long chats. |

---

## 🚀 Features

* **👻 Invisible Integration:** Works on **any** platform (WhatsApp Web, Instagram, Discord, Tinder, etc.) because it uses the system clipboard.
* **🧠 Context Memory (V3):** Remembers what was said 5 messages ago, so you don't repeat yourself.
* **🎭 Three Distinct Vibes:**
    * **Friendly (Alt+1):** Chill, low-pressure, "best friend" energy.
    * **Flirty (Alt+2):** Confident, charming "Rizz" lines.
    * **Roast (Alt+3):** Witty comebacks for when you need to clap back.
* **⚡ Powered by Gemini:** Uses Google's latest `gemini-1.5-flash` or `gemini-2.5-flash` models for speed and creativity.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
* Python 3.10 or higher installed.
* A Google Cloud Project or AI Studio account with a **Gemini API Key** (Get it free [here](https://aistudio.google.com/)).

### 2. Clone the Repository
```bash
git clone [https://github.com/sera1i/genzAi.git](https://github.com/sera1i/genzAi.git)
cd genzAi
````

### 3\. Create a Virtual Environment (Recommended)

This keeps your system clean.

```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

*(Windows Note: If you get a "Scripts is disabled" error, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

### 4\. Install Dependencies

```bash
pip install google-genai pyperclip keyboard colorama
```

### 5\. Configure API Key

Open `wingman_v3_memory.py` (or the version you want to use) in your code editor.
Find the line:

```python
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
```

Replace the text inside the quotes with your actual API key.

-----

## 🎮 How to Use

**IMPORTANT:** On Windows, you must run your terminal/CMD as **Administrator**. This is required for the script to detect hotkeys while you are using other apps (like Chrome).

1.  **Run the script:**
    ```powershell
    python wingman_v3_memory.py
    ```
2.  **Go to your chat app** (e.g., WhatsApp Web).
3.  **Highlight** the message you just received.
4.  **Copy it** (`Ctrl + C`).
5.  **Press a Trigger Key:**

| Key Combo | Mode | Description |
| :--- | :--- | :--- |
| **`ALT + 1`** | **Friendly** | Casual replies. Good for friends/family. |
| **`ALT + 2`** | **Flirty** | The "Rizz" button. Bold and charming. |
| **`ALT + 3`** | **Roast** | Funny, slightly savage comebacks. |
| **`ALT + 0`** | **RESET** | **Wipes Memory.** Use this when switching to a new person\! |

6.  **Paste** (`Ctrl + V`) the reply and send\!

-----

## ❓ Troubleshooting

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| **Script ignores hotkeys** | Windows Security | Run Terminal/VS Code as **Administrator**. |
| **`429 RESOURCE_EXHAUSTED`** | API Limit | Switch `MODEL_ID` in code to `gemini-1.5-flash`. |
| **`404 NOT_FOUND`** | Wrong Model Name | Run `python check_models.py` to see available models. |
| **Clipboard Error** | Linux Missing Libs | Install xclip (`sudo apt install xclip`). |

-----

## ⚠️ Disclaimer

This tool is for educational and entertainment purposes only. The AI generates text based on patterns and does not have real feelings.

  * **Always read the reply before sending.**
  * The developer is not responsible if the bot accidentally ruins your relationship or starts a text war. 🤷‍♂️

-----

## 🤝 Contributing

Got an idea to make it smarter?

1.  Fork the repo.
2.  Create a feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.

-----

### **Connect**

Created by [Sera1i](https://github.com/sera1i)

```
```