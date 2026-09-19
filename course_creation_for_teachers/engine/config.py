"""
Teacher Course Configuration Engine
Teachers customize their school name, mascot, branding colors, typography,
and course metadata in this single file. All presentation builders read from here.
"""

from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# =============================================================================
# 1. INSTITUTIONAL IDENTITY & BRAND METADATA (CUSTOMIZE THIS!)
# =============================================================================
INSTITUTION_NAME = "Laramie County Community College"
INSTITUTION_ACRONYM = "LCCC"
INSTITUTION_TAGLINE = "GOLDEN EAGLES"
DEPARTMENT_NAME = "Artificial Intelligence Program"
COURSE_TRACK_NAME = "Workforce Technical Incubator"
COURSE_CODE = "AI ML 2060"
COREQUISITE_NAME = "Capstone Project Corequisite"
FOOTER_TEXT = f"{INSTITUTION_NAME}  |  {DEPARTMENT_NAME}"

# =============================================================================
# 2. COLOR PALETTE (WCAG 2.1 AAA High-Contrast Standards)
# =============================================================================
# Primary Institutional Palette (Default: Navy & Gold)
# To change to Crimson & White:
#   COLOR_PRIMARY_NAVY = RGBColor(165, 0, 38)
#   COLOR_DARK_NAVY    = RGBColor(103, 0, 31)
COLOR_PRIMARY_NAVY  = RGBColor(0, 50, 120)     # #003278 (Deep Institutional Navy)
COLOR_DARK_NAVY     = RGBColor(0, 32, 85)      # #002055 (Rich Section Divider Navy)
COLOR_ACCENT_BLUE   = RGBColor(7, 107, 182)    # #076BB6 (Secondary Accent Blue)
COLOR_GOLD          = RGBColor(255, 192, 1)    # #FFC001 (Bright Gold Highlight)
COLOR_WARM_GOLD     = RGBColor(190, 135, 0)    # #BE8700 (High-Contrast Warm Gold)

# Neutral & Body Text Colors
COLOR_CHARCOAL_TEXT = RGBColor(31, 41, 55)     # #1F2937 (Crisp Body Text - 11:1 on white)
COLOR_MUTED_TEXT    = RGBColor(75, 85, 99)     # #4B5563 (Muted Captions & Subtitles)
COLOR_WHITE         = RGBColor(255, 255, 255)
COLOR_LIGHT_ICE     = RGBColor(200, 225, 250)

# Content Card Container Colors
CARD_BG_PRIMARY     = RGBColor(243, 247, 252)  # Subtle Ice Blue Card Fill
CARD_LINE_PRIMARY   = RGBColor(194, 214, 236)  # Subtle Ice Blue Border
CARD_BG_SECONDARY   = RGBColor(255, 253, 240)  # Warm Cream/Gold Card Fill
CARD_LINE_SECONDARY = RGBColor(240, 205, 90)   # Gold Accent Border

# Code & Terminal Container Colors
CODE_CONTAINER_BG   = RGBColor(17, 24, 39)     # #111827 (Deep Midnight Slate)
CODE_CONTAINER_LINE = RGBColor(55, 65, 81)     # #374151 (Border Slate)
CODE_SYNTAX_TEXT    = RGBColor(138, 212, 255)  # #8AD4FF (Cyan/Ice Blue Monospace)

# =============================================================================
# 3. TYPOGRAPHY & FONT SPECIFICATIONS
# =============================================================================
FONT_PRIMARY_HEADING = "Arial"
FONT_BODY            = "Arial"
FONT_CODE_MONO       = "Consolas"

# Font Sizes
SIZE_TITLE_HERO      = Pt(64)
SIZE_TITLE_MAIN      = Pt(40)
SIZE_SECTION_TITLE   = Pt(36)
SIZE_SLIDE_HEADING   = Pt(30)
SIZE_CARD_HEADER     = Pt(21)
SIZE_BODY_TEXT       = Pt(13.5)
SIZE_CODE_TEXT       = Pt(10.5)
SIZE_EYEBROW         = Pt(11)
SIZE_FOOTER          = Pt(10.5)

# Code Container Formatting
CODE_ALIGNMENT       = PP_ALIGN.LEFT            # STRICTLY ENFORCED LEFT-ALIGNMENT
CODE_LINE_SPACING    = Pt(1.5)

# =============================================================================
# 4. SLIDE GEOMETRY (Standard 16:9 Widescreen)
# =============================================================================
SLIDE_WIDTH_INCHES   = Inches(13.333)
SLIDE_HEIGHT_INCHES  = Inches(7.5)

# Layout Coordinates
MARGIN_LEFT_STANDARD = Inches(0.8)
MARGIN_TOP_STANDARD  = Inches(0.4)
HEADER_WIDTH         = Inches(11.7)
CARD_TOP_STANDARD    = Inches(1.8)
CARD_HEIGHT_STANDARD = Inches(4.9)
