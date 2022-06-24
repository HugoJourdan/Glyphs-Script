#MenuTitle: Generate "Axis Mappings" & "Axis Location"
# -*- coding: utf-8 -*-

__doc__ = """
Will set "Axis Mapping" Custom Parameter in Font. For axes [wght] and [wdth], values are based on usWeightClass/usWidthClass from Exports. For custom axe, values are based on axes value from Exports.
If the font has masters corresponding exports, it will set "Axis Location" Custom Parameter to masters with value based on them.
WeightClass and WidthClass values follow OpenType OS/2 specification"

"""


Message("Axis Mappings are not always working as expected in 3.0.x, and may create faulty entries in the fvar table.", title='⚠️', OKButton=None)

font = Glyphs.font
AxisMappingsDic = {}
AxisIndexDic = {}

scriptName = "Generate Axis Mappings CP"

print("[Adding Axis Mapping]\n")
axeIndex = -1
for axe in font.axes:
	axeMappingDic = {}
	axeIndex += 1	
	axeTag = axe.axisTag
	AxisMappingsDic[axe.axisTag]=None
	for instance in font.instances:
		if instance.type == 0:
			axeValue = instance.axes[axeIndex]
			if axeTag == "wght":
				mapValue = instance.weightClass

			elif axeTag == "wdth":
				if instance.widthClass <= 7:
					mapValue = (instance.widthClass-1)*12.5+50
				if instance.widthClass == 8:
					mapValue = 150
				if instance.widthClass == 9:
					mapValue = 200
			else:
				mapValue = instance.axes[axeIndex]
			axeMappingDic[axeValue]=mapValue
	AxisMappingsDic[axe.axisTag]=axeMappingDic

font.customParameters["Axis Mappings"]=AxisMappingsDic
print('✅ FontInfo > Font > Custom Parameters "Axis Mappings" added\n')
print("-"*60)


print("\n[Adding Axis Location]\n")
for master in font.masters:
	allAxisLocation = ()
	axeIndex = -1
	for axe in font.axes:
		axeIndex += 1
		axisLocationDic = {}
		if master.axes[axeIndex] in AxisMappingsDic[axe.axisTag]:
			axisLocationDic = {"Axis":axe.name, "Location":""}
			axisLocationDic["Location"]= AxisMappingsDic[axe.axisTag][master.axes[axeIndex]]
		else:
			print('⚠️ %s Master > CP "Axis Location" [%s] value cannot be set, set in manually (default value is 999)\n' % (master.name, axe.name))
			axisLocationDic = {"Axis":axe.name, "Location":"999"}
		allAxisLocation = list(allAxisLocation)
		allAxisLocation.append(axisLocationDic)
		allAxisLocation = tuple(allAxisLocation)
	master.customParameters["Axis Location"]=(allAxisLocation)
	
print('✅ FontInfo > Masters > Custom Parameters "Axis Location" added for each masters')
