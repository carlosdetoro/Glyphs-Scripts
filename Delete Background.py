#MenuTitle: Delete background
# -*- coding: utf-8 -*-
# Written by Carlos de Toro @ 2018
__doc__="""
Delete background in all glyphs present in font.
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Script Delete Background run – " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
thisFont.disableUpdateInterface()
for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        layer.setBackground_( None )
thisFont.enableUpdateInterface()

print "Backgrounds have been deleted 🦄"
