import sys
import os
from os import system
from xmlrpc.client import boolean
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import * #QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget
#clear if exists
import requests
from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from time import sleep
import keyboard as kb
import json
import undetected_chromedriver as uc

options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

## driver.maximize_window()
with open("text_output_pyside6.py","w") as f:
    f.write("#>>>> HERE is the text you Input"+ "\n")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupwidget()
        self.Click = []
        self.Write = []
        self.button_click = False
        self.button_write = False

        self.welcome1 = QLabel("Welcome to my app",self.centralWidget())
        self.welcome2 = QLabel("<----------HI ! I'm RITH---------->",self.centralWidget())
        self.welcome3 = QLabel("<----------TEMPLET Auto bot chrome---------->",self.centralWidget())

        self.buttonApp = QPushButton("Set",self.centralWidget())
        self.buttonLink = QPushButton("Set",self.centralWidget())
        self.buttonOpenlink = QPushButton("Open",self.centralWidget())
        self.buttonReady = QPushButton("Ready",self.centralWidget())
        self.buttonQuit = QPushButton("Quit",self.centralWidget())
        self.buttonInput = QPushButton("Add",self.centralWidget())
        self.buttonClick = QPushButton("Click",self.centralWidget())
        self.buttonWrite = QPushButton("Write",self.centralWidget())
        
        self.lineeditApp = QLineEdit(self.centralWidget())
        self.lineeditLink = QLineEdit(self.centralWidget())
        self.lineeditInput = QLineEdit(self.centralWidget())
        self.lineeditApp.setPlaceholderText("Name")
        self.lineeditLink.setPlaceholderText("Broswer")
        self.lineeditInput.setPlaceholderText("Add")
        #return by pressed or clicked

        self.buttonApp.clicked.connect(self.return_pressed_without_deleted_App)
        self.buttonLink.clicked.connect(self.return_pressed_without_deleted_Link)
        self.buttonOpenlink.clicked.connect(self.OpenLink_new)
        self.buttonQuit.clicked.connect(QApplication.quit)
        self.buttonReady.clicked.connect(self.Ready)
        self.buttonClick.clicked.connect(self.Ative_Click)
        self.buttonWrite.clicked.connect(self.Ative_Write)
        self.buttonInput.clicked.connect(self.AddXpath)
        self.lineeditApp.textChanged.connect(self.lineChangeApp)
        self.lineeditLink.textChanged.connect(self.lineChangeLink)
        
        self.lineeditApp.setFixedWidth(480)
        self.lineeditApp.setMinimumHeight(15)
        self.lineeditLink.setFixedWidth(480)
        self.lineeditLink.setMinimumHeight(15)
        self.lineeditInput.setFixedWidth(480)
        self.lineeditInput.setMinimumHeight(15)
        self.buttonOpenlink.setFixedWidth(194)
        self.buttonOpenlink.setMinimumHeight(15)
        
        self.welcome1.move(450,50)
        self.welcome2.move(400,80)
        self.welcome3.move(350,110)
        
        self.buttonApp.move(700,200)
        self.buttonLink.move(700,240)
        self.buttonInput.move(700,280)
        self.buttonOpenlink.move(800,240)
        self.buttonClick.move(800,280)
        self.buttonWrite.move(900,280)
        self.buttonQuit.move(800,320)
        self.buttonReady.move(700,320)
        self.lineeditApp.move(200,200)
        self.lineeditLink.move(200,240)
        self.lineeditInput.move(200,280)
        
    def setupwidget(self):
        
        script_path = os.path.abspath(__file__)
        script_dir = (os.path.dirname(script_path)  + "/Screenshot_2025-03-19_125716.ico")
        
        #setup the widget
        self.setWindowTitle("Automatic bot*")
        self.resize(1000, 900)
        self.setMinimumSize(1000, 400)
        
        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: rgb(59, 58, 61);")
        # path = os.path.join(os.getcwd(), "Screenshot_2025-03-19_125716.ico")
        self.setWindowIcon(QIcon(script_dir))
        self.setLayout(None)
    
    def return_pressed_without_deleted_App(self):
        #clisk eas set
        textApp = self.lineeditApp.text()
        if textApp.strip() :
            self.buttonApp.setText("✅")
            
    def return_pressed_without_deleted_Link(self):
        #click was det
        textLink = self.lineeditLink.text()
        if textLink.strip() :
            self.buttonLink.setText("✅") 
            
    def Ready(self) :
        
        #save all the output to a file
        if self.lineeditApp.text().strip() and self.lineeditLink.text().strip():
            system('cls')
            setup = str(self.setup())
            with open("text_output_pyside6.py","a") as f:
                f.write( setup + "\n" )
            
            print(setup)
            self.Attempt_Run()
        self.message_box()
        
    def message_box(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Output")
        msg_box.setText(f"The output has been saved want to open?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setIcon(QMessageBox.Question)
        response = msg_box.exec()
        path = os.path.join(os.getcwd(), "text_output_pyside6.py")
        print(os.getcwd())
        url = QUrl.fromLocalFile(path)
        if response == QMessageBox.Yes:
            QDesktopServices.openUrl(url)

            
                   
    def AddXpath(self):
        #This function is to chooses between click or write
        
        self.AddXpath_Write_or_Click()
        
    def AddXpath_Write_or_Click(self):
        
        if self.lineeditInput.text().strip() :
            if self.button_click == True :
                self.Click.append(self.lineeditInput.text())
                self.Write.append("")
                print(">>" + self.lineeditInput.text()+ " click["+ str(self.button_click) + "] Write : [" + str(self.button_write)+"]")
                print("--------------------------------------------------------------------------------------")
                self.lineeditInput.clear()
            if self.button_write == True :
                self.Write.append(self.lineeditInput.text())
                self.Click.append("")
                print(">>" + self.lineeditInput.text()+ " click["+ str(self.button_click) + "] Write : [" + str(self.button_write)+"]")
                print("--------------------------------------------------------------------------------------")
                self.lineeditInput.clear()
                  
    def lineChangeApp(self):
        #check when user try to change the text
        self.buttonApp.setText("Set")
        
    def lineChangeLink(self):
        #check when user try to change the text
        self.buttonLink.setText("Set")
        
    def Ative_Write(self):
        #when user click it try to change the mode 
        self.button_click = False
        self.button_write = True   
        self.buttonWrite.setStyleSheet("background-color: red")
        self.buttonClick.setStyleSheet("background-color: none")
        
    def Ative_Click(self):
        #when user click it try to change the mode
        self.buttonClick.setStyleSheet("background-color: red")
        self.buttonWrite.setStyleSheet("background-color: none")
        self.button_click = True
        self.button_write = False
        

    #   Nothing use remind ?? if not QDesktopServices.openUrl(url):

    def OpenLink_new(self):
        driver = webdriver.Chrome(options=options)
        driver.get(self.LinkChecker())

        
    def LinkChecker(self):
        url = self.lineeditLink.text()
        if not url.startswith("https://"):
            url = f"https://{url}"
        return url
                
    def setup(self):
        url = self.LinkChecker()
        out = str(f'''import os
import requests
from pystyle import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from time import sleep
import keyboard as kb
import json
import undetected_chromedriver as uc
os.system(f'cls & title {self.lineeditApp.text() } ~ unofficialdxnny')
options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--log-level=OFF")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
print('{self.lineeditApp.text()}')
driver = webdriver.Chrome(options=options) 
driver.get("{url}")
wait = WebDriverWait(driver, 100)
## driver.maximize_window()''') 
        return out 
        
    def Attempt_Run(self):
        #Try to create the write and click function
            for i in range(len(self.Write)):
                if self.Write[i] :
                    printout = f'''click.clear()\nclick.send_keys('{self.Write[i]}')'''
                    print(printout)
                    with open("text_output_pyside6.py","a") as f:

                        f.write(  printout+ "\n")
                    
                if self.Click[i] : 
                    
                    printout = f'''click = wait.until(EC.presence_of_element_located((By.XPATH, "{self.Click[i]}")))\nclick.click()'''
                    print(printout)
                    with open("text_output_pyside6.py","a") as f:

                        f.write(  printout+ "\n")
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
system('cls')
print("Automatic bot* loading...")
print(">>>> HERE is the text you Input")

app.exec()
