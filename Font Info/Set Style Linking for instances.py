#MenuTitle: Set Style Linking for Instances
# -*- coding: utf-8 -*-
__doc__=""" Set Style Linking for instances based on their names
"""

font = Glyphs.font

# Check Italic box in Style Linking
for instance in font.instances:
	styleLinking = ""
	if "Italic" in instance.name:
		instance.isItalic=True
		styleLinking = instance.name.split()[0]
		instance.linkStyle= styleLinking
	if "Bold" in instance.name:
		instance.isBold=True
	if instance.isBold == True and instance.isItalic == True :
		instance.linkStyle= "Regular"