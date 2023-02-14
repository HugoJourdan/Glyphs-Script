# MenuTitle: CleanMyGlyphs 🧹✨
# -*- coding: utf-8 -*-
__doc__ = """
CleanMyGlyph is an all-in-one script to make your Glyphs file sparkle. 
It cleans up megatons of rubbish and makes your file look brand new. 
Just like the first day.
"""

from vanilla import*

# TO DO :
# - Add Layer Color
# - Add Glyph Color



class CleanMyGlyphWindow:
    def __init__(self):
        self.w = FloatingWindow((400, 220), "CleanMyGlyphs 🧹✨")
        self.w.title = TextBox("auto", "Delete in selected Glyphs in :")
        self.w.radio = HorizontalRadioGroup("auto",["Selected Master", "All Masters"])
        self.w.radio.set(0)
        self.w.anchor = CheckBox("auto", "Anchors")
        self.w.GROUP = Group("auto")
        self.w.GROUP.guide = CheckBox("auto", "Local Guides")
        self.w.GROUP.guideGlobal = CheckBox("auto", "Global Guides")
        nestRules = [
        "H:|[guide(==110)]-[guideGlobal]|",
        "V:|[guide]|"
        ]  

        
        
        self.w.SHAPE = Group("auto") 
        self.w.SHAPE.component = CheckBox("auto", "Components")
        self.w.SHAPE.path = CheckBox("auto", "Paths")
        SHAPERules = [
        "H:|[component(==110)]-[path(==110)]|",
        "V:|[component]|"
        ]  

        self.w.COLOR = Group("auto") 
        self.w.COLOR.glyphColor = CheckBox("auto", "Glyph Color")
        self.w.COLOR.layerColor = CheckBox("auto", "Layer Color")
        COLORRules = [
        "H:|[glyphColor(==110)]-[layerColor]|",
        "V:|[glyphColor]|"
        ]  


        self.w.LAYER = Group("auto") 
        self.w.LAYER.backupLayer = CheckBox("auto", "Backup Layer")
        self.w.LAYER.specialLayer = CheckBox("auto", "Special Layer")
        LAYERRules = [
        "H:|[backupLayer(==110)]-[specialLayer]|",
        "V:|[backupLayer]|"
        ] 
        
        
        self.w.hint = CheckBox("auto", "Hints")
        self.w.background = CheckBox("auto", "Background")
        self.w.annotation = CheckBox("auto", "Annotations")
        
        self.w.metricKey = CheckBox("auto", "Metrics Keys")
        self.w.kerningGroup = CheckBox("auto", "Kerning Groups")
        self.w.corner = CheckBox("auto", "Corners")
        self.w.tag = CheckBox("auto", "Tags")
        self.w.tab = CheckBox("auto", "Editview Tabs")
        
        self.w.run = Button("auto", "Run", callback=self.runCallback)
        self.w.setDefaultButton(self.w.run)

        self.w.sep1 = HorizontalLine("auto")
        self.w.sep2 = HorizontalLine("auto")
        self.w.sep3 = HorizontalLine("auto")
        self.w.sep4 = HorizontalLine("auto")
        self.w.sep5 = HorizontalLine("auto")
        self.w.sep6 = HorizontalLine("auto")
        self.w.sep7 = HorizontalLine("auto")
        self.w.sep8 = HorizontalLine("auto")
        self.w.sep9 = HorizontalLine("auto")
        self.w.sep10 = HorizontalLine("auto")
        self.w.sep11 = HorizontalLine("auto")
        self.w.sep12 = HorizontalLine("auto")
        

        
        rules = [
            # Horizontal
            "H:|-border-[title]-border-|",
            "H:|-border-[radio]-border-|",
            "H:|-border-[metricKey]-border-|",
            "H:|-border-[sep1]-border-|",
            "H:|-border-[kerningGroup]-border-|",
            "H:|-border-[sep2]-border-|",
            "H:|-border-[LAYER]-border-|",
            "H:|-border-[sep3]-border-|",
            "H:|-border-[anchor]-border-|",
            "H:|-border-[sep4]-border-|",
            "H:|-border-[GROUP]-border-|",
            "H:|-border-[sep5]-border-|",
            "H:|-border-[SHAPE]-border-|",
            "H:|-border-[sep6]-border-|",
            "H:|-border-[hint]-border-|",
            "H:|-border-[sep7]-border-|",
            "H:|-border-[background]-border-|",
            "H:|-border-[sep8]-border-|",
            "H:|-border-[annotation]-border-|",
            "H:|-border-[sep9]-border-|",
            "H:|-border-[corner]-border-|",
            "H:|-border-[sep10]-border-|",
            "H:|-border-[COLOR]-border-|",
            "H:|-border-[sep11]-border-|",
            "H:|-border-[tag]-border-|",
            "H:|-border-[sep12]-border-|",
            "H:|-border-[tab]-border-|",
            
            
            "H:|-border-[run]-border-|",
            
            # Vertical
            "V:|-border-[title]-space-[radio]-border-[metricKey]-space-[sep1]-space-[kerningGroup]-space-[sep2]-space-[LAYER]-space-[sep3]-space-[anchor]-space-[sep4]-space-[GROUP]-space-[sep5]-space-[SHAPE]-space-[sep6]-space-[hint]-space-[sep7]-space-[background]-space-[sep8]-space-[annotation]-space-[sep9]-space-[corner]-space-[sep10]-space-[COLOR]-space-[sep11]-space-[tag]-space-[sep12]-space-[tab]-border-[run]-border-|",

        ]
        metrics = {
            "border" : 20,
            "space" : 5
            
        }
        self.w.addAutoPosSizeRules(rules, metrics)
        self.w.GROUP.addAutoPosSizeRules(nestRules, metrics)
        self.w.SHAPE.addAutoPosSizeRules(SHAPERules, metrics)
        self.w.COLOR.addAutoPosSizeRules(COLORRules, metrics)
        self.w.LAYER.addAutoPosSizeRules(LAYERRules, metrics)

        self.w.open()
        self.w.center()


    def runCallback(self, sender):
        
        font = Glyphs.font

        selectedLayers = []
        if self.w.radio.get()==0:
            selectedLayers = font.selectedLayers
        else:
            for layer in font.selectedLayers:
                glyph = layer.parent
                for layer in glyph.layers:
                    selectedLayers.append(layer)
        
        for layer in selectedLayers:
            layer.parent.beginUndo()

            # Anchors
            if self.w.anchor.get()== True:
                for anchor in layer.anchors:
                    del(layer.anchors[anchor.name])

            # Path
            if self.w.SHAPE.path.get()== True:
                self.DeleteAllPaths(layer)

            # Backup Layers
            
            if self.w.LAYER.backupLayer.get()== True:
                self.DeleteAllBackupLayers(layer)

            # Component
            if self.w.SHAPE.component.get()== True:
                self.DeleteAllComponent(layer)

            # Background
            if self.w.background.get()== True:
                layer.background.clear()

            # Annotations
            if self.w.annotation.get()== True:
                self.DeleteAllAnnotations(layer)

            # Hints
            if self.w.hint.get()== True:
                self.DeleteAllHints(layer)

            # Corner Component
            if self.w.hint.get()== True:
                self.DeleteAllCornerComponent(layer)

            # Layer Color
            if self.w.COLOR.layerColor.get()== True:
                layer.color = None

            # Glyph Color
            if self.w.COLOR.glyphColor.get()== True:
                glyph = layer.parent
                if glyph.color:
                    glyph.color = None
            
            # Corner Component
            if self.w.hint.get()== True:
                self.DeleteAllCornerComponent(layer)

            # Tags
            if self.w.tag.get()== True:
                self.DeleteAllTags(layer)

            # Tags
            if self.w.metricKey.get()== True:
                self.DeleteMetricKey(layer)
                
            layer.parent.endUndo()
        Glyphs.redraw()


        if self.w.tab.get()==True:
            for i in range(len(font.tabs)):
                del font.tabs[0]

    def DeleteMetricKey(self, thisLayer):
        if self.w.radio.get()==0:
            print("m")
            thisLayer.rightMetricsKey = thisLayer.leftMetricsKey = thisLayer.widthMetricsKey = None
        if self.w.radio.get()==1:
            glyph = thisLayer.parent
            glyph.rightMetricsKey = glyph.leftMetricsKey = glyph.widthMetricsKey = None
    
    def DeleteAllTags(self, thisLayer):
        glyph = thisLayer.parent
        for i in range(len(glyph.tags)):
            #print(f"{list(glyph.tags)} tags removed in {glyph.name}")
            del glyph.tags[i]

    def DeleteAllCornerComponent(self, thisLayer):
        for i in range(len(thisLayer.hints))[::-1]:
            if thisLayer.hints[i].type == CORNER:
                #print(f"{list(thisLayer.hints[i].name)} hints removed in {thisLayer.name}")
                del thisLayer.hints[i]
                
    def DeleteAllBackupLayers(self, thisLayer):
        associateLayers = [layer.layerId for layer in thisLayer.parent.layers if layer.associatedMasterId == thisLayer.associatedMasterId]

        for layerID in associateLayers:
            del(glyph.layers[layerID])
                
    def DeleteAllHints(self, thisLayer):
        for i in range(len(thisLayer.hints)):
            del thisLayer.hints[0]
        
    def DeleteAllAnnotations(self, thisLayer):
        for i in range(len(thisLayer.annotations)):
            del thisLayer.annotations[0]
        
    def DeleteAllPaths(self, thisLayer):
        for i in range(len(thisLayer.shapes)-1, -1, -1):
            path = thisLayer.shapes[i]
            if isinstance(path, GSPath):
                del thisLayer.shapes[i]
        
    def DeleteAllComponent(self, thisLayer):
        for i in range(len(thisLayer.shapes)-1, -1, -1):
            path = thisLayer.shapes[i]
            if isinstance(path, GSComponent):
                del thisLayer.shapes[i]
CleanMyGlyphWindow()