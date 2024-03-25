import os
from ti6huff import Huffman
from ti6hamm import Hamming

# Проверка наличия файла logfile.txt и его создание, если не существует
if not os.path.exists("logfile.txt"):
    with open("logfile.txt", "w") as file:
        file.write("Log file created.\n")

def menu():
    print("1. Кодировать")
    print("2. Декодировать")
    choice = input("Выберите операцию (1/2): ")
    return choice

def main():
    choice = menu()
    if choice == '1':
        encoding_method = input("Выберите метод кодирования (huffman/hamming): ")
        data = input("Введите данные для кодирования: ")
        if encoding_method == 'huffman':
            huffman = Huffman()
            encoded_data = huffman.encode(data)
            print("Закодированные данные:", encoded_data)
            with open("logfile.txt", "a") as file:
                file.write("Huffman encoding: {}\n".format(encoded_data))
        elif encoding_method == 'hamming':
            hamming = Hamming()
            encoded_data = hamming.encode(data)
            print("Закодированные данные:", encoded_data)
            with open("logfile.txt", "a") as file:
                file.write("Hamming encoding: {}\n".format(encoded_data))
        else:
            print("Неверный метод кодирования.")
    elif choice == '2':
        decoding_method = input("Выберите метод декодирования (huffman/hamming): ")
        encoded_data = input("Введите закодированные данные: ")
        if decoding_method == 'huffman':
            huffman = Huffman()
            decoded_data = huffman.decode(encoded_data, {})  # Пустой словарь, так как для декодирования не требуется
            print("Декодированные данные:", decoded_data)
            with open("logfile.txt", "a") as file:
                file.write("Huffman decoding: {}\n".format(decoded_data))
        elif decoding_method == 'hamming':
            hamming = Hamming()
            decoded_data = hamming.decode(encoded_data)
            print("Декодированные данные:", decoded_data)
            with open("logfile.txt", "a") as file:
                file.write("Hamming decoding: {}\n".format(decoded_data))
        else:
            print("Неверный метод декодирования.")
    else:
        print("Неверный выбор операции.")

if __name__ == "__main__":
    main()
