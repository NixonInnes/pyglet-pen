
from .layout import Layout


class FloatingLayout(Layout):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.contents = []
        return instance
    
    @property
    def n_items(self):
        return len(self.contents)
    
    def add_content(self, item):
        self.contents.append(item)
        self.update_content_geometry()

    def update_content_geometry(self):
        if self.n_items < 1:
            return
        
        available_width = self.width - (2 * self.margin)
        available_height = self.height - (2 * self.margin)
        
        start_x = self.x + self.margin
        start_y = self.y + self.margin

        for item in self.contents:
            if self.n_items < 1:
                return
            
            if self.horizontal_fill:
                item.width = available_width
            else:
                item.width = item.initial.width
            
            if self.vertical_fill:
                item.height = available_height
            else:
                item.height = item.initial.height
            
            if self.horizontal_alignment == "left":
                item.x = start_x
            else:
                space = available_width - item.width
                if self.horizontal_alignment == "center":
                    item.x = start_x + (space // 2)
                elif self.horizontal_alignment == "right":
                    item.x = start_x + space
                else:
                    raise ValueError("Invalid horizontal alignment: {self.horizontal_alignment}")
            
            if self.vertical_alignment == "bottom":
                item.y = start_y
            else:
                space = available_height - item.height
                if self.vertical_alignment == "center":
                    item.y = start_y + (space // 2)
                elif self.vertical_alignment == "top":
                    item.y = start_y + space
                else:
                    raise ValueError("Invalid vertical alignment: {self.vertical_alignment}")
            
            
            if isinstance(item, Layout):
                item.update_content_geometry()