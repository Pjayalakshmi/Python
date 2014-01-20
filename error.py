try
c=2/0
except(ZeroDivisionError):
 print("divided by zero")
else:
 print("no error")
finally:
 print("program executed")
