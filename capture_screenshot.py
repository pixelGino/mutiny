#!/usr/bin/env python3
import subprocess
import os
import time

# Path to the HTML file
html_path = "/Users/juansanchez/Dropbox/Mac (4)/Desktop/mutiny website/theme4_liquid_ecosystem.html"
output_path = "/Users/juansanchez/Dropbox/Mac (4)/Desktop/mutiny website/theme4_liquid_ecosystem.png"

# Try using Safari via osascript
applescript = f'''
tell application "Safari"
    activate
    open location "file://{html_path}"
    delay 3
end tell
'''

try:
    # Use Safari with AppleScript
    subprocess.run(['osascript', '-e', applescript], check=True)
    print("Opened in Safari. Please manually capture the screenshot or use screencapture command.")
except Exception as e:
    print(f"Error: {e}")
    print("Please open the HTML file manually in a browser and take a screenshot.")
