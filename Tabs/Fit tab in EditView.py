#MenuTitle: Fit tab in EditView
# -*- coding: utf-8 -*-

# get current view port
editView = Font.currentTab
viewPort = editView.viewPort
margin = editView.bounds.size.width*0.05

# set position and size
viewPort.origin.x = editView.bounds.origin.x-margin/2
viewPort.origin.y = editView.bounds.origin.y
viewPort.size.width = editView.bounds.size.width+margin
viewPort.size.height = editView.bounds.size.height

# reposition view port of Edit View
editView.viewPort = viewPort
#editView.viewPort = viewPort

