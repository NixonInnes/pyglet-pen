import logging
import pyglet

from .view import View


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        
        self.previous_view = None
        self.active_view = None
        self.views = {
        }
        self.text_cursor = self.get_system_mouse_cursor("text")

    def set_view(self, view_name):
        self.logger.debug(f"Setting view to {view_name}")

        if isinstance(view_name, str):
            if view_name not in self.views:
                raise ValueError(f"View {view_name} does not exist")
            
            self.previous_view = self.active_view
            if self.previous_view:
                self.previous_view.on_exit()

            self.active_view = self.views[view_name]
            self.active_view.on_enter()

        elif isinstance(view_name, View):
            self.previous_view = self.active_view
            if self.previous_view:
                self.previous_view.on_exit()

            self.active_view = view_name
            self.active_view.on_enter()
        else:
            raise ValueError(f"Invalid view type {type(view_name)}")

    def process_message(self, message):
        if self.active_view:
            self.active_view.process_message(message)

    def update(self, dt):
        if self.active_view:
            self.active_view.update(dt)

    def on_activate(self):
        if self.active_view:
            self.active_view.on_activate()

    def on_context_lost(self):
        if self.active_view:
            self.active_view.on_context_lost()

    def on_context_state_lost(self):
        if self.active_view:
            self.active_view.on_context_state_lost()

    def on_deactivate(self):
        if self.active_view:
            self.active_view.on_deactivate()

    def on_draw(self):
        self.clear()
        if self.active_view:
            self.active_view.on_draw()

    def on_expose(self):
        if self.active_view:
            self.active_view.on_expose()

    def on_file_drop(self, x, y, paths):
        if self.active_view:
            self.active_view.on_file_drop(x, y, paths)

    def on_hide(self):
        if self.active_view:
            self.active_view.on_hide()

    def on_key_press(self, symbol, modifiers):
        if self.active_view:
            self.active_view.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if self.active_view:
            self.active_view.on_key_release(symbol, modifiers)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.active_view:
            self.active_view.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_enter(self, x, y):
        if self.active_view:
            self.active_view.on_mouse_enter(x, y)

    def on_mouse_leave(self, x, y):
        if self.active_view:
            self.active_view.on_mouse_leave(x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.active_view:
            self.active_view.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.active_view:
            self.active_view.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.active_view:
            self.active_view.on_mouse_release(x, y, button, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if self.active_view:
            self.active_view.on_mouse_scroll(x, y, scroll_x, scroll_y)

    def on_key_press(self, symbol, modifiers):
        if self.active_view:
            self.active_view.on_key_press(symbol, modifiers)

    def on_move(self, x, y):
        if self.active_view:
            self.active_view.on_move(x, y)

    def on_refresh(self, dt):
        if self.active_view:
            self.active_view.on_refresh(dt)

    def on_resize(self, width, height):
        if self.active_view:
            self.active_view.on_resize(width, height)

    def on_show(self):
        if self.active_view:
            self.active_view.on_show()

    def on_text(self, text):
        if self.active_view:
            self.active_view.on_text(text)

    def on_text_motion(self, motion):
        if self.active_view:
            self.active_view.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self.active_view:
            self.active_view.on_text_motion_select(motion)
