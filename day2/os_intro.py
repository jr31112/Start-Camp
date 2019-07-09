# 운영체제 조작 시 필요한 파일 입력
import os
# listdir : ls
# 현재 디렉토리에 있는 파일 및 폴더들
ls = os.listdir('.')
print(ls)

# getcwd(get current working directory) : pwd
# 현재 파일이 실행된 디렉토리(작업하고 있는 디렉토리)
pwd = os.getcwd()
print(pwd)

# os.chdir(r'C:\Users\student\Desktop\start camp\day2\dummy')
# chdir(change directory) : cd
# 해당 디렉토리 위치로 이동한다.
os.chdir('./dummy')
pwd = os.getcwd()    
print(pwd)