
from pyglet_pen.view import View
from pyglet_pen.layouts import StackLayout

from pyglet_pen.example.common import build_view_title
from pyglet_pen.example.style import Style


class LayoutsView(View):
    Layout = StackLayout
    background_color = Style.DARK

    def setup(self):
        self.layout.margin = 10

        title_layout = build_view_title(self, "Layouts")
        self.add_content(title_layout)




