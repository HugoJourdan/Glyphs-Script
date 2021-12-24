#MenuTitle: Change LayerColor to Red

font = Glyphs.font

selectedLayers = font.selectedLayers
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.layers[font.selectedFontMaster.id].color = 0
