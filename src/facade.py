from datetime import datetime

from src.ciphers.caeser import CeaserCipher
from src.files import JSONManager
from src.history import Record, OperationType


class Menu:
    def __init__(self):
        self.__is_running = True
        self.options = {
            "1": self.encrypt_sentence,
            "2": self.decrypt_sentence,
            "3": self.save_history_to_json_file,
            "4": self.load_history_from_json_file,
            "5": self.display_operations,
            "6": self.exit,
        }
        self.history: list[Record] = []
        self.cipher = CeaserCipher()
        self.file_manager = JSONManager()

    def loop(self):
        while self.__is_running:
            self.show_menu()
            try:
                self.get_and_execute_choice()
            except KeyError:
                self.show_error()
                print("Invalid choice. Please try again.")

    @staticmethod
    def show_menu():
        print("====\nCaesar Cipher Menu:===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Save History to JSON file")
        print("4. Load History from JSON file")
        print("5. Display Operations")
        print("6. Exit")

    def get_and_execute_choice(self):
        user_choice = input("Enter your choice: ")
        self.options.get(user_choice, self.show_error)()

    def display_operations(self):
        print("Operations:")
        if not self.history:
            print("No operations yet.")
        for idx, operation in enumerate(self.history, 1):
            print(f"{idx}.")
            print(operation)

    @staticmethod
    def show_error():
        print("Invalid choice.")

    def encrypt_sentence(self):
        text = input("Enter text to encrypt: ")
        shift = int(input("Enter shift value: "))
        encrypted_text = self.cipher.encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
        self.history.append(
            Record(OperationType.ENCRYPTING, text, encrypted_text, shift)
        )

    def decrypt_sentence(self):
        print("Decrypting")
        text = input("Enter text to decrypt: ")
        shift = int(input("Enter shift value: "))
        decrypted_text = self.cipher.decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")
        self.history.append(
            Record(OperationType.DECRYPTING, text, decrypted_text, shift)
        )

    def save_history_to_json_file(self):
        if not self.history:
            print("No operations to save.")
            return
        else:
            print("=== Saving to history.json ===")
            file_name = input("Enter file name: ")
            self.file_manager.save_to_json(self.history, file_name)
            print(f"History saved to {file_name}.")

    from datetime import datetime

    def load_history_from_json_file(self):
        print("=== Loading from history.json ===")
        file_name = input("Enter file name: ")
        loaded_data = JSONManager.load_from_json(file_name)

        self.history = [
            Record(
                operation=OperationType(record['operation']),
                input_text=record['input_text'],
                output_text=record['output_text'],
                shift=record['shift'],
                time=datetime.strptime(record['time'], '%Y-%m-%d %H:%M:%S')  # Konwersja na datetime
            ) for record in loaded_data
        ]

        print(f"Data loaded from {file_name} and data is: {loaded_data}")

    def exit(self):
        self.__is_running = False
        print("Goodbye")
