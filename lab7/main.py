from lab7.api_handler import APIHandler
from lab7.user_input_handler import UserInputHandler
from lab7.data_visualizer import DataVisualizer
from lab7.data_saver import DataSaver

def main():
    api_handler = APIHandler()
    user_input_handler = UserInputHandler()
    data_visualizer = DataVisualizer()
    data_saver = DataSaver()

    # Отримуємо дані з API
    data = api_handler.fetch_data()
    if data is None:
        return

    # Головний цикл програми
    while True:
        choice = user_input_handler.get_user_choice()
        if user_input_handler.validate_choice(choice):
            if choice == "1":
                data_visualizer.display_data(data, display_type="table")
            elif choice == "2":
                data_visualizer.display_data(data, display_type="list")
            elif choice == "3":
                file_format = input("Оберіть формат (json/csv/txt): ").strip().lower()
                data_saver.save_data(data, file_format=file_format)
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        next_action = input("Бажаєте продовжити? (y/n): ").strip().lower()
        if next_action != "y":
            break

if __name__ == "__main__":
    main()
