from RuntimeCallable import runtime_only
from CipherInput import CipherInput

class Cipher:

    def __init__(self, alphabet: list[str], original_text: str, shift_amount: int):
        """
            Initialise the Cipher object.
            Parameters:
                alphabet (list[str]): Alphabet list
                original_text (str): Original text to be ciphered
                shift_amount (int): Shift amount
        """
        self.alphabet = alphabet
        self.original_text = original_text
        self.shift_amount = shift_amount

    # @functools.lru_cache(maxsize=None, typed=True)
    @runtime_only
    def encrypt(self) -> str:
        """
            Encrypt the input text using a Caesar cipher.
            Returns:
                str: Encrypted text.
        """

        alphabet_size = len(self.alphabet)

        normalised_shift_amount = self.shift_amount % alphabet_size # normalize shift

        result = []

        # Precompute lookup: O(n)
        index_map = {char: i for i, char in enumerate(self.alphabet)}

        for char in self.original_text:
            idx = index_map[char] # find position
            new_idx = (idx + normalised_shift_amount) % alphabet_size # shift + wrap
            result.append(self.alphabet[new_idx])  # map back

        # legacy: without map O(n^2)
        # for char in self.original_text:
        #     idx = self.alphabet.index(char)  # find position
        #     new_idx = (idx + normalised_shift_amount) % alphabet_size  # shift + wrap
        #     result.append(self.alphabet[ new_idx ])  # map back

            # legacy: without list
            # encrypted_char = chr((ord(char) - ord('a') + shift_amount) % alphabet_size + ord('a'))
            # result.append(encrypted_char)

        return "".join(result)


def run_app() -> None:

    init_obj = CipherInput()
    init_obj.cipher_input()

    cipher_obj = Cipher(alphabet=init_obj.alphabet, original_text=init_obj.text, shift_amount=init_obj.shift)

    if init_obj.direction == 'encode':
        print(cipher_obj.encrypt())

if __name__ == '__main__':
    run_app()

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the ALPHABET
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

