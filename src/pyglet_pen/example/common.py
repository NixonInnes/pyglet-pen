
from pyglet_pen.layouts import FloatingLayout, StackLayout
from pyglet_pen.elements.shapes import Background
from pyglet_pen.elements.text import Label

from pyglet_pen.example.style import Style


def build_view_title(view, title_text):
    title_layout = FloatingLayout(
        width=view.window.width,
        height=view.window.height//5,
        horizontal_fill=True,
        vertical_alignment="center",
        horizontal_alignment="left",
    )

    title_background = Background(
        width=title_layout.width,
        height=title_layout.height,
        color=Style.SEMI_DARK,
        batch=view.batch,
    )
    title_layout.add_content(title_background)

    title_label = Label(
        width=100,
        height=24*1.2,
        align="center",
        font_name="Noto Sans",
        font_size=24,
        color=Style.LIGHT,
        text=title_text,
        batch=view.batch,
    )
    title_layout.add_content(title_label)

    # import pyglet
    # from pyglet_pen.elements.shapes import Box
    # title_label_box = Box(
    #     width=200,
    #     height=24*1.2,
    #     color=(255, 255, 255, 255),
    #     batch=view.batch,
    #     group=pyglet.graphics.Group(4),
    # )
    # title_layout.add_content(title_label_box)

    return title_layout

def view_row_stack_factory(view):
    row = StackLayout(
        x=0,
        y=0,
        stack_direction="horizontal",
        width=view.window.width,
        height=2*view.window.height//5,
        vertical_alignment="top",
        horizontal_alignment="center",
        #vertical_fill=True,
        horizontal_fill=True,
        margin=10,
    )
    return row