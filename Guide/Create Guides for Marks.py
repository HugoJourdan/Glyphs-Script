#MenuTitle: Create Guides for Marks
# -*- coding: utf-8 -*-

from AppKit import NSPoint, NSPredicate

font = Glyphs.font

for master in font.masters:
	upCase = font.glyphs["Acircumflex"].layers[master.id].shapes[1]
	lwCase = font.glyphs["acircumflex"].layers[master.id].shapes[1]
	uppercaseTopMark = upCase.bounds.origin.y
	uppercaseLowerMark = upCase.bounds.size.height+upCase.bounds.origin.y
	lowercaseTopMark = lwCase.bounds.origin.y
	lowercaseLowerMark = lwCase.bounds.size.height+lwCase.bounds.origin.y
	print(uppercaseTopMark,uppercaseLowerMark,lowercaseTopMark,lowercaseLowerMark)
	
	guideNames = ["Uppercase – Top Mark", "Uppercase – Lower Mark", "Lowercase – Top Mark", "Lowercase – Lower Mark"]

	try:
		for guideName in guideNames:
			for guide in master.guides:
				if guide.name == guideName:
					master.guides.remove(guide)
					break
	except:pass

	
	newGuide = GSGuide()
	newGuide.position = NSPoint(-500, uppercaseLowerMark)
	newGuide.name = "Uppercase – Lower Mark"
	newGuide.angle = 0
	newGuide.filter = NSPredicate.predicateWithFormat_("case == 1")
	master.guides.append(newGuide)
	
	newGuide = GSGuide()
	newGuide.position = NSPoint(-500, uppercaseTopMark)
	newGuide.name = "Uppercase – Top Mark"
	newGuide.angle = 0
	newGuide.filter = NSPredicate.predicateWithFormat_("case == 1")
	master.guides.append(newGuide)
	
	newGuide = GSGuide()
	newGuide.position = NSPoint(-500, lowercaseTopMark)
	newGuide.name = "Lowercase – Top Mark"
	newGuide.angle = 0
	newGuide.filter = NSPredicate.predicateWithFormat_("case == 2")
	master.guides.append(newGuide)
	
	newGuide = GSGuide()
	newGuide.position = NSPoint(-500, lowercaseLowerMark)
	newGuide.name = "Lowercase – Lower Mark"
	newGuide.angle = 0
	newGuide.filter = NSPredicate.predicateWithFormat_("case == 2")
	master.guides.append(newGuide)
	
	master.guides.append(newGuide)
	
	
