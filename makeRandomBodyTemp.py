import random

print("ランダムな体温のデータを作成しましょう")
print("最低体温を入力してください")

minBodyTemp = input()

print("最高体温を入力してください")

maxBodyTemp = input()

print("作成するデータの個数を入力してください")

numberOfData = input()

try:
    for i in range(int(numberOfData)):
        print(random.uniform(float(minBodyTemp), float(maxBodyTemp)))

except:
    print("型が違います")