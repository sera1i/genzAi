import os
import time
import pyperclip  # To read/write to clipboard
import keyboard   # To detect hotkeys
from google import genai
from google.genai import types
from colorama import Fore, Style, init

# Initialize colors for the "Vibe" coding look
init(autoreset=True)

# --- CONFIGURATION ---
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

# The "Persona" - This makes it a Love Guru
SYSTEM_INSTRUCTION = """
You are a 'Rizz Master' and expert conversationalist helping an introvert. 
Your goal: Generate a reply that is funny, engaging, or flirty (depending on context). 
Keep it under 30 words. No cringy hashtags. 
If the input is "Help me start", give a funny opening line.
"""

# Setup Gemini Client
client = genai.Client(api_key=API_KEY)

def get_guru_reply(incoming_text):
    print(Fore.CYAN + "\n[+] Asking the Guru..." + Style.RESET_ALL)
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", # Fast and smart
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7, # Higher creativity
            ),
            contents=incoming_text
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print(Fore.GREEN + "=== WINGMAN AI ACTIVATED ===" + Style.RESET_ALL)
    print(Fore.YELLOW + "Instructions:")
    print("1. Copy the message you received (Ctrl+C).")
    print("2. Press 'alt+g' to generate a reply.")
    print("3. The reply will be copied to your clipboard automatically.")
    print("4. Just Paste (Ctrl+V) and Send!")
    print(Fore.RED + "Press 'esc' to exit." + Style.RESET_ALL)

    while True:
        try:
            # Wait for the hotkey trigger
            if keyboard.is_pressed('alt+g'):
                # 1. Read what you just copied
                incoming_msg = pyperclip.paste()
                
                if not incoming_msg:
                    print(Fore.RED + "Clipboard is empty! Copy something first." + Style.RESET_ALL)
                    time.sleep(1)
                    continue

                print(f"Message received: {incoming_msg}")

                # 2. Get the Rizz
                reply = get_guru_reply(incoming_msg)

                # 3. Put reply back in clipboard
                pyperclip.copy(reply)
                
                print(Fore.MAGENTA + f"Guru Suggests: {reply}" + Style.RESET_ALL)
                print(Fore.GREEN + "[+] Copied to clipboard! Just Paste it." + Style.RESET_ALL)
                
                # Prevent double firing
                time.sleep(1) 
            
            if keyboard.is_pressed('esc'):
                print("Exiting Wingman...")
                break
                
            time.sleep(0.05) # Save CPU
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()