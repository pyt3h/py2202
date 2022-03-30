import traceback
try:
    x = float(input('x: '))
    y = float(input('y: '))
    z = x/y

#except ValueError:
#    print("Invalid input number")

#except ZeroDivisionError:
#    print("Cannot divide by 0")

except Exception as e:
    traceback.print_exc()
    print('error', e)