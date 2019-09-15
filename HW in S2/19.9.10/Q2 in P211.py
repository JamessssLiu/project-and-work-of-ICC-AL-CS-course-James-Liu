UpcseLetterCount=0
DigitCount=0

userid=eval(input("Please input your userid"))
for i in range(len(id)):
    if userid[i].isalnum():
        DigitCount+=1
    elif userid[i].isupper():
        UpcseLetterCount+=1

if UpcseLetterCount>=3 and DigitCount>=4:
    print("The user ID is valid")
else:
    print("The user ID is not valid")
