import pyglet

from pyglet_pen.layouts.stack import StackLayout
from pyglet_pen.proxies.text import LabelProxy


def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    box1 = pyglet.shapes.Box(x=50, y=50, width=400, height=400, color=(255,255,255,255), batch=batch, group=fg_group)
    l1 = StackLayout(
        x=50, 
        y=50, 
        width=400, 
        height=400, 
        stack_direction="vertical", 
        vertical_alignment="bottom",
        horizontal_alignment="center",
        padding=5,
        vertical_fill=False,
        horizontal_fill=True,
    )

    t1 = LabelProxy(x=0, y=0, width=200, height=20, text="Hello World!", batch=batch, group=bg_group)

    l1.add(t1)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()

if __name__ == "__main__":
    main()