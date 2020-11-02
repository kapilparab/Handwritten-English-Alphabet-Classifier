import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

from prediction import predictAlphabet

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        # Loading UI
        uic.loadUi('./ui/main.ui', self)

        # Alert Box
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setWindowTitle("Error")

        # Instance Variables
        self.imagePath = None

        # Image Window Reference
        self.imageWindow = self.findChild(QtWidgets.QLabel, 'imageWindow')
        self.imageWindow.setScaledContents(True)
        
        # Output Label Reference
        self.outputLabel = self.findChild(QtWidgets.QLabel, 'outputLabel')

        # Button References
        clearBtn = self.findChild(QtWidgets.QPushButton, 'clearBtn')
        clearBtn.clicked.connect(self.clearImage)

        predictBtn = self.findChild(QtWidgets.QPushButton, 'predictBtn')
        predictBtn.clicked.connect(self.predict)

        openImageBtn = self.findChild(QtWidgets.QPushButton, 'openImageBtn')
        openImageBtn.clicked.connect(self.openImage)

    def openImage(self):
        """
        Open Image
        Input: None
        Returns: None
        """

        # Resize window to fit image
        self.imageWindow.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        # Open dialog box
        self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        pixmap = QtGui.QPixmap(self.imagePath) # Loading image
        self.imageWindow.setPixmap(pixmap) # Setting image on label

    def clearImage(self):
        """
        Clear Image Window
        Input: None
        Returns: None
        """
        self.imageWindow.clear()

    def predict(self):
        """
        Predict Alphabet
        Input: None
        Returns: None
        """

        # If image not opened
        if not self.imagePath:
            # Alert 
            self.msg.setText("Please open image first")
            self.msg.exec()

        else:
            # Get result from model
            result = predictAlphabet(self.imagePath)

            # Set result on output label
            self.outputLabel.setText(result)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
