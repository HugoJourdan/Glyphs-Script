#MenuTitle: Delete Anchors in all Masters for Selected Glyphs
# -*- coding: utf-8 -*-

font = Glyphs.font

selectedLayers = font.selectedLayers
for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	for layer in thisGlyph.layers:
		print(layer)
		for anchor in layer.anchors:
			print(anchor.name)
			del(layer.anchors[anchor.name])
