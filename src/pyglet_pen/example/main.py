import pyglet

from pyglet_pen.window import Window
from pyglet_pen.example.views.buttons import ButtonsView


if __name__ == "__main__":
    window = Window()
    window.views["buttons"] = ButtonsView(window)

    window.set_view("buttons")
    pyglet.app.run()