from lab4.user_input import get_user_input
from lab4.art_generator import generate_ascii_art, align_text
from lab4.art_display import display_art, preview_art
from lab4.art_saver import save_art

def main():
    symbols = ['@', '#', '*', '+', '.']
    text, width, height, alignment, color_option = get_user_input()

    # Обмеження на розміри
    width = min(width, 100)
    height = min(height, 30)

    art = generate_ascii_art(text, width, height, symbols)
    aligned_art = align_text(art, alignment, width)

    preview_art(aligned_art)

    save_option = input("Бажаєте зберегти ASCII-арт? (yes/no): ").strip().lower()
    if save_option == 'yes':
        save_art(aligned_art)

if __name__ == "__main__":
    main()