import time
import pyperclip
import keyboard
from google import genai
from google.genai import types
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# --- CONFIGURATION ---
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE" # <--- PASTE KEY HERE
MODEL_ID = "gemini-2.5-flash" # Use the model that worked for you in the list

client = genai.Client(api_key=API_KEY)

# --- MEMORY STORAGE ---
# This list will hold the conversation: [{"role": "user", "parts": [...]}, ...]
chat_history = []

# --- THE PERSONAS ---
MODES = {
    "friendly": "You are a chill friend. Keep it casual, low-key, and use slang (lol, rn, tbh). Under 15 words.",
    "flirty": "You are a Rizz Master. Be bold, charming, and slightly teasing. Goal: Escalate the romance. Under 20 words.",
    "roast": "You are a savage comedian. Give a witty, playful roast. Don't be mean, just funny."
}

def get_reply(incoming_text, mode):
    global chat_history
    
    print(Fore.CYAN + f"\n[+] Reading context & generating ({mode.upper()})..." + Style.RESET_ALL)
    
    # 1. Add the User's (Them) message to history temporarily to generate context
    # We construct a "Prompt" that includes the history manually for total control
    
    # Format history for the AI to understand "Them" vs "You"
    context_str = ""
    for msg in chat_history:
        role = "Them" if msg['role'] == "user" else "You"
        context_str += f"{role}: {msg['text']}\n"
    
    full_prompt = f"""
    SYSTEM INSTRUCTION: {MODES[mode]}
    
    --- CONVERSATION HISTORY ---
    {context_str}
    
    --- LATEST MESSAGE (Reply to this) ---
    Them: {incoming_text}
    """

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=full_prompt
        )
        
        reply_text = response.text.strip()
        
        # 2. Update Memory on Success
        # Add what THEY said
        chat_history.append({"role": "user", "text": incoming_text})
        # Add what YOU (The Bot) said
        chat_history.append({"role": "model", "text": reply_text})
        
        return reply_text
        
    except Exception as e:
        return f"Error: {e}"

def main():
    print(Fore.GREEN + "=== WINGMAN V3.0 (WITH MEMORY) ===" + Style.RESET_ALL)
    print("1. Copy text (Ctrl+C)")
    print(Fore.BLUE + "2. ALT + 1 = Friendly Reply")
    print(Fore.MAGENTA + "3. ALT + 2 = Flirty Reply")
    print(Fore.RED + "4. ALT + 3 = Roast")
    print(Fore.YELLOW + "5. ALT + 0 = CLEAR MEMORY (New Person)")
    print("---------------------------------------")

    while True:
        try:
            mode = None
            if keyboard.is_pressed('alt+1'): mode = "friendly"
            elif keyboard.is_pressed('alt+2'): mode = "flirty"
            elif keyboard.is_pressed('alt+3'): mode = "roast"
            
            # RESET MEMORY TRIGGER
            if keyboard.is_pressed('alt+0'):
                global chat_history
                chat_history = []
                print(Fore.YELLOW + "\n[!] MEMORY WIPED. Ready for new chat." + Style.RESET_ALL)
                time.sleep(1)
                continue

            if mode:
                incoming_msg = pyperclip.paste()
                if not incoming_msg:
                    print(Fore.RED + "Clipboard empty!" + Style.RESET_ALL)
                else:
                    print(f"Input: {incoming_msg}")
                    
                    reply = get_reply(incoming_msg, mode)
                    
                    pyperclip.copy(reply)
                    print(Fore.YELLOW + f"Generated: {reply}" + Style.RESET_ALL)
                    print(Fore.GREEN + ">> Copied! <<" + Style.RESET_ALL)
                    
                    # Show current memory depth
                    print(Fore.CYAN + f"(Memory Depth: {len(chat_history)} messages stored)" + Style.RESET_ALL)
                
                time.sleep(1) 

            if keyboard.is_pressed('esc'):
                break
            time.sleep(0.05)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()