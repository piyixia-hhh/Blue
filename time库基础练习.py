import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("\r{:>3.0f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(1.5)
print("\n" + "------执行结束------")


#单行动态刷新
import time
for i in range(101):
    print("\r{:3}%".format(i),end=" ")
    time.sleep(0.1)

#由于IDLE为开发环境，故屏蔽了单行刷新功能，无法显示单行刷新效果，可在cmd中运行

#带刷新的文本进度条
import time
scale = 50
print("执行开始".center(scale//2,'-'))
start = time.perf_counter()
for i in range (scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:>3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end=' ')
    time.sleep(0.25)
print("\n"+"执行结束".center(scale//2,'-'))
