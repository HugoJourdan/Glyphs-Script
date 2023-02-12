#MenuTitle: Vertically Center Manager
# -*- coding: utf-8 -*-

__doc__="""
Vertically centers selected Layers relative to a vertical metrics.
"""

from vanilla import FloatingWindow, PopUpButton, TextBox, CheckBox, Button
from AppKit import NSPoint



def align_xHeight():
	if PopUpButtonDemo.selectedLayers:
		x_height = font.selectedLayers[0].master.xHeight
		for layer in PopUpButtonDemo.selectedLayers:
			layerBottom = layer.bounds.origin.y
			layerHeight =  layer.bounds.size.height
			move_to = (x_height/2) - (layerHeight/2)
			offsetY = (layerBottom - move_to)*-1
		
			layer.applyTransform((
				1.0, # x scale factor
				0.0, # x skew factor
				0.0, # y skew factor
				1.0, # y scale factor
				0.0, # x position			
				offsetY  # y position
			))
			
def align_CapHeight():
	if PopUpButtonDemo.selectedLayers:
		x_height = font.selectedLayers[0].master.capHeight
		for layer in PopUpButtonDemo.selectedLayers:
			layerBottom = layer.bounds.origin.y
			layerHeight =  layer.bounds.size.height
			move_to = (x_height/2) - (layerHeight/2)
			offsetY = (layerBottom - move_to)*-1
		
			layer.applyTransform((
				1.0, # x scale factor
				0.0, # x skew factor
				0.0, # y skew factor
				1.0, # y scale factor
				0.0, # x position			
				offsetY  # y position
			))	
	
def align_Descender():
	if PopUpButtonDemo.selectedLayers:
		Descender = font.selectedLayers[0].master.descender
		for layer in PopUpButtonDemo.selectedLayers:
			layerBottom = layer.bounds.origin.y
			layerHeight =  layer.bounds.size.height
			move_to = (Descender/2) - (layerHeight/2)
			offsetY = (layerBottom - move_to)*-1
		
			layer.applyTransform((
				1.0, # x scale factor
				0.0, # x skew factor
				0.0, # y skew factor
				1.0, # y scale factor
				0.0, # x position			
				offsetY  # y position
			))	
    
def align_Ascender():
	if PopUpButtonDemo.selectedLayers:
		Ascender = font.selectedLayers[0].master.ascender
		for layer in PopUpButtonDemo.selectedLayers:
			layerBottom = layer.bounds.origin.y
			layerHeight =  layer.bounds.size.height
			move_to = (Ascender/2) - (layerHeight/2)
			offsetY = (layerBottom - move_to)*-1
		
			layer.applyTransform((
				1.0, # x scale factor
				0.0, # x skew factor
				0.0, # y skew factor
				1.0, # y scale factor
				0.0, # x position			
				offsetY  # y position
			))	
    

class PopUpButtonDemo:

	def __init__(self):
		self.w = FloatingWindow((260, 110), "Vertical Align Manager")
		self.w.TextBox = TextBox((10, 10, -10, 50), "Vertically align selected layers relative to :", sizeStyle="small")
		self.w.popUpButton = PopUpButton((10, 26, -10, 20), ["Ascender", "Cap Height", "x-Height", "Descender"], sizeStyle="small")
		self.w.checkBox = CheckBox((14, 48, -10, 20), "For all Masters", sizeStyle="small")
		self.w.button = Button((10, 80, -10, 20), "Run", callback=self.buttonCallback)
		self.w.open()

	def buttonCallback(self, sender):
		font = Glyphs.font
		PopUpButtonDemo.selectedLayers = font.selectedLayers
		
		if self.w.checkBox.get() == True:
			allLayers = []
			for layer in PopUpButtonDemo.selectedLayers:
				parent = layer.parent
				for layer in parent.layers:
					allLayers.append(layer)
			PopUpButtonDemo.selectedLayers = allLayers

			

		if self.w.popUpButton.getItem() == "x-Height":
			align_xHeight()
		if self.w.popUpButton.getItem() == "Ascender":
			align_Ascender()
		if self.w.popUpButton.getItem() == "Cap Height":
			align_CapHeight()
		if self.w.popUpButton.getItem() == "Descender":
			align_Descender()

PopUpButtonDemo()