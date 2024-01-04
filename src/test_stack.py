import pyglet
from pyglet_pen.layouts import StackLayout
from pyglet_pen.proxies.shapes import RectangleProxy


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

    box2 = pyglet.shapes.Box(x=50, y=50, width=200, height=200, color=(255,255,255,255), batch=batch, group=fg_group)
    l2 = StackLayout(
        x=50, 
        y=50, 
        width=200, 
        height=200, 
        stack_direction="horizontal", 
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=20,
        margin=10,
        vertical_fill=True,
        horizontal_fill=True,
    )
    r1 = RectangleProxy(width=50, height=50, color=(255, 0, 0, 255), batch=batch, group=bg_group)
    r2 = RectangleProxy(width=50, height=50, color=(0, 255, 0, 255),  batch=batch, group=bg_group)
    r3 = RectangleProxy(width=50, height=50, color=(0, 0, 255, 255),  batch=batch, group=bg_group)

    l1.add_content(l2)
    l2.add_content(r1)
    l2.add_content(r2)
    l2.add_content(r3)

    for item in l2.contents:
        print(item)
    
    
    @window.event
    def on_draw():
        window.clear()
        #rr.draw()
        batch.draw()
    
    pyglet.app.run()

if __name__ == "__main__":
    main()