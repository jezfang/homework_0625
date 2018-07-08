print("------------------------------------------------")
print("四則運算")
print("計算機模式開啟")
print("輸入要計算的數值")

n1=int(input("第一個數:"))
n2=int(input("第二個數:"))
op=input("運算 :+, -, *, /")

if op=="+":
    result=n1+n2
elif op=="-":
    result=n1-n2
elif op=="*":
    result=n1*n2
elif op=="/":
    result=n1/n2
print("計算完成：",int(result))


print("------------------------------------------------")
print("開根號運算")

n=int(input("輸入一個正整數: "))
c=n**0.5
if c%1==0:
    print(n,"的平方根是",c)
else:
    print(n,"沒有整數平方根")


print("------------------------------------------------")
print("99 乘法表運算")
print("算給你看")
for i in range(1,10):
    for c in range(1,10):
        print(i,"*",c,"=",i*c)

print("算完了")