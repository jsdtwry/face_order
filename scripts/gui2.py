import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
        
        lb = QLabel('zetcode', self)
        lb.move(20,20)

        pixmap = QPixmap('tmp/t2.jpeg')

        lbimg = QLabel(self)
        lbimg.setPixmap(pixmap)
        lbimg.move(50,20)

        self.resize(550, 550)
        self.center()
         
        self.setWindowTitle('Center')   
        self.show()
    '''
    def closeEvent(self, event):
         
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    '''
    def center(self):     
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


