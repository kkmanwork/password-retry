password = "a123456"
i = 2

while i >= 0:
    test = input("請輸入密碼:")
    if password == test:
        print("登入成功")
        break
    if i == 0:
        print("你沒機會了")
        break
    else:
        print("密碼錯誤! 還有", i, "次機會")
    i = i-1