#MenuTitle: Export Trial Version 
# -*- coding: utf-8 -*-
__doc__="""
Export trials for all active instances (except variable instance)
"""
from vanilla import*







class TextEditorDemo:
	
	global defaultTrialGlyphset
	
	
	if not Glyphs.defaults["com.hugjourdan.ExportFontTrials.defaultTrialGlyphset"]:
		defaultTrialGlyphset = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v ,w, x, y, z, zero, one, two, three, four, five, six, seven, eight, nine, space, comma, period, parenleft, parenright, exclam, question, at, ampersand, .notdef"
	else:
		defaultTrialGlyphset = Glyphs.defaults["com.hugjourdan.ExportFontTrials.defaultTrialGlyphset"]
		
	def __init__(self):
		linePos, inset, lineHeight = 12, 15, 22
		
		if not Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosX"]:
			Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosX"] = 200
		if not Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosY"]:
			Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosY"] = 200
		
		x = Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosX"]
		y = Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosY"]
		self.w = FloatingWindow((x,y ,400, 200), title="Export trials version")
		self.w.textBox = TextBox((inset, linePos, -inset, 17), "Trial glyphset (All glyphs need to be separated by a comma)", sizeStyle='small')
		self.w.textBox.getNSTextField().setToolTip_(u"All glyphs need to be separated by a comma")
		
		linePos += lineHeight
		
		self.w.textEditor = TextEditor((inset, linePos, -inset, 100), text=defaultTrialGlyphset, callback=self.textEditorCallBack)
		linePos += 88
		linePos += lineHeight
		
		self.w.text = TextBox((inset, linePos, -inset, 40), "Export format :", sizeStyle='small')
		self.w.popUpButton = PopUpButton((inset+85, linePos-2, -inset-220, 17),["TTF", "OTF", "WOFF", "WOFF2"], sizeStyle='small')
		
		linePos += lineHeight
		
		
		self.w.buttonFolder = Button((inset, linePos, -inset-188, 20), "Select Save Folder", callback=self.buttonFolderCallback)
		self.w.buttonGenerate = Button((inset+188, linePos, -inset, 20), "Generate trials", callback=self.buttonGenerateCallback)
		self.w.buttonGenerate.enable(False)
		self.w.setDefaultButton( self.w.buttonGenerate)
		
		self.w.bind("close", self.windowClosed)
		self.w.open()
	def textEditorCallBack(self, sender):
		Glyphs.defaults["com.hugjourdan.ExportFontTrials.defaultTrialGlyphset"] = sender.get()
	
	def windowClosed(self, sender):
		windowPosSize = self.w.getPosSize()
		Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosX"] = windowPosSize[0]
		Glyphs.defaults["com.hugjourdan.ExportFontTrials.windowPosY"] = windowPosSize[1]
		

	
	def buttonFolderCallback(self, sender):
		global SaveFolder
		SaveFolder = GetFolder(message='Select save location', allowsMultipleSelection=False, path=None)
		if SaveFolder:
			self.w.buttonGenerate.enable(True)

	def buttonGenerateCallback(self, sender):
		Font.disableUpdateInterface()
		Glyphs.clearLog()
		Glyphs.showMacroWindow()
		print("[Export Trial Version is running]\nSave location : %s" % SaveFolder)
		
		
		global trialGlyphset
		trialGlyphset = self.w.textEditor.get()
		fontFormat = self.w.popUpButton.getItem()
		document = Glyphs.currentDocument
		font = document.font
		
		instanceActive = []
		fontClass = []
		exportedGlyphsSave = []
		featuresSave = {}
		
		for glyph in font.glyphs:
			if glyph.export is True:
				exportedGlyphsSave.append(glyph.name)
		
		for classe in font.classes:
			classe.active = False
		
		for feature in font.features:
			featuresSave[feature.name]=feature.code
		
		#Disable export for all glyphs	
		for glyph in font.glyphs:
			glyph.export = False
		
		
		#Enable export for defaultTrialGlyphset glyphs
		for glyph in font.glyphs:
			if glyph.name in defaultTrialGlyphset:
				glyph.export = True
					
		#Update all features(twice for aalt)
		for feature in font.features:
			feature.update()
		for feature in font.features:
			feature.update()
		
		if fontFormat == "TTF":
			fontFormat = "plain"
		
		
		for instance in font.instances:
			if instance.active == True and instance.type == 0 :
				instanceActive.append(instance.name)
				



		
		
		print("════════════════════════════════════════════════════════\nFont : %s\nActive Instance : %s\n════════════════════════════════════════════════════════" % (font.familyName, len(instanceActive)))

		for instance in font.instances:
			if instance.active == True:
				
				#If instance is INSTANCETYPESINGLE
				if instance.type == 0 :
					
					if instance.familyName:
						savedInstanceName = instance.familyName
						instance.familyName = instance.familyName.replace(" ", "-") + str("-Trial")
						instance.customParameters["Keep Glyphs"] = trialGlyphset
						instance.generate(FontPath = SaveFolder, Containers = [fontFormat])						
						instance.familyName = savedInstanceName
						if (instance.generate(FontPath = SaveFolder, Containers = [fontFormat])) is not True:
							print("⚠️ %s-Trial cannot be generated (check compatibility)\n--------------------------------------------------------" % (instance.familyName, instance.name))
						else:
							print("🅰️ %s %s-Trial generated\n--------------------------------------------------------" % (instance.familyName, instance.name))
					
					else :
						savedInstanceName = instance.name
						instance.name = instance.name.replace(" ", "-") + str("-Trial")
						instance.customParameters["Keep Glyphs"] = trialGlyphset
						instance.generate(FontPath = SaveFolder, Containers = [fontFormat])
						instance.name = savedInstanceName
						if (instance.generate(FontPath = SaveFolder, Containers = [fontFormat])) is not True:
							print("⚠️ %s-Trial cannot be generated (check compatibility)\n--------------------------------------------------------" % savedInstanceName)
						else:
							print("🅰️ %s-Trial generated\n--------------------------------------------------------" % savedInstanceName)
				else:
					pass
		# Delete Keep Glyph CP created
		for instance in font.instances:
			del(instance.customParameters["Keep Glyphs"])
		#Disable export for defaultTrialGlyphset glyphs
		for glyph in font.glyphs:
			if glyph.name in defaultTrialGlyphset:
				glyph.export = False
		
		#Restore exported glyphs from exportedGlyphSave
		for glyph in font.glyphs:
			if glyph.name in exportedGlyphsSave:
				glyph.export = True
		
		#Restore feature from featuresSave
		for i in featuresSave:
			for feature in font.features:
				if feature.name == i:
					feature.code = featuresSave[i]
					
		for classe in font.classes:
			classe.active = True
				
		Message("All exports are done",title='Trial Exports', OKButton=None)
		Font.enableUpdateInterface()
		
		
TextEditorDemo()
