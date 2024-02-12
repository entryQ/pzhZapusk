#MORSE_CODE_DICT_program.py

from encoder import text_to_morse, encode_input
from decoder import morse_to_text, decode_input

def main():
    while True:
        print("Выберите действие:")
        print("1. Кодировать текст в азбуке Морзе")
        print("2. Декодировать азбуку Морзе в текст")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            text_input = encode_input()
            MORSE_CODE_DICT = text_to_morse(text_input)
            print("Результат кодирования: ", MORSE_CODE_DICT)

            save_to_file = input("Желаете сохранить результат в файл? (y/n): ")
            if save_to_file.lower() == 'y':
                filename = input("Введите имя файла: ")
                with open(filename, 'w') as file:
                    file.write(MORSE_CODE_DICT)

        elif choice == '2':
            morse_input = decode_input()
            text = morse_to_text(morse_input)
            print("Результат декодирования: ", text)

            save_to_file = input("Желаете сохранить результат в файл? (y/n): ")
            if save_to_file.lower() == 'y':
                filename = input("Введите имя файла: ")
                with open(filename, 'w') as file:
                    file.write(text)

        elif choice == '3':
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()