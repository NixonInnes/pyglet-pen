from typing import Literal


from .layout import Layout, LayoutAttribute


class GridLayout(Layout):
    n_rows = LayoutAttribute[int](1)
    n_cols = LayoutAttribute[int](1)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.contents = {}
        for i in range(instance.n_rows):
            for j in range(instance.n_cols):
                instance.contents[(i, j)] = GridLayoutCell(
                    vertical_alignment=instance.vertical_alignment,
                    horizontal_alignment=instance.horizontal_alignment,
                    vertical_fill=instance.vertical_fill,
                    horizontal_fill=instance.horizontal_fill,
                    margin=instance.margin,
                )
        return instance
    
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
    vertical_alignment = LayoutAttribute[Literal["top", "center", "bottom"]]("center")
    horizontal_alignment = LayoutAttribute[Literal["left", "center", "right"]]("center")
    vertical_fill = LayoutAttribute[bool](False)
    horizontal_fill = LayoutAttribute[bool](False)
    margin = LayoutAttribute[int](0)

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
