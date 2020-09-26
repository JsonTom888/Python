import subprocess
import time, os

def createFile(filename, content):
    if os.path.exists(filename) == False: # 文件不存在则创建
        open(filename, "a").close()
    if os.path.getsize(filename): # 判断文件是否有内容
        pass
    else: # 没有内容则写入内容
        f = open(filename, "a")
        f.write('\n')
        f.write('\n')
        f.write(content)
        f.close()

def printTips(filename, content):
    createFile(filename, content); # 创建提示文件
    sub2 = subprocess.Popen(['notepad', filename]); # 打开提示文件

try:
    timefile = 'mytime.ini' # 配置提示的间隔时间
    fileName = "温馨提示"
    success = 'success'
    if (os.path.exists(fileName)):
        os.remove(fileName)
    if (os.path.exists(success)):
        os.remove(success)
    if (os.path.exists(timefile)):
        with open(timefile, 'r', encoding='utf-8') as f:  # 打开文件
            lines = f.readlines()  # 读取所有行
            first_line = lines[0].strip()  # 取第一行

        t = int(first_line)
        if t < 60:
            content = '恭喜你已经成功开启定时提醒喝水功能了！您设置了' + str(t) + '秒钟提醒一次！'
        else:
            content = '恭喜你已经成功开启定时提醒喝水功能了！您设置了' + str(round(t / 60, 2)) + '分钟提醒一次！'
    else:
        t = 30*60
        content = '恭喜你已经成功开启定时提醒喝水功能了！默认半个小时提醒一次！'

    printTips(success, content)
    content = "    您已经持续工作" + str(round(t / 60, 2)) + "分钟了，该喝水啦!!"
    if (t < 60):
        content = "    您已经持续工作" + str(t) + "秒钟了，该喝水啦!!"
    while True:
        time.sleep(t)  # t秒钟循环一次
        printTips(fileName, content)

except Exception as e:
    f = open("error.log", "a")
    f.write(str(e) + "\n")
    f.close()


# 转换成exe只需运行以下命令
# pyinstaller -w your_file_name.pyw
# 注意：运行上面的命令之前需要先安装pyinstaller。要安装，请运行以下命令
# pip install pyinstaller
# exe文件就存在于该文件夹的XXXXX\dist  文件夹中，
# 此处的.exe文件单独移动到任何地方都可以执行不依赖于任何其他额外文件（ico等资源文件除外）