Number=int(input())
Ones=Number//100
Tens=(Number//10)%10
Hundreds=Number%10
Result=((Hundreds*100)+(Tens*10)+Ones)*2
print(Result)