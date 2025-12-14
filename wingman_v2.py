import time
import pyperclip
import keyboard
from google import genai
from google.genai import types
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

# --- CONFIGURATION ---
# PASTE YOUR API KEY HERE
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

client = genai.Client(api_key=API_KEY)

# --- THE PERSONAS ---
MODES = {
    "friendly": """
        You are a chill, funny best friend helping an introvert text. 
        Reply in a casual, low-pressure way. Use lowercase, minimal punctuation, and slang like 'lol', 'rn', 'tbh'. 
        Keep it under 15 words.
    """,
    "flirty": """
        You are a smooth 'Rizz Master'. 
        Generate a reply that is confident, slightly teasing, and charming. 
        Your goal is to escalate the vibe or get a date. 
        Keep it short (under 20 words). Don't be creepy.
    """,
    "roast": """
        You are a witty comedian. 
        The incoming text needs a savage but playful comeback. 
        Roast them lightly. Make it funny, not mean.
    """
}

def get_reply(incoming_text, mode):
    print(Fore.CYAN + f"\n[+] Wingman activating ({mode.upper()} MODE)..." + Style.RESET_ALL)
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=MODES[mode],
                temperature=0.8, # High creativity
            ),
            contents=incoming_text
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print(Fore.GREEN + "=== WINGMAN V2.0 ONLINE ===" + Style.RESET_ALL)
    print("1. Copy text (Ctrl+C)")
    print(Fore.BLUE + "2. ALT + 1 = Friendly Reply")
    print(Fore.MAGENTA + "3. ALT + 2 = Flirty Reply (Rizz)")
    print(Fore.RED + "4. ALT + 3 = Roast/Savage Reply")
    print("---------------------------------------")

    while True:
        try:
            mode = None
            if keyboard.is_pressed('alt+1'):
                mode = "friendly"
            elif keyboard.is_pressed('alt+2'):
                mode = "flirty"
            elif keyboard.is_pressed('alt+3'):
                mode = "roast"
            
            # If a key was pressed, execute the logic
            if mode:
                # 1. Grab Clipboard
                incoming_msg = pyperclip.paste()
                if not incoming_msg:
                    print(Fore.RED + "Clipboard empty!" + Style.RESET_ALL)
                else:
                    print(f"Input: {incoming_msg}")
                    
                    # 2. Generate
                    reply = get_reply(incoming_msg, mode)
                    
                    # 3. Copy back
                    pyperclip.copy(reply)
                    print(Fore.YELLOW + f"Generated: {reply}" + Style.RESET_ALL)
                    print(Fore.GREEN + ">> Copied to clipboard! <<" + Style.RESET_ALL)
                
                time.sleep(1) # Prevent double triggering

            if keyboard.is_pressed('esc'):
                print("Exiting...")
                break
                
            time.sleep(0.05)
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()