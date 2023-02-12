#MenuTitle: Toggle Reporters
# -*- coding: utf-8 -*-

font = Glyphs.font
activeReporters = Glyphs.activeReporters

if not font.userData["com.hugojourdan.ToggleReporters"]:
	font.userData["com.hugojourdan.ToggleReporters"] = activeReporters
	
if len(activeReporters) != 0:
	font.userData["com.hugojourdan.ToggleReporters"] = activeReporters
	for reporter in font.userData["com.hugojourdan.ToggleReporters"]:
		Glyphs.deactivateReporter(reporter)
else:
	for reporter in font.userData["com.hugojourdan.ToggleReporters"]:
		 Glyphs.activateReporter(reporter)
