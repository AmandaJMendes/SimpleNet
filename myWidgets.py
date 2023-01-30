from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont

class Connection(QWidget):
    def __init__(self, username, weight, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)
        self.verticalLayout = QVBoxLayout()
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        userlabel = QLabel(username)
        userlabel.setFont(font)
        userlabel.setObjectName("userlabel")
        self.verticalLayout.addWidget(userlabel)
        label = QLabel(weight)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        label.setFont(font)
        label.setObjectName("label")
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.addWidget(label)
        self.verticalLayout.addStretch(1)
        self.setLayout(self.verticalLayout)
        
class Post(QWidget):
    def __init__(self, username, post_text, post_date, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.verticalLayout = QVBoxLayout() 
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        userlabel = QLabel(username)
        userlabel.setFont(font)
        userlabel.setObjectName("userlabel")
        self.verticalLayout.addWidget(userlabel)
        label = QLabel(post_text)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        label.setFont(font)
        label.setObjectName("label")
        label.setStyleSheet("border: 1px solid black;")
        self.verticalLayout.addWidget(label)
        label_2 = QLabel(post_date)
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(label_2)
        self.verticalLayout.addStretch(1)
        self.setLayout(self.verticalLayout)