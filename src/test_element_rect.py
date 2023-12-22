import pyglet
from pyglet_pen.layout.stack import StackLayout
from pyglet_pen.elements.shapes import Rectangle


def main():
    window = pyglet.window.Window(width=800, height=600)
    #rr = pyglet.shapes.Rectangle(x=0, y=0, width=50, height=50, color=(0, 0, 255, 255))

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

    r = Rectangle(
        width=50, 
        height=50, 
        color=(255, 0, 0, 255), 
        batch=batch, 
        group=bg_group,
        callback_on_mouse_enter=lambda _: print("Mouse entered"),
    )

    l1.add(r)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        if r.is_mouse_over(x, y):
            r.on_mouse_enter(x, y)

    pyglet.app.run()

if __name__ == "__main__":
    main()
