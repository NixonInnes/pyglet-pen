from random import randint

from pyglet_pen.view import View
from pyglet_pen.layouts import StackLayout
from pyglet_pen.widgets.button import ButtonWidget, ToggleButtonWidget
from pyglet_pen.elements.text import Label
from pyglet_pen.icons import Icon


class ButtonsView(View):
    Layout = StackLayout

    def setup(self):

        basic_buttons_layout = StackLayout(
            x=0,
            y=0,
            stack_direction="horizontal",
            width=self.window.width,
            height=self.window.height,
            vertical_alignment="center",
            horizontal_alignment="center",
            horizontal_fill=True,
            margin=10,
        )

        basic_buttons_label = Label(
            width=100,
            height=50,
            color=(255, 255, 255, 255),
            text="Basic Buttons",
            batch=self.batch,
        )
        basic_buttons_layout.add_content(basic_buttons_label)

        self.basic_button_1 = ButtonWidget(
            width=100,
            height=50,
            label_text="Basic",
            on_click=self.on_basic_button_click,
            batch=self.batch,
        )
        self.basic_button_1.background_color = (0, 0, 200, 255)
        basic_buttons_layout.add_content(self.basic_button_1)

        basic_button_2 = ButtonWidget(
            width=50,
            height=50,
            border_width=5,
            border_color=(255, 255, 255, 255),
            label_text=Icon.HOME,
            label_font_name="Material Icons",
            label_font_size=24,
            on_click=lambda *_, **__: print("Go Home"),
            batch=self.batch,
        )
        basic_buttons_layout.add_content(basic_button_2)

        toggle_button = ToggleButtonWidget(
            width=50,
            height=50,
            label_text=Icon.CHECK_BOX_OUTLINE_BLANK,
            label_font_name="Material Icons",
            label_font_size=24,
            label_text_false=Icon.CHECK_BOX_OUTLINE_BLANK,
            label_text_true=Icon.CHECK_BOX,
            on_toggle=lambda state: print("Toggle State:", state),
            batch=self.batch,

        )
        basic_buttons_layout.add_content(toggle_button)

        self.add_content(basic_buttons_layout)

    def on_basic_button_click(self, *_, **__):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.basic_button_1.background_color = (r, g, b, 255)
        self.basic_button_1.border_color = (r//5, g//5, b//5, 255)