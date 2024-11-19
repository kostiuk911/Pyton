import pyfiglet

# Генерація ASCII-арту
def generate_ascii_art(text, font):
    return pyfiglet.figlet_format(text, font=font)

# Вибір шрифту
def choose_font():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Доступні шрифти:")
    for i, font in enumerate(fonts):
        print(f"{i + 1}. {font}")
    choice = int(input("\nВиберіть шрифт за номером: ")) - 1
    return fonts[choice]

# Масштабування ASCII-арту
def resize_ascii_art(text, font, width):
    figlet = pyfiglet.Figlet(font=font)
    ascii_art_lines = figlet.renderText(text).splitlines()
    
    resized_ascii_art = ""
    for line in ascii_art_lines:
        wrapped_line = [line[i:i+width] for i in range(0, len(line), width)]
        resized_ascii_art += "\n".join(wrapped_line) + "\n"
    
    return resized_ascii_art

# Заміна символів
def replace_characters(ascii_art, old_char, new_char):
    return ascii_art.replace(old_char, new_char)
