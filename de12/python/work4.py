for i in range(1,3):
    print(i,"人目")
    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))

    print(name, "は腹囲",waist, "年齢",age, "度ですね。")

    if waist<=20 or age<=10:
        print(name,"危険")
    else:
        print(name,"not危険")
#　出力結果
# 1 人目
# 2 人目
