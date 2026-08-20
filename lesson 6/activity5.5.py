temp = int(input("please enter the tempreture in celcius"))

if temp<20:
    print("its cold outside so you should probably wear something warm.")
else:
    print("the weather is preety warm so it's preferd to wear somthing not to hot")

is_raning=str(input("is it raning? (yes/no)"))
if is_raning == "yes" :
    print("get something that can shelter you")
else:
    print("the weathers great you should go for a walk")


wind_speed=int(input("enter the wind speed in kp/h"))
if wind_speed>30:
    print("it's windy today so be careful and wear a wind breaker if you can")
else:
    print("the winds calm today")