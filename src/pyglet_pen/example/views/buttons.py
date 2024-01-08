from random import randint

from pyglet_pen.view import View
from pyglet_pen.layouts import StackLayout
from pyglet_pen.widgets.button import BaseButtonWidget, ButtonWidget, ToggleButtonWidget
from pyglet_pen.elements.text import Label
from pyglet_pen.icons import Icon

from pyglet_pen.example.style import Style
from pyglet_pen.example.common import build_view_title, view_row_stack_factory


class ButtonsView(View):
    Layout = StackLayout
    background_color = Style.DARK

    def setup(self):
        self.layout.margin = 10

        title_layout = build_view_title(self, "Buttons")
        self.add_content(title_layout)

        def button_stack_factory():
            stack = StackLayout(
                width=200,
                height=200,
                vertical_alignment="top",
                horizontal_alignment="center",
                margin=10,
            )
            return stack
        
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
        
        row1 = view_row_stack_factory(self)
        self.add_content(row1)
        row2 = view_row_stack_factory(self)
        self.add_content(row2)

        # Base button
        base_button_desc_text = "Base Button.\nThis is the base button widget, it has a simple background with border and label text."
        base_button_stack = button_stack_factory()
        base_button = BaseButtonWidget(
            width=100,
            height=50,
            label_text="Base",
            batch=self.batch,
        )
        base_button_stack.add_content(base_button)
        base_button_desc = button_desc_label_factory(base_button_desc_text)
        base_button_stack.add_content(base_button_desc)
        row1.add_content(base_button_stack)

        # Standard button
        standard_button_desc_text = "Standard Button.\nThis is the standard button widget, it extends the Base button adding some on-click \"animation\"."
        standard_button_stack = button_stack_factory()
        standard_button = ButtonWidget(
            width=100,
            height=50,
            label_color=Style.LIGHT,
            label_text="Standard",
            batch=self.batch,
        )
        standard_button_stack.add_content(standard_button)
        standard_button_desc = button_desc_label_factory(standard_button_desc_text)
        standard_button_stack.add_content(standard_button_desc)
        row1.add_content(standard_button_stack)

        # Border button
        border_button_desc_text = "Border Button.\nThis is the same as the Standard button, with a modified border."
        border_button_stack = button_stack_factory()
        border_button = ButtonWidget(
            width=100,
            height=50,
            label_color=Style.LIGHT,
            label_text="Border",
            border_width=5,
            border_color=Style.HIGHLIGHT,
            batch=self.batch,
        )
        border_button_stack.add_content(border_button)
        border_button_desc = button_desc_label_factory(border_button_desc_text)
        border_button_stack.add_content(border_button_desc)
        row1.add_content(border_button_stack)

        # On-Click button
        on_click_button_desc_text = "On-Click Button.\nThis is the same as the Standard button, with a callback on click."
        on_click_button_stack = button_stack_factory()
        self.on_click_button = ButtonWidget(
            width=100,
            height=50,
            label_color=Style.LIGHT,
            label_text="On-Click",
            batch=self.batch,
            on_click=self.on_click_button_callback,
        )
        on_click_button_stack.add_content(self.on_click_button)
        on_click_button_desc = button_desc_label_factory(on_click_button_desc_text)
        on_click_button_stack.add_content(on_click_button_desc)
        row1.add_content(on_click_button_stack)

        # Icon button
        icon_button_desc_text = "Icon Button.\nThis is the same as the Standard button, with an icon (Google Material Icons) instead of text."
        icon_button_stack = button_stack_factory()
        icon_button = ButtonWidget(
            width=50,
            height=50,
            label_text=Icon.HOME,
            label_color=Style.LIGHT,
            label_font_name="Material Icons",
            label_font_size=24,
            on_click=lambda *_, **__: print("Go Home"),
            batch=self.batch,
        )
        icon_button_stack.add_content(icon_button)
        icon_button_desc = button_desc_label_factory(icon_button_desc_text)
        icon_button_stack.add_content(icon_button_desc)
        row1.add_content(icon_button_stack)

        # Toggle button
        toggle_button_desc_text = "Toggle Button.\nThis extends the Standard button, adding a toggle state."
        toggle_button_stack = button_stack_factory()
        toggle_button = ToggleButtonWidget(
            width=50,
            height=50,
            label_color=Style.LIGHT,
            label_text=Icon.CHECK_BOX_OUTLINE_BLANK,
            label_font_name="Material Icons",
            label_font_size=24,
            label_text_false=Icon.CHECK_BOX_OUTLINE_BLANK,
            label_text_true=Icon.CHECK_BOX,
            on_toggle=lambda state: print("Toggle State:", state),
            batch=self.batch,
        )
        toggle_button_stack.add_content(toggle_button)
        toggle_button_desc = button_desc_label_factory(toggle_button_desc_text)
        toggle_button_stack.add_content(toggle_button_desc)
        row1.add_content(toggle_button_stack)

        self.layout.update_content_geometry()
        

    def on_click_button_callback(self, *_, **__):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.on_click_button.background_color = (r, g, b, 255)
        self.on_click_button.border_color = (r//5, g//5, b//5, 255)