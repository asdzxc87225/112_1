# 上課內容

- 子圖的設定
- latex的文字顯示


## 子圖的設定
### ex1
第一個範例可以看出最簡單的設定方式。\
但是如果子圖超過10個就不建議用此方法。

```py

    plt.figure(1) #第1個圖表
    plt.subplot(211)#將圖切成2*1的大小畫在1號位置
#===================================
def ex01():
    plt.figure(1) 
    plt.subplot(211)
    plt.plot([1,2,3],'r+-')

    plt.subplot(212)
    plt.plot([4,5,5],'g-d')

    plt.figure(2)
    plt.subplot(251)
    plt.plot([1,2,3],'k-+')

    plt.subplot(2,5,10)
    plt.plot([4,5,5],'b-s')

    plt.show()

```

### ex2 

在著個範例顯示如何設定共同的刻度這樣讓我們可以看出不同張圖之間的變化。

這裡也示範了不同的建立子圖的方法。

```py
    f,ax = plt.subplots(2,2, sharex = 'col', sharey='row') #建立一張大圖f與子圖ax
    """
    這之中的f大圖
    ax是代表子圖
    2,2 這個是建立2*2的區塊用來化子圖
    sharex是設定要共用標尺
    """

    ax[0,0].set_title('sin(x)')
    ax[0,0].set_ylabel('Y1')
    """
    在這裡可以看出ax[o, o]裡面就可以設定要修改的子圖
    一般情況下就是用 .set_要設定指令(變數)這樣就好了
    """
#================================================
def ex02():
    f,ax = plt.subplots(2,2, sharex = 'col', sharey='row')
    x = np.linspace(0, 2*np.pi,20)
    y = np.sin(x)

    ax[0,0].plot(x,y)
    ax[0,0].set_title('sin(x)')
    ax[0,0].set_ylabel('Y1')

    ax[0,1].plot(x,y*2)
    ax[0,1].set_title('2*sin(x)')

    ax[1,0].plot(x,y*0.5)
    ax[1,0].set_title('0.5*sin(x)')
    ax[1,0].set_xlabel('X3')
    ax[1,0].set_ylabel('Y3')
    ax[1,0].set_xticks((0,2,4,6))
    
    ax[1,1].plot(x,y*3)
    ax[1,1].set_title('3*sin(x)')
    ax[1,1].set_xlabel('X4')
```

## latex的文字顯示

