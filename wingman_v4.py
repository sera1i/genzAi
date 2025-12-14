import time
import pyperclip
import keyboard
from google import genai
from google.genai import types
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# --- CONFIGURATION ---
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

# --- FALLBACK LIST (Priority Order) ---
# It tries the first one. If it fails (quota limit), it tries the second, etc.
MODEL_LIST = [
    "gemini-1.5-flash",          # Best balance (High Rate Limit)
    "gemini-2.0-flash-exp",      # Newest/Smartest (Low Rate Limit)
    "gemini-1.5-pro",            # Smarter but slower
    "gemini-1.5-flash-8b"        # Tiny/Fast backup
]

client = genai.Client(api_key=API_KEY)

# --- MEMORY STORAGE ---
chat_history = []

# --- PERSONAS ---
MODES = {
    "friendly": "Role: Chill friend. Style: Lowercase, slang. Constraint: Under 10 words.",
    "flirty": "Role: Rizz Master. Style: Smooth, confident. Constraint: Under 15 words. One sentence.",
    "roast": "Role: Witty Roaster. Style: Savage, dry humor. Constraint: Under 12 words."
}

def get_reply(incoming_text, mode):
    global chat_history
    
    # Context Builder (Last 4 messages)
    context_str = ""
    recent_history = chat_history[-4:] 
    for msg in recent_history:
        role = "Them" if msg['role'] == "user" else "You"
        context_str += f"{role}: {msg['text']}\n"
    
    full_prompt = f"""
    SYSTEM: {MODES[mode]}
    HISTORY:
    {context_str}
    TARGET MESSAGE:
    Them: {incoming_text}
    YOUR REPLY:
    """

    # --- FALLBACK LOGIC ---
    for model_id in MODEL_LIST:
        try:
            print(Fore.CYAN + f"[+] Trying model: {model_id}..." + Style.RESET_ALL)
            
            response = client.models.generate_content(
                model=model_id,
                contents=full_prompt
            )
            
            reply_text = response.text.strip().replace('"', '').replace("'", "")
            
            # Update Memory
            chat_history.append({"role": "user", "text": incoming_text})
            chat_history.append({"role": "model", "text": reply_text})
            
            return reply_text # Success! Return immediately.
            
        except Exception as e:
            # Check if it is a Quota/Resource error
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(Fore.RED + f"[-] {model_id} LIMIT REACHED. Switching..." + Style.RESET_ALL)
                continue # Try the next model in the list
            else:
                # If it's a different error (like bad API key), stop trying
                return f"Critical Error: {e}"
    
    return "Error: All models exhausted."

def main():
    print(Fore.GREEN + "=== WINGMAN V4.0 (AUTO-FALLBACK) ===" + Style.RESET_ALL)
    print(Fore.YELLOW + f"Active Models: {len(MODEL_LIST)} available")
    print("1. Copy text (Ctrl+C)")
    print("2. Use Hotkeys: Alt+1 (Friend), Alt+2 (Flirty), Alt+3 (Roast)")
    print("3. Alt+0 to Clear Memory")
    print("---------------------------------------")

    while True:
        try:
            mode = None
            if keyboard.is_pressed('alt+1'): mode = "friendly"
            elif keyboard.is_pressed('alt+2'): mode = "flirty"
            elif keyboard.is_pressed('alt+3'): mode = "roast"
            
            if keyboard.is_pressed('alt+0'):
                global chat_history
                chat_history = []
                print(Fore.YELLOW + "\n[!] MEMORY WIPED." + Style.RESET_ALL)
                time.sleep(1)
                continue

            if mode:
                incoming_msg = pyperclip.paste()
                if not incoming_msg:
                    print(Fore.RED + "Clipboard empty!" + Style.RESET_ALL)
                else:
                    print(f"\nInput: {incoming_msg}")
                    reply = get_reply(incoming_msg, mode)
                    pyperclip.copy(reply)
                    print(Fore.YELLOW + f"Generated: {reply}" + Style.RESET_ALL)
                    print(Fore.GREEN + ">> Copied! <<" + Style.RESET_ALL)
                
                time.sleep(0.5)

            if keyboard.is_pressed('esc'):
                break
            time.sleep(0.05)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()