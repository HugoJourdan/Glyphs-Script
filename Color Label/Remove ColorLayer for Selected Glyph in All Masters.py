#MenuTitle: Remove LayerColor for Selected Glyph in All Master
# -*- coding: utf-8 -*-

from GlyphsApp import *

font = Glyphs.font
glyph = font.glyphs
master = font.masters

for master in font.masters:
	for glyph in font.glyphs:
		if glyph.selected:		
			glyph.layers[master.id].color = None
