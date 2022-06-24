#MenuTitle: Copy GlyphColor to None LayerColor
# -*- coding: utf-8 -*-
font = Glyphs.font

for glyph in font.glyphs:
	for layer in glyph.layers:
		if layer.isMasterLayer and layer.color == None:
			layer.color = glyph.color