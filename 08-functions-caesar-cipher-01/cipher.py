"""
Core Caesar Cipher logic.

Contains:
- Data model for cipher input
- Caesar cipher implementation
"""

from dataclasses import dataclass
from typing import Literal

from runtime_callable import runtime_only


@dataclass
class CipherInput:
    """
    Data model representing input required for Caesar cipher.

    Attributes:
        alphabet: List of characters defining the cipher domain
        direction: Operation type ("encode" or "decode")
        text: Input text to transform
        shift: Shift amount for cipher
    """
    alphabet: list[str]
    direction: str
    text: str
    shift: int


class CaesarCipher:
    """
    Caesar Cipher implementation using a configurable alphabet.
    """

    def __init__(self, cipher_input: CipherInput):
        """
        Initialize cipher with input configuration.

        Args:
            cipher_input: Structured input data for cipher
        """
        self.alphabet = cipher_input.alphabet
        self.text = cipher_input.text
        self.shift = cipher_input.shift

        # Precompute lookup map for O(1) character index access
        self._index_map = {char: i for i, char in enumerate(self.alphabet)}

    @runtime_only
    def transform(self, direction: Literal["encode", "decode"]) -> str:
        """
        Transform text using Caesar cipher logic.

        Args:
            direction: "encode" to encrypt, "decode" to decrypt

        Returns:
            Transformed text

        Raises:
            ValueError: If direction is invalid
        """
        if direction not in ("encode", "decode"):
            raise ValueError("direction must be 'encode' or 'decode'")

        alphabet_size = len(self.alphabet)

        # Normalize shift to handle large values
        shift = self.shift % alphabet_size

        # Reverse shift direction for decoding
        if direction == "decode":
            shift = -shift

        result: list[str] = []

        # Transform each character using index-based shifting
        for char in self.text:
            idx = self._index_map[char]
            new_idx = (idx + shift) % alphabet_size
            result.append(self.alphabet[new_idx])

        return "".join(result)

# end of file