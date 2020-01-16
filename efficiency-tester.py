import subprocess
import time
import os
import sys
argvs = sys.argv
# print(argvs)
path = ""   # 记录文件夹名称
if len(argvs) == 1:
    path = "./testinput" # 如果给的参数只是一个则path为默认值 testinput
else:
    path = str(argvs[1])

files = os.listdir(path)  # 得到文件夹下的所有文件名称,为最后输出的第一列
files_full_name = []
print("Testcase", "\t", "RealTime", "\t", "CPUTime")
for i in range(len(files)):
    files_full_name.append(str(path + '/' + files[i]))

for i in range(len(files)):
    print(files[i])
    start_real = time.time()
    start_CPU = time.process_time()
    args = ["python3", "wc.py", "./testinput/fizzbuzz.py"]
    p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutput, erroutput) = p.communicate()
    end_CPU = time.process_time()
    end_real = time.time()
    print(end_real - start_real)
    print(end_CPU - start_CPU)
    # print(stdoutput, erroutput)

