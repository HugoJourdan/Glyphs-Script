#MenuTitle: Toggle Preview Blur
# -*- coding: utf-8 -*-
font = Glyphs.font

if not font.userData["com.hugojourdan.TogglePreviewBlurValue"]:
	font.userData["com.hugojourdan.TogglePreviewBlurValue"] = Font.currentTab.previewView().radius()

if Font.currentTab.previewView().radius() != 0:
	font.userData["com.hugojourdan.TogglePreviewBlurValue"] = Font.currentTab.previewView().radius()
	Font.currentTab.previewView().setRadius_(0)
else:
	Font.currentTab.previewView().setRadius_(font.userData["com.hugojourdan.TogglePreviewBlurValue"])
	font.userData["com.hugojourdan.TogglePreviewBlurValue"] = Font.currentTab.previewView().radius()
