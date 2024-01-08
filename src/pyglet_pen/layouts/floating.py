
from .layout import Layout


class FloatingLayout(Layout):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._contents = []
        return instance
    
    @property
    def contents(self):
        return self._contents
    
    def add_content(self, item):
        self._contents.append(item)
        # self.update_content_geometry()

    def update_content_geometry(self):
        if self.n_items < 1:
            return
        
        start_x = self.x + self.margin
        start_y = self.y + self.margin

        for item in self.contents:
            if self.n_items < 1:
                return
            
            match (self.horizontal_fill, self.vertical_fill, self.allow_oversize):
                case (True, True, True):
                    item.width = max(self.available_width, item.initial.width)
                    item.height = self.available_height
                
                case (True, True, False):
                    item.width = self.available_width
                    item.height = max(self.available_height, item.initial.height)
                
                case (True, False, True):
                    item.width = max(self.available_width, item.initial.width)
                    item.height = item.initial.height

                case (True, False, False):
                    item.width = self.available_width
                    item.height = min(self.available_height, item.initial.height)
                
                case (False, True, True):
                    item.width = item.initial.width
                    item.height = max(self.available_height, item.initial.height)

                case (False, True, False):
                    item.width = min(self.available_width, item.initial.width)
                    item.height = self.available_height
                
                case (False, False, True):
                    item.width = item.initial.width
                    item.height = item.initial.height
                
                case (False, False, False):
                    item.width = min(self.available_width, item.initial.width)
                    item.height = min(self.available_height, item.initial.height)

                case _:
                    raise NotImplementedError()

            match (self.horizontal_alignment, self.vertical_alignment):
                case ("left", "top"):
                    item.x = start_x
                    y_space = self.available_height - item.height
                    item.y = start_y + y_space
                
                case ("left", "center"):
                    item.x = start_x
                    y_space = self.available_height - item.height
                    item.y = start_y + (y_space // 2)

                case ("left", "bottom"):
                    item.x = start_x
                    item.y = start_y

                case ("center", "top"):
                    x_space = self.available_width - item.width
                    item.x = start_x + (x_space // 2)
                    y_space = self.available_height - item.height
                    item.y = start_y + y_space
                
                case ("center", "center"):
                    x_space = self.available_width - item.width
                    item.x = start_x + (x_space // 2)
                    y_space = self.available_height - item.height
                    item.y = start_y + (y_space // 2)

                case ("center", "bottom"):
                    x_space = self.available_width - item.width
                    item.x = start_x + (x_space // 2)
                    item.y = start_y

                case ("right", "top"):
                    x_space = self.available_width - item.width
                    item.x = start_x + x_space
                    y_space = self.available_height - item.height
                    item.y = start_y + y_space

                case ("right", "center"):
                    x_space = self.available_width - item.width
                    item.x = start_x + x_space
                    y_space = self.available_height - item.height
                    item.y = start_y + (y_space // 2)

                case ("right", "bottom"):
                    x_space = self.available_width - item.width
                    item.x = start_x + x_space
                    item.y = start_y


            
            
            if isinstance(item, Layout):
                item.update_content_geometry()