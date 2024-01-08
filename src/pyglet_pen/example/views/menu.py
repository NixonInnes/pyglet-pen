from pyglet_pen.view import View
from pyglet_pen.layouts import StackLayout
from pyglet_pen.widgets.button import ButtonWidget

from pyglet_pen.example.style import Style

class MenuView(View):
    Layout = StackLayout
    background_color = Style.ALT_DARK

    def setup(self):

        layouts_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Layouts",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("layouts"),
        )
        self.add_content(layouts_button)

        buttons_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Buttons",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.set_view("buttons"),
        )
        self.add_content(buttons_button)

        exit_button = ButtonWidget(
            width=400,
            height=50,
            label_text="Exit",
            label_font_size=14,
            background_color=Style.SEMI_DARK,
            batch=self.batch,
            on_click=lambda *_, **__: self.window.close(),
        )
        self.add_content(exit_button)

        self.update_content_geometry()

