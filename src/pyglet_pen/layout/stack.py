from typing import Literal

from .layout import Layout, LayoutAttribute


class StackLayout(Layout):
    stack_direction = LayoutAttribute[Literal["vertical", "horizontal"]]("vertical")
    padding = LayoutAttribute[int](0)

    def __init__(self, *args, **kwargs):
        self.contents = []
    
    @property
    def n_items(self):
        return len(self.contents)
    
    def add(self, item):
        self.contents.append(item)
        self.update_content_geometry()

    def update_content_geometry(self):
        if self.n_items < 1:
            return
        
        total_padding = (self.n_items - 1) * self.padding
        available_width = self.width - (2 * self.margin)
        available_height = self.height - (2 * self.margin)

        start_x = self.x + self.margin
        start_y = self.y + self.margin

        if self.horizontal_fill:
            if self.stack_direction == "horizontal":
                fill_width = (available_width - total_padding) // self.n_items
            else:  # stack_direction == "vertical"
                fill_width = available_width
        else:
            fill_width = None
        
        if self.vertical_fill:
            if self.stack_direction == "horizontal":
                fill_height = available_height
            else:  # stack_direction == "vertical"
                fill_height = (available_height - total_padding) // self.n_items
        else:
            fill_height = None

        item_heights = []
        item_widths = []

        # Set and record the height and width of each item
        for item in self.contents:
            item.height = item.initial.height if fill_height is None else fill_height
            item_heights.append(item.height)
            item.width = item.initial.width if fill_width is None else fill_width
            item_widths.append(item.width)

        # Calculate the x and y of all items
        for i, item in enumerate(self.contents):
            # Calculate the position for each item
            if self.stack_direction == "horizontal":
                # Horizontal stack: Calculate x position (horizontal alignment)
                if self.horizontal_alignment == "left":
                    item.x = start_x + sum(item_widths[:i]) + i * self.padding
                else:
                    space = available_width - sum(item_widths) - total_padding
                    if self.horizontal_alignment == "center":
                        item.x = start_x + (space // 2) + sum(item_widths[:i]) + i * self.padding
                    elif self.horizontal_alignment == "right":
                        item.x = start_x + space + sum(item_widths[:i]) + i * self.padding
                    else:
                        raise ValueError(f"Invalid horizontal alignment: {self.horizontal_alignment}")

                # Horizontal stack: Calculate y position (vertical alignment)
                if self.vertical_alignment == "top":
                    item.y = start_y + available_height - item.height
                else:
                    space = available_height - item.height
                    if self.vertical_alignment == "center":
                        item.y = start_y + (space // 2)
                    elif self.vertical_alignment == "bottom":
                        item.y = start_y
                    else:
                        raise ValueError(f"Invalid vertical alignment: {self.vertical_alignment}")

            elif self.stack_direction == "vertical":
                # Vertical stack: Calculate x position (horizontal alignment)
                if self.horizontal_alignment == "left":
                    item.x = start_x
                else:
                    space = available_width - item.width
                    if self.horizontal_alignment == "center":
                        item.x = start_x + (space // 2)
                    elif self.horizontal_alignment == "right":
                        item.x = start_x + space
                    else:
                        raise ValueError(f"Invalid horizontal alignment: {self.horizontal_alignment}")

                # Vertical stack: Calculate y position (vertical alignment)
                if self.vertical_alignment == "top":
                    #item.y = start_y + available_height - sum(item_heights) - total_padding + sum(item_heights[:i]) + i * self.padding
                    item.y = start_y + available_height - sum(item_heights[i:]) - (self.n_items - i - 1) * self.padding
                else:
                    space = available_height - sum(item_heights) - total_padding
                    if self.vertical_alignment == "center":
                        item.y = start_y + (space // 2) + sum(item_heights[:i]) + i * self.padding
                    elif self.vertical_alignment == "bottom":
                        item.y = start_y + sum(item_heights[:i]) + i * self.padding
                    else:
                        raise ValueError(f"Invalid vertical alignment: {self.vertical_alignment}")
            
            else:
                raise ValueError(f"Invalid stack direction: {self.stack_direction}")
        
            if isinstance(item, Layout):
                item.update_content_geometry()

        # No need to reset current_x or current_y as they are recalculated each time this method is called


    

