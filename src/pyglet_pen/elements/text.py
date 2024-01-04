from pyglet_pen.interactable import Interactable
from pyglet_pen.proxies.text import LabelProxy, IncrementalTextLayoutProxy



class Label(Interactable, LabelProxy):
    pass


class TextDisplay(Interactable, IncrementalTextLayoutProxy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_mouse_press.subscribe(self.caret.on_mouse_press)
        self.on_mouse_drag.subscribe(self.caret.on_mouse_drag)


class TextInput(Interactable, IncrementalTextLayoutProxy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)