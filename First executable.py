import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(200, 100, 1000, 700)
        
        self.welcomeLabel = QLabel("Welcome to 'GUI Name'! Select any Tab to begin!", self)
        self.disclaimerLabel = QLabel("This is a first executable file. The real product will look nicer and do much more than this :)", self)
        self.measureButton = QPushButton("Measurements Schedule", self)
        self.dataButton = QPushButton("Data", self)
        self.deviceButton = QPushButton("Device", self)
        self.settingsButton = QPushButton("Settings", self)

        self.initUI()


    def initUI(self):
        #Labels
        self.welcomeLabel.setFont(QFont("Helvetica", 20))
        self.welcomeLabel.setGeometry(200, 100, 800, 200)
        self.disclaimerLabel.setFont(QFont("Helvetica", 10))
        self.disclaimerLabel.setGeometry(100, 500, 800, 100)        

        #Buttons
        self.measureButton.clicked.connect(self.measureSelected)
        self.measureButton.setGeometry(10, 10, 150, 40)
        self.dataButton.clicked.connect(self.dataSelected)
        self.dataButton.setGeometry(170, 10, 150, 40)
        self.deviceButton.clicked.connect(self.deviceSelected)
        self.deviceButton.setGeometry(330, 10, 150, 40)
        self.settingsButton.clicked.connect(self.settingsSelected)
        self.settingsButton.setGeometry(490, 10, 150, 40)

        
    def measureSelected(self):
        self.welcomeLabel.setText("You've selected the Measurement Schedule Tab.")

    def dataSelected(self):
        self.welcomeLabel.setText("You've selected the Data Tab.")

    def deviceSelected(self):
        self.welcomeLabel.setText("You've selected the Device Tab.")

    def settingsSelected(self):
        self.welcomeLabel.setText("You've selected the Settings Tab.")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
