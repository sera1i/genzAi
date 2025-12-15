import time
import pyperclip
import keyboard
import sys
import google.generativeai as genai
from colorama import Fore, Style, init

init(autoreset=True)

# ==================================================
# 🔐 CONFIGURATION
# ==================================================
API_KEY = "enter_your_api_key_here"

# Configure Gemini
genai.configure(api_key=API_KEY)

# ✅ Correct models (from your scan)
MODEL_LIST = [
    "models/gemini-2.5-flash",
    "models/gemini-flash-latest",
    "models/gemini-2.0-flash-lite",
    "models/gemini-pro-latest"
]

chat_history = []

# ==================================================
# 🧠 MASTER SYSTEM PROMPT
# ==================================================
MASTER_SYSTEM = """
You are helping a real human reply to a real chat.

Rules:
- Never sound like AI
- Never explain yourself
- Never give advice
- Never overtalk
- Match the other person’s tone and effort
- If interest is low, do not chase
- Replies should feel effortless and natural
"""

# ==================================================
# 🎭 MODES
# ==================================================
MODES = {
    "friendly": """
Reply like a chill, socially comfortable friend.
- Casual everyday texting
- Lowercase is fine
- No forced jokes
- 1 short sentence
""",

    "flirty": """
Reply with subtle, confident attraction.
- Flirting should feel accidental
- No pickup lines
- No sexual words
- No emojis
- Exactly 1 sentence
""",

    "roast": """
Reply with dry, playful wit.
- Friendly roast only
- No insults
- No emojis
- 1 short line
"""
}

# ==================================================
# 🧪 HELPERS
# ==================================================
def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(
            f"\r{Fore.YELLOW}[!] Cooling down... {i}s {Style.RESET_ALL}"
        )
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r" + " " * 50 + "\r")

def is_dry(msg):
    msg = msg.strip().lower()
    return len(msg) <= 4 or msg in [
        "hmm", "ok", "okay", "lol", "nice", "k"
    ]

BAD_PATTERNS = [
    "haha that's interesting",
    "sounds fun",
    "i think",
    "absolutely",
    "that's cool",
    "to be honest"
]

# ==================================================
# 🧠 CORE LOGIC
# ==================================================
def get_reply(incoming_text, mode):
    global chat_history

    # Build short memory (last 4 turns)
    context_str = ""
    for msg in chat_history[-4:]:
        role = "Them" if msg["role"] == "user" else "You"
        context_str += f"{role}: {msg['text']}\n"

    dry_hint = ""
    if is_dry(incoming_text):
        dry_hint = """
The incoming message is dry or low-effort.
Do NOT chase.
Keep reply neutral or lightly disengaged.
"""

    full_prompt = f"""
{MASTER_SYSTEM}

STYLE:
{MODES[mode]}

RECENT CHAT:
{context_str}

INCOMING MESSAGE:
"{incoming_text}"

{dry_hint}

Reply naturally like a real human would text.
"""

    for model_id in MODEL_LIST:
        for attempt in range(1, 3):
            try:
                model = genai.GenerativeModel(model_id)
                response = model.generate_content(full_prompt)

                reply = response.text.strip()
                reply = reply.replace('"', "").replace("'", "")
                reply = reply.replace("!!", "!").replace("??", "?")

                for bp in BAD_PATTERNS:
                    reply = reply.replace(bp, "")

                # Save memory
                chat_history.append({"role": "user", "text": incoming_text})
                chat_history.append({"role": "model", "text": reply})

                print(Fore.GREEN + f"[+] Success ({model_id})")
                return reply

            except Exception as e:
                err = str(e)

                if "429" in err or "RESOURCE_EXHAUSTED" in err:
                    countdown(attempt * 5)
                    continue
                else:
                    break

    return "Error: All models failed."

# ==================================================
# 🚀 MAIN LOOP
# ==================================================
def main():
    print(Fore.GREEN + "=== WINGMAN (GEMINI 2.5 STABLE) ===")
    print(Fore.YELLOW + f"Models Loaded: {len(MODEL_LIST)}")
    print("Copy text → Alt+1 Friend | Alt+2 Flirty | Alt+3 Roast")
    print("Alt+0 Clear Memory | Esc Exit\n")

    while True:
        try:
            mode = None

            if keyboard.is_pressed("alt+1"):
                mode = "friendly"
            elif keyboard.is_pressed("alt+2"):
                mode = "flirty"
            elif keyboard.is_pressed("alt+3"):
                mode = "roast"

            if keyboard.is_pressed("alt+0"):
                chat_history.clear()
                print(Fore.YELLOW + "\n[!] MEMORY CLEARED\n")
                time.sleep(1)
                continue

            if mode:
                incoming_msg = pyperclip.paste()

                if not incoming_msg:
                    print(Fore.RED + "Clipboard empty!")
                else:
                    print(f"\nInput: {incoming_msg}")
                    reply = get_reply(incoming_msg, mode)

                    # Typing realism delay
                    time.sleep(min(len(reply) * 0.05, 1.2))

                    pyperclip.copy(reply)
                    print(Fore.YELLOW + f"Reply: {reply}")
                    print(Fore.GREEN + ">> Copied to clipboard <<")

                time.sleep(2)

            if keyboard.is_pressed("esc"):
                break

            time.sleep(0.05)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
