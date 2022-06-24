#MenuTitle: Switch layerColor to glyphColor
# -*- coding: utf-8 -*-
__doc__="""Switch layerColor to glyphColor if for all master layer layerColor are same, and then remove colorLayer
"""

font = Glyphs.font

masterIdDic = []
glyphsAffected = []

for master in font.masters:
	masterIdDic.append(master.id)
	
for glyph in font.glyphs:
	layerColorCheck = []
	for layer in glyph.layers :
		if layer.layerId in masterIdDic:
			layerColorCheck.append(layer.color)
	sameLayerColor = all(element == layerColorCheck[0] for element in layerColorCheck)
	
	#Prevent if colorLayers are not set
	if sameLayerColor == True and layerColorCheck[0] == None:
		pass
	else:
	
		#If master layers have same layerColor, set glyphColor with same color and remove all layerColor
		if sameLayerColor == True :
			glyph.color = layerColorCheck[0]
			for layer in glyph.layers:
				if layer.layerId in masterIdDic:
					layer.color = None
			glyphsAffected.append(glyph.name)
		else:
			pass
			
print ("Switch layerColor to glyphColor : %s" % glyphsAffected)