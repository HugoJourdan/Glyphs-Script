#MenuTitle: Font Dashboard
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
__doc__="""
Follow the development progress of a file based on the Layer Color of your glyphs.
(PS : Layer Color and not Glyph Color, to set Layer Color, you have to press RightClick + Option)
"""

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
# Order of the report is based on the order of position
positions = {
	Red: "Redrawing",
	Purple: "Check Anchors",
	LightBlue: "No Spacing",
	Yellow: "No Kerning",
	Magenta: "To Generate",
	Charcoal: "Not Exported",
	LightGreen: "Ready to Export",
	Orange: "",
	Brown: "",
	DarkGreen: "",
	DarkBlue: "",
	LightGray: "",
	NoColor: "",
}

font = Glyphs.font
glyphsCount = len(font.glyphs)
Glyphs.clearLog()

def reportLine(statusName, colorCount, glyphsCount):
	percentage = (colorCount/glyphsCount)*100
	on = int(percentage/2.5)
	off = 40-on
	tab="\t\t"
	tab_percentage=""
	if len(statusName) < 13:
		tab="\t\t\t"
	if int(percentage) < 10:
		tab_percentage=""
	print("\t" +statusName + tab +
		": %d/%d\t(%0.1f%%)\t%s\t%s%s" % (
			colorCount,
			glyphsCount,
			percentage,
			tab_percentage,
			"█"*on, "░"*off
		)
	)

for master in font.masters:	
	print ("\n🅰 %s\n" % master.name)
	
	for colorValue in positions.keys():
		position = positions[colorValue]
		if position:
			colorCount = 0
			for glyph in font.glyphs:
				masterLayer = glyph.layers[master.id]
				if masterLayer.color == colorValue:
					colorCount += 1
			reportLine(position, colorCount, glyphsCount)
	
	print ("\n▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n")

Glyphs.showMacroWindow()
