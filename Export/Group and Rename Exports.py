# MenuTitle: Group and Rename Exports
font = Glyphs.font

for instance in font.instances:
	if instance.familyName:
		instance.customParameters["Export Folder"] = instance.familyName
		instance.customParameters["fileName"] = f"{instance.familyName} {instance.name}".replace(" ", "-")
	else:
		instance.customParameters["Export Folder"] = font.familyName
		instance.customParameters["fileName"] = f"{font.familyName} {instance.name}".replace(" ", "-")
	
	
