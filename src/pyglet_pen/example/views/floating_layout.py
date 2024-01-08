from pyglet_pen.view import View
from pyglet_pen.layouts import FloatingLayout, StackLayout
from pyglet_pen.elements.shapes import Box, Rectangle
from pyglet_pen.elements.text import Label
from pyglet_pen.widgets.button import ButtonWidget

from pyglet_pen.example.common import build_view_title, view_row_stack_factory
from pyglet_pen.example.style import Style


class FloatingLayoutView(View):
    Layout = StackLayout
    background_color = Style.DARK

    def setup(self):
        self.layout.margin = 10
        self.layout.vertical_alignment = "top"

        title_layout = build_view_title(self, "Floating Layout")
        self.add_content(title_layout)

        content_layout = StackLayout(
            width=self.window.width,
            height=4*self.window.height//5,
            stack_direction="horizontal",
            vertical_alignment="center",
            horizontal_alignment="center",
            margin=10,
            padding=10,
        )
        self.add_content(content_layout)

        self.example_layout = FloatingLayout(
            width=300,
            height=300,
            vertical_alignment="center",
            horizontal_alignment="center",
            margin=10,
        )
        content_layout.add_content(self.example_layout)

        example_layout_box = Box(
            width=self.example_layout.width,
            height=self.example_layout.height,
            batch=self.batch,
        )

        self.example_layout.subscribe_to_attribute("x", lambda value: setattr(example_layout_box, "x", value))
        self.example_layout.subscribe_to_attribute("y", lambda value: setattr(example_layout_box, "y", value))
        self.example_layout.subscribe_to_attribute("width", lambda value: setattr(example_layout_box, "width", value))
        self.example_layout.subscribe_to_attribute("height", lambda value: setattr(example_layout_box, "height", value))

        r1 = Rectangle(
            width=100,
            height=100,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        self.example_layout.add_content(r1)

        r2 = Rectangle(
            width=50,
            height=50,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        self.example_layout.add_content(r2)

        r3 = Rectangle(
            width=25,
            height=25,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        self.example_layout.add_content(r3)

        button_stack = StackLayout(
            width=self.window.width//2,
            height=4*self.window.height//5,
            stack_direction="horizontal",
            vertical_alignment="center",
            horizontal_alignment="center",
            margin=10,
        )
        content_layout.add_content(button_stack)

        button_stack_col1 = StackLayout(
            width=button_stack.width//2,
            height=button_stack.height,
            padding=10,
        )
        button_stack.add_content(button_stack_col1)

        button_stack_col2 = StackLayout(
            width=button_stack.width//2,
            height=button_stack.height,
            padding=10,
        )
        button_stack.add_content(button_stack_col2)

        def button_factory(text, callback):
            button = ButtonWidget(
                width=200,
                height=50,
                label_text=text,
                label_font_size=14,
                background_color=Style.SEMI_DARK,
                batch=self.batch,
                on_click=callback,
            )
            return button
        
        button_horizontal_fill = button_factory("Horizontal Fill", self.callback_horizontal_fill)
        button_stack_col1.add_content(button_horizontal_fill)
        button_vertical_fill = button_factory("Vertical Fill", self.callback_vertical_fill)
        button_stack_col1.add_content(button_vertical_fill)
        
        button_horizontal_left = button_factory("Horizontal Left", self.callback_horizontal_left)
        button_stack_col2.add_content(button_horizontal_left)
        button_horizontal_center = button_factory("Horizontal Center", self.callback_horizontal_center)
        button_stack_col2.add_content(button_horizontal_center)
        button_horizontal_right = button_factory("Horizontal Right", self.callback_horizontal_right)
        button_stack_col2.add_content(button_horizontal_right)
        
        button_vertical_top = button_factory("Vertical Top", self.callback_vertical_top)
        button_stack_col2.add_content(button_vertical_top)
        button_vertical_center = button_factory("Vertical Center", self.callback_vertical_center)
        button_stack_col2.add_content(button_vertical_center)
        button_vertical_bottom = button_factory("Vertical Bottom", self.callback_vertical_bottom)
        button_stack_col2.add_content(button_vertical_bottom)
        
        self.update_content_geometry()

    def callback_stack_direction_horizontal(self, *_, **__):
        self.example_layout.stack_direction = "horizontal"
        self.update_content_geometry()
    
    def callback_stack_direction_vertical(self, *_, **__):
        self.example_layout.stack_direction = "vertical"
        self.update_content_geometry()

    def callback_horizontal_fill(self, *_, **__):
        self.example_layout.horizontal_fill = not self.example_layout.horizontal_fill
        self.update_content_geometry()

    def callback_vertical_fill(self, *_, **__):
        self.example_layout.vertical_fill = not self.example_layout.vertical_fill
        self.update_content_geometry()

    def callback_vertical_top(self, *_, **__):
        self.example_layout.vertical_alignment = "top"
        self.update_content_geometry()
    
    def callback_vertical_center(self, *_, **__):
        self.example_layout.vertical_alignment = "center"
        self.update_content_geometry()
    
    def callback_vertical_bottom(self, *_, **__):
        self.example_layout.vertical_alignment = "bottom"
        self.update_content_geometry()

    def callback_horizontal_left(self, *_, **__):
        self.example_layout.horizontal_alignment = "left"
        self.update_content_geometry()

    def callback_horizontal_center(self, *_, **__):
        self.example_layout.horizontal_alignment = "center"
        self.update_content_geometry()
    
    def callback_horizontal_right(self, *_, **__):
        self.example_layout.horizontal_alignment = "right"
        self.update_content_geometry()

    
