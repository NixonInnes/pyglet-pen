import unicodedata

# Replace 'YourFontFile.ttf' with the path to your TTF font file
font_file = 'src/pyglet_pen/assets/MaterialIcons-Regular.ttf'

# Open the font file in binary mode
with open(font_file, 'rb') as file:
    # Read the file content
    font_data = file.read()

# Initialize an empty set to store unique characters
unique_characters = set()

# Iterate through each byte in the font data
for byte in font_data:
    # Convert the byte to a Unicode character
    try:
        char = chr(byte)
        # Check if the character is printable and not a control character
        if unicodedata.category(char) != 'Cc':
            unique_characters.add(char)
    except UnicodeDecodeError:
        pass

# Sort the unique characters and print them
sorted_characters = sorted(unique_characters)
for char in sorted_characters:
    print(char)
