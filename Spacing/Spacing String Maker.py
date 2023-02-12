#MenuTitle: Spacing String Maker
# -*- coding: utf-8 -*-

font = Glyphs.font

spacingString = []
for g in font.glyphs:
	if g.name.endswith('.sc'):
		spacingString.append("/h.sc/o.sc/h.sc/o.sc/h.sc"+"/"+g.name+"/ nonon")
	else:
		spacingString.append("HOHOH"+"/"+g.name+"/ nonon")
	


def addToSampleText( kernStrings, marker="### CUSTOM KERN STRING ###"):
	if kernStrings is None:
		print("No kern strings generated.")
		return False
	else:
		# Get current sample texts:
		if Glyphs.versionNumber >= 3:
			# Glyphs 3 code
			
			kernStringLines = "\n".join(kernStrings)
			newKernStringEntry = dict( name=marker, text=kernStringLines )
			sampleTexts = Glyphs.defaults["SampleTextsList"].mutableCopy()

			# clear old kern strings with same marker:
			indexesToRemove = []
			#print(sampleTexts)
			for index, sampleTextEntry in enumerate(sampleTexts):
				if sampleTextEntry["name"] == marker: # there could be multiple ones
					indexesToRemove.append(index)
			for index in reversed(indexesToRemove):
				sampleTexts.removeObjectAtIndex_(index)
			
			
			# build new kern string entry :
			sampleTexts.append(newKernStringEntry)
			
			Glyphs.defaults["SampleTextsList"] = sampleTexts
			return True
		else:
			# Glyphs 2 code
			# Get current sample texts:
			sampleTexts = Glyphs.defaults["SampleTexts"].mutableCopy()
		
			# Cut off after marker text:
			i = sampleTexts.indexOfObject_(marker)
			if i == NSNotFound:
				print("Warning: Could not find this marker:\n%s\nAppending it..." % marker)
				sampleTexts.append(marker)
			else:
				sampleTexts = sampleTexts[:i+1]
		
			# Add new kern strings to the list:
			if len(kernStrings) > 0:
				sampleTexts.extend(kernStrings)
			else:
				return False
		
			# Exchange the stored Sample Texts with the new ones:
			Glyphs.defaults["SampleTexts"] = sampleTexts
			return True
			
addToSampleText( spacingString , marker="Spacing Strings")
print("✅ %s Spacing String has been generated\nLocated in Edit > Select Sample Text > Spacing Strings" % len(spacingString))