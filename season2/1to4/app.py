with open('pattern.txt' , encoding="utf-8") as f:
    pattern = f.read()
data = []
with open('data.txt' , encoding="utf-8") as f:
    for line in f.readlines():
       data.append(line.strip().split(' ,'))
for i in data:
    with open(f'messages/{i[0]}.txt' , 'w', encoding="utf-8" ) as f:
        f.write(pattern.format(*i))
