# -*- coding: utf-8 -*-
import sys
from bui.backend.render import RenderNode

class TestRenderNode():
    def test_create_render_node(self):
        render_node = RenderNode()
        
        assert render_node.children == []
        assert render_node.parents == []
        assert render_node.parent == None
        
        assert render_node.bg_color == None
        assert render_node.visible == True
        
        assert render_node.x == 0
        assert render_node.y == 0
        
        assert render_node.auto_width ==  False
        assert render_node.width == 0
        assert render_node.min_width == 0
        assert render_node.max_width == sys.maxint
        
        assert render_node.auto_height == False
        assert render_node.height == 0
        assert render_node.min_height == 0
        assert render_node.max_height == sys.maxint
    
    def test_append_render_node(self):
        render_node1, render_node2 = RenderNode(), RenderNode()
        
        render_node1.append(render_node2)
        
        assert render_node1.children[0] == render_node2
        assert render_node2.parents[0] == render_node1
        assert render_node2.parent == render_node1
    
    def test_remove_render_node(self):
        render_node1, render_node2 = RenderNode(), RenderNode()
        
        render_node1.append(render_node2)
        render_node1.remove(render_node2)
        
        assert len(render_node1.children) == 0
        assert len(render_node2.parents) == 0
        assert render_node2.parent == None
    
    # width
    # height
    # visibility
    # render
