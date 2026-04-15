from string import ascii_lowercase
from RuntimeCallable import runtime_only

class CipherInput:

    def __init__(self) -> None:
        """
        Initialise the user-specific Cipher input.
        """

        self.alphabet = list(ascii_lowercase)
        self.direction = ''
        self.text = ''
        self.shift = 0

    @runtime_only
    def cipher_input(self) -> None:

        self.direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if self.direction not in ('encode', 'decode'):
            raise ValueError("Invalid direction. Please enter 'encode' or 'decode'.")

        self.text = input('Type your message:\n').lower()
        if not self.text.isalpha():
            raise ValueError("Invalid input. Please enter message as alphabets only.")

        self.shift = input('Type the shift number:\n')
        if not self.shift.isdecimal():
            raise ValueError("Invalid shift. Please enter a valid shift amount.")
        else:
            self.shift = int(self.shift)