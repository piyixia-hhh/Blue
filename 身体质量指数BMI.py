
height,weight = eval(input("请输入身高（米）和体重（公斤）【逗号隔开】："))
bmi = weight / pow(height,2)
print("BMI指数为：{:.2f}".format(bmi))
who,dom =  "",""
#国际标准
if bmi < 18.5:
    who = "偏瘦"
elif bmi < 25:              #执行该语句的条件是bmi<18.5，故此处条件为18.5 <= bmi < 25
    who = "正常"
elif bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"
#国内标准
if bmi < 18.5:
    dom = "偏瘦"
elif bmi < 24:
    dom = "正常"
elif bmi < 28:
    dom = "偏胖"
else:
    dom = "肥胖"

print("BMI指标为：国际'{0}',国内'{1}'".format(who,dom))
