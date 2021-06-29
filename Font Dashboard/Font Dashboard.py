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
# You can change the color after LayerColor_ to set your own order
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
	percentage = (colorCount*1.0)/glyphsCount
	on = int(percentage//10)
	off = 10-on
	print(
		"\t%s%s %s: %d/%d (%0.1f%%)" % (
			"█"*on, "░"*off,
			statusName,
			colorCount,
			glyphsCount,
			percentage
		)
	)

for master in font.masters:	
	print ("\n🅰 %s\n" % master.name)
	
	for colorValue in sorted(positions.keys()):
		position = positions[colorValue]
		if position:
			colorCount = 0
			for glyph in font.glyphs:
				masterLayer = glyph.layers[master.id]
				if masterLayer.color == colorValue:
					colorCount += 1
			reportLine(position, colorCount, glyphsCount)
	
	print ("\n▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n")

Glyphs.showMacroWindow()
