# 信號處理方式

## 訊號 v.s 能量

### 頻率(Freguency)
每秒可以產生得週期

### 頻譜(Spectrum)
訊號在不同頻率下的能量

## 分析方式

時域

頻域

系統-具備 in/out 的處理單元

#### 一街線方式
開路Open Loop
閉路Close Loop

#### 一特性

線性/非線性-in/out 成線性關係



#### 重疊定理
1. 輸入
1. 
1. 輸入線性組合

$x = 2x_1+3x_2$

$y = 2y_1+3y_2$

得到Y為$y_1$合$y_2$的線性組合則此係懂據重疊性

線性主和後送入系統X = 送入系統後在性信主和Y


#### 非時變/時變訊號

時域中輸入信號延遲則輸出也跟著延遲,但in/out的關西不便

#### 因果/非因果系統(Causal)
統一的輸出關只與現在及過去有關與未來無關

#### 靜態系統
系統的輸出只與現在有關

#### 動態系統
系統的輸出與現在過去合未來有關<非因果


## 六.信號

### 測試訊號
1. 步階波
1. 脈衝波

### 類比訊號

$x(t)=f(t)$
$=A \cos (\omega t + \phi)$

1. A:政幅
1. t:時間
1. $\omega$:(弳度/sec);=$2\pi f$
1. $\phi$:像位移;$\phi , \pi / 4 ; \pi / 2 (rad)$
1. f:
1. T:

## ex 2-5

```py
t = np.linspace(0,1,1000,endpcint=False)
x = np.cos(2 * np.pi * 5 * t)
```