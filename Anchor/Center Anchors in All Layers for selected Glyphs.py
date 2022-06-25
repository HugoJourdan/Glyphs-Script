#MenuTitle: Center Anchors in All Layers for selected Glyphs
# -*- coding: utf-8 -*-

from vanilla import*
from math import * 
font = Glyphs.font



class FloatingWindowDemo:

	def __init__(self):
		self.w = FloatingWindow((150, 98), "Center Anchors")
		self.w.text = TextBox((10, 10, -10, 17), "Select anchor name", sizeStyle='small')
		self.w.popUpButton = PopUpButton((10, 30, -10, 20),["center", "_center"])
		self.w.button = Button((10, 64, -10, 20), "Move",callback=self.buttonCallback)
		self.w.open()

	def buttonCallback(self, sender):
		print(self.w.popUpButton.getItem())
		print("ok")



		# If no glyph selected in Font View, take layer.parent
		selectedGlyphs = []
		if font.selection:
			for glyph in font.selection:
				selectedGlyphs.append(glyph)
		else:
			selectedLayers = font.selectedLayers
			for thisLayer in selectedLayers:
				glyph = thisLayer.parent
				selectedGlyphs.append(glyph)

		for glyph in selectedGlyphs:
			print(glyph.name)
			for thisLayer in glyph.layers:
				if thisLayer.isMasterLayer:
					print(thisLayer.name)
					angle = thisLayer.master.italicAngle
					xHeight = font.selectedFontMaster.xHeight
					offset = atan(angle)*xHeight/2
				glyphWidth = thisLayer.bounds.size.width
				glyphHeight = thisLayer.bounds.size.height

	
				yCenter = glyphHeight/2 + thisLayer.bounds.origin.y
				shift = atan(radians(angle)) * yCenter - offset
	
				thisLayer.anchors[self.w.popUpButton.getItem()] = GSAnchor(self.w.popUpButton.getItem(),
										       (glyphWidth/2 + shift + thisLayer.bounds.origin.x+offset, glyphHeight/2 + thisLayer.bounds.origin.y))	
FloatingWindowDemo()
