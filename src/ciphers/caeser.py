class CeaserCipher:
    polish_alphabet = "abcdefghijklmnopqrstuvwxyząćęłńóśźż"

    def _shift_index(self, char: str, shift: int) -> str:
        if char in self.polish_alphabet:
            index = self.polish_alphabet.index(char)
            new_index = (index + shift) % len(self.polish_alphabet)
            return self.polish_alphabet[new_index]
        elif char in self.polish_alphabet.upper():
            index = self.polish_alphabet.upper().index(char)
            new_index = (index + shift) % len(self.polish_alphabet.upper())
            return self.polish_alphabet.upper()[new_index]
        return char

    def encrypt(self, text: str, shift: int) -> str:
        if shift < 0:
            raise ValueError("Shift value cannot be negative.")
        return ''.join(self._shift_index(char, shift) for char in text)

    def decrypt(self, text: str, shift: int) -> str:
        if shift < 0:
            raise ValueError("Shift value cannot be negative.")
        return ''.join(self._shift_index(char, shift) for char in text)
