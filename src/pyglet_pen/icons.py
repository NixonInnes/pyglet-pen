import json

class Icon:
    pass

with open("src/pyglet_pen/assets/MaterialIcons-CharacterList.json") as file:
    material_icons_dict = json.load(file)

for icon in material_icons_dict["icons"]:
    setattr(Icon, icon["id"].upper(), chr(int(icon['unicode'], 16)))
