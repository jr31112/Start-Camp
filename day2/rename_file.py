import os

# 1. dummy 폴더로 들어간다.
os.chdir('./dummy')
print(os.getcwd())
# 2. 파일들을 하나하나씩 파일명을 변경한다. -> 반목문 활용
files = os.listdir('.')
print(files)
# print(type(files))
for file in files:
    os.rename(file, f'SAMSUNG_{file}')
# 3. 파일명 변경(SAMSUNG -> SAFFY)
for file in files:
    os.rename(file, file.replace('SAMSUNG', 'SSAFY'))