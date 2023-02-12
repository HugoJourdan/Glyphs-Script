# Glyphs Script

## `Anchors`
* **`Delete Anchors in all Masters for Selected Glyphs`**

<br>

## `App`
* **`Toggle Preview Blur`** : Useful if used with shortcut.
* **`Toggle Reporters`** : Show/Hide all activated reporters.

<br>

## `Color Label`
*Script for colour labels. Useful if you assign a keyboard shortcut to them*

* **`Set LayerColor to [XXX]`** : Change LayerColor to all Selected Glyph
* **`Update LayerColor of full Component Glyph`** : If a Glyph is made only with components, and if these components share same layer color label, sync it to the glyph.
* **`Remove ColorLayer for Selected Glyph in All Masters`**
* **`Swicth LayerColor to GlyphColor`** : If all layers of a Glyph has same LayerColor, set GlyphColor same and remove LayerColor Labels.
* **`Copy GlyphColor to None LayerColor`** : Copy GlyphColor to LayerColor is layer doesn't have Color Label.

<br>

## `Components`
* **`Propagande Component to other Masters`** : Copy components of selected layer to other masters if missing.
* **`Remove all Corner Component for Selected Master`**

<br>

## `Export`
* **`Export Trial Version`** : Export Trial version 
* **`Group and Rename Exports`** : Generate "FileName" and "Export Folder" CP for each instances.

<br>

## `Font Info`
* **`Set Axis Location for all masters and instances`** : Set "Axis Mapping" Custom Parameter in Font. For axes [wght] and [wdth], values are based on usWeightClass/usWidthClass from Exports. For custom axe, values are based on axes value from Exports.
If the font has masters corresponding exports, it will set "Axis Location" Custom Parameter to masters with value based on them.  
WeightClass and WidthClass values follow OpenType OS/2 specification"  

* **`Set Axis Location for all masters and instances`** : Set Axis Location for all masters and instances based on Weight Class and Width Class. (Only set Axis Location to master if they share same axe values as Insstance)

<br>

## `Guide`
* **`Create Guides for Marks`** : Create global guides based on circumflex position in Â and â. Guides are visible only in Uppercase and Lowercase.

## `Instance`
* **`Show Only Active Instances` :** Show only active Instances in Preview.

<br>

## `Layer`
* **`Clear Selected Glyph in all Masters`**
* **`Delete Special Layers for Selected Glyph`**
* **`Selects points above selection`**
* **`Selects points below selection`**
* **`Selects points right selection`**
* **`Selects points left selection`**
* **`Vertically Center Manager`** : User interface to vertically align layers to your vertical metrics.

<br>

## `Kerning`
* **`Report missing revelant Kerning Pairs`** : Report a list of possible revelant kerning pair missing for selected Master in Sample Strings array.
It use data from [Reveland Kerning Raw.json](https://github.com/andre-fuchs/kerning-pairs/blob/master/result/relevant_kerning_raw.json) by André Fuchs (@andre-fuchs)

<br>

## `Selection`
* **`Selected point handles`**

<br>

## `Spacing`
* **`Spacing String Maker`**

<br>

## `Tabs`
* **`Fit tab in EditView`**