#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import os

def capture_screenshot(html_file, output_file):
    """Capture full page screenshot of HTML file"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 4800})

        # Load the HTML file
        file_path = f"file://{os.path.abspath(html_file)}"
        page.goto(file_path)

        # Wait for page to load completely
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(2000)  # Additional wait for animations

        # Take full page screenshot
        page.screenshot(path=output_file, full_page=True, type='jpeg', quality=90)

        browser.close()
        print(f"Screenshot saved: {output_file}")

# Generate screenshots for all three palettes
palettes = [
    ('theme4_purple_palette1_deep_lavender.html', 'theme4_purple_palette1_deep_lavender.jpg'),
    ('theme4_purple_palette2_rich_gold.html', 'theme4_purple_palette2_rich_gold.jpg'),
    ('theme4_purple_palette3_violet_silver.html', 'theme4_purple_palette3_violet_silver.jpg')
]

for html_file, jpg_file in palettes:
    print(f"Generating screenshot for {html_file}...")
    capture_screenshot(html_file, jpg_file)

print("\nAll screenshots generated successfully!")
