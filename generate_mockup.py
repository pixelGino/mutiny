#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

# Create canvas
width, height = 1920, 4800
img = Image.new('RGB', (width, height), color='#F5F1E8')
draw = ImageDraw.Draw(img, 'RGBA')

# Load fonts (system fonts)
try:
    font_huge = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 110)
    font_display = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 80)
    font_large = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 65)
    font_title = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 52)
    font_heading = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 28)
    font_subhead = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 24)
    font_body = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 20)
    font_small = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
    font_tiny = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 14)
    font_logo = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf', 32)
except:
    # Fallback to default
    font_huge = ImageFont.load_default()
    font_display = font_large = font_title = font_heading = font_subhead = font_body = font_small = font_tiny = font_logo = font_huge

# Color palette
cream = (245, 241, 232)
sage = (143, 166, 149)
coral = (232, 155, 126)
forest = (44, 62, 47)
terracotta = (196, 155, 107)
white_glass = (255, 255, 255, 160)
text_dark = (44, 62, 47)
text_medium = (90, 107, 93)

def draw_organic_shape(draw, x, y, size, color, opacity=100):
    """Draw an organic blob shape"""
    shape_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    shape_draw = ImageDraw.Draw(shape_img)

    # Create organic shape using ellipse
    r, g, b = color
    shape_draw.ellipse([0, 0, size, size], fill=(r, g, b, opacity))

    # Apply blur for organic effect
    shape_img = shape_img.filter(ImageFilter.GaussianBlur(radius=40))

    # Paste onto main image
    img.paste(shape_img, (x, y), shape_img)

def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = xy

    # Draw main rectangles
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

    # Draw corners
    draw.ellipse([x1, y1, x1 + radius * 2, y1 + radius * 2], fill=fill)
    draw.ellipse([x2 - radius * 2, y1, x2, y1 + radius * 2], fill=fill)
    draw.ellipse([x1, y2 - radius * 2, x1 + radius * 2, y2], fill=fill)
    draw.ellipse([x2 - radius * 2, y2 - radius * 2, x2, y2], fill=fill)

    # Draw outline if specified
    if outline:
        draw.rectangle([x1 + radius, y1, x2 - radius, y1 + width], fill=outline)
        draw.rectangle([x1 + radius, y2 - width, x2 - radius, y2], fill=outline)
        draw.rectangle([x1, y1 + radius, x1 + width, y2 - radius], fill=outline)
        draw.rectangle([x2 - width, y1 + radius, x2, y2 - radius], fill=outline)

def draw_glass_card(draw, x, y, w, h, radius=40):
    """Draw a glassmorphic card"""
    draw_rounded_rect(draw, [x, y, x + w, y + h], radius, fill=white_glass)
    draw_rounded_rect(draw, [x, y, x + w, y + h], radius, outline=(255, 255, 255, 200), width=2)

# Draw organic background shapes
draw_organic_shape(draw, 1200, -150, 800, terracotta, 80)
draw_organic_shape(draw, -200, 800, 700, sage, 80)
draw_organic_shape(draw, 1400, 1400, 600, coral, 70)

# === HEADER SECTION ===
# Logo
draw.text((120, 60), "MUTINY LABS", font=font_logo, fill=forest)

# Navigation
nav_items = ["Services", "Work", "About", "Insights"]
nav_x = 1200
for item in nav_items:
    draw.text((nav_x, 68), item, font=font_small, fill=text_medium)
    nav_x += 140

# CTA Button in nav
draw_rounded_rect(draw, [1720, 56, 1800, 96], 20, fill=coral)
draw.text((1735, 67), "Let's Talk", font=font_small, fill=(255, 255, 255))

# === HERO SECTION ===
y_pos = 220

# Hero tag
draw_rounded_rect(draw, [120, y_pos, 400, y_pos + 40], 20, fill=white_glass)
draw.text((145, y_pos + 11), "DIGITAL INNOVATION PARTNERS", font=font_tiny, fill=text_medium)

y_pos += 80

# Hero title
draw.text((120, y_pos), "Transform", font=font_huge, fill=forest)
y_pos += 120
draw.text((120, y_pos), "Your Digital", font=font_huge, fill=forest)
y_pos += 120
draw.text((120, y_pos), "Ecosystem", font=font_huge, fill=coral)

y_pos += 140

# Hero description
desc_lines = [
    "We cultivate growth through human-centered design,",
    "innovative technology, and strategic thinking that",
    "evolves with your business."
]
for line in desc_lines:
    draw.text((120, y_pos), line, font=font_subhead, fill=text_medium)
    y_pos += 35

y_pos += 30

# Hero buttons
draw_rounded_rect(draw, [120, y_pos, 380, y_pos + 70], 25, fill=forest)
draw.text((165, y_pos + 20), "Start Your Journey", font=font_body, fill=(255, 255, 255))

draw_rounded_rect(draw, [400, y_pos, 670, y_pos + 70], 25, fill=white_glass)
draw_rounded_rect(draw, [400, y_pos, 670, y_pos + 70], 25, outline=sage, width=2)
draw.text((430, y_pos + 20), "Explore Our Work", font=font_body, fill=forest)

# Floating stats card
card_x, card_y = 1220, 300
draw_glass_card(draw, card_x, card_y, 580, 450, 40)

draw.text((card_x + 50, card_y + 50), "Growing Together", font=font_heading, fill=forest)
desc_text = [
    "Building digital solutions that adapt,",
    "evolve, and flourish in today's",
    "dynamic landscape."
]
ty = card_y + 100
for line in desc_text:
    draw.text((card_x + 50, ty), line, font=font_small, fill=text_medium)
    ty += 24

# Mini stats in card
stats = [
    ("150+", "PROJECTS"),
    ("98%", "SATISFACTION"),
    ("12+", "YEARS"),
    ("40+", "INDUSTRIES")
]

stat_y = card_y + 220
for i, (num, label) in enumerate(stats):
    stat_x = card_x + 50 + (i % 2) * 250
    stat_y_pos = stat_y + (i // 2) * 100

    draw_rounded_rect(draw, [stat_x, stat_y_pos, stat_x + 210, stat_y_pos + 80], 20, fill=(255, 255, 255, 130))
    draw.text((stat_x + 25, stat_y_pos + 15), num, font=font_subhead, fill=coral)
    draw.text((stat_x + 25, stat_y_pos + 50), label, font=font_tiny, fill=text_medium)

# === SERVICES SECTION ===
section_y = 1050

# Section header
draw.text((960 - 150, section_y), "WHAT WE CULTIVATE", font=font_tiny, fill=sage)
section_y += 50
draw.text((960 - 380, section_y), "Services That Grow", font=font_large, fill=forest)
section_y += 75
draw.text((960 - 330, section_y), "With Your Vision", font=font_large, fill=forest)
section_y += 70

desc_lines = [
    "From strategy to execution, we nurture every aspect",
    "of your digital presence with care and expertise."
]
for line in desc_lines:
    draw.text((960 - 360, section_y), line, font=font_body, fill=text_medium)
    section_y += 30

section_y += 50

# Service cards
services = [
    ("🎯", "Digital Strategy", "We plant the seeds of success with\ncomprehensive strategies rooted in\ndata, insight, and innovation."),
    ("✨", "Experience Design", "Crafting intuitive, beautiful interfaces\nthat naturally connect users with\nyour brand and products."),
    ("⚡", "Development", "Building robust, scalable solutions\nusing cutting-edge technology and\nbest practices that stand the test."),
    ("🚀", "Growth & Scale", "Nurturing your digital products from\nlaunch to maturity with continuous\noptimization and support."),
    ("🔄", "Transformation", "Guiding organizations through digital\nevolution with change management\nand modernization expertise."),
    ("💡", "Innovation Lab", "Exploring emerging technologies and\nexperimental approaches to solve\ntomorrow's challenges today.")
]

card_width = 540
card_height = 350
gap = 40
cards_per_row = 3

for i, (icon, title, desc) in enumerate(services):
    row = i // cards_per_row
    col = i % cards_per_row

    card_x = 120 + col * (card_width + gap)
    card_y = section_y + row * (card_height + gap)

    # Draw card
    draw_glass_card(draw, card_x, card_y, card_width, card_height, 40)

    # Icon background
    draw_rounded_rect(draw, [card_x + 40, card_y + 40, card_x + 120, card_y + 120], 24, fill=coral)
    draw.text((card_x + 60, card_y + 55), icon, font=font_title, fill=(255, 255, 255))

    # Title
    draw.text((card_x + 40, card_y + 150), title, font=font_heading, fill=forest)

    # Description
    desc_lines = desc.split('\n')
    ty = card_y + 195
    for line in desc_lines:
        draw.text((card_x + 40, ty), line, font=font_small, fill=text_medium)
        ty += 22

    # Link
    draw.text((card_x + 40, card_y + 300), "Learn More →", font=font_small, fill=coral)

# === PROCESS SECTION ===
process_y = 2850

# Process container (glass)
draw_glass_card(draw, 120, process_y, 1680, 650, 60)

# Section header
draw.text((960 - 130, process_y + 80), "OUR APPROACH", font=font_tiny, fill=sage)
py = process_y + 130
draw.text((960 - 320, py), "An Organic Process", font=font_large, fill=forest)
py += 75
draw.text((960 - 250, py), "for Lasting Impact", font=font_large, fill=forest)
py += 70

desc_lines = [
    "Like nature itself, great digital experiences require patience,",
    "care, and the right environment to thrive."
]
for line in desc_lines:
    draw.text((960 - 410, py), line, font=font_body, fill=text_medium)
    py += 30

# Process steps
steps = [
    ("01", "Discover & Root", "We dig deep to understand\nyour business, users, and\ngoals through research."),
    ("02", "Design & Grow", "Iterative design processes\nthat allow ideas to develop\nnaturally and evolve."),
    ("03", "Build & Bloom", "Bringing designs to life with\nclean, scalable code and\nrigorous testing."),
    ("04", "Nurture & Scale", "Ongoing support and\noptimization to ensure\ncontinued growth.")
]

step_y = process_y + 380
step_width = 370

for i, (num, title, desc) in enumerate(steps):
    step_x = 180 + i * (step_width + 30)

    # Large number
    draw.text((step_x, step_y), num, font=font_display, fill=(143, 166, 149, 100))

    # Title
    draw.text((step_x, step_y + 100), title, font=font_subhead, fill=forest)

    # Description
    desc_lines = desc.split('\n')
    ty = step_y + 145
    for line in desc_lines:
        draw.text((step_x, ty), line, font=font_small, fill=text_medium)
        ty += 22

# === STATS SECTION ===
stats_y = 3650

# Dark stats container
draw_rounded_rect(draw, [120, stats_y, 1800, stats_y + 350], 60, fill=forest)

# Organic accent
draw_organic_shape(draw, 100, stats_y - 100, 450, sage, 40)

# Stats grid
big_stats = [
    ("150+", "Projects Delivered"),
    ("$2.4M", "Revenue Generated"),
    ("98%", "Client Satisfaction"),
    ("12yr", "Industry Experience")
]

stat_width = 420
for i, (num, label) in enumerate(big_stats):
    stat_x = 120 + i * stat_width

    # Number
    draw.text((stat_x + 150, stats_y + 100), num, font=font_display, fill=(255, 255, 255))

    # Label
    draw.text((stat_x + 150, stats_y + 200), label, font=font_small, fill=(255, 255, 255, 180))

# === CTA SECTION ===
cta_y = 4100

# CTA container
draw_rounded_rect(draw, [120, cta_y, 1800, cta_y + 400], 60, fill=(232, 155, 126, 80))
draw_rounded_rect(draw, [120, cta_y, 1800, cta_y + 400], 60, outline=(255, 255, 255, 150), width=2)

# Organic accent
draw_organic_shape(draw, 1200, cta_y + 100, 600, coral, 50)

# CTA content
draw.text((960 - 300, cta_y + 90), "Ready to Grow", font=font_large, fill=forest)
draw.text((960 - 310, cta_y + 165), "Something Great?", font=font_large, fill=forest)

cta_desc = [
    "Let's cultivate a digital experience that transforms your",
    "business and delights your customers."
]
ty = cta_y + 250
for line in cta_desc:
    draw.text((960 - 380, ty), line, font=font_body, fill=text_medium)
    ty += 28

# Email form
form_y = cta_y + 320
draw_rounded_rect(draw, [560, form_y, 1060, form_y + 60], 30, fill=white_glass)
draw_rounded_rect(draw, [560, form_y, 1060, form_y + 60], 30, outline=sage, width=2)
draw.text((590, form_y + 19), "Enter your email", font=font_body, fill=(143, 166, 149, 180))

draw_rounded_rect(draw, [1080, form_y, 1360, form_y + 60], 30, fill=forest)
draw.text((1140, form_y + 19), "Get Started", font=font_body, fill=(255, 255, 255))

# === COLOR PALETTE ===
palette_y = 4600
draw.text((120, palette_y), "COLOR PALETTE - LIQUID ECOSYSTEM THEME", font=font_small, fill=forest)

colors_info = [
    ("Cream Canvas", "#F5F1E8", cream),
    ("Sage Garden", "#8FA695", sage),
    ("Coral Bloom", "#E89B7E", coral),
    ("Forest Deep", "#2C3E2F", forest),
    ("Terracotta Earth", "#C49B6B", terracotta),
    ("Glass Frost", "rgba(255,255,255,0.6)", (255, 255, 255))
]

swatch_width = 270
for i, (name, code, color) in enumerate(colors_info):
    sx = 120 + i * (swatch_width + 20)

    # Swatch
    if i == 5:  # Glass frost
        draw_rounded_rect(draw, [sx, palette_y + 40, sx + swatch_width, palette_y + 160], 24, fill=white_glass)
        draw_rounded_rect(draw, [sx, palette_y + 40, sx + swatch_width, palette_y + 160], 24, outline=sage, width=2)
        text_color = forest
    else:
        draw_rounded_rect(draw, [sx, palette_y + 40, sx + swatch_width, palette_y + 160], 24, fill=color)
        text_color = (255, 255, 255) if i > 0 else forest

    # Text
    draw.text((sx + 20, palette_y + 100), name, font=font_small, fill=text_color)
    draw.text((sx + 20, palette_y + 125), code, font=font_tiny, fill=text_color if i == 5 else text_color)

# Save as JPG
img = img.convert('RGB')
img.save('/Users/juansanchez/Dropbox/Mac (4)/Desktop/mutiny website/theme4_liquid_ecosystem.jpg',
         'JPEG', quality=95, optimize=True)

print("Mockup generated successfully: theme4_liquid_ecosystem.jpg")
