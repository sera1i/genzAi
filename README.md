# 💘 AI Wingman (The Rizz App)

**Your personal AI Copilot for dating, networking, and social survival.**

> *"Don't just text. Perform."*

This Python-based tool acts as a "Digital Wingman" for introverts. It sits quietly in the background, reads the text you copy to your clipboard, and uses Google's advanced **Gemini LLM** to generate the perfect reply instantly.

Whether you need a simple reply, a savage roast, or a long-term conversation strategy, the Wingman has your back.

---

## 📂 Project Versions

This repository contains three versions of the Wingman, each smarter than the last:

| Version | File Name | Description | Best For |
| :--- | :--- | :--- | :--- |
| **V1.0** | `wingman.py` | **The Basic Bot.** Single hotkey (`Alt+G`). Generates one generic "helpful" reply. | Testing if it works. Simple replies. |
| **V2.0** | `wingman_v2.py` | **The Mood Switcher.** Adds personas (Friendly, Flirty, Roast) via different hotkeys. | Dating apps, group chats, banter. |
| **V3.0** | `wingman_v3_memory.py` | **The Memory Master.** Remembers conversation history for context-aware replies. | **Deep conversations**, arguments, long chats. |

---

## 🚀 Features

* **Invisible Copilot:** Runs in the background; works on **WhatsApp Web, Instagram, Tinder, Discord, etc.**
* **Privacy First:** You control the send button. The AI only suggests; you choose to paste.
* **Powered by Gemini:** Uses Google's latest high-speed, creative AI models (`gemini-2.5-flash` / `gemini-1.5-flash`).
* **Context Awareness (V3 Only):** Remembers what *they* said 5 messages ago so you don't look like a goldfish.

---

## 🛠️ Prerequisites

* **Python 3.10+**
* **Google Gemini API Key** (Get it free at [Google AI Studio](https://aistudio.google.com/))
* **OS:** Windows 10/11 (Recommended) or Linux/Mac (Requires `sudo`)

---

## 📦 Installation

1.  **Clone or Download this repository** to your local machine.

2.  **Create a Virtual Environment** (Keeps your PC clean):
    ```powershell
    # Windows PowerShell
    python -m venv venv_win
    .\venv_win\Scripts\activate
    ```
    *(If you get a permission error, run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*

3.  **Install Dependencies:**
    ```bash
    pip install google-genai pyperclip keyboard colorama
    ```

4.  **Add Your API Key:**
    Open the python files (`wingman_v3_memory.py`, etc.) and paste your key into the `API_KEY` variable:
    ```python
    API_KEY = "AIzaSyD......"
    ```

---

## 🎮 How to Use (Controls)

Run the version you want to use. **Note:** On Windows, run your terminal as **Administrator** so the hotkeys work inside apps like Chrome/WhatsApp.

### **Run Command:**
```powershell
python wingman_v3_memory.py