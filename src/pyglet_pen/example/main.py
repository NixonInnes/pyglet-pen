import pyglet

from pyglet_pen.window import Window

from pyglet_pen.example.views import ButtonsView, MenuView, StackLayoutView, FloatingLayoutView, GridLayoutView


if __name__ == "__main__":
    window = Window(caption="Pyglet Pen Example")
    print(f"Window: {window.width}x{window.height}")
    window.views["buttons"] = ButtonsView(window)
    window.views["stack_layout"] = StackLayoutView(window)
    window.views["floating_layout"] = FloatingLayoutView(window)
    window.views["grid_layout"] = GridLayoutView(window)
    window.views["menu"] = MenuView(window)
    window.set_view("menu")

    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            if window.active_view == window.views["menu"]:
                if window.previous_view:
                    window.set_view(window.previous_view)
            else:
                window.set_view("menu")
            
    pyglet.app.run()
