import pyglet

from pyglet_pen.layouts import GridLayout
from pyglet_pen.proxies.shapes import RectangleProxy

def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    #box1 = pyglet.shapes.Box(x=50, y=50, width=400, height=400, color=(255,255,255,255), batch=batch, group=fg_group)
    grid = GridLayout(
        x=50,
        y=50,
        width=400,
        height=400,
        n_rows=3,
        n_cols=3,
        vertical_alignment="center",
        horizontal_alignment="center",
        vertical_fill=False,
        horizontal_fill=False,
        margin=10,
    )
    boxes = []
    for r in range(grid.n_rows):
        for c in range(grid.n_cols):
            box = pyglet.shapes.Box(
                x=grid.x + (c * grid.width // grid.n_cols),
                y=grid.y + (r * grid.height // grid.n_rows),
                width=grid.width // grid.n_cols,
                height=grid.height // grid.n_rows,
                batch=batch,
                group=fg_group,
            )
            boxes.append(box)

    r1 = RectangleProxy(width=50, height=50, color=(255, 0, 0, 255), batch=batch, group=bg_group)
    r2 = RectangleProxy(width=50, height=50, color=(0, 255, 0, 255),  batch=batch, group=bg_group)
    r3 = RectangleProxy(width=50, height=50, color=(0, 0, 255, 255),  batch=batch, group=bg_group)
    r4 = RectangleProxy(width=50, height=50, color=(255, 255, 0, 255),  batch=batch, group=bg_group)
    r5 = RectangleProxy(width=50, height=50, color=(255, 0, 255, 255),  batch=batch, group=bg_group)
    r6 = RectangleProxy(width=50, height=50, color=(0, 255, 255, 255),  batch=batch, group=bg_group)
    r7 = RectangleProxy(width=50, height=50, color=(255, 255, 255, 255),  batch=batch, group=bg_group)
    r8 = RectangleProxy(width=50, height=50, color=(128, 128, 128, 255),  batch=batch, group=bg_group)
    r9 = RectangleProxy(width=50, height=50, color=(16, 16, 16, 255),  batch=batch, group=bg_group)
    print(grid)

    grid.add_content(r1, 0, 0)
    grid.add_content(r2, 0, 1)
    grid.add_content(r3, 0, 2)
    grid.add_content(r4, 1, 0)
    grid.add_content(r5, 1, 1)
    grid.add_content(r6, 1, 2)
    grid.add_content(r7, 2, 0)
    grid.add_content(r8, 2, 1)
    grid.add_content(r9, 2, 2)

    grid.update_content_geometry()

    @window.event
    def on_draw():
        window.clear()
        batch.draw()
    
    pyglet.app.run()

if __name__ == "__main__":
    main()
