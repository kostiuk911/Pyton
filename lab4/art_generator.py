def generate_ascii_art(text, width, height, symbols):
    art = []
    for i in range(height):
        line = ""
        for j in range(width):
            if j < len(text):
                line += symbols[i % len(symbols)] if text[j] != ' ' else ' '
            else:
                line += ' '
        art.append(line)
    return art

def align_text(art, alignment, width):
    aligned_art = []
    for line in art:
        if alignment == 'left':
            aligned_art.append(line)
        elif alignment == 'center':
            aligned_art.append(line.center(width))
        elif alignment == 'right':
            aligned_art.append(line.rjust(width))
    return aligned_art