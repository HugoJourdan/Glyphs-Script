#MenuTitle: Set Localized Family Names and Localized Style Names 
# -*- coding: utf-8 -*-
__doc__="""
Set for each instance general Parameters General Parameters "Localized Family Names" and "Variable Styles Names". "Weight Class","Width Class" and "Style Name" need to set for script work"
"""


font = Glyphs.font
fontAxes = []
exportAxesValues = {}
axeCount = -1

for axe in font.axes:
	fontAxes.append(axe.name)

for instance in font.instances:

	
	# Set Localized Family Names and Variable Style Names
	if instance.widthClassName.split()[0]=="Medium":
		instance.familyName = "%s" % (font.familyName)
		instance.variableStyleName = "%s" % (instance.name)

	else:
		instance.familyName = "%s %s" % (font.familyName, instance.widthClassName.split()[0])
		instance.variableStyleName = "%s %s" % (instance.widthClassName, instance.name)
		



