import random
import sys
import pandas
import string
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

class StartWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.generate.clicked.connect(self.genpass)
        self.copy.clicked.connect(self.copass)

    def genpass(self):  
        length = self.spinBox.value()
        combo = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.sample(combo, length))
        
        self.lineEdit.setText(password)
        self.msg.setText('')
        
    def copass(self):
        if self.lineEdit.text() == '':
            self.msg.setStyleSheet('color: red;')
            self.msg.setText('Line is empty.\nPlease generate a password first!')
        else:
            pandas.DataFrame([self.lineEdit.text()]).to_clipboard(index=False,header=False)  
            self.msg.setStyleSheet('color: green;')
            self.msg.setText('Password copied to clipboard!')
            self.lineEdit.setText('')
def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = StartWindow()
    window.show()
    app.exec_()
        
if __name__ == '__main__':
    main()