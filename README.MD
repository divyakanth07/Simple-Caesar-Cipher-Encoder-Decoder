# Caesar Cipher Encoder

This project provides a basic implementation of a Caesar Cipher Encoder. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a certain number of positions down or up the alphabet. In this version, the code allows you to encode a string of text by shifting each character by a specified number.

## How It Works

The `encrypt()` function accepts two inputs:

1. `text` (string): The text you want to encode.
2. `s` (int): The number of positions to shift each letter in the text.

For each character in the input `text`, the function checks if the character is uppercase or lowercase and applies the appropriate shift. The result is a string where each letter is shifted by `s` positions.

### Example Output
``` bash
What happened to ceaser? he died
What number is under that rock ???3
CEASERRRRRRRRRRRRRRRRRRRR :he died
CEASERRRRRRRRRRRRRRRRRRRRrrrrrrrrrrrrr:3
ccccCCeaserrrrrrrrrrrrrrrRRRRRRRRRRRRRRRRRRRRRRRRRRR: khqglhg

```


> The `encrypt()` function shifts each letter by the value `3` in this example (which is the number chosen in the prompt). This function will be used for encoding the text.

## Usage

1. Run the code.
2. You will be prompted to enter the text you want to encode.
3. You will also be prompted to enter the number of positions you'd like to shift each character.
4. The output will display the original text and the encoded string.

### Inputs:
- **Text**: The sentence or phrase to be encoded.
- **Shift Number**: The number of positions to shift each character in the text.

## Future Enhancements

- A decoder function will be added soon to reverse the encryption and decode the message.
