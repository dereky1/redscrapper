from PyQt5.QtWidgets import (QApplication, QScrollArea,QHeaderView, QAbstractItemView, QTabWidget,QListWidget, QWidget, QTableWidget, QPushButton, QRadioButton, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QMainWindow, QFrame, QPlainTextEdit)
import redscrapper
import sys

class Init_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.reddit = redscrapper.init()
        self.width = 900
        self.height = 600
        self.resize(self.width,self.height)
        self.layout = QGridLayout()
        self.setup();
        self.show()

    def setup(self):
        self.layout.addLayout(self.searchBar(),0,0)
        self.layout.addLayout(self.mainContent(),1,0,3,3)
        self.setLayout(self.layout)

    def searchBar(self):
        searchBarLayout = QHBoxLayout()
        searchLabel = QLabel("Search")
        self.searchBarBox = QLineEdit()
        self.searchBarBox.returnPressed.connect(self.displayContent)
        searchBarLayout.addWidget(searchLabel)
        searchBarLayout.addWidget(self.searchBarBox)
        return searchBarLayout

    def mainContent(self):
        mainContentLayout = QVBoxLayout()
        mainContentScrollable = QScrollArea()
        self.content = QLabel("")
        mainContentScrollable.setWidget(self.content)
        mainContentLayout.addWidget(mainContentScrollable)
        return mainContentLayout

    def clearSearchBox(self):
        self.searchBarBox.setText("")

    def getSearchBox(self):
        return self.searchBarBox.text()

    def displayContent(self):
        subredditTitle = self.getSearchBox()
        string = ""
        for submission in redscrapper.getSubreddit(self.reddit,subredditTitle):
            string += "{Title}\n{text}".format(Title=submission.title, text=submission.selftext)
            string += "Comments:\n{comments}".format(comments = submission.comments.list())
        self.content.setText(string)
        print(string)


def startGUI():
    app = QApplication([])
    home = Init_GUI()
    sys.exit(app.exec_())

startGUI()
