import pyglet

from pyglet_pen.layout.grid import GridLayout
from pyglet_pen.proxies import shapes

def main():
    window = pyglet.window.Window(width=800, height=600)

    bg_group = pyglet.graphics.Group(0)
    fg_group = pyglet.graphics.Group(10)
    batch = pyglet.graphics.Batch()

    grid = GridLayout(
        x=50,
        y=50,
        width=700,
        height=500,
        n_rows=500//250,
        n_cols=700//100,
        vertical_alignment="center",
        horizontal_alignment="center",
        vertical_fill=False,
        horizontal_fill=True,
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
            

    shape_color = (100, 100, 100, 255)

    s1 = shapes.ArcProxy(
        x=0,
        y=0,
        width=50,
        height=50,
        radius=50,
        angle=3.0,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s1, 0, 0)

    s2 = shapes.CircleProxy(
        x=0,
        y=0,
        width=150,
        height=150,
        #radius=25,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s2, 0, 1)

    s3 = shapes.EllipseProxy(
        x=0,
        y=0,
        a=25,
        b=50,
        width=50,
        height=50,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s3, 0, 2)

    s4 = shapes.SectorProxy(
        x=0,
        y=0,
        width=50,
        height=50,
        radius=50,
        angle=3.0,
        start_angle=0.0,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s4, 0, 3)

    s5 = shapes.LineProxy(
        x=0,
        y=0,
        width=50,
        height=50,
        x2=50,
        y2=50,
        thickness=5,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s5, 0, 4)

    s6 = shapes.RectangleProxy(
        x=0,
        y=0,
        width=40,
        height=40,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s6, 0, 5)

    s7 = shapes.BoxProxy(
        x=0,
        y=0,
        width=40,
        height=40,
        thickness=3,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s7, 0, 6)

    s8 = shapes.BorderedRectangleProxy(
        x=0,
        y=0,
        width=40,
        height=40,
        border=3,
        color=shape_color,
        border_color=(255, 0, 0, 255),
        batch=batch,
        group=bg_group,
    )
    grid.add(s8, 1, 0)

    s9 = shapes.TriangleProxy(
        x=0,
        y=0,
        width=50,
        height=50,
        x2=50,
        y2=50,
        x3=0,
        y3=50,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s9, 1, 1)

    s10 = shapes.StarProxy(
        x=0,
        y=0,
        width=50,
        height=50,
        outer_radius=50,
        inner_radius=25,
        num_spikes=5,
        color=shape_color,
        batch=batch,
        group=bg_group,
    )
    grid.add(s10, 1, 2)


    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()


if __name__ == "__main__":
    main()