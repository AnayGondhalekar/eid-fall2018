# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myapp.ui'
# Owner: Anay Gondhalekar
# Created by: PyQt5 UI code generator 5.7
# Library credits and API credits: Adafruit_DHT library- https://github.com/adafruit/Adafruit_Python_DHT
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT
import sys
# Class to create the main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(376, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 81, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 50, 81, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 290, 301, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 300, 151, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 210, 301, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 10, 281, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 370, 51, 21))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 360, 301, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 90, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getTempHum) #Call the function to get temp. & hum. when button is pressed
        self.pushButton_2.clicked.connect(self.convert) #Function to convert Celcius and Fahrenheit
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#Retranslate Class to Set Labels and Window Title
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Temperature:"))
        self.label_2.setText(_translate("MainWindow", "Humidity:"))
        self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.label_4.setText(_translate("MainWindow", "Sensor Connectivity:"))
        self.label_3.setText(_translate("MainWindow", "Last Refreshed at:"))
        self.label_5.setText(_translate("MainWindow", "Anay\'s Temperature & Humidity meter"))
        self.label_6.setText(_translate("MainWindow", "Alarm:"))
        self.pushButton_2.setText(_translate("MainWindow", "Fah. / Cel. "))

    def getTempHum(self):
        _translate = QtCore.QCoreApplication.translate
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity, temperature = Adafruit_DHT.read(sensor, pin)
        if humidity is not None and temperature is not None:
            temp1 = '{0:0.1f}* C'.format(temperature) #Converting to string
            hum1 = '{0:0.1f} %'.format(humidity) #Converting to string
            self.lineEdit.setText(_translate("MainWindow", temp1))
            self.lineEdit_2.setText(_translate("MainWindow", hum1))
            self.lineEdit_3.setText(_translate("MainWindow", "Sensor Connected!"))
            self.lineEdit_4.setText(QtCore.QDateTime.currentDateTime().toString())
            #Check temperature ranges to set alarm
            if temperature > 25 and humidity > 40:    
                self.lineEdit_5.setText(_translate("MainWindow", "It's hot!"))
            elif temperature > 25 and humidity < 40:
                self.lineEdit_5.setText(_translate("MainWindow", "It's hot and dry!"))
            elif temperature < 25 and temperature > 15 and humidity < 40:
                self.lineEdit_5.setText(_translate("MainWindow", "It's dry!"))
            elif temperature < 15 and humidity > 40:
                self.lineEdit_5.setText(_translate("MainWindow", "It's cold!"))
            elif temperature < 15 and humidity < 40:
                self.lineEdit_5.setText(_translate("MainWindow", "It's cold and dry!"))
            else:
                self.lineEdit_5.setText(_translate("MainWindow", "Don't worry,it's perfect!"))
            
            
        else:
            humidity, temperature = Adafruit_DHT.read(sensor, pin)  
            #Check if the sensor is connected or not
            if humidity is None and temperature is None:
                self.lineEdit.setText(_translate("MainWindow", "-"))
                self.lineEdit_2.setText(_translate("MainWindow", "-"))
                self.lineEdit_3.setText(_translate("MainWindow", "Sensor Disconnected!"))
                self.lineEdit_4.setText(QtCore.QDateTime.currentDateTime().toString())
                self.lineEdit_5.setText(_translate("MainWindow", "-"))
            else:
                temp1 = '{0:0.1f}* C'.format(temperature)
                hum1 = '{0:0.1f} %'.format(humidity)
                self.lineEdit.setText(_translate("MainWindow", temp1))
                self.lineEdit_2.setText(_translate("MainWindow", hum1))
                self.lineEdit_3.setText(_translate("MainWindow", "Sensor Connected!"))
                self.lineEdit_4.setText(QtCore.QDateTime.currentDateTime().toString())
                if temperature > 25 and humidity > 40:
                    self.lineEdit_5.setText(_translate("MainWindow", "It's hot!"))
                elif temperature > 25 and humidity < 40:
                    self.lineEdit_5.setText(_translate("MainWindow", "It's hot and dry!"))
                elif temperature < 25 and temperature > 15 and humidity < 40:
                    self.lineEdit_5.setText(_translate("MainWindow", "It's dry!"))
                elif temperature < 15 and humidity > 40:
                    self.lineEdit_5.setText(_translate("MainWindow", "It's cold!"))
                elif temperature < 15 and humidity < 40:
                    self.lineEdit_5.setText(_translate("MainWindow", "It's cold and dry!"))
                else:
                    self.lineEdit_5.setText(_translate("MainWindow", "Don't worry,it's perfect!"))
    
    def convert(self): 
        #convert Celcius to Fahrenheit
        _translate = QtCore.QCoreApplication.translate
        sensor = Adafruit_DHT.DHT22
        pin = 4
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        temperature1 = int(temperature) * 9/5.0 + 32
        temperature1 = '{0:0.1f}* F'.format(temperature1)
        temperature2 = '{0:0.1f}* C'.format(temperature)
        value = len(self.lineEdit.text())
        value1= str(self.lineEdit.text())
        mychar = value1[value-1]
        if mychar=='F':
            self.lineEdit.setText(_translate("MainWindow", temperature2)) 
        else:
            self.lineEdit.setText(_translate("MainWindow", temperature1)) 
        
           
#Main Function Class as generated by Qt5
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

