# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:49:14 2022
GROUP 5: GROUP ASSIGNMENT
CSIT303: COMPUTER SECURITY
Group Members: Gouthami Reddy, Vidya Peddinti and Vijayasree Asam

Encryption 
"""
#reading message from the file

inputfilename =input("enter the input file name: ")

with open(inputfilename) as f:
    lines = [line.rstrip() for line in f]
message = "".join(lines)
message = str(message)

#message = str(input("Enter your message: "))
#dictionaries for all levels of encryption

dictLevel_1 = {"A":"N","B":"O","C":"P","D":"Q","E":"R","F":"S","G":"T","H":"U","I":"V","J":"W","K":"X","L":"Y","M":"Z",
                "N":"A","O":"B","P":"C","Q":"D","R":"E","S":"F","T":"G","U":"H","V":"I","W":"J","X":"K","Y":"L","Z":"M",
                "a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l": "y","m":"z",
                "n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m",
               " ":"ñ","0":"5","1":"6","2":"7","3":"8","4":"9","5":"0","6":"1","7":"2","8":"3","9":"4","!":"[","@":";",
               "#":"|","$":"}","_":"?","%":"/",")":"]","^":"'","-":">","&":"{","(":":","*":"<","+":",","=":".","[":"!",
               ";":"@","|":"#","}":"$","?":"_","/":"%","]":")","'":"^",">":"-","{":"&",":":"(","<":"*",",":"+",".":"=",
               "~":"`","`":"~",'"':'√'}
dictLevel_2 = {"A":"D","B":"E","C":"F","D":"G","E":"H","F":"I","G":"J","H":"K","I":"L","J":"M","K":"N","L":"O",
               "M":"P","N":"Q","O":"R","P":"S","Q":"T","R":"U","S":"V","T":"W","U":"X","V":"Y","W":"Z","X":"A",
               "Y":"B","Z":"C","a":"d","b":"e","c":"f","d":"g","e":"h","f":"i","g":"j","h":"k","i":"l","j":"m",
               "k":"n","l":"o","m":"p","n":"q","o":"r","p":"s","q":"t","r":"u","s":"v","t":"w","u":"x","v":"y",
               "w":"z","x":"a","y":"b","z":"c","9":"7","8":"6","7":"5","6":"4","5":"3","4":"2","3":"1","2":"0",
               "1":"9","0":"8","ñ":"力","~":"అ","!":"ఆ","@":"ఇ","#":"ఈ","$":"ఉ","_":"ఊ","%":"ఋ",")":"ౠ",
               "^":"ఏ","-":"ఐ","&":"ఒ","(":"ఔ","*":"ఎ","+":"ఓ","=":"క","`":"ఖ","[":"ఘ",";":"ఙ","|":"చ",
               "}":"ఛ","?":"జ","/":"ఝ","]":"ఞ","'":"ట",">":"ఠ","{":"డ",":":"ఢ","<":"ణ",",":"త",
               ".":"థ","√":"స"}
dictLevel_3 ={"A":"A","B":"B","C":"C","D":"D","E":"E","F":"F","G":"G","H":"H","I":"I","J":"J","K":"K","L":"L",
         "M":"M","N":"N","O":"O","P":"P","Q":"Q","R":"R","S":"S","T":"T","U":"U","V":"V","W":"W","X":"X",
         "Y":"Y","Z":"Z","a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j",
         "k":"k","l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u","v":"v",
         "w":"w","x":"x","y":"y","z":"z","9":"Ӓ","8":"8","7":"7","6":"6","5":"ß","4":"4","3":"3","2":"ä",
         "1":"ü","0":"ö","力":"人","అ":"అ","ఆ":"ఆ","ఇ":"ఇ","ఈ":"ఈ","ఉ":"ఉ","ఊ":"ఊ",
        "ఋ":"ఋ","ౠ":"ౠ","ఎ":"ఎ","ఏ":"ఏ","ఐ":"ఐ","ఒ":"ఒ","ఓ":"ఓ","ఔ":"ఔ","స":"స","క":"క",
        "ఖ":"ఖ","ఘ":"ఘ","ఙ":"ఙ","చ":"చ","ఛ":"ఛ","జ":"జ","ఝ":"ఝ","ఞ":"ఞ",
        "ట":"ట","ఠ":"ఠ","డ":"డ","ఢ":"ఢ","ణ":"ణ","త":"త","థ":"థ"}  



#message = input("Enter your message: ")
'''
Divides Alphabet into 2 sets
Replace each alphabet with corresponding alphabet in the other set
Repeat the same with numbers and special characters
Replace 'spaces' with 'ñ'
'''

l = []
def EncryptionLevel_1(message):    
    cipher1 = ''
    message = str(message)
    for i in message:
        cipher1 +=dictLevel_1[i] 
    l.append(cipher1)
    return cipher1
    
EncryptionLevel_1(message)
'''
Alphabet -> Alphabet + 2
Number -> Number - 2
Special Characters -> Telugu Letters
ñ -> 力
'''
en_message1 = l[0]
def EncryptionLevel_2(en_message1):
    cipher2 = ''
    en_message1 = str(en_message1)
    for i in en_message1:
        cipher2 += dictLevel_2[i]
    l.append(cipher2)
    return cipher2

EncryptionLevel_2(en_message1)
'''
[0,1,2,5,9] -> ['ö','ü','ä','ß','Ӓ']
力 -> 人
'''
en_message2 = l[1]
def EncryptionLevel_3(en_message2):
    cipher3 = ''
    en_message2 = str(en_message2)
    for i in en_message2:
        cipher3 += dictLevel_3[i]
    l.append(cipher3)
    return cipher3

EncryptionLevel_3(en_message2)
'''
Reverse Everything!
'''
en_message3 = l[2]
def EncrypionLevel_4(en_message3):
    en_message3 = en_message3[::-1]
    l.append(en_message3)
    return en_message3
EncrypionLevel_4(en_message3)


text = l[3]
str1 = text
checkpoint = str1[0]

key = "g^2r£"
why = ''
if checkpoint.isupper():    
   why = key + text 
   l.append(why)

key1 = "A;/P₳"
who = ''
if checkpoint.islower():    
   who = key1 + text
   l.append(who)
   
key2 = "s=5%₹"
numbers = ['0','1','2','3','4','5','6','7','8','9']
what = ''
if checkpoint in numbers:    
   what = key2 + text 
   l.append(what)
   
key3 = "V@1:¥"
German_letters = ['ö','ü','ä','ß','Ӓ']
when = ''
if checkpoint in German_letters:
    when = key3 + text
    l.append(when)
 
key4 = 'P!4]€'
Telugu_Letters = ["అ","ఆ","ఇ","ఈ","ఉ","ఊ","ఋ","ౠ","ఎ","ఏ","ఐ","ఒ","ఓ","ఔ","క",
            "ఖ","ఘ","ఙ","చ","ఛ","జ","ఝ","ఞ","ట","ఠ","డ","ఢ","ణ","త","థ","స"]
where = ''
if checkpoint in Telugu_Letters:
    where = key4 + text
    l.append(where)  
encrypted_message = l[4]

hashText = 'SecurityIssue'
hashvalue = str(hash(hashText))


encrypted_message = encrypted_message[:5] + hashvalue + encrypted_message[5:]
OutputFileName = input("Enter your output file name: ")
with open(OutputFileName, "w", encoding = 'utf8') as f:
    f.write(encrypted_message)
print("written")