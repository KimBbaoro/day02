small =input("작나요 : ")
green =input("녹색인가요 : ")

if small: #작으면
    if green: #녹색이면
        print('pea')
    else: #녹색이 아니면
        print("cherry")
else:
    if green: #녹색이면
        print('watermelon')
    else: #녹색이 아니면
        print("pumpkin")