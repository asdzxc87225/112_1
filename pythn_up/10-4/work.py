import cv2
import os 
import numpy

class img_set():
    def __init__(self):
        self.ImgPath = r'../img/'
        self.ImgName = ''
        self.TotalImgPath = ''
        self.ImgCenter_x = 0
        self.ImgCenter_y = 0
        self.ImgW = 0
        self.ImgH = 0

        self.Mode = ['r', 'f', 'a', 't']
        self.OutFileType = ['bmp', 'tiff', 'png', 'jpg']
        self.ImgSrc = None
        self.RunMode = ''


        self.Rotation_ang = 90
        self.Rotation_scale = 1

        self.Resize_dsize_scale = 1.5
        self.Resize_dsize_W = 0
        self.Resize_dsize_H = 0

        self.Flip_para = 0

        self.flage = 0
        self.flage_mode = ''
        self.Run()


    def Run(self):
        while True:
            if self.flage == 0:#得到圖片
                print('============================')
                self.Get_Img()
                self.flage = 1
            elif self.flage == 1:#引導選折功能
                print('============================')
                self.Guide_to_use()
                self.flage = 2
            elif self.flage == 2:#加工圖片與確定參數
                print('============================')
                self.Run_Mode()
                self.flage = 3
            elif self.flage == 3:#引導後許動作
                print('============================')
                print(r'0.切換功能')
                print(r'1.修改參數')
                print(r'2.換圖片')
                print(r'3.存檔')
                print(r'4.結束')
                self.flage_mode = input('請選擇:')
                if self.flage_mode == '1':
                    print('============================')
                    self.flage = 2
                elif self.flage_mode == '0':
                    print('============================')
                    self.flage = 1
                elif self.flage_mode == '2':
                    print('============================')
                    self.flage = 0
                elif self.flage_mode == '3':
                    print('============================')
                    self.Out_Img()
                    self.flage = 3
                elif self.flage_mode == '4':
                    self.flage = 4
                    break
                else:
                    self.flage = 2
            elif self.flage == 4:
                pass



    def Get_Img(self):
        while True:
            a = (os.listdir(self.ImgPath))
            index = 0
            for x in a :
                print(f'[{index}]:{x}')
                index+=1
            self.ImgName = a[int(input('請輸入你要的圖片編號'))]
            self.TotalImgPath = self.ImgPath + self.ImgName 
            self.ImgSrc = cv2.imread(self.TotalImgPath,-1)
            print('img source path:',self.TotalImgPath)
            print('img source shape:', self.ImgSrc.shape)
            print('img source ndim:', self.ImgSrc.ndim)
            print('等等會輸出一張圖,請自行關閉圖片視窗')
            input('請按enter後繼續')
        
            self.ImgW = int(self.ImgSrc.shape[1])
            self.ImgH = int(self.ImgSrc.shape[0])
            self.ImgCenter_x = self.ImgW//2
            self.ImgCenter_y = self.ImgH//2
            
            cv2.imshow(self.ImgName,self.ImgSrc)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            if input('這是你要的圖片(y/n):') == 'y':
                print('圖片確定')
                break
    def Out_Img(self):
        while True:
            print('-------------------------------------------------------')
            for x in range(len(self.OutFileType)):
                print(f'{x}:{self.OutFileType[x]}')
            x = int(input('你要的檔案格式是:'))
            y = input('檔案的名稱:')
            cv2.imwrite(y+'.'+self.OutFileType[x],self.DoImg)
            break


    def Guide_to_use(self):
        showStr = ''
        showStr += '請根據以下的提示進行抄做\n'
        showStr += 'r 縮放\n'
        showStr += 'f 翻轉\n'
        showStr += 'a 選轉Rotation\n'
        showStr += 't 選轉Transpose\n'
        print(showStr)
        while True:
            self.RunMode = input('請輸入你要的功能')
            if self.RunMode in self.Mode:
                print('你的選擇是',self.RunMode)
                break
            else:
                print('請輸入有定義的功能')

    def Run_Mode(self):
        self.flage_mode = ''
        if self.RunMode == 'a':
            while True:
                print(f'旋轉角度:{self.Rotation_ang}')
                print(f'旋轉中心:({self.ImgCenter_x},{self.ImgCenter_y})')
                print(f'放大倍率:{self.Rotation_scale}')
                if input('你確定參數正確嗎(y/n):') == 'y' :
                    print('運行')
                    break
                else :
                    while True:
                        print('--------------------------------------------------')
                        print('你要修改的是什麼？')
                        print(f'1.旋轉角度:{self.Rotation_ang}')
                        print(f'2.旋轉中心:({self.ImgCenter_x},{self.ImgCenter_y})')
                        print(f'3.放大倍率:{self.Rotation_scale}')
                        print(f'4.修改結束')
                        self.flage_mode = input('請輸入上面的編號來修改')
                        if self.flage_mode == '1':
                            self.Rotation_ang = float(input('旋轉角度：'))
                        elif self.flage_mode == '2':
                            self.ImgCenter_x = int(input('旋轉中心W：'))
                            self.ImgCenter_y = int(input('旋轉中心H：'))
                        elif self.flage_mode == '3':
                            self.Rotation_scale = float(input('放大倍率:'))
                        else:
                            print('--------------------------------------------------')
                            break
            self.Rotation()

        elif self.RunMode == 'f':
            while True:
                print('1.水平')
                print('0.垂直')
                print('-1.水平與垂直')
                print(f'你選折的翻轉方式:{self.Flip_para}')
                if input('你確定參數正確嗎(y/n):') == 'y' :
                    print('運行')
                    break
                else :
                    self.Flip_para = int(input('你要選折的模式'))

                print('--------------------------------------------------')
            self.Flip()

        elif self.RunMode == 'r':
            while True:
                print(f'放大率{self.Resize_dsize_scale}')
                if input('你確定參數正確嗎(y/n):') == 'y' :
                    print('運行')
                    break
                else :
                    print('--------------------------------------------------')
                    self.Resize_dsize_scale = float(input('放大倍率'))

            self.Resize_dsize_W = int(self.ImgW * self.Resize_dsize_scale)
            self.Resize_dsize_H = int(self.ImgH * self.Resize_dsize_scale)
            self.Resize_dize = (self.Resize_dsize_W,self.Resize_dsize_H)
            self.Resize()

        elif self.RunMode == 't':
            self.Transpose()

    def Rotation(self):
        self.mat = cv2.getRotationMatrix2D((self.ImgCenter_x, self.ImgCenter_y),self.Rotation_ang,self.Rotation_scale)
        self.DoImg = cv2.warpAffine(self.ImgSrc,self.mat,(self.ImgW,self.ImgH))
        
        cv2.imshow("Rotation",self.DoImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Transpose(self):
        self.DoImg = cv2.transpose(self.ImgSrc)
        cv2.imshow("Transpose",self.DoImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Flip(self):
        self.DoImg = cv2.flip(self.ImgSrc,self.Flip_para)
        cv2.imshow("Flip",self.DoImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Resize(self):
        self.DoImg = cv2.resize(self.ImgSrc,self.Resize_dize) 
        cv2.imshow("Resize",self.DoImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    img = img_set()
