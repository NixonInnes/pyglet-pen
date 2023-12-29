import pyglet

from pyglet_pen.widgets.button import ButtonWidget


def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    b = ButtonWidget(
        x=50,
        y=50,
        width=200,
        height=50,
        label_text="Hello World!",
        #color=(255, 255, 255, 255),
        batch=batch,
        background_group=bg_group,
        label_group=fg_group,
        on_click=lambda *_, **__: print("Hello World!"),
    )

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        b.on_mouse_press(x, y, button, modifiers)

    b.label_text = "Something else"
    
    pyglet.app.run()

if __name__ == "__main__":
    main()