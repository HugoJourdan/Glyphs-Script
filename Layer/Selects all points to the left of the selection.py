#MenuTitle: Selects all points to the left of the selection
# -*- coding: utf-8 -*-

font = Glyphs.font

X = {}
for layer in font.selectedLayers:
	for path in layer.paths:
		selectedNode = []
		for node in path.nodes: 
			if node.selected:
				selectedNode.append(node)
		X[path]=selectedNode

for layer in font.selectedLayers:
	layer.clearSelection()	
	
for path, node in X.items():
	if path.direction == 1:
		try:
			while node[0] != node[1]:
				node[0] = node[0].prevNode
				node[0].selected = True
		except:pass
	else:
		try:
			while node[0] != node[1]:
				node[0] = node[0].nextNode
				node[0].selected = True
		except:pass
			
for path, node in X.items():
	try:
		for n in node:
			n.selected = False
	except:pass

