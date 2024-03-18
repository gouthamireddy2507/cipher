"""
DECRYPTION

"""

inputfilename =input("enter the input file name: ")



with open(inputfilename, 'r', encoding = 'utf8') as f:
    lines = [line.rstrip() for line in f]
message = "".join(lines)
message = str(message)
#removes the key added after encryption

x = hash('SecurityIssue')
def containsAny(x, message):
    for c in message:
        if c in x:
            return True
        else:
            return 'tampered'

l = []
for key in message:
    if message[:5] in ['g^2r£','s=5%₹','A;/P₳','P!4]€','V@1:¥']:
        l.append(message[15:])
    else:
        break
        
cipher = l[0]

dec_dictLevel_1 ={'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                  'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R',
                  'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z', 'a': 'a',
                  'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
                  'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's',
                  't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', 'Ӓ': '9', '8': '8',
                  '7': '7', '6': '6', 'ß': '5', '4': '4', '3': '3', 'ä': '2', 'ü': '1', 'ö': '0', '人': '力',
                  'అ': 'అ', 'ఆ': 'ఆ', 'ఇ': 'ఇ', 'ఈ': 'ఈ', 'ఉ': 'ఉ', 'ఊ': 'ఊ', 'ఋ': 'ఋ','ౠ':'ౠ',
                  'ఎ': 'ఎ', 'ఏ': 'ఏ', 'ఐ': 'ఐ', 'ఒ': 'ఒ', 'ఓ': 'ఓ', 'ఔ': 'ఔ', 'స': 'స', 'క': 'క','ఖ':'ఖ',
                  'ఘ': 'ఘ', 'ఙ': 'ఙ', 'చ': 'చ', 'ఛ': 'ఛ', 'జ': 'జ', 'ఝ': 'ఝ', 'ఞ': 'ఞ', 'ట': 'ట',
                  'ఠ': 'ఠ', 'డ': 'డ', 'ఢ': 'ఢ', 'ణ': 'ణ', 'త': 'త', 'థ': 'థ'}
dec_dictLevel_2 = {'D': 'A', 'E': 'B', 'F': 'C', 'G': 'D', 'H': 'E', 'I': 'F', 'J': 'G', 'K': 'H', 'L': 'I',
                   'M': 'J', 'N': 'K', 'O': 'L', 'P': 'M', 'Q': 'N', 'R': 'O', 'S': 'P', 'T': 'Q', 'U': 'R',
                   'V': 'S', 'W': 'T', 'X': 'U', 'Y': 'V', 'Z': 'W', 'A': 'X', 'B': 'Y', 'C': 'Z', 'd': 'a',
                   'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g', 'k': 'h', 'l': 'i', 'm': 'j',
                   'n':'k','o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't',
                   'x': 'u', 'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z', '7': '9', '6': '8', '5': '7',
                   '4': '6', '3': '5', '2': '4', '1': '3', '0': '2', '9': '1', '8': '0', '力': 'ñ', 'అ': '~',
                   'ఆ': '!', 'ఇ': '@', 'ఈ': '#', 'ఉ': '$', 'ఊ': '_', 'ఋ': '%', 'ౠ': ')', 'ఏ': '^',
                   'ఐ': '-', 'ఒ': '&', 'ఔ': '(', 'ఎ': '*', 'ఓ': '+', 'క': '=', 'ఖ': '`', 'ఘ': '[', 'ఙ':';',
                   'చ': '|', 'ఛ': '}', 'జ': '?', 'ఝ': '/', 'ఞ': ']', 'ట': "'", 'ఠ': '>', 'డ': '{',
                   'ఢ': ':', 'ణ': '<', 'త': ',', 'థ': '.', 'స': '√'}
dec_dictLevel_3 = {'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
                   'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
                   'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'n': 'a',
                   'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
                   'x': 'k', 'y': 'l', 'z': 'm', 'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
                   'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'ñ': ' ', '5': '0',
                   '6': '1', '7': '2', '8': '3', '9': '4', '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',
                   '[': '!', ';': '@', '|': '#', '}': '$', '?': '_', '/': '%', ']': ')', "'": '^', '>': '-',
                   '{': '&', ':': '(', '<': '*', ',': '+', '.': '=', '!': '[', '@': ';', '#': '|', '$': '}',
                   '_': '?', '%': '/', ')': ']', '^': "'", '-': '>', '&': '{', '(': ':', '*': '<', '+': ',',
                   '=': '.', '`': '~', '~': '`', '√': '"'}

'''
Reverse Everything!
'''

d = []

def decryption_Level1(cipher):
    dec_cipher = cipher[::-1]
    d.append(dec_cipher)
    return dec_cipher

decryption_Level1(cipher)

'''
['ö','ü','ä','ß','Ӓ'] -> [0,1,2,5,9]
人 -> 力
'''
dec_cipher1 = d[0]
def decryption_Level2(dec_cipher1):
    dec_msg1= ''
    dec_cipher1 = str(dec_cipher1)
    for i in dec_cipher1:
        dec_msg1 += dec_dictLevel_1[i]
    d.append(dec_msg1)
    return dec_msg1

decryption_Level2(dec_cipher1)

'''
力 -> ñ
Telugu Alphabets -> Special Characters
Numbers -> Number + 2 (Not Addition)
Alphabet -> Alphabet - 3
'''
dec_cipher2 = d[1]
def decryption_Level3(dec_cipher2):
    dec_msg2 = ''
    dec_cipher2 = str(dec_cipher2)
    for i in dec_cipher2:
        dec_msg2 += dec_dictLevel_2[i]
    d.append(dec_msg2)
    return dec_msg2
decryption_Level3(dec_cipher2)

'''
Divides Alphabet into 2 sets
Replace each alphabet with corresponding alphabet in the other set 
Repeat the same with numbers and special characters
Replace 'ñ' with 'space'
'''
dec_cipher3 = d[2]
def decryption_Level4(dec_cipher3):
    dec_msg3 = ''
    dec_cipher3 = str(dec_cipher3)
    for i in dec_cipher3:
        dec_msg3 += dec_dictLevel_3[i]
    d.append(dec_msg3)
    return dec_msg3
decryption_Level4(dec_cipher3)

decrypted_message = d[3]
#print(decrypted_message)


#saves decrypted cipher into a text file
OutputFileName = input("Enter your output file name: ")
with open(OutputFileName, "w", encoding = 'utf8') as f:
    f.write(decrypted_message)
print("written")
