#MenuTitle: Font Dashboard
# -*- coding: utf-8 -*-


# Don't change these values
Red=0
Orange=1
Brown=2
Yellow=3
LightGreen=4
DarkGreen=5
LightBlue=6
DarkBlue=7
Purple=8
Magenta=9
LightGray=10
Charcoal=11
NoColor=12


# If a Layer Color is not used, keep it empty
# You can change the color after LayerColor_ to set your own order
Position_1  = LayerColor_Red = "Redrawing"
Position_2  = LayerColor_Purple = "Check Anchors"
Position_3  = LayerColor_LightBlue = "No Spacing"
Position_4  = LayerColor_Yellow = "No Kerning"
Position_5  = LayerColor_Magenta = "To Generate"
Position_6  = LayerColor_Charcoal = "Not Exported"
Position_7  = LayerColor_LightGreen = "Ready to Export"
Position_8  = LayerColor_Orange = ""
Position_9  = LayerColor_Brown = ""
Position_10 = LayerColor_DarkGreen = ""
Position_11 = LayerColor_DarkBlue = ""
Position_12 = LayerColor_LightGray = ""
Position_13 = LayerColor_NoColor = ""


font = Glyphs.font
glyphsCount = len(Font.glyphs)
Glyphs.clearLog()


for master in font.masters:	
	print ("\n\U0001F170 "  +master.name+"\n")
	
	#Position 1
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == Red:
			colorCount += 1
			percent= round((colorCount/glyphsCount)*100,1)
	
	if Position_1:
		if 100 <= percent <= 100:
			print ("\t" + Position_1 + ": \t\t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_1 + ": \t\t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_1 + ": \t\t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_1 + ": \t\t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_1 + ": \t\t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_1 + ": \t\t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_1 + ": \t\t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_1 + ": \t\t\t███░░░░░░░" + " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_1 + ": \t\t\t██░░░░░░░░ "+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_1 + ": \t\t\t█░░░░░░░░░ "+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_1 + ": \t\t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
			
		else:			
			pass

	
	#Position 1
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == Purple:
			colorCount += 1
			percent= round((colorCount/glyphsCount)*100,1)
	
	if Position_2:
		if 100 <= percent <= 100:
			print ("\t" + Position_2 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_2 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_2 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_2 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_2 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_2 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_2 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_2 + ": \t\t███░░░░░░░" + " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_2 + ": \t\t██░░░░░░░░ "+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_2 + ": \t\t█░░░░░░░░░ "+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_2 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
			
		else:			
			pass
	#Position 3
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightBlue:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_3:		
		if 100 <= percent <= 100:
			print ("\t" + Position_3 + ": \t\t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_3 + ": \t\t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_3 + ": \t\t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_3 + ": \t\t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_3 + ": \t\t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_3 + ": \t\t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_3 + ": \t\t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_3 + ": \t\t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_3 + ": \t\t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_3 + ": \t\t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_3 + ": \t\t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
	
	#Position 4
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == Yellow:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_2:		
		if 100 <= percent <= 100:
			print ("\t" + Position_4 + ": \t\t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_4 + ": \t\t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_4 + ": \t\t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_4 + ": \t\t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_4 + ": \t\t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_4 + ": \t\t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_4 + ": \t\t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_4 + ": \t\t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_4 + ": \t\t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_4 + ": \t\t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_4 + ": \t\t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
	
	#Position 5
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == Magenta:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_5:		
		if 100 <= percent <= 100:
			print ("\t" + Position_5 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_5 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_5 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_5 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_5 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_5 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_5 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_5 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_5 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_5 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_5 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 6
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == Charcoal:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_6:		
		if 100 <= percent <= 100:
			print ("\t" + Position_6 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_6 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_6 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_6 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_6 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_6 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_6 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_6 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_6 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_6 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_6 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 7
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_7:		
		if 100 <= percent <= 100:
			print ("\t" + Position_7 + ": \t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_7 + ": \t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_7 + ": \t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_7 + ": \t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_7 + ": \t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_7 + ": \t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_7 + ": \t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_7 + ": \t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_7 + ": \t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_7 + ": \t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_7 + ": \t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 8
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_8:		
		if 100 <= percent <= 100:
			print ("\t" + Position_8 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_8 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_8 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_8 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_8 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_8 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_8 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_8 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_8 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_8 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_8 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 9
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_9:		
		if 100 <= percent <= 100:
			print ("\t" + Position_9 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_9 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_9 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_9 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_9 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_9 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_9 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_9 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_9 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_9 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_9 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 10
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_10:		
		if 100 <= percent <= 100:
			print ("\t" + Position_10 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_10 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_10 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_10 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_10 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_10 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_10 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_10 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_10 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_10 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_10 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 11
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_11:		
		if 100 <= percent <= 100:
			print ("\t" + Position_11 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_11 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_11 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_11 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_11 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_11 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_11 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_11 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_11 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_11 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_11 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	#Position 12
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_12:		
		if 100 <= percent <= 100:
			print ("\t" + Position_12 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_12 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_12 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_12 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_12 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_12 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_12 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_12 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_12 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_12 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_12 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
	
	#Position 13
	colorCount = 0
	percent= 0
	for glyph in font.glyphs:
		layer = glyph.layers[master.id]
		if layer.color == LightGreen:
			colorCount += 1
			percent = round((colorCount/glyphsCount)*100,1)
			
	if Position_13:		
		if 100 <= percent <= 100:
			print ("\t" + Position_13 + ": \t\t██████████"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 81 <= percent <= 99:
			print ("\t" + Position_13 + ": \t\t█████████░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 71 <= percent <= 80:
			print ("\t" + Position_13 + ": \t\t████████░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 61 <= percent <= 70:
			print ("\t" + Position_13 + ": \t\t███████░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 51 <= percent <= 60:
			print ("\t" + Position_13 + ": \t\t██████░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 41 <= percent <= 50:
			print ("\t" + Position_13 + ": \t\t█████░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 31 <= percent <= 40:
			print ("\t" + Position_13 + ": \t\t████░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 21 <= percent <= 30:
			print ("\t" + Position_13 + ": \t\t███░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 11 <= percent <= 20:
			print ("\t" + Position_13 + ": \t\t██░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 1 <= percent <= 10:
			print ("\t" + Position_13 + ": \t\t█░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		elif 0 <= percent <= 0:
			print ("\t" + Position_13 + ": \t\t░░░░░░░░░░"+ " %d" % colorCount + "/" + "%d" % glyphsCount)
		else:
			pass
			
			
	colorCount = 0
	print ("\n▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n")
	
Glyphs.showMacroWindow()