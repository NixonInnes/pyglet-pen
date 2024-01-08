
from .layout import Layout, LayoutAttribute


class GridLayout(Layout):
    n_rows = LayoutAttribute[int](1)
    n_cols = LayoutAttribute[int](1)
    cell_margin = LayoutAttribute[int](0)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._contents = {}
        for i in range(instance.n_rows):
            for j in range(instance.n_cols):
                instance._contents[(i, j)] = GridLayoutCell(
                    width=instance.available_width // instance.n_cols,
                    height=instance.available_height // instance.n_rows,
                    vertical_alignment=instance.vertical_alignment,
                    horizontal_alignment=instance.horizontal_alignment,
                    vertical_fill=instance.vertical_fill,
                    horizontal_fill=instance.horizontal_fill,
                    margin=instance.cell_margin,
                )
        return instance
    
    @property
    def contents(self):
        return list(self._contents.values())

    def add_content(self, item, row, col):
        self._contents[(row, col)].add_content(item)
        # self.update_content_geometry()

    def update_content_geometry(self):
        print("Updating content geometry")
        if self.n_items < 1:
            return

        start_x = self.x + self.margin
        start_y = self.y + self.margin

        cell_width = self.available_width // self.n_cols
        cell_height = self.available_height // self.n_rows

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                cell = self._contents[(i, j)]
                cell.x = start_x + (j * cell_width)
                cell.y = start_y + (i * cell_height)
                cell.width = cell_width
                cell.height = cell_height
                cell.vertical_alignment = self.vertical_alignment
                cell.horizontal_alignment = self.horizontal_alignment
                cell.vertical_fill = self.vertical_fill
                cell.horizontal_fill = self.horizontal_fill
                cell.update_content_geometry()

        
class GridLayoutCell(Layout):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._contents = None
        return instance
    
    @property
    def contents(self):
        return [self._contents]
    
    @property
    def content(self):
        return self._contents
    
    def add_content(self, item):
        self._contents = item

    def update_content_geometry(self):
        if self.content is None:
            return

        start_x = self.x + self.margin
        start_y = self.y + self.margin

        if self.horizontal_fill:
            self.content.width = self.available_width
        else:
            self.content.width = self.content.initial.width
        
        if self.vertical_fill:
            self.content.height = self.available_height
        else:
            self.content.height = self.content.initial.height

        if self.horizontal_alignment == "left":
            self.content.x = start_x
        else:
            space = self.available_width - self.content.width
            if self.horizontal_alignment == "center":
                self.content.x = start_x + (space // 2)
            elif self.horizontal_alignment == "right":
                self.content.x = start_x + space
            else:
                raise ValueError(f"Invalid horizontal alignment: {self.horizontal_alignment}")
        
        if self.vertical_alignment == "bottom":
            self.content.y = start_y
        else:
            space = self.available_height - self.content.height
            if self.vertical_alignment == "center":
                self.content.y = start_y + (space // 2)
            elif self.vertical_alignment == "top":
                self.content.y = start_y + space
            else:
                raise ValueError(f"Invalid vertical alignment: {self.vertical_alignment}")
        
        if isinstance(self.content, Layout):
            self.content.update_content_geometry()
