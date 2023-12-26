import pyglet

from pyglet_pen.widgets.button import ButtonWidget


def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    b = ButtonWidget(
        vertical_alignment="center",
        horizontal_alignment="center",
        x=50,
        y=50,
        width=200,
        height=50,
        text="Hello World!",
        #color=(255, 255, 255, 255),
        batch=batch,
        group=fg_group,
    )

    @window.event
    def on_draw():
        window.clear()
        batch.draw()
    
    pyglet.app.run()

if __name__ == "__main__":
    main()