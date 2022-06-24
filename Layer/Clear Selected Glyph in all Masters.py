#MenuTitle: Clear selected glyph in all Masters
# -*- coding: utf-8 -*-
__doc__ = """
"""

font = Glyphs.font
for glyph in font.glyphs:
	if glyph.selected:
		for layer in glyph.layers:
			if layer.isMasterLayer:
				layer.clear()