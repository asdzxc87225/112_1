#物件向量
print("物件向量")
print("1,x2")
x = 1:5
x1 = 1:16
print(x)
print(x2)

print("==========================")
print("連些函數C()")
x2 = c(1,2,4,5)
x3 = 2:8
x4 = c(x2,x3)
print(x2)
print(x3)
print(x4)
print("==========================")
print("重複向量物件")
a = rep(5,5)
a1 = rep(1:5,3)
a2 = rep(1:3,times = 3,each =2)
a3 = rep(1:3, each =2, length.out =8)
print(a)
print(a1)
print(a2)
print(a3)
print("---修改內容")
print(a[1])
a[1] = 9
print(a[1])
print(a)
print("==========================")
#向量（Vector）、矩陣（Matrix）、陣列組（Array）"
print("向量（Vector）、矩陣（Matrix）、陣列組（Array）")

