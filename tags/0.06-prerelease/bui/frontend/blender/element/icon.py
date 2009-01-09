# -*- coding: utf-8 -*-
import Blender
from Blender import Draw
from bui.graphics.opengl.decorators import enable_alpha
from abstract import AbstractBlenderElement
from utils import load_image

class Icon(AbstractBlenderElement):
    def initialize(self, **kvargs):
        """ Adapted from txtPyBrowser114j.py by Remigiusz Fiedler """
        def get_icon_position(index):
            row = index / 25
            col = index - (row * 25)
            return row, col
        
        self.file = 'blenderbuttons.png'
        super(Icon, self).initialize(**kvargs)
        
        index = BLENDER_ICONS.index(self.name)
        row, col = get_icon_position(index)
        self.width = 20
        self.height = 21
        self.clip_x = col * self.width + 3
        self.clip_y = row * self.height + 3
        self.clip_width = 15
        self.clip_height = 15
        
        uscriptsdir = Blender.Get('uscriptsdir')
        self.image_block = load_image(uscriptsdir, self.file)
    
    @enable_alpha
    def render(self):
        Draw.Image(self.image_block, self.x, self.y, 1.0, 1.0, self.clip_x,
                   self.clip_y, self.clip_width, self.clip_height)

BLENDER_ICONS = [
    'view3d',
    'ipo',
    'oops',
    'buts',
    'filesel',
    'image_col',
    'info',
    'sequence',
    'text',
    'imasel',
    'sound',
    'action',
    'nla',
    'scriptwin',
    'time',
    'node',
    'space2',
    'space3',
    'space4',
    'left_triangle',
    'up_triangle',
    'fontpreview',
    'blank4',
    'wordwrap',
    'wordwrap_off',
    
    'ortho',
    'persp',
    'camera',
    'particles',
    'bbox',
    'wire',
    'solid',
    'smooth',
    'potato',
    'marker_hlt',
    'pmarker_act',
    'pmarker_sel',
    'pmarker',
    'viewzoom',
    'sortalpha',
    'sorttime',
    'sortsize',
    'longdisplay',
    'shortdisplay',
    'down_triangle',
    'right_triangle',
    'ndof_turn',
    'ndof_fly',
    'ndof_trans',
    'ndof_dom',
    
    'view_axis_all',
    'view_axis_none',
    'view_axis_none2',
    'view_axis_top',
    'view_axis_front',
    'view_axis_side',
    'pose_dehlt',
    'pose_hlt',
    'bordermove',
    'maybe_its_a_lasso',
    'blank1',
    
    'verse',
    'mod_boolean',
    'armature',
    'pause',
    'align',
    'rec',
    'play',
    'ff',
    'rew',
    'python',
    'python_on',
    'blank12',
    'blank13',
    'blank14',
    
    'dotsup',
    'dotsdown',
    'menu_panel',
    'axis_side',
    'axis_front',
    'axis_top',
    'sticky_uvs_loc',
    'sticky_uvs_disable',
    'sticky_uvs_vert',
    'prev_keyframe',
    'next_keyframe',
    'envmap',
    'transp_hlt',
    'transp_dehlt',
    'circle_dehlt',
    'circle_hlt',
    'tpaint_dehlt',
    'tpaint_hlt',
    'wpaint_dehlt',
    'wpaint_hlt',
    'marker',
    'blank15',
    'blank16',
    'blank17',
    'blank18',
    
    'x',
    'go_left',
    'no_go_left',
    'unlocked',
    'locked',
    'parlib',
    'datalib',
    'auto',
    'material_dehlt2',
    'ring',
    'grid',
    'propedit',
    'keeprect',
    'desel_cube_verts',
    'editmode_dehlt',
    'editmode_hlt',
    'vpaint_dehlt',
    'vpaint_hlt',
    'facesel_dehlt',
    'facesel_hlt',
    'edit_dehlt',
    'bookmarks',
    'blank20',
    'blank21',
    'blank22',
    
    'help',
    'error',
    'folder_dehlt',
    'folder_hlt',
    'blueimage_dehlt',
    'blueimage_hlt',
    'bpibfolder_dehlt',
    'bpibfolder_hlt',
    'bpibfolder_err',
    'ugly_green_ring',
    'ghost',
    'sortbyext',
    'sculptmode_hlt',
    'vertexsel',
    'edgesel',
    'facesel',
    'plus',
    'bpibfolder_x',
    'bpibfoldergrey',
    'magnify',
    'info2',
    'blank23',
    'blank24',
    'blank25',
    'blank26',
    
    'rightarrow',
    'downarrow_hlt',
    'roundbevelthing',
    'fulltexture',
    'hook',
    'dot',
    'world_dehlt',
    'checkbox_dehlt',
    'checkbox_hlt',
    'link',
    'inlink',
    'zoomin',
    'zoomout',
    'pastedown',
    'copydown',
    'constant',
    'linear',
    'cyclic',
    'key_dehlt',
    'key_hlt',
    'grid2',
    'blank27',
    'blank28',
    'blank29',
    'blank30',
    
    'eye',
    'lamp',
    'material',
    'texture',
    'anim',
    'world',
    'scene',
    'edit',
    'game',
    'paint',
    'radio',
    'script',
    'speaker',
    'pasteup',
    'copyup',
    'pasteflipup',
    'pasteflipdown',
    'cycliclinear',
    'pin_dehlt',
    'pin_hlt',
    'littlegrid',
    'blank31',
    'blank32',
    'blank33',
    'blank34',
    
    'fullscreen',
    'splitscreen',
    'rightarrow_thin',
    'disclosure_tri_right',
    'disclosure_tri_down',
    'scene_sepia',
    'scene_dehlt',
    'object',
    'mesh',
    'curve',
    'mball',
    'lattice',
    'lamp_dehlt',
    'material_dehlt',
    'texture_dehlt',
    'ipo_dehlt',
    'library_dehlt',
    'image_dehlt',
    'eyedropper',
    'window_window',
    'panel_close',
    'physics',
    'layer_used',
    'layer_active',
    'blank38',
    
    'blender',
    'package',
    'uglypackage',
    'matplane',
    'matsphere',
    'matcube',
    'scene_hlt',
    'object_hlt',
    'mesh_hlt',
    'curve_hlt',
    'mball_hlt',
    'lattice_hlt',
    'lamp_hlt',
    'material_hlt',
    'texture_hlt',
    'ipo_hlt',
    'library_hlt',
    'image_hlt',
    'constraint',
    'camera_dehlt',
    'armature_dehlt',
    'snap_gear',
    'snap_geo',
    'snap_normal',
    'blank42',
    
    'smoothcurve',
    'spherecurve',
    'rootcurve',
    'sharpcurve',
    'lincurve',
    'nocurve',
    'rndcurve',
    'prop_off',
    'prop_on',
    'prop_con',
    'syntax',
    'syntax_off',
    'monkey',
    'hair',
    'viewmove',
    'home',
    'clipuv_dehlt',
    'clipuv_hlt',
    'blank2',
    'blank3',
    'vpaint_col',
    'restrict_select_off',
    'restrict_select_on',
    'mute_ipo_off',
    'mute_ipo_on',
    
    'man_trans',
    'man_rot',
    'man_scale',
    'manipul',
    'blank_47',
    'modifier',
    'mod_wave',
    'mod_build',
    'mod_decim',
    'mod_mirror',
    'mod_soft',
    'mod_subsurf',
    'seq_sequencer',
    'seq_preview',
    'seq_luma_waveform',
    'seq_chroma_scope',
    'rotate',
    'cursor',
    'rotatecollection',
    'rotatecenter',
    'rotactive',
    'restrict_view_off',
    'restrict_view_on',
    'restrict_render_off',
    'restrict_render_on',
    
    'view3d',
    'edit',
    'editmode_dehlt',
    'editmode_hlt',
    'disclosure_tri_right',
    'disclosure_tri_down',
    'move_up',
    'move_down',
]