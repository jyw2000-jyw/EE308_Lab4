# EE308_Lab4 YUWEI,JIANG & JIYUAN,XU
MIEC Software Engineering：Design a small game

import sys # 导入sys模块
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication # 导入Qt模块
from Game import Ui_Form # 导入ui设计模块
import picture # 导入背景图模块
from random import randint # 导入随机数函数

class Game(QWidget, Ui_Form):
    # 初始化
    def __init__(self):
        super(Game, self).__init__()
        self.setupUi(self)
    
    # 结果展示函数
    def show_message(self):
        results = []
        for roll_num in range(6):
            result = randint(1,6)
            results.append(result) # 将随机数存于列表
        
        sides = [1,2,3,4,5,6]
        countDict = {} # 该字典用于统计和存储每个点数出现次数
        for i in results:
            if i in countDict:
                countDict[i] += 1 # 对于重复出现的，每出现一次，次数增加1
            else:
                countDict[i] = 1
        for j in sides: # 对于未出现的点数，记为0次
            if j not in results:
                countDict[j] = 0
        
        # 函数判断结果
        def sixred_or_black():
            for i in range(1,7):
                if countDict[i] == 6:
                    if i == 4:
                        return '六博红'
                    else:
                        return '六博黑'
        
        def chajinhua():
            if countDict[4] == 4 and countDict[1] == 2:
                return '状元插金花'

        def duitang():
            if len(set(list(countDict.values()))) == 1:
                return '对堂'

        def wuzidengke():
            if 5 in list(countDict.values()):
                return '五子登科'

        def zhuangyuan():
            if countDict[4] == 4:
                return '状元'

        def sijin():
            for i in range(1,7):
                if countDict[i] == 4:
                    return '四进'

        def sanhong_erju_yixiu():
            if countDict[4] == 3:
                return '三红'
            elif countDict[4] == 2:
                return '二举'
            elif countDict[4] == 1:
                return '一秀'
            else:
                return '抱歉无奖励'

        count = 7
        while count:
            if sixred_or_black() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{sixred_or_black()}')
                break
            
            if chajinhua() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{chajinhua()}')
                break
            
            if duitang() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{duitang()}')
                break
            
            if wuzidengke() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{wuzidengke()}')
                break
            
            if zhuangyuan() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{zhuangyuan()}')
                break 
            
            if sijin() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{sijin()}')
                break
            
            if sanhong_erju_yixiu() == None:
                count -= 1
            else:
                QMessageBox.about(self, '结果',f'点数分别为：{results[0]} '
                                                           f'{results[1]} '
                                                           f'{results[2]} '
                                                           f'{results[3]} '
                                                           f'{results[4]} '
                                                           f'{results[5]}\n'
                                                           f'你获得了：{sanhong_erju_yixiu()}')
                break

        
     
    # 退出函数
    def closeEvent(self, QCloseEvent):
        # 弹窗询问是否需要退出
        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QCloseEvent.accpet()
        else:
            QCloseEvent.ignore()

            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Game()
    ui.show()
    sys.exit(app.exec_())
