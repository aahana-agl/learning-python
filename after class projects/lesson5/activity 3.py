height=float(input('enter your height in cm:'))
weight=float(input('enter your weight in kg:'))


BMI= weight/(height/100)**2
if BMI <=18:
    print('you are under weight')
elif BMI<=25:
    print('you are healthy')
else:
    print('you are overweight')
