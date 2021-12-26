#MenuTitle: Set STAT tables for instances (BETA)
# -*- coding: utf-8 -*-
__doc__=""" Set STAT tables for instances. This script is in BETA Version"
"""


font = Glyphs.font
fontAxes = []
exportAxesValues = {}
axeCount = -1
	
for axe in font.axes:
	fontAxes.append(axe.axisTag)
	
# Delete all CP related to STAT
for instance in font.instances:
	instanceParameters = []
	for parameter in instance.customParameters:
		if "STAT" in parameter.name:
			instanceParameters.append(parameter.name)
	for i in instanceParameters:
		del(instance.customParameters[i])

# Detect if another axe values except Width and Weight axes are diffrent from 0
for instance in font.instances:
	OtherAxeInstance = True
	OtherAxeInstanceDic = []
	for tag in fontAxes:
		if tag == "wght" or tag == "wdth":
			pass
		else:
			indexTag = fontAxes.index(tag)
			OtherAxeInstanceDic.append(instance.axes[indexTag])
	print(OtherAxeInstanceDic)
	if (all(x == 0 for x in OtherAxeInstanceDic)) == True :
		OtherAxeInstance = False
	

	# Set STAT Entry and Elidable for Instances if:
	#	Width = Medium(normal) 5
	#	Weight = Regular(400)
	#	All other Axes Values equal 0
	if instance.widthClass == 5 and instance.weightClass == 400 and OtherAxeInstance == False :
		for tag in fontAxes:
			indexTag = fontAxes.index(tag)
			instance.customParameters['Style Name as STAT entry %s' % (indexTag)] = tag
			if tag != "wght":
				instance.customParameters['Elidable STAT Axis Value Name %s' % (indexTag)] = tag
	
	# Set STAT Entry and Elidable for Instances if:
	#	Width = Medium(normal) 5
	#	Weight = All except Regular(400)
	#	All other Axes Values equal 0
	# Set STAT Entry for Instances with "Normal" Width but not "Regular" Weight
	if instance.widthClass == 5 and instance.weightClass != 400 and OtherAxeInstance == False  :
		instance.customParameters['Style Name as STAT entry'] = "wght"
	
	# Set STAT Entry and Elidable for Instances if:
	#	Width = All except Medium(normal) 5
	#	Weight = Regular(400)
	#	All other Axes Values equal 0
	if instance.widthClass != 5 and instance.weightClass == 400 and OtherAxeInstance == False  :
		instance.customParameters['Style Name as STAT entry'] = "wdth"

	# Set STAT Entry and Elidable for Instances if:
	#	Width = Medium(normal) 5
	#	Weight = Regular(400)
	#	One other axes except(Weight/Width) not equal 0
	for indexTag in fontAxes:
		if indexTag == "wght" or indexTag == "wdth":
			pass
		else:
			indexTag = fontAxes.index(indexTag)
			if instance.axes[indexTag] != 0 :
				if instance.widthClass == 5 and instance.weightClass == 400 and OtherAxeInstance == True :
					instance.customParameters['Style Name as STAT entry %s' % (indexTag)] = fontAxes[indexTag]
					break


	# Delete last char of CP with "STAT" in string name
	for parameter in instance.customParameters:
		if "STAT" in parameter.name:
			parameter.name = parameter.name[:-1]
			
