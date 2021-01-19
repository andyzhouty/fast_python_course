# BMI指数计算程序
height = float(input("Your Height(meter): "))
weight = float(input("Your Weight(kilogram): "))
bmi = weight / (height * height) # BMI指数为体重（千克）除以身高（米）的平方
print(f"Your BMI: {bmi}.", end='') # 不换行输出
if bmi <= 0:
    print(f"Invalid input.")
elif bmi <= 18.5:
    print("Too thin.")
elif 18.5 < bmi <= 23.9:
    print("You are fit!")
elif 23.9 < bmi <= 27.9:
    print("A little bit overweight...")
else:
    print("Fat...")
