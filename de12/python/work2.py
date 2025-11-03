a=1
if a > 10:
    print("10より大きい")
    
else:
    print("10より小さい")

#ifの時は：を忘れずに

name=input("名前を教えて下さい")
waist=float(input("腹囲は？"))
age=int(input("年齢は？"))

print(name, "は腹囲",waist, "年齢",age, "度ですね。")

if waist<=20 or age<=10:
    print(name,"危険")
else:
    print(name,"not危険")

#if A and Bで、AかつBのとき　という意味になる
#int・・・整数
#str・・・文字