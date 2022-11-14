import fontforge

from pathlib import Path
import os

# https://fontforge.org/docs/scripting/python.html

glyphWidth = 500 # Thin
upperCaseHeight = 730 # Thin
lowerCaseHeight = 550 # Thin
glyphPadding = 70 # Thin

# glyphWidth = 320 # v2
# upperCaseHeight = 384 # v2
# lowerCaseHeight = 256 # v2
# glyphPadding = 32 # v2

fontName = "Aurebesh Code"
fontVariant = "Regular"

# Create a new font
font = fontforge.font()

# Configure the font
font.familyname = fontName
font.fullname = "%s %s"%(fontName, fontVariant)
font.fontname = "AurebeshCode-Regular"
font.ascent = upperCaseHeight + glyphPadding
font.descent = glyphPadding
font.appendSFNTName("English (US)", "Family", "Aurebesh Code")
font.appendSFNTName("English (US)", "Fullname", "Aurebesh Code Regular")
font.appendSFNTName("English (US)", "UniqueID", "AurebeshCode:Regular")

# Import each svg
for glyphSvgFile in list(Path('src/svg/').glob('*.svg')):
	charIdentifier = glyphSvgFile.stem.split(" ", 1)[0]
	charUnicodeValue = charIdentifier[2:]
	charNumber = int(charUnicodeValue, 16)

	glyph = font.createChar(charNumber)
	glyph.width = glyphWidth + (glyphPadding * 2)
	glyph.importOutlines(str(glyphSvgFile), scale=False)

# Output the font in all file formats
font.save("build/Aurebesh Code.sfd")
font.generate("build/Aurebesh Code.otf")
font.generate("build/Aurebesh Code.ttf")
font.generate("build/Aurebesh Code.woff")
font.generate("build/Aurebesh Code.woff2")
