import pyglet

from pyglet_pen.layouts import StackLayout
from pyglet_pen.widgets.button import ButtonWidget
from pyglet_pen.icons import Icon


def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()
    
    font = pyglet.font.load('Material Icons')

    l = StackLayout(
        x=100,
        y=50,
        width=600,
        height=400
    )

    b = ButtonWidget(
        x=50,
        y=50,
        width=200,
        height=50,
        label_text=Icon.MAP,
        label_font_name=font.name,
        label_font_size=20,
        background_color=(200, 200, 100, 255),
        batch=batch,
        background_group=bg_group,
        label_group=fg_group,
        on_click=lambda *_, **__: print("Hello World!"),
    )

    print(b)
    print(b.layout)

    l.add_content(b)

    print(b)
    print(b.layout)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        b.on_mouse_press(x, y, button, modifiers)
    
    pyglet.app.run()

if __name__ == "__main__":
    main()