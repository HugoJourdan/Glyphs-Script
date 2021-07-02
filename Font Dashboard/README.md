# Font Dashboard

<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/thumbnail.jpg" width="620" />

This script allows you to follow the development progress of a file based on the Layer Color of your glyphs.  
(PS : Layer Color and not Glyph Color, to set Layer Color, you have to press RightClick + Option)

By default, the script is based on this color model :

<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/Default%20color%20system.jpg" width="200"/>


# Glyph Color vs Layer Color
First, it's important to understand difference between Glyph Color and Layer Color.  
## Glyph Color
To set Glyph Color you have to do a Right Click on a glyph. The Glyph Color of a glyph is shared with all your masters.    

<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/Glyph-Color_Example.jpg" width="200"/>.    
*("A' with Red Glyph Color)*

## Layer Color
Layer Color is specific to each masters, to set a Layer Color you have to do a Right Click and keep pressing Option key.  

<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/Layer-Color_Example.jpg" width="200"/>.    
*("A with Red Layer Color)*

## Glyph + Layer Color
This mean that a glyph can have only one Glyph Color, but many Layer Color (as many as number of masters).  
A glyph can have a Glyph Color and a Layer Color at same time.  


<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/Glyph-Color_and_Layer-Color_Example.jpg" width="200"/>.     
*("A with Red Glyph Color and LightGreen Layer Color)*

That's why this script is based on Layer Color and NOT on Glyph Color, to follow progress for each masters.


# Change Order and Color Description
To change the order and the description of the colors edit in the .py file these values :

```
positions = {
	Red: "Redrawing",
	Purple: "Check Anchors",
	LightBlue: "No Spacing",
	Yellow: "No Kerning",
	Magenta: "To Generate",
	Charcoal: "Not Exported",
	LightGreen: "Ready to Export",
	Orange: "",
	Brown: "",
	DarkGreen: "",
	DarkBlue: "",
	LightGray: "",
	NoColor: "",
}
```
