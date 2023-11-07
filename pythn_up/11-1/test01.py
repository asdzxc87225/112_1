a=15
b=20
sum=a+b
def add_gol():
  global a,b,sum
  a=50
  b=40
  sum=a+b
  print("add_gol處:%3d=%3d+%3d"%(sum,a,b))
def add_re():
  a=55
  b=30
  sum=a+b
  print("add_re處:%3d=%3d+%3d"%(sum,a,b))
  return sum,a,b
def add_out():
  a = 30
  sum = a+b
  print("add_out處:%3d=%3d+%3d"%(sum,a,b))
  def add_in():
    nonlocal a 
    a=10
    b=25
    sum=a+b
    print("add_in處:%3d=%3d+%3d"%(sum,a,b))
  add_in()
  sum = a+b
  print("add_in後:%3d=%3d+%3d"%(sum,a,b))
print("主程式處:%3d=%3d+%3d"%(sum,a,b))
add_gol()
print("主試處(呼叫add_gol):%3d=%3d+%3d"%(sum,a,b))
sum,a,b =add_re()
print("主程式(add_re後):%3d=%3d+%3d"%(sum,a,b))
add_out()
sum=a+b
print("主程式(add_out()):%3d=%3d+%3d"%(sum,a,b))

