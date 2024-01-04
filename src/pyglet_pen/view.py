import pyglet
import logging

from pyglet_pen.layouts import LayoutMixin


class View(LayoutMixin):

    def __init__(self, window):
        self.logger = logging.getLogger(f"{__name__}")
        self.window = window
        super().__init__()
        self.batch = pyglet.graphics.Batch()
        self.focus = None
        self.setup()
        self._mouse_over_widget = None

    @property
    def width(self):
        return self.window.width
    
    @property
    def height(self):
        return self.window.height
    
    @property
    def x(self):
        return 0
    
    @property
    def y(self):
        return 0

    # Convenience
    def setup(self):
        pass

    def set_focus(self, widget):
        # if already focused, do nothing
        if widget is self.focus:
            return

        # unfocus current focus
        if self.focus is not None:
            self.focus.unfocus()

        # set new focus
        self.focus = widget

        # focus new focus
        if widget is not None:
            widget.focus()

    # Called when view activated by the main Window
    def on_enter(self):
        pass

    # Called when view deactivated by the main Window
    def on_exit(self):
        pass


    # Window events
    def update(self, dt):
        pass

    def on_activate(self):
        pass

    def on_close(self):
        pass

    def on_context_lost(self):
        pass

    def on_context_state_lost(self):
        pass

    def on_deactivate(self):
        pass

    def on_draw(self):
        self.batch.draw()

    def on_expose(self):
        pass

    def on_file_drop(self, x, y, paths):
        pass

    def on_hide(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.focus:
            self.focus.on_mouse_drag(self.window, x, y, dx, dy, buttons, modifiers)

    def on_mouse_enter(self, x, y):
        pass

    def on_mouse_leave(self, x, y):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        over_widget = None
        for widget in self.widgets:
            if widget.visible and widget.is_mouse_over(x, y):
                over_widget = widget
                break

        if over_widget is not None:
            if self._mouse_over_widget is not over_widget:
                if self._mouse_over_widget is not None:
                    self._mouse_over_widget.on_mouse_leave(self.window, x, y, dx, dy)
                over_widget.on_mouse_enter(self.window, x, y, dx, dy)

            over_widget.on_mouse_motion(self.window, x, y, dx, dy)
            self._mouse_over_widget = over_widget
        else:
            if self._mouse_over_widget is not None:
                self._mouse_over_widget.on_mouse_leave(self.window, x, y, dx, dy)
                self._mouse_over_widget = None

    def on_mouse_press(self, x, y, button, modifiers):
        if self._mouse_over_widget is not None:
            self.set_focus(self._mouse_over_widget)
            self._mouse_over_widget.on_mouse_press(self.window, x, y, button, modifiers)
        else:
            self.set_focus(None)

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def on_move(self, x, y):
        pass

    def on_refresh(self, dt):
        pass

    def on_resize(self, width, height):
        pass

    def on_show(self):
        pass

    def on_text(self, text):
        if self.focus:
            self.focus.on_text(self.window, text)

    def on_text_motion(self, motion):
        if self.focus:
            self.focus.on_text_motion(self.window, motion)

    def on_text_motion_select(self, motion):
        if self.focus:
            self.focus.on_text_motion_select(self.window, motion)
