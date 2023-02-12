#MenuTitle: Update LayerColor of full Component Glyphs
# -*- coding: utf-8 -*-

import codecs
import os
import re

def Get_Key_File():
	keyFile = None
	try:
		thisDirPath = os.path.dirname(Glyphs.font.filepath)
		localKeyFile = thisDirPath + '/colorNames.txt'
		if os.path.exists(localKeyFile):
			keyFile = localKeyFile
	except:
		pass

	dirInfo = os.path.expanduser("~/Library/Application Support/Glyphs 3/info")
	if not os.path.exists(dirInfo):
		os.mkdir(dirInfo)

	if keyFile is None:
		keyFile = os.path.expanduser('~/Library/Application Support/Glyphs 3/info/colorNames.txt')

	if not os.path.exists(keyFile):
		f = open(keyFile,"w+")
		f.write("None=None\nred=Red\norange=Orange\nbrown=Brown\nyellow=Yellow\nlightGreen=Light green\ndarkGreen=Dark green\nlightBlue=Light blue\ndarkBlue=Dark blue\npurple=Purple\nmagenta=Magenta\nlightGray=Light Gray\ncharcoal=Charcoal")
	else:
		pass
	return keyFile

# Build Dic from ColorNames.txt content
def Map_Keys(keyFile):

	colourLabels = {}
	if os.path.exists(keyFile):
		with codecs.open(keyFile, "r", "utf-8") as file:
			for line in file:
				colour = re.match(r".*?(?=\=)", line).group(0)
				label = re.search(r"(?<=\=).*", line).group(0)
				colourLabels[colour] = label
	switch = {}
	replace = {"None":None,"red":0, "orange":1, "brown":2, "yellow":3, "lightGreen":4, "darkGreen":5, "lightBlue":6, "darkBlue":7, "purple":8, "magenta":9, "lightGray":10, "charcoal":11}

	for k, v in colourLabels.items():
		switch[replace[k]] = v

	colourLabels = switch
	return colourLabels

colorMeaningDic = Map_Keys(Get_Key_File())
orderColor = list(colorMeaningDic.keys())

font = Glyphs.font
font.disableUpdateInterface()


def SyncLabelColor():
	
	for glyph in font.glyphs:
		try:
			for layer in [layer for layer in glyph.layers if layer.isMasterLayer]:
				if len(layer.shapes) > 1 and 4 in [shape.shapeType for shape in layer.shapes]:
					
					checkLayerColor = {component.componentLayer.color:0 for component in layer.components}
					if len(checkLayerColor) == 1 and layer.color != list(checkLayerColor.keys())[0]:
						layer.color = list(checkLayerColor.keys())[0]

					elif len(checkLayerColor) != 1:
						temp = {}
						for color in checkLayerColor:
							temp[color]=orderColor[color]
						layer.color = min(temp)
					else:
						pass
				if len(layer.shapes) == 1:
					layer.color = layer.components[0].componentLayer.color
		except:pass
	
SyncLabelColor()


font.enableUpdateInterface()
