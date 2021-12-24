#MenuTitle: Delete Special Layers for Selected Glyph
# -*- coding: utf-8 -*-
__doc__ = """
Delete Special Layers (brace, bracket or a smart component layer) for Selected Glyph
"""

font = Glyphs.font
selectedLayers = font.selectedLayers
specialLayerIdList = []

for selectedLayer in selectedLayers:
	for layer in selectedLayer.parent.layers:
		if layer.isSpecialLayer == True:
			print(layer)
			specialLayer = layer
			specialLayerId = layer.layerId
			specialLayerIdList.append(specialLayerId)
			
for i in specialLayerIdList :
	del(font.glyphs[specialLayer.parent.name].layers[i])
	
