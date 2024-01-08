from pyglet_pen.elements.text import Label
from pyglet_pen.view import View
from pyglet_pen.layouts import StackLayout
from pyglet_pen.widgets.button import ButtonWidget

from pyglet_pen.example.style import Style

class MenuView(View):
    Layout = StackLayout
    background_color = Style.ALT_DARK

    def setup(self):
        self.layout.margin = 10

        title_label = Label(
            width=self.window.width,
            height=self.window.height//5,
            align="center",
            font_name="Noto Sans",
            font_size=28,
            color=Style.LIGHT,
            text="Pyglet Pen Example App",
            multiline=True,
            batch=self.batch,
        )
        self.add_content(title_label)

        views_stack = StackLayout(
            width=self.window.width,
            height=4*self.window.height//5,
            vertical_alignment="center",
            horizontal_alignment="center",
            padding=10,
        )
        self.add_content(views_stack)

        exit_stack = StackLayout(
            width=self.window.width,
            height=self.window.height//5,
            vertical_alignment="center",
            horizontal_alignment="center",
        )
        self.add_content(exit_stack)

        stack_layout_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Stack Layout",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("stack_layout"),
        )
        views_stack.add_content(stack_layout_button)

        floating_layout_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Floating Layout",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("floating_layout"),
        )
        views_stack.add_content(floating_layout_button)

        grid_layout_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Grid Layout",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("grid_layout"),
        )
        views_stack.add_content(grid_layout_button)

        buttons_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Buttons",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("buttons"),
        )
        views_stack.add_content(buttons_button)

        exit_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Exit",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.close(),
        )
        exit_stack.add_content(exit_button)

        self.update_content_geometry()

