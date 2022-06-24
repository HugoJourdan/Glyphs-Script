#MenuTitle: Copy LayerColor to full Component Glyphs
# -*- coding: utf-8 -*-

font = Glyphs.font

for glyph in font.glyphs:
	try:
		for layer in glyph.layers:
			if layer.isMasterLayer:
				
				#Check if layer is composed only with component and do stuff if True
				checkComp = []
				for shape in layer.shapes:
					if shape.shapeType not in checkComp:
						checkComp.append(shape.shapeType)
				try:
					if len(checkComp) <= 1 and 4 in checkComp :
						checkLayerColor = []
						for component in layer.components:
							componentName = component.name
							parentGlyph = component.componentLayer
							colorLayer = parentGlyph.color
							if colorLayer not in checkLayerColor:
								checkLayerColor.append(colorLayer)
						if len(checkLayerColor) == 1:
							layer.color = colorLayer
				except:
					break

	except:
		pass