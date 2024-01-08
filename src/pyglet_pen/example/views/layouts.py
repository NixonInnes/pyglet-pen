
from pyglet_pen.view import View
from pyglet_pen.layouts import FloatingLayout, StackLayout
from pyglet_pen.elements.shapes import Box, Rectangle
from pyglet_pen.elements.text import Label

from pyglet_pen.example.common import build_view_title, view_row_stack_factory
from pyglet_pen.example.style import Style


class LayoutsView(View):
    Layout = StackLayout
    background_color = Style.DARK

    def setup(self):
        self.layout.margin = 10
        self.layout.vertical_alignment = "top"

        title_layout = build_view_title(self, "Layouts")
        self.add_content(title_layout)

        intro_text_layout = FloatingLayout(
            width=self.window.width,
            height=100,
            vertical_alignment="top",
            horizontal_alignment="center",
            horizontal_fill=True,
            margin=10,
        )
        intro_text_border = Box(
            width=self.window.width,
            height=80,
            color=Style.SEMI_DARK,
            batch=self.batch,
        )
        intro_text_layout.add_content(intro_text_border)
        intro_text = (
            "Floating layouts layer content on top of each other. " +
            "The following examples demonstrate some of the basic layouts."
        )
        intro_text_label = Label(
            width=self.window.width,
            height=80,
            font_name="Noto Sans",
            font_size=14,
            color=Style.SEMI_LIGHT,
            text=intro_text,
            multiline=True,
            batch=self.batch,
        )
        intro_text_layout.add_content(intro_text_label)
        self.add_content(intro_text_layout)

        row1 = view_row_stack_factory(self)
        self.add_content(row1)
        row2 = view_row_stack_factory(self)
        self.add_content(row2)

        def layout_stack_factory():
            layout = StackLayout(
                width=200,
                height=200,
                vertical_alignment="top",
                horizontal_alignment="center",
                margin=10,
            )
            return layout
        
        def button_desc_label_factory(text):
            label = Label(
                width=180,
                height=50,
                font_name="Noto Sans",
                font_size=10,
                color=Style.SEMI_LIGHT,
                text=text,
                multiline=True,
                batch=self.batch,
            )
            return label
        
        # Basic FloatingLayout
        basic_floating_layout_desc_text = "Basic FloatingLayout.\nCentral alignment.\nNo margin or fills."
        basic_floating_layout_stack = layout_stack_factory()
        basic_floating_layout = FloatingLayout(
            width=200,
            height=200,
        )
        basic_floating_layout_stack.add_content(basic_floating_layout)
        basic_floating_layout_desc = button_desc_label_factory(basic_floating_layout_desc_text)
        basic_floating_layout_stack.add_content(basic_floating_layout_desc)

        r1 = Rectangle(
            width=150,
            height=150,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        basic_floating_layout.add_content(r1)

        r2 = Rectangle(
            width=100,
            height=100,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r2)

        r3 = Rectangle(
            width=50,
            height=50,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r3)

        row1.add_content(basic_floating_layout_stack)


        # Basic FloatingLayout - Align top left
        basic_floating_layout_desc_text = "Basic FloatingLayout.\nCentral alignment.\nNo margin or fills."
        basic_floating_layout_stack = layout_stack_factory()
        basic_floating_layout = FloatingLayout(
            width=200,
            height=200,
            vertical_alignment="top",
            horizontal_alignment="left",
        )
        basic_floating_layout_stack.add_content(basic_floating_layout)
        basic_floating_layout_desc = button_desc_label_factory(basic_floating_layout_desc_text)
        basic_floating_layout_stack.add_content(basic_floating_layout_desc)

        r1 = Rectangle(
            width=150,
            height=150,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        basic_floating_layout.add_content(r1)

        r2 = Rectangle(
            width=100,
            height=100,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r2)

        r3 = Rectangle(
            width=50,
            height=50,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r3)

        row1.add_content(basic_floating_layout_stack)


        # Basic FloatingLayout - Align bottom lright
        basic_floating_layout_desc_text = "Basic FloatingLayout.\nCentral alignment.\nNo margin or fills."
        basic_floating_layout_stack = layout_stack_factory()
        basic_floating_layout = FloatingLayout(
            width=200,
            height=200,
            vertical_alignment="bottom",
            horizontal_alignment="right",
        )
        basic_floating_layout_stack.add_content(basic_floating_layout)
        basic_floating_layout_desc = button_desc_label_factory(basic_floating_layout_desc_text)
        basic_floating_layout_stack.add_content(basic_floating_layout_desc)

        r1 = Rectangle(
            width=150,
            height=150,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        basic_floating_layout.add_content(r1)

        r2 = Rectangle(
            width=100,
            height=100,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r2)

        r3 = Rectangle(
            width=50,
            height=50,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r3)

        row1.add_content(basic_floating_layout_stack)

        # Basic FloatingLayout - horizontal fill
        basic_floating_layout_desc_text = "Basic FloatingLayout.\nCentral alignment.\nNo margin or fills."
        basic_floating_layout_stack = layout_stack_factory()
        basic_floating_layout = FloatingLayout(
            width=200,
            height=200,
            horizontal_fill=True,
        )
        basic_floating_layout_stack.add_content(basic_floating_layout)
        basic_floating_layout_desc = button_desc_label_factory(basic_floating_layout_desc_text)
        basic_floating_layout_stack.add_content(basic_floating_layout_desc)

        r1 = Rectangle(
            width=150,
            height=150,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        basic_floating_layout.add_content(r1)

        r2 = Rectangle(
            width=100,
            height=100,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r2)

        r3 = Rectangle(
            width=50,
            height=50,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r3)

        row2.add_content(basic_floating_layout_stack)

        # Basic FloatingLayout - vertical fill
        basic_floating_layout_desc_text = "Basic FloatingLayout.\nCentral alignment.\nNo margin or fills."
        basic_floating_layout_stack = layout_stack_factory()
        basic_floating_layout = FloatingLayout(
            width=200,
            height=200,
            vertical_fill=True,
        )
        basic_floating_layout_stack.add_content(basic_floating_layout)
        basic_floating_layout_desc = button_desc_label_factory(basic_floating_layout_desc_text)
        basic_floating_layout_stack.add_content(basic_floating_layout_desc)

        r1 = Rectangle(
            width=150,
            height=150,
            color=(200, 0, 0, 255),
            batch=self.batch,
        )
        basic_floating_layout.add_content(r1)

        r2 = Rectangle(
            width=100,
            height=100,
            color=(0, 200, 0, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r2)

        r3 = Rectangle(
            width=50,
            height=50,
            color=(0, 0, 200, 255),
            batch=self.batch
        )
        basic_floating_layout.add_content(r3)

        row2.add_content(basic_floating_layout_stack)

        self.layout.update_content_geometry()
        









