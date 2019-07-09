# number.txt를 읽어서
with open('number.txt','r') as f:
    lines = f.readlines()

# print(lines)

lines.reverse()

with open('number_reverse.txt','w') as f:
    f.writelines(lines)

# umver_reverse.txt로 저장!
#4
#3
#2
#1
#0