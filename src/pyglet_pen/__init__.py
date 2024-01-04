# SPDX-FileCopyrightText: 2023-present James Innes <james.innes@echonet.io>
#
# SPDX-License-Identifier: MIT

import os
import pyglet

material_icons_file = os.path.join(os.path.dirname(__file__), "assets", "MaterialIcons-Regular.ttf")

pyglet.font.add_file(material_icons_file)