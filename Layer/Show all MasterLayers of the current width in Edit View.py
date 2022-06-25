#MenuTitle:Show all MasterLayers of the current Selected Master width in Edit View.
# -*- coding: utf-8 -*-
__doc__="""
Make MasterLayers visible of the width of Selected Master. Visible mean enable "eye" in layer panel.
"""

font = Glyphs.font

axeDic = {}
axeIndex = -1
for axe in font.axes:
	axeIndex += 1
	axeDic[axeIndex] = axe.name

for key, value in axeDic.items():
	if value == "Width":
		widthIndex = key
	if value == "Slanted":
		slantedIndex = key


showMasters = []
for master in font.masters:
	if master.axes[widthIndex] == font.selectedFontMaster.axes[widthIndex] and master.axes[slantedIndex] == font.selectedFontMaster.axes[slantedIndex]:
		showMasters.append(master)
		

for layer in font.glyphs[0].layers:
	if layer.isMasterLayer:
		if layer.master in showMasters:
			layer.setVisible_(True)
		else:
			layer.setVisible_(False)
