#MenuTitle: Set weightClass for instances
# -*- coding: utf-8 -*-
__doc__="""
Try to set weightClass (USWeightClass) values for each instances based on naming "
"""


font = Glyphs.font

# Set USWeightClass values for instances based on naming
for instance in font.instances:
	if "Thin" in instance.name or "Hair" in instance.name or "Hairline" in instance.name:
		instance.weightClass = 100
	if "Light" in instance.name:
		instance.weightClass = 300
	if "ExtraLight" in instance.name or "UltraLight" in instance.name:
		instance.weightClass = 200
	if "Regular" in instance.name or "Normal" in instance.name:
		instance.weightClass = 400
	if "Medium" in instance.name:
		instance.weightClass = 500
	if "Bold" in instance.name:
		instance.weightClass = 700
	if "SemiBold" in instance.name or "DemiBold" in instance.name:
		instance.weightClass = 600
	if "ExtraBold" in instance.name or "UltraBold" in instance.name:
		instance.weightClass = 800
	if "Black" in instance.name or "Heavy" in instance.name:
		instance.weightClass = 900