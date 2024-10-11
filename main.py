from PyQt5 import QtGui, QtWidgets
import sys
from PyQt5.uic import loadUi
import json
from save_config import save_config
from live_advance import LiveAdvance
import threading

"""
enter your client secret and ID obtained from emotiv cortex account   
"""
your_app_client_id = 'dqjqk4evWb44WruQv8YV2wl0rPEtucMm4vdsKzfL'
your_app_client_secret = 'GAMtxFPmlDt8InsYkYM5vHqnbzyh6YzKDcRP7xxZM2j9sbY3G2ScNLFjBJi6nbhU8P4QG6tuln6iM24GBsXVA19rqDYYxt57wcGRNsgUCH3VK4v7mUBcJVw3nxrPe7ul'
trained_profile_name = 'testprof'
trained_cmd = 'push'

class WelcomeScreen(QtWidgets.QMainWindow):
    """
    class that handles UI generation based on MainWindow.ui file and connects buttons and combo boxes to their functions
    """
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("MainWindow.ui", self)
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        self.settings = [config["push"], config["pull"], config["left"], config["right"]]
        self.l = LiveAdvance(your_app_client_id, your_app_client_secret)
        self.PushCombo.setCurrentIndex(self.settings[0])
        self.PullCombo.setCurrentIndex(self.settings[1])
        self.LeftCombo.setCurrentIndex(self.settings[2])
        self.RightCombo.setCurrentIndex(self.settings[3])
        self.StartButton.clicked.connect(lambda: self.start_mapping())
        self.PauseButton.clicked.connect(lambda: self.pause_mapping())
        self.PullCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('pull', self.PullCombo.currentIndex()))
        self.PushCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('push', self.PushCombo.currentIndex()))
        self.LeftCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('left', self.LeftCombo.currentIndex()))
        self.RightCombo.currentIndexChanged.connect(lambda: self.on_combobox_changed('right', self.RightCombo.currentIndex()))


    def on_combobox_changed(self, name, value):
        """
        to handle combo box value changes

        new values are updated in a json file using the save_config(settings) function
        """
        if name == 'push':
            self.settings[0] = value
        elif name == 'pull':
            self.settings[1] = value
        elif name == 'left':
            self.settings[2] = value
        elif name == 'right':
            self.settings[3] = value
        save_config(self.settings)

    def start_mapping(self):
        """
        to start key mapping

        create a thread of emotiv live_advance class (altered on_new_cmd function that maps the keys based
        on the key mapping values given in config.json file
        """
        print('start_mapping')
        self.l = LiveAdvance(your_app_client_id, your_app_client_secret)
        liveThread = threading.Thread(target=self.l.start, args=[trained_profile_name], daemon=False)
        liveThread.start()

    def pause_mapping(self):
        """
        to pause mapping

        use stop function added to emotiv live_advance class
        """
        print('pause mapping')
        if self.l:
            self.l.stop()

"""
generating UI using the MainWindow.ui file and WelcomeScreen class  
"""
app = QtWidgets.QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setWindowIcon(QtGui.QIcon("logo.png")) #add a logo here
widget.setWindowTitle("Emotiv DJI Controller")
widget.resize(796,349)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")