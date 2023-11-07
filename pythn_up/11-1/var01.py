#測試
#1.副程式內未定義變數時-->會以(外面)全域變數為主
#2.副程式內有定義變數(區域)時,依"變數的宣告方式"以及"變數改變內容值"的不同寫法
#  -->會影響變數間的內容是否會連動
#3.副程式內有定義變數(區域)時,且"有宣告內容"時
#  -->此變數視為區域變數(與(外面)全域變數不同,不連動影響)
#--------------------------------------------------------------------

#全域變數(主程式處/外面)
a = [1, 2]
b = a
c = [7, 8]
d = c

#1.副程式內未定義變數時-->會以(外面)全域變數為主
def f1():
    print("副程式處f1--: a = %10s; 位址 = %d"%(a,id(a)))
    print("副程式處f1--: b = %10s; 位址 = %d"%(b,id(b)))
    print("副程式處f1--: c = %10s; 位址 = %d"%(c,id(c)))
    print("副程式處f1--: d = %10s; 位址 = %d"%(d,id(d)))
    print("---------------------------------------------")
    
#2.副程式內有定義變數(區域)時,依"變數的宣告方式"以及"變數改變內容值"的不同寫法
#  -->會影響變數間的內容是否會連動
def f2():  
    a.append(1)  #連動影響--(全域變數)
    c = [1]      #重新指向,不連動影響--(區域變數)
    print("副程式處f2--: a = %10s; 位址 = %d"%(a,id(a))) #連動影響--(全域變數)
    print("副程式處f2--: b = %10s; 位址 = %d"%(b,id(b))) #連動影響--(全域變數)
    print("副程式處f2--: c = %10s; 位址 = %d"%(c,id(c))) #重新指向為另一位址
    print("副程式處f2--: d = %10s; 位址 = %d"%(d,id(d))) #不受影響--(全域變數)
    print("---------------------------------------------")

#3.副程式內有定義變數(區域)時,且"有宣告內容"時
#  -->此變數視為區域變數(與(外面)全域變數不同,不連動影響)
def f3():
    a = [8, 8]  #重新指向,不連動影響--(區域變數)
    c = [5, 5]  #重新指向,不連動影響--(區域變數)
    print("副程式處f3--: a = %10s; 位址 = %d"%(a,id(a))) #重新指向為另一位址--(區域變數)
    print("副程式處f3--: b = %10s; 位址 = %d"%(b,id(b))) # 不受影響--(全域變數)
    print("副程式處f3--: c = %10s; 位址 = %d"%(c,id(c))) #重新指向為另一位址--(區域變數)
    print("副程式處f3--: d = %10s; 位址 = %d"%(d,id(d))) # 不受影響--(全域變數)
    print("---------------------------------------------")

def f4():
    a[0] = 9  #重新指向,不連動影響--(區域變數)
    c[0] = [5, 5]  #重新指向,不連動影響--(區域變數)
    print("副程式處f4--: a = %10s; 位址 = %d"%(a,id(a))) #重新指向為另一位址--(區域變數)
    print("副程式處f4--: b = %10s; 位址 = %d"%(b,id(b))) # 不受影響--(全域變數)
    print("副程式處f4--: c = %10s; 位址 = %d"%(c,id(c))) #重新指向為另一位址--(區域變數)
    print("副程式處f4--: d = %10s; 位址 = %d"%(d,id(d))) # 不受影響--(全域變數)
    print("---------------------------------------------")

print("主程式處----: a = %10s; 位址 = %d"%(a,id(a)))
print("主程式處----: b = %10s; 位址 = %d"%(b,id(b)))
print("主程式處----: c = %10s; 位址 = %d"%(c,id(c)))
print("主程式處----: d = %10s; 位址 = %d"%(d,id(d)))
print("---------------------------------------------")

f1()
f2()
f3()
f4(
