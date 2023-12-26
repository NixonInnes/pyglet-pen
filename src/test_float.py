import pyglet

from pyglet_pen.layout.floating import FloatingLayout
from pyglet_pen.proxies.shapes import RectangleProxy

def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    box1 = pyglet.shapes.Box(x=50, y=50, width=400, height=400, color=(255,255,255,255), batch=batch, group=fg_group)
    layout = FloatingLayout(
        x=50,
        y=50,
        width=400,
        height=400,
        n_rows=3,
        n_cols=3,
        vertical_alignment="center",
        horizontal_alignment="center",
        vertical_fill=False,
        horizontal_fill=True,
        margin=0,
    )

    r1 = RectangleProxy(width=300, height=300, color=(255, 0, 0, 255), batch=batch, group=bg_group)
    print(r1.named_attributes)
    r2 = RectangleProxy(width=100, height=100, color=(0, 255, 0, 255),  batch=batch, group=bg_group)
    r3 = RectangleProxy(width=50, height=50, color=(0, 0, 255, 255),  batch=batch, group=bg_group)

    layout.add(r1)
    layout.add(r2)
    layout.add(r3)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()
    
    pyglet.app.run()


if __name__ == "__main__":
    main()