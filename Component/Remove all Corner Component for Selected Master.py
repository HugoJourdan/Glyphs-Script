#MenuTitle: Remove all Corner Component for Selected Master
# -*- coding: utf-8 -*-

font = Glyphs.font
masterID = font.selectedFontMaster.id
for glyph in font.glyphs:
	delCount = 0
	LAYER = glyph.layers[masterID]
	for i in range(len(LAYER.hints))[::-1]:
		if LAYER.hints[i].type == CORNER:
			del LAYER.hints[i]
			delCount += 1
	if delCount:
		print ("Deleted %i corner component%s in '%s', layer '%s'." % (delCount, "s" if delCount>1 else "", LAYER.parent.name, LAYER.name))