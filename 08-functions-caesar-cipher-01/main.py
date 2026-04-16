"""
Application entry point.

Handles:
- User input
- Validation
- Orchestration of cipher logic
"""

from string import ascii_lowercase

from runtime_callable import runtime_only
from cipher import CipherInput, CaesarCipher


@runtime_only
def get_cipher_input(alphabet: list[str]) -> CipherInput:
    """
    Collect and validate user input for cipher.

    Returns:
        CipherInput: Validated input data

    Raises:
        ValueError: If any input is invalid
    """

    # Collect direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ("encode", "decode"):
        raise ValueError("Invalid direction. Please enter 'encode' or 'decode'.")

    # Collect text
    text = input("Type your message:\n").lower()
    if not text.isalpha():
        raise ValueError("Invalid input. Please enter message as alphabets only.")

    # Collect shift
    shift_input = input("Type the shift number:\n")
    if not shift_input.isdecimal():
        raise ValueError("Invalid shift. Please enter a valid shift amount.")

    shift = int(shift_input)

    return CipherInput(
        alphabet=alphabet,
        direction=direction,
        text=text,
        shift=shift,
    )


@runtime_only
def run_app() -> None:
    """
    Run the interactive Caesar cipher application loop.
    """
    while True:
        try:
            # Get validated user input
            cipher_input = get_cipher_input(alphabet=list(ascii_lowercase))

            # Initialize cipher engine
            cipher = CaesarCipher(cipher_input)

            # Perform transformation
            result = cipher.transform(cipher_input.direction)
            print(result)

            # Continue prompt
            choice = input('Do you wish to continue? "y" for yes and "n" for no: ').lower()

            if choice == "y":
                continue
            if choice == "n":
                break

            raise ValueError("Invalid choice!")

        except ValueError as e:
            print(f"Error: {e}\n---------------")


if __name__ == "__main__":
    run_app()