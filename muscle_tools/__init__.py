# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Muscle Tools",
    "author": "coloremblem, kromar ",
    "version": (1, 0, 0),
    "blender": (2, 7, 1),
    "location": "View 3D > Tool Shelf",
    "description": "grow some muscles!",
    "warning": "",
    "wiki_url": "",
    "tracker ur_url": "https://github.com/coloremblem/MuscleToolsAddOn", 
    "category": "Rigging"}

if "bpy" in locals():
    import imp
    if "muscle_tools" in locals():
        imp.reload(muscle_tools)


import bpy
from bpy.types import Panel

#use this for configs and GUI
        
class MuscleToolsPanel(Panel):     # panel to display new property
    '''Muslce Tools'''
    bl_category = "Muscle Tools"
    bl_idname = "object.muscle_tools_panel"
    bl_label = "Muscle Tools"           # name of the new panel
    bl_space_type = 'VIEW_3D'       # show up in: 3d-window
    bl_region_type = 'TOOLS'          # show up in: properties panel
 
    def draw(self, context):    
        layout = self.layout     
        layout.operator(
                MUSCLETOOLS_OT_panel.object.muscle_tools,
                text = "Muscle Tools", 
                icon = 'POSE_DATA')
        '''
        self.layout.prop(bpy.context.active_object, '["View Resolution"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Render Resolution"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Muscle Shape"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Base Lenght"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Volume"]', slider = True)
        '''
        
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()

    
    