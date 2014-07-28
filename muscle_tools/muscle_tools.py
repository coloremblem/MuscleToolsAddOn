import bpy

class myPanel(bpy.types.Panel):     # panel to display new property
    bl_space_type = "VIEW_3D"       # show up in: 3d-window
    bl_region_type = "TOOLS"           # show up in: properties panel
    bl_label = "Muscle Adjustments"           # name of the new panel
 
    def draw(self, context):
        # display "Properties" ID-property, of the active object
        self.layout.prop(bpy.context.active_object, '["View Resolution"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Render Resolution"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Muscle Shape"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Base Lenght"]', slider = True)
        self.layout.prop(bpy.context.active_object, '["Volume"]', slider = True)
 
 
 
bpy.utils.register_class(myPanel)   # register panel
