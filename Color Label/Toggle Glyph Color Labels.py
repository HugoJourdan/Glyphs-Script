# MenuTitle: Toggle Glyph Color Labels

font = Glyphs.font

font.disableUpdateInterface()

if font.userData["glyphColor_dic"]:
	for glyph in font.glyphs:
		if glyph.id in font.userData["glyphColor_dic"].keys():
			glyph.color = font.userData["glyphColor_dic"][glyph.id]
	del(font.userData["glyphColor_dic"])
else:
	glyphColor_dic = {}
	for glyph in font.glyphs:
		glyphColor_dic[glyph.id]=glyph.color
	font.userData["glyphColor_dic"] = glyphColor_dic
	for glyph in font.glyphs:
		glyph.color = None
		
font.enableUpdateInterface()