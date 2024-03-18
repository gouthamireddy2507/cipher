# cipher
**A toy text encryption model using python.**

Create your own Cipher:  You can choose from a variety of substitution, transposition, morse, or anything else. Cipher should have both encrypt and decrypt capabilities.

Build a command line tool with following possible options:

<name-of-your-cipher-program>  -encrypt <input file> <output file>: Given an input text, create cipherText in output file

<name-of-your-cipher-program>  -decrypt <input file> <output file>: Given your own Cipher text as input , decrypt and create plain text in output file.

<name-of-your-cipher-program>  -test <input file> , Tests if given input file was encrypted using your own cipher tool.  Returns True if the input was your own ciphertext, False for everything else

<name-of-your-cipher-program>  -help: Prints help for the tool

e.g. myCipher -encrypt input.txt output.txt
myCipher -test <Myciphertext> : -> True

**Must have:**

Your cipher logic should not be obvious. For example, if I run your Cipher with Input of A to Z characters and 0 to 9 numbers, I should not get a cipher text that easily tells me logic of substitution. (e.g Each letter is replaced by next letter etc)

The Cipher should insert some identification in the cipher text so that you identify it is your own cipher

Your cipher should only decrypt your own Cipher text, it should reject any other input.

Lossless conversion. If I cycle between encryption and decryption, it should not result in any loss of plaintext

Multi-round substitutions are possible, doable. Makes the cipher more unique and robust, but I leave this choice to you. This is not mandatory  

Running cipher multiple times on cipher text is not required, to keep this simple.  

Build anti-tampering: You should be able to detect if your Cipher text is tampered with

- Refer to cipher_encryption.py and cipher_decryption.py for encryption and decryption codes respectively.
