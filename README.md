# 🧞 genzAi: The AI Wingman (V4)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![API](https://img.shields.io/badge/Powered%20By-Google%20Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> **"Don't just text. Perform."**

**genzAi** is a desktop-based "Digital Wingman" that functions as a universal, context-aware chat assistant for any messaging platform (WhatsApp, Instagram, Tinder) without requiring risky direct API integrations. By monitoring the system clipboard and listening for global hotkeys (`Alt+1/2/3`), the tool instantly sends incoming text to Google’s **Gemini 1.5 Flash** model. It uses a sliding memory buffer of conversation history to generate brief, relevant replies tailored to specific social vibes (Friendly, Flirty, or Roast), bridging the gap between social anxiety and effortless communication.

---

## 📂 Project Evolution

This repository contains the evolution of the Wingman bot. The latest version (**V4**) combines all previous features into a stable release.

| Version | Description | Key Features |
| :--- | :--- | :--- |
| **V1.0** | Basic Bot | Single hotkey, one generic reply style. |
| **V2.0** | The Mood Switcher | Added **Personas** (Friendly, Flirty, Roast) via specific hotkeys. |
| **V3.0** | Memory Master | Added **Conversation History** so the bot understands context. |
| **V4.0** | **The Stabilizer** | Added **Anti-Dry Logic** (detects boring texts), **Auto-Retry** for API limits, and **Model Fallback**. |

---

## 🚀 Key Features (V4)

* **👻 Invisible & Universal:** Works on **WhatsApp Web, Instagram, Tinder, Discord, Slack**—anywhere you can copy text.
* **🧠 Context Memory:** Remembers the last 4 messages so you don't repeat yourself or lose the thread of the conversation.
* **🌵 Anti-Dry Logic:** Automatically detects low-effort messages (e.g., "k", "lol", "nice") and switches to a "Don't Chase" strategy to maintain your status.
* **🛡️ Auto-Fallback System:** If one AI model is busy or hits a rate limit, it automatically waits and retries, or switches to a backup model.
* **🎭 Three Distinct Vibes:**
    * **Friendly (`Alt+1`):** Chill, low-pressure, "best friend" energy.
    * **Flirty (`Alt+2`):** Confident, charming, and subtle. (No cringey pickup lines).
    * **Roast (`Alt+3`):** Witty, playful banter.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
* **Python 3.10** or higher.
* A Google Cloud Project or AI Studio account with a **Gemini API Key** (Get it free [here](https://aistudio.google.com/)).

### 2. Clone the Repository
```bash
git clone [https://github.com/sera1i/genzAi.git](https://github.com/sera1i/genzAi.git)
cd genzAi
````

### 3\. Create a Virtual Environment (Recommended)

This keeps your system clean and prevents conflicts.

```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4\. Install Dependencies

```bash
pip install google-generativeai pyperclip keyboard colorama
```

### 5\. Configure Your API Key

Open `wingman_v4.py` (or your main script) in a text editor and paste your key:

```python
# Inside the script
API_KEY = "AIzaSy......" 
```

-----

## 🎮 How to Use

**Note:** On Windows, you **must** run your terminal/CMD as **Administrator**. This is required for the script to detect hotkeys while you are using other apps (like Chrome or Discord).

1.  **Run the script:**
    ```powershell
    python wingman_v4.py
    ```
2.  **Go to your chat app** (e.g., WhatsApp Web).
3.  **Highlight** the message you just received.
4.  **Copy it** (`Ctrl + C`).
5.  **Press a Trigger Key:**

| Key Combo | Mode | Description |
| :--- | :--- | :--- |
| **`ALT + 1`** | **Friendly** | Casual replies. Good for friends/family. |
| **`ALT + 2`** | **Flirty** | The "Rizz" button. Smooth and confident. |
| **`ALT + 3`** | **Roast** | Witty comebacks. Use with caution. |
| **`ALT + 0`** | **RESET** | **Wipes Memory.** Use this instantly when switching to a new person\! |

6.  **Paste** (`Ctrl + V`) the generated reply and send\!

-----

## ⚙️ Customization

You can customize the **System Prompts** inside the script to change the AI's personality. Look for the `MODES` dictionary in the code:

```python
MODES = {
    "flirty": """
    Reply with bold confidence. 
    Constraint: Keep it under 10 words. 
    Style: Use emojis.
    """
}
```

-----

## ❓ Troubleshooting

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| **Script ignores hotkeys** | Windows Security | Run Terminal/VS Code as **Administrator**. |
| **`429 RESOURCE_EXHAUSTED`** | API Limit | The script will auto-retry. If it fails often, get a new API key. |
| **`404 NOT_FOUND`** | Wrong Model Name | Ensure your `MODEL_LIST` uses the prefix `models/` (e.g., `models/gemini-flash-latest`). |
| **`400 INVALID_ARGUMENT`** | Bad Key | Your API Key is expired or deleted. Generate a new one at Google AI Studio. |

-----

## ⚠️ Disclaimer

This tool is for educational and entertainment purposes only. The AI generates text based on patterns and does not have real feelings or social awareness.

  * **Always read the reply before sending.**
  * The developer is not responsible if the bot accidentally ruins your relationship or starts a text war. 🤷‍♂️

-----

### **Connect**

Created by [Sera1i](https://github.com/sera1i)