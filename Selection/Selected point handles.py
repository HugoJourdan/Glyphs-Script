#MenuTitle: Selected point handles
# -*- coding: utf-8 -*-

for path in Layer.paths:
	for node in path.nodes:
		if node.selected:
			Layer.selection += node.nextNode, node.prevNode
			break