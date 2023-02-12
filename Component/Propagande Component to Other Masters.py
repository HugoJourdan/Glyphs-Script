# MenuTitle: Propagande Component to other Masters
__doc__ = """
Copy Components of Selected Layers to others Masters.
If layers have paths and selected layer not, clear layer.
"""

font = Glyphs.font
for selectedLayer in font.selectedLayers:
	glyph = selectedLayer.parent
	components = [component.name for component in selectedLayer.components]
	for layer in glyph.layers:
		if layer != selectedLayer:
			if not selectedLayer.paths:
				layer.clear()
				for component in components:
					layer.shapes.append(GSComponent(component))

