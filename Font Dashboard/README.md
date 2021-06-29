# Font Dashboard

This script allows you to follow the development progress of a file based on the Layer Color of your glyphs.
(PS : Layer Color and not Glyph Color, to set Layer Color, you have to press RightClick + Option)

By default, the script is based on this color model :

<img src="https://github.com/HugoJourdan/Glyphs-Script/blob/main/Font%20Dashboard/Default%20color%20system.jpg" width="200"/>

# Change Color Order
To change the order of the colors edit in the .py file these values :

```
Position_1  = LayerColor_Red 
Position_2  = LayerColor_Purple 
Position_3  = LayerColor_LightBlue 
Position_4  = LayerColor_Yellow 
Position_5  = LayerColor_Magenta 
Position_6  = LayerColor_Charcoal 
Position_7  = LayerColor_LightGreen
Position_8  = LayerColor_Orange 
Position_9  = LayerColor_Brown 
Position_10 = LayerColor_DarkGreen 
Position_11 = LayerColor_DarkBlue 
Position_12 = LayerColor_LightGray 
Position_13 = LayerColor_NoColor 
```
# Change Color Description
To change color description edit in the .py file these values :
(PS : To hide a color, keep it empty)
```
LayerColor_Red = "Redrawing"
LayerColor_Purple = "Check Anchors"
LayerColor_LightBlue = "No Spacing"
LayerColor_Yellow = "No Kerning"
LayerColor_Magenta = "To Generate"
LayerColor_Charcoal = "Not Exported"
LayerColor_LightGreen = "Ready to Export"
LayerColor_Orange = ""
LayerColor_Brown = ""
LayerColor_DarkGreen = ""
LayerColor_DarkBlue = ""
LayerColor_LightGray = ""
LayerColor_NoColor = ""
```
