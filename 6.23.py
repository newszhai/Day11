age=int(input("请输入您的年龄"))
name=input("请输入您的姓名")

if age<18:
    print("姓名:"+name+"年龄：",age,"您是未成年人")
elif 60>age>=18:
    print("姓名:"+name+"年龄：",age,"您是成年人")
else:
    print("姓名:"+name+"年龄：",age,"您是老年人")
