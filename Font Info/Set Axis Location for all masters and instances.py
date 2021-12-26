#MenuTitle: Set Axis Location for all masters and instances
# -*- coding: utf-8 -*-
__doc__="""
Set Axis Location for all masters and instances based on Weight Class and Width Class"""


font = Glyphs.font
fontAxes = []
instancewidthClass = []
instanceweightClass = []
exportAxesValues = {}
axeCount = -1

for axe in font.axes:
	fontAxes.append(axe.name)

for instance in font.instances:
	instancewidthClass.append(instance.widthClass)
	instanceweightClass.append(instance.weightClass)

# Warning messages if widthClass and weightClass are potentially not correclty set
if (all(instanceweightClass)) == True:
	print("⚠️ All instances Weight Class have the same value.\n Weight Class need to be set correctly for the script to work properly.\n If you have only one weight in your font, ignore this warning.\n"
)
if (all(instancewidthClass)) == True:
	print("⚠️ All instances Width Class have the same value.\n Width Class need to be set correctly for the script to work properly.\n If you have only one width in your font, ignore this warning.\n")



# Set Axis Location Custom Parameter for each instances
for instance in font.instances:

	exportAxes = []	
	axisIndex = -1
	for i in fontAxes:
		axisIndex += 1
		exportAxesValues[i]=instance.axes[axisIndex]
	for i in exportAxesValues :
		print(i)
		if i == "Weight":
			exportAxes.append({"Axis":"Weight", "Location":instance.weightClass})
		elif i == "Width":
			exportAxes.append({"Axis":"Width", "Location":instance.widthClass*20})
		else:
			exportAxes.append({"Axis":i, "Location":exportAxesValues[i]})
	print("Export Info from '%s' instance has been updated" % (instance.name))
	instance.customParameters['Axis Location'] = exportAxes

# Set Axis Location Custom Parameter for eache masters
# ⚠️ this work only if a master share same axe values as an instance.
for master in font.masters:
	for instance in font.instances :
		for master in font.masters:
			if master.axes == instance.axes :
				axisLocation = instance.customParameters['Axis Location']
				master.customParameters['Axis Location'] = axisLocation
				print("%s master copied 'Axis Location' from %s instance" % ( master.name, instance.name))
			else :
				print("%s master 'Axis Location' cannot be set because no instance shares same axis values." % (master.name))
		
		
	print("Export Info from '%s' master has been updated" % (master.name))
	master.customParameters['Axis Location'] = exportAxes


