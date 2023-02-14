#MenuTitle: Filter Layer Color in FontView
# -*- coding: utf-8 -*-
__doc__="""
Generates a new "glyphOrder" that filters glyphs according to the colour of the selected master layer.
If a glyphOrder already exists, it will create a new one, and switch them when the script is triggered.
"""


import os
import codecs
import re

font = Glyphs.font



# Generate code for custom parameter "glyphOrder"
def GenerateLayerColorGlyphOrder():
	colorMeaning = Map_Keys(Get_Key_File())
	colorLabels = {}
	masterID = font.selectedFontMaster.id
	for glyph in font.glyphs:
		color = glyph.layers[masterID].color
		if color not in colorLabels:
			colorLabels[color] = []
		colorLabels[color].append(glyph.name)
	if colorLabels[13]:
		colorLabels[13] = colorLabels.pop(None)
	myKeys = list(colorLabels.keys())
	myKeys.sort()
	colorLabels = {i: colorLabels[i] for i in myKeys}
	if colorLabels[13]:
		colorLabels["Not set"] = colorLabels.pop(13)

	code = ["#Color Layer Filter:"]
	for color, glyph in colorLabels.items():
		if str(color) in colorMeaning.keys():
			code.append(f"**{colorMeaning[str(color)]}**")
			code.extend(glyph)

	return code

if  Glyphs.font.customParameters["glyphOrder"] == None:
	Glyphs.font.customParameters["glyphOrder"] = GenerateLayerColorGlyphOrder()
	newParam = GSCustomParameter.alloc().init()
	newParam.name = "glyphOrder"
	newParam.value = ()
	font.addCustomParameter_(newParam)

CP = list(Glyphs.font.customParameters)

index = []
for cp in CP:
	i = CP.index(cp)
	if cp.name == "glyphOrder":
		index.append(i)

if len(index) <= 1 :
	newParam = GSCustomParameter.alloc().init()
	newParam.name = "glyphOrder"
	newParam.value = GenerateLayerColorGlyphOrder()
	font.addCustomParameter_(newParam)

first = CP[index[0]].copy()
second = CP[index[1]].copy()

Glyphs.font.customParameters[index[0]].value = second.value
Glyphs.font.customParameters[index[1]].value = first.value
#print(Glyphs.font.customParameters[index[0]].value)
if "#Color Layer Filter:" in Glyphs.font.customParameters[index[0]].value:
	Glyphs.font.customParameters[index[0]].value = GenerateLayerColorGlyphOrder()
if "#Color Layer Filter:" in Glyphs.font.customParameters[index[1]].value:
	Glyphs.font.customParameters[index[1]].value = GenerateLayerColorGlyphOrder()

# Get or build colorNames.text
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
		f.write("None=🫥 None\nred=🚨 Red\norange=🦊 Orange\nbrown=🪵 Brown\nyellow=🌼 Yellow\nlightGreen=🍀 Light green\ndarkGreen=🫑 Dark green\nlightBlue=💎 Light blue\ndarkBlue=🌀 Dark blue\npurple=🔮 Purple\nmagenta=🌺 Magenta\nlightGray=🏐 Light Gray\ncharcoal=🎱 Charcoal")
	else:
		pass
	return keyFile

# Build Dic from colorNames.txt content
def Map_Keys(keyFile):
	colourLabels = {}
	if os.path.exists(keyFile):
		with codecs.open(keyFile, "r", "utf-8") as file:
			for line in file:
				colour = re.match(r".*?(?=\=)", line).group(0)
				label = re.search(r"(?<=\=).*", line).group(0)
				if colour != "None":
					colourLabels[colour] = label
	switch = {}
	replace = {"red":"0", "orange":"1", "brown":"2", "yellow":"3", "lightGreen":"4", "darkGreen":"5", "lightBlue":"6", "darkBlue":"7", "purple":"8", "magenta":"9", "lightGray":"10", "charcoal":"11"}

	for k, v in colourLabels.items():
		switch[replace[k]] = v

	colourLabels = switch
	return colourLabels

