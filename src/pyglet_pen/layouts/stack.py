from typing import Literal, Optional, List

from pyglet_pen.widgets.widget import Widget
from .layout import Layout, LayoutAttribute


class StackLayout(Layout):
    stack_direction = LayoutAttribute[Literal["vertical", "horizontal"]]("vertical")
    padding = LayoutAttribute[int](0)

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance._contents = []
        return instance
    
    @property
    def contents(self):
        return self._contents
    
    @property
    def total_padding(self):
        return (self.n_items - 1) * self.padding
    
    def add_content(self, item):
        if self.stack_direction == "horizontal":
            self.contents.append(item)
        else:  # stack_direction == "vertical"
            self.contents.insert(0, item)
        # self.update_content_geometry()

    def update_content_geometry(self):
        print("Updating content geometry")
        if self.n_items < 1:
            return

        start_x = self.x + self.margin
        start_y = self.y + self.margin

        total_initial_item_width = sum(item.initial.width for item in self.contents)
        total_initial_item_height = sum(item.initial.height for item in self.contents)

        item_proportional_widths = [item.initial.width / total_initial_item_width for item in self.contents]
        item_proportional_heights = [item.initial.height / total_initial_item_height for item in self.contents]

        if self.stack_direction == "horizontal":
            # Calculate width and height of item
            match (self.horizontal_fill, self.vertical_fill, self.allow_oversize):
                case (True, True, True):
                    item_widths = [(self.available_width - self.total_padding) * item_proportional_widths[i] for i, _ in enumerate(self.contents)]
                    item_heights = [max(self.available_height, item.initial.height) for item in self.contents]

                case (True, True, False):
                    item_widths = [(self.available_width - self.total_padding) * item_proportional_widths[i] for i, _ in enumerate(self.contents)]
                    item_heights = [self.available_height for _ in self.contents]
                
                case (True, False, True):
                    item_widths = [(self.available_width - self.total_padding) * item_proportional_widths[i] for i, _ in enumerate(self.contents)]
                    item_heights = [item.initial.height for item in self.contents]
                
                case (True, False, False):
                    item_widths = [(self.available_width - self.total_padding) * item_proportional_widths[i] for i, _ in enumerate(self.contents)]
                    item_heights = [min(self.available_height, item.initial.height) for item in self.contents]
                
                case (False, True, True):
                    item_widths = [item.initial.width for item in self.contents]
                    item_heights = [max(self.available_height, item.initial.height) for item in self.contents]

                case (False, True, False):
                    item_widths = [min((self.available_width - self.total_padding) * item_proportional_widths[i], item.initial.width) for i, item in enumerate(self.contents)]
                    item_heights = [self.available_height for _ in self.contents]

                case (False, False, True):
                    item_widths = [item.initial.width for item in self.contents]
                    item_heights = [item.initial.height for item in self.contents]
                
                case (False, False, False):
                    item_widths = [min((self.available_width - self.total_padding) * item_proportional_widths[i], item.initial.width) for i, item in enumerate(self.contents)]
                    item_heights = [min(self.available_height, item.initial.height) for item in self.contents]

                case _:
                    raise NotImplementedError()
                
        elif self.stack_direction == "vertical":
            match (self.horizontal_fill, self.vertical_fill, self.allow_oversize):
                case (True, True, True):
                    item_widths = [max(self.available_width, item.initial.width) for item in self.contents]
                    item_heights = [(self.available_height - self.total_padding) * item_proportional_heights[i] for i, _ in enumerate(self.contents)]
                
                case (True, True, False):
                    item_widths = [self.available_width for _ in self.contents]
                    item_heights = [(self.available_height - self.total_padding) * item_proportional_heights[i] for i, _ in enumerate(self.contents)]
                
                case (True, False, True):
                    item_widths = [max(self.available_width, item.initial.width) for item in self.contents]
                    item_heights = [item.initial.height for item in self.contents]

                case (True, False, False):
                    item_widths = [self.available_width for _ in self.contents]
                    item_heights = [min((self.available_height - self.total_padding) * item_proportional_heights[i], item.initial.height) for i, item in enumerate(self.contents)]
                
                case (False, True, True):
                    item_widths = [item.initial.width for item in self.contents]
                    item_heights = [(self.available_height - self.total_padding) * item_proportional_heights[i] for i, _ in enumerate(self.contents)]
                
                case (False, True, False):
                    item_widths = [min(self.available_width, item.initial.width) for item in self.contents]
                    item_heights = [(self.available_height - self.total_padding) * item_proportional_heights[i] for i, _ in enumerate(self.contents)]
                
                case (False, False, True):
                    item_widths = [item.initial.width for item in self.contents]
                    item_heights = [item.initial.height for item in self.contents]
                
                case (False, False, False):
                    item_widths = [min(self.available_width, item.initial.width) for item in self.contents]
                    item_heights = [min((self.available_height - self.total_padding) * item_proportional_heights[i], item.initial.height) for i, item in enumerate(self.contents)]

                case _:
                    raise NotImplementedError()

        for i, item in enumerate(self.contents):
            item.width = item_widths[i]
            item.height = item_heights[i]

            # Calculate x and y of item
            if self.stack_direction == "horizontal":
                match (self.horizontal_alignment, self.vertical_alignment):
                    case ("left", "top"):
                        item.x = start_x + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + self.available_height - item.height
                    
                    case ("left", "center"):
                        item.x = start_x + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + (self.available_height // 2) - (item.height // 2)
                    
                    case ("left", "bottom"):
                        item.x = start_x + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y
                    
                    case ("center", "top"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + (space // 2) + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + self.available_height - item.height
                    
                    case ("center", "center"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + (space // 2) + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + (self.available_height // 2) - (item.height // 2)
                    
                    case ("center", "bottom"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + (space // 2) + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y
                    
                    case ("right", "top"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + space + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + self.available_height - item.height
                    
                    case ("right", "center"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + space + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y + (self.available_height // 2) - (item.height // 2)

                    case ("right", "bottom"):
                        space = self.available_width - sum(item_widths) - self.total_padding
                        item.x = start_x + space + sum(item_widths[:i]) + i * self.padding
                        item.y = start_y
                    
                    case _:
                        raise NotImplementedError()
            
            elif self.stack_direction == "vertical":
                match (self.horizontal_alignment, self.vertical_alignment):
                    case ("left", "top"):
                        item.x = start_x
                        item.y = start_y + self.available_height - sum(item_heights[i:]) - (self.n_items - i - 1) * self.padding

                    case ("left", "center"):
                        space = self.available_height - sum(item_heights) - self.total_padding
                        item.x = start_x
                        item.y = start_y + (space // 2) + sum(item_heights[:i]) + i * self.padding
                    
                    case ("left", "bottom"):
                        item.x = start_x
                        item.y = start_y + sum(item_heights[:i]) + i * self.padding

                    case ("center", "top"):
                        space = self.available_width - item.width
                        item.x = start_x + (space // 2)
                        item.y = start_y + self.available_height - sum(item_heights[i:]) - (self.n_items - i - 1) * self.padding

                    case ("center", "center"):
                        x_space = self.available_width - item.width
                        item.x = start_x + (x_space // 2)
                        y_space = self.available_height - sum(item_heights) - self.total_padding
                        item.y = start_y + (y_space // 2) + sum(item_heights[:i]) + i * self.padding

                    case ("center", "bottom"):
                        space = self.available_width - item.width
                        item.x = start_x + (space // 2)
                        item.y = start_y + sum(item_heights[:i]) + i * self.padding

                    case ("right", "top"):
                        space = self.available_width - item.width
                        item.x = start_x + space
                        item.y = start_y + self.available_height - sum(item_heights[i:]) - (self.n_items - i - 1) * self.padding
                    
                    case ("right", "center"):
                        space = self.available_width - item.width
                        item.x = start_x + space
                        y_space = self.available_height - sum(item_heights) - self.total_padding
                        item.y = start_y + (y_space // 2) + sum(item_heights[:i]) + i * self.padding
                    
                    case ("right", "bottom"):
                        space = self.available_width - item.width
                        item.x = start_x + space
                        item.y = start_y + sum(item_heights[:i]) + i * self.padding

                    case _:
                        raise NotImplementedError()

            if isinstance(item, (Layout, Widget)):
                item.update_content_geometry()
