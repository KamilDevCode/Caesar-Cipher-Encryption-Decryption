from src.ciphers.caeser import CeaserCipher


class Menu:
    def __init__(self):
        self.__is_running = True
        self.options = {
            "1": self.encrypt_sentence,
            "2": self.decrypt_sentence,
            "3": self.display_operations,
            "4": self.exit,
        }
        self.history = []
        self.cipher = CeaserCipher()

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

    def decrypt_sentence(self):
        print("Decrypting")
        text = input("Enter text to decrypt: ")
        shift = int(input("Enter shift value: "))
        decrypted_text = self.cipher.decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")

    def exit(self):
        self.__is_running = False
        print("Goodbye")
