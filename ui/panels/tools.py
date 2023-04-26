from bpy.types import Context

from .. import declarations
from .. import icon_manager
from . import VIEW3D_PT_sketcher_base


class VIEW3D_PT_sketcher_tools(VIEW3D_PT_sketcher_base):
    """
    Tools Menu: List of useful tools for sketching
    """

    bl_label = "Tools"
    bl_idname = declarations.Panels.SketcherTools
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context):
        layout = self.layout

        # Constraints
        layout.label(text="Constraints:")
        col = layout.column(align=True)

        for op in declarations.ConstraintOperators:
            col.operator(op, icon_value=icon_manager.get_constraint_icon(op))

        layout.separator()

        # Drawing
        layout.label(text="Drawing:")
        layout.prop(context.scene.sketcher, "use_construction")

        layout.operator(declarations.Operators.Offset).wait_for_input = True
