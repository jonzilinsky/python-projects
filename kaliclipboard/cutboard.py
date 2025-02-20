# nohup python3 cutboard.py & (to run)
# nohup python3 cutboard.py > /dev/null 2>&1 & (to run no error logging)
# cat ~/clippy.txt (to view copies)
# ps aux | grep clipboard.py
# kill pid to quit

import pyperclip
import time
from datetime import datetime

def monitor_clipboard(output_file="clippy.txt"):
    previous_text = ""
    print(f"Monitoring clipboard. Logging to '{output_file}'.")
    while True:
        try:
            current_text = pyperclip.paste()
            if current_text != previous_text:
                with open(output_file, "a", encoding="utf-8") as f:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                    f.write("-----------------------------------------------------\n")
                    f.write(f"Timestamp: {timestamp}\n")
                    f.write(f"{current_text}\n")
                    f.write("-----------------------------------------------------\n")
                previous_text = current_text
            time.sleep(0.5)  # Check clipboard every 0.5 seconds
        except Exception as e:
            with open("clipboard_errors.log", "a", encoding="utf-8") as f:
                f.write(f"Error: {e}\n")
            time.sleep(1)

if __name__ == "__main__":
    monitor_clipboard()
