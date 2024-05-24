# MenuTitle: Export Trial Version
# -*- coding: utf-8 -*-

__doc__ = """
Export trials for all active instances (except variable instance)
"""

from vanilla import FloatingWindow, TextBox, TextEditor, PopUpButton, Button
from GlyphsApp import Glyphs, GSFeature, GetFolder, Message, PLAIN, TTF, OTF, WOFF, WOFF2


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
		self.w = FloatingWindow((x, y, 400, 200), title="Export trials version")
		self.w.textBox = TextBox((inset, linePos, -inset, 17), "Trial glyphset (All glyphs need to be separated by a comma)", sizeStyle='small')
		self.w.textBox.getNSTextField().setToolTip_("All glyphs need to be separated by a comma")

		linePos += lineHeight

		self.w.textEditor = TextEditor((inset, linePos, -inset, 100), text=defaultTrialGlyphset, callback=self.textEditorCallBack)
		linePos += 88
		linePos += lineHeight

		self.w.text = TextBox((inset, linePos, -inset, 40), "Export format :", sizeStyle='small')
		self.w.popUpButton = PopUpButton((inset + 85, linePos - 2, -inset - 220, 17), [TTF, OTF, WOFF, WOFF2], sizeStyle='small')

		linePos += lineHeight

		self.w.buttonFolder = Button((inset, linePos, -inset - 188, 20), "Select Save Folder", callback=self.buttonFolderCallback)
		self.w.buttonGenerate = Button((inset + 188, linePos, -inset, 20), "Generate trials", callback=self.buttonGenerateCallback)
		self.w.buttonGenerate.enable(False)
		self.w.setDefaultButton(self.w.buttonGenerate)

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
		Glyphs.font.disableUpdateInterface()
		Glyphs.clearLog()
		Glyphs.showMacroWindow()
		print("[Export Trial Version is running]\nSave location : %s" % SaveFolder)

		global trialGlyphset
		trialGlyphset = self.w.textEditor.get()
		fontFormat = self.w.popUpButton.getItem()
		document = Glyphs.currentDocument
		font = document.font

		instanceActive = []

		global exportedGlyphsSave
		exportedGlyphsSave = []
		global featuresSave
		featuresSave = {}

		for glyph in font.glyphs:
			if glyph.export is True:
				exportedGlyphsSave.append(glyph.name)

		for classe in font.classes:
			classe.active = False

		for feature in font.features:
			featuresSave[feature.name] = feature.code, feature.automatic

		# Disable export for all glyphs
		for glyph in font.glyphs:
			glyph.export = False

		# Enable export for defaultTrialGlyphset glyphs
		for glyph in font.glyphs:
			if glyph.name in defaultTrialGlyphset:
				glyph.export = True

		# Update all features(twice for aalt)
		for feature in font.features:
			del font.features[0]

		font.updateFeatures()

		if fontFormat in (TTF, OTF):
			fontFormat = PLAIN

		for instance in font.instances:
			if instance.active:
				instanceActive.append(instance.name)

		print("════════════════════════════════════════════════════════\nFont : %s\nActive Instance : %s\n════════════════════════════════════════════════════════" % (font.familyName, len(instanceActive)))

		for instance in font.instances:
			if instance.active:
				if instance.familyName:
					instance.familyName = instance.familyName.replace(" ", "-")
					savedInstanceName = instance.name
					instance.name = instance.name.replace(" ", "-") + str("-TRIAL")

					exportStatement = instance.generate(FontPath=SaveFolder, Containers=[fontFormat])
					instance.name = savedInstanceName
					if exportStatement is not True:
						print(exportStatement)
						print("⚠️ %s %s-Trial not generated correctly\n⚠️ (Export it with Cmd+E to access export report)\n--------------------------------------------------------" % (instance.familyName, instance.name))
					else:
						print("✅ %s %s-Trial generated\n--------------------------------------------------------" % (instance.familyName, instance.name))

				else:
					savedInstanceName = instance.name
					instance.name = instance.name.replace(" ", "-") + str("-Trial")
					exportStatement = instance.generate(FontPath=SaveFolder, Containers=[fontFormat])
					instance.name = savedInstanceName
					if exportStatement is not True:
						print(exportStatement)
						print("⚠️ %s-Trial not generated correctly\n⚠️ (Export it with Cmd+E to access export report)\n--------------------------------------------------------" % savedInstanceName)
					else:
						print("✅ %s-Trial generated\n--------------------------------------------------------" % savedInstanceName)
			else:
				pass
		# T his duration depending on the number of glyphs in your font
		print("Restoring initial instances... (it can last a minute)")

		# Disable export for defaultTrialGlyphset glyphs
		for item in defaultTrialGlyphset:
			font.glyphs[item].export = False

		# Restore exported glyphs from exportedGlyphSave
		for item in exportedGlyphsSave:
			font.glyphs[item].export = True

		for feature in font.features:
			del font.features[0]

		# Restore feature from featuresSave
		for item in featuresSave:
			font.features.append(GSFeature(item, featuresSave[item][0]))
			font.features[item].automatic = featuresSave[item][1]

		for classe in font.classes:
			classe.active = True

		Message("All exports are done", title='Trial Exports', OKButton=None)
		Glyphs.font.enableUpdateInterface()


TextEditorDemo()
