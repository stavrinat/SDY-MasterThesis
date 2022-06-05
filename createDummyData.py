import json
f = open("dummyData.txt","a+")

s = ""
i = 1
data = {}
while s!="stop":
    s = input('enter your answer:')
    data[i] = s
    print(data[i])
    i = i + 1
print(data)
f.write(json.dumps(data, ensure_ascii = False))
f.close()
