from typing import Literal

from pyglet_pen.component import ComponentProperty

from .layout import Layout


class GridLayout(Layout):
    n_rows = ComponentProperty[int](1)
    n_cols = ComponentProperty[int](1)

    def __init__(self, *args, **kwargs):
        self.contents = {}
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.contents[(i, j)] = GridLayoutCell(
                    vertical_alignment=self.vertical_alignment,
                    horizontal_alignment=self.horizontal_alignment,
                    vertical_fill=self.vertical_fill,
                    horizontal_fill=self.horizontal_fill,
                    margin=self.margin,
                )
    
    @property
    def n_items(self):
        return len(self.contents)

    def add(self, item, row, col):
        self.contents[(row, col)].content = item
        self.update_content_geometry()

    def update_content_geometry(self):
        if self.n_items < 1:
            return
        
        available_width = self.width
        available_height = self.height

        start_x = self.x
        start_y = self.y

        cell_width = available_width // self.n_cols
        cell_height = available_height // self.n_rows

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                cell = self.contents[(i, j)]
                cell.x = start_x + (j * cell_width)
                cell.y = start_y + (i * cell_height)
                cell.width = cell_width
                cell.height = cell_height
                cell.update_content_geometry()

        

class GridLayoutCell(Layout):
    vertical_alignment = ComponentProperty[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = ComponentProperty[Literal["left", "center", "right"]]("center")
    vertical_fill = ComponentProperty[bool](False)
    horizontal_fill = ComponentProperty[bool](False)
    margin = ComponentProperty[int](0)

    def __init__(self, *args, **kwargs):
        self.content = None
    
    def update_content_geometry(self):
        if self.content is None:
            return
        
        available_width = self.width - (2 * self.margin)
        available_height = self.height - (2 * self.margin)

        start_x = self.x + self.margin
        start_y = self.y + self.margin

        if self.horizontal_fill:
            self.content.width = available_width
        else:
            self.content.width = self.content.initial.width
        
        if self.vertical_fill:
            self.content.height = available_height
        else:
            self.content.height = self.content.initial.height

        if self.horizontal_alignment == "left":
            self.content.x = start_x
        else:
            space = available_width - self.content.width
            if self.horizontal_alignment == "center":
                self.content.x = start_x + (space // 2)
            elif self.horizontal_alignment == "right":
                self.content.x = start_x + space
            else:
                raise ValueError(f"Invalid horizontal alignment: {self.horizontal_alignment}")
        
        if self.vertical_alignment == "bottom":
            self.content.y = start_y
        else:
            space = available_height - self.content.height
            if self.vertical_alignment == "center":
                self.content.y = start_y + (space // 2)
            elif self.vertical_alignment == "top":
                self.content.y = start_y + space
            else:
                raise ValueError(f"Invalid vertical alignment: {self.vertical_alignment}")
        
        if isinstance(self.content, Layout):
            self.content.update_content_geometry()
