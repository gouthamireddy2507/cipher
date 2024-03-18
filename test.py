
InputFile =input("enter the input file name: ")

with open(InputFile, 'r', encoding = 'utf8') as f:
    lines = [line.rstrip() for line in f]
message = "".join(lines)
message = str(message)

for key in message:
        if message[:4] in ['g^2r£','s=5%₹','A;/P₳','P!4]€','V@1:¥']:
            print("True!")
        else:
            print("False!")
        
