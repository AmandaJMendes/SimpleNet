import sys
sys.path.append("/home/amanda/Área de Trabalho/FURG/2/AEDii/TrabalhoGrafos/Windows")

from datetime import datetime
from graphClass import Graph
from socialNet import SimpleNet
from myWidgets import Post, Connection

from PyQt5.QtCore import (QDate, QDateTime)
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.uic import loadUi

from signin import SignIn_MainWindow
from signupPersonal import SignUpPersonal_MainWindow
from signupOrg import SignUpOrg_MainWindow
from menu import Menu_MainWindow
from myprofileP import MyProfileP_MainWindow
from myprofileO import MyProfileO_MainWindow
from conns import Conns_MainWindow
from profileP import ProfileP_MainWindow
from profileO import ProfileO_MainWindow
from search import Search_MainWindow
from userSearch import UsrSearch_MainWindow
from graph import Graph_MainWindow



class SignInWin(QMainWindow, SignIn_MainWindow):
    """
    Sign In Window.
    """
    def __init__(self, SNet, parent = None):
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        #SimpleNet instance
        self.SNet = SNet
        
        #Connections
        self.CreatePpushButton.pressed.connect(self.openSignUpPersonal)
        self.CreateOpushButton.pressed.connect(self.openSignUpOrg)
        self.signinpushButton.pressed.connect(self.siginAttempt)
        
    def openSignUpPersonal(self):
        """
        Open window to create personal account
        """
        self.signup = SignUpPersonalWin(self.SNet)
        self.signup.show()

    def openSignUpOrg(self):
        """
        Open window to create business account
        """
        self.signup = SignUpOrgWin(self.SNet)
        self.signup.show()
        
    def siginAttempt(self):
        """
        Sign in attempt
        
        User and password must be correct --> Open Menu window
        Ohterwise, show error message
        """
        username = self.usrLineEdit.text()
        passwrd = self.passwrdLineEdit.text()
        
        userV = self.SNet.getUser(username)
        if userV and userV.value["passwrd"] == passwrd:
            self.menu = MenuWin(self.SNet, userV)
            self.menu.show()
            self.close()
        else:
            self.invalidUsrLabel.setText("Usuário e/ou senha inválidos")
            self.usrLineEdit.setText("")
            self.passwrdLineEdit.setText("")
        
class SignUpPersonalWin(QMainWindow, SignUpPersonal_MainWindow):
    def __init__(self, SNet, parent = None):
        """
        Window to create personal account 
        """
        
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance
        self.SNet = SNet
        
        #Connections
        self.CreatepushButton.pressed.connect(self.createAccount)

    def createAccount(self):
        """
        Attempt to create account
        
        All data must be valid --> create account --> add vertex to graph
        Otherwise, show error message
        """
        user = self.usrLineEdit.text()
        passwrd = self.passwrdLineEdit.text()
        
        person = True
        data = [field.text() for field in [self.nameLineEdit, self.emailLineEdit,
                                             self.cityLineEdit, self.cpfLineEdit]] + [self.dateEdit.date().toString('dd/MM/yyyy')]
        unexpected_data = [""]*4 + [QDate.currentDate().addYears(-15).addDays(1).toString('dd/MM/yyyy')]
        private = [cb.isChecked() for cb in [self.namecheckBox, self.emailcheckBox,
                                              self.citycheckBox, self.cpfcheckBox, self.borncheckBox]]
        labels = ["name","email", "city", "cpf", "born"]
            
        flag = self.SNet.createAccount(user, passwrd, person, data, unexpected_data, private, labels)
        if flag == -1:
            self.UrsErrorlabel.setText("Usuário inválido")
        elif flag == 0:
            self.UrsErrorlabel.setText("Preencha corretamente todos os campos")        
        else:
            self.close()

        
class SignUpOrgWin(QMainWindow, SignUpOrg_MainWindow):
    def __init__(self, SNet, parent=None):
        """
        Window to create business account 
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance
        self.SNet = SNet
        
        #Connections
        self.CreatepushButton.pressed.connect(self.createAccount)

    def createAccount(self):
        """
        Attempt to create account
        
        All data must be valid --> create account --> add vertex to graph
        Otherwise, show error message
        """
        user = self.usrLineEdit.text()
        passwrd = self.passwrdLineEdit.text()
        
        person = False
        data = [field.text() for field in [self.nameLineEdit, self.emailLineEdit,
                                           self.segmLineEdit, self.cityLineEdit, self.cnpjLineEdit]]
        data[2] = data[2] if data[2] else self.comboBox.currentText()
        unexpected_data = [""]*5 
        private = [cb.isChecked() for cb in [self.namecheckBox, self.emailcheckBox,
                                             self.segmcheckBox, self.citycheckBox, self.cnpjcheckBox]]
        labels = ["name","email", "segment","city", "cnpj"]
            
        flag = self.SNet.createAccount(user, passwrd, person, data, unexpected_data, private, labels)
        if flag == -1:
            self.UrsErrorlabel.setText("Usuário inválido")
        elif flag == 0:
            self.UrsErrorlabel.setText("Preencha corretamente todos os campos")        
        else:
            self.close()
            
    
class MenuWin(QMainWindow, Menu_MainWindow):
    def __init__(self, SNet, user, parent=None):
        """
        Main window (Menu / Posts)
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user) 
        self.SNet = SNet
        self.user = user
        
        #Connections
        self.postpushButton.pressed.connect(self.post)
        self.profilepushButton.pressed.connect(self.openProfile)
        self.searchpushButton.pressed.connect(self.openSearch)
        self.graphpushButton.pressed.connect(self.openGraph)
        self.logoutpushButton.pressed.connect(self.logout)
        self.connspushButton.pressed.connect(self.conns)
        self.pushButton.pressed.connect(self.refresh)
        self.pushButton_2.pressed.connect(self.refresh)
    
        #Setup posts
        self.refresh()
        
    def refresh(self):
        """
        Refresh comboBox and posts based on adjacent users
        """
        self.setUsersCB()
        self.setPosts(self.comboBox.currentText())
        
    def setUsersCB(self):
        """
        Setup comboBox options based on adjacent users
        """
        allItems = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
        for user in self.user.adjacent.values():
            if user[0].key not in allItems:
                self.comboBox.addItem(user[0].key)

    def setPosts(self, usr_filter):
        """
        Setup posts based on adjacent users
        """
    
        if usr_filter == "Todas" or usr_filter == "Minhas":
            posts = [[self.user.key, post[0], datetime.strptime(post[1], '%d/%m/%Y - %H:%M')] for post in self.user.value["posts"]]
        else:
            posts = []
        
        if usr_filter == "Todas":
            for user in self.user.adjacent.values():
                for post in user[0].value["posts"]:
                    posts.append([user[0].key, post[0], datetime.strptime(post[1], '%d/%m/%Y - %H:%M')])
        elif usr_filter != "Minhas":
            for post in self.user.adjacent[usr_filter][0].value["posts"]:
                posts.append([usr_filter, post[0], datetime.strptime(post[1], '%d/%m/%Y - %H:%M')])
        
        posts = sorted(posts, key = lambda x: x[2], reverse = True)
        self.widget = QWidget()
        self.vbox = QVBoxLayout()          
        for username, post, date in posts:
            post_widget = Post(username, post, datetime.strftime(date, '%d/%m/%Y - %H:%M'))
            self.vbox.addWidget(post_widget) 
        self.widget.setLayout(self.vbox)
        self.scrollArea.setWidget(self.widget)
        self.scrollArea.setStyleSheet("QScrollArea {background-color: #EFF0F1;}")
        self.textEdit.setPlainText("")
        
    def post(self):
        """
        Save new post
        """
        self.user.value["posts"].append([self.textEdit.toPlainText(), QDateTime.currentDateTime().toString('dd/MM/yyyy - hh:mm')])
        self.setPosts(self.comboBox.currentText())

    def openProfile(self):
        """
        Open user's profile
        """
        if self.user.value["person"]:
            self.myprofile = MyProfilePWin(self.SNet, self.user)
        else:
            self.myprofile = MyProfileOWin(self.SNet, self.user)
        self.myprofile.show()
    
    def openSearch(self):
        """
        Open search window
        """
        self.search = SearchWin(self.SNet, self.user)
        self.search.show()
        
    def openGraph(self):
        """
        Open graph visualization window
        """
        self.SNetgraph = GraphWin(self.SNet, self.user)
        self.SNetgraph.show()
    
    def logout(self):
        """
        Logout
        """
        self.signin = SignInWin(self.SNet)
        self.signin.show()
        self.close()
    
    def conns(self):
        """
        Open connections window
        """
        self.conns = ConnsWin(self.SNet, self.user)
        self.conns.show()        

class ConnsWin(QMainWindow, Conns_MainWindow):
    def __init__(self, SNet, user, parent=None):
        """
        Connections window (show following and followers)
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user) 
        self.SNet = SNet
        self.user = user
        
        #Setup 
        self.configure()
        
    def configure(self):
        """
        Setup
        """
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        for node in self.user.adjacent.values():
            usr_widget = Connection(node[0].key, node[1])
            self.vbox.addWidget(usr_widget,stretch=1)
        self.widget.setLayout(self.vbox)
        self.scrollArea.setStyleSheet("QScrollArea {background-color: #EFF0F1;}")
        self.scrollArea.setWidget(self.widget)
        
        self.widget2 = QWidget()
        self.vbox2 = QVBoxLayout()
        incident = self.SNet.getFollowers(self.user.key)
        for node in incident:
            usr_widget = Connection(node.key, self.SNet.getConnection(node, self.user))
            self.vbox2.addWidget(usr_widget,stretch=1)
        self.widget2.setLayout(self.vbox2)
        self.scrollArea_2.setStyleSheet("QScrollArea {background-color: #EFF0F1;}")
        self.scrollArea_2.setWidget(self.widget2)
        
class MyProfilePWin(QMainWindow, MyProfileP_MainWindow):
    def __init__(self, SNet, user, parent=None):
        """
        Profile window (personal / editable)
        """
        
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user)
        self.SNet = SNet
        self.user = user
        
        #Setup
        userInfo = {}
        userInfo.update(self.user.value["private"])
        userInfo.update(self.user.value["public"])       
        for le, value in zip([self.label, self.nameLineEdit, self.emailLineEdit, self.cityLineEdit, self.cpfLineEdit],
                             [self.user.key, userInfo["name"], userInfo["email"], userInfo["city"], userInfo["cpf"]]):
            le.setText(value)
        self.bornLineEdit.setDate(QDate.fromString(userInfo["born"], "dd/MM/yyyy"))
        for cb, field in zip([self.namecheckBox, self.borncheckBox, self.emailcheckBox, self.citycheckBox, self.cpfcheckBox],
                             ["name", "born", "email", "city", "cpf"]):
            cb.setChecked(field in user.value["private"].keys())    
        
        #Connections
        self.pushButton.pressed.connect(self.updateInfo)
        
    def updateInfo(self):
        """
        Update user data --> update vertex value
        """
        data = [field.text() for field in [self.nameLineEdit, self.emailLineEdit,
                                             self.cityLineEdit, self.cpfLineEdit]] + [self.bornLineEdit.date().toString('dd/MM/yyyy')]
        unexpected_data = [""]*4 + [QDate.currentDate().addYears(-15).addDays(1)]
        private = [cb.isChecked() for cb in [self.namecheckBox, self.emailcheckBox,
                                              self.citycheckBox, self.cpfcheckBox, self.borncheckBox]]
        labels = ["name","email", "city", "cpf", "born"]
            
        flag = self.SNet.updateAccount(self.user, data, unexpected_data, private, labels)
        
        if not flag:
            self.label_2.setText("Preencha corretamente todos os campos")        
        else:
            self.close()

class MyProfileOWin(QMainWindow, MyProfileO_MainWindow):
    def __init__(self, SNet, user, parent=None):
        """
        Profile window (business / editable)
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user)
        self.SNet = SNet
        self.user = user

        #Setup
        userInfo = {}
        userInfo.update(self.user.value["private"])
        userInfo.update(self.user.value["public"])
        for le, value in zip([self.label, self.nameLineEdit, self.emailLineEdit, self.cityLineEdit, self.cnpjLineEdit],
                             [self.user.key, userInfo["name"], userInfo["email"], userInfo["city"], userInfo["cnpj"]]):
            le.setText(value)
        if self.comboBox.findText(userInfo["segment"]) != -1: 
            self.comboBox.setCurrentIndex(self.comboBox.findText(userInfo["segment"]))
        else:
            self.comboBox.setCurrentIndex(4)
            self.segmLineEdit.setText(userInfo["segment"])
        for cb, field in zip([self.namecheckBox, self.segmcheckBox, self.emailcheckBox, self.citycheckBox, self.cnpjcheckBox],
                             ["name", "segment", "email", "city", "cnpj"]):
            cb.setChecked(field in user.value["private"].keys())

        #Connections
        self.pushButton.pressed.connect(self.updateInfo)
        
    def updateInfo(self):
        """
        Update user data --> update vertex value
        """
        data = [field.text() for field in [self.nameLineEdit, self.emailLineEdit,
                                           self.segmLineEdit, self.cityLineEdit, self.cnpjLineEdit]]
        data[2] = data[2] if data[2] else self.comboBox.currentText()
        unexpected_data = [""]*5 
        private = [cb.isChecked() for cb in [self.namecheckBox, self.emailcheckBox,
                                             self.segmcheckBox, self.citycheckBox, self.cnpjcheckBox]]
        labels = ["name","email", "segment","city", "cnpj"]
            
        flag = self.SNet.updateAccount(self.user, data, unexpected_data, private, labels)
        
        if not flag:
            self.label_2.setText("Preencha corretamente todos os campos")        
        else:
            self.close()
        
class ProfilePWin(QMainWindow, ProfileP_MainWindow):
    def __init__(self, SNet, userAccount, userProfile, parent=None):
        """
        Profile window (personal)
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instances (users)
        self.SNet = SNet
        self.userAccount = userAccount #User who is accessing the profile (person or organization)
        self.userProfile = userProfile #User whose profile is being accessed (person)
        
        #Setup
        self.label.setText(self.userProfile.key)
        lEdits = dict(zip(["name", "email", "city", "cpf", "born"],
                          [self.nameLabel_2, self.emailLabel_2, self.cityLabel_2, self.cpfLabel_2, self.bornLabel_2])) 
        for field in self.userProfile.value["private"].keys():
            lEdits[field].setText("INFORMAÇÃO PRIVADA")
        for field, value in self.userProfile.value["public"].items():
            lEdits[field].setText(value)  
        connection = self.SNet.getConnection(userAccount, userProfile)
        if connection:
            self.connLabel_2.setText(connection)
        else:
            self.connLabel_2.setText("Nenhuma")
        
        #Connections
        self.ConnectpushButton.pressed.connect(self.addConnection)
        self.DisconnectpushButton.pressed.connect(self.removeConnection)
    
    def addConnection(self):
        """
        Create connection between the users / Add edge to graph
        """
        self.disconnectedLabel.setText("")
        if self.userAccount == self.userProfile:
            self.disconnectedLabel.setText("Conexão inválida. Esse é o seu perfil.")
            return

        if not self.SNet.getConnection(self.userAccount, self.userProfile): 
            conn_type = self.comboBox.currentText()
            if self.userAccount.value["person"] and conn_type == "Cliente":
                self.disconnectedLabel.setText("Tipo de conexão inválida")
                return
            if not self.userAccount.value["person"]:
                self.disconnectedLabel.setText("Não é possível realizar conexão com pessoas")
                return
            elif conn_type == "Amigo":
                self.SNet.addFriendship(self.userAccount, self.userProfile)
            elif conn_type == "Conhecido":
                self.SNet.addAcquaintance(self.userAccount, self.userProfile)
            elif conn_type == "Família":
                self.SNet.addFamily(self.userAccount, self.userProfile)
            else:
                self.SNet.addClient(self.userAccount, self.userProfile)
            self.connLabel_2.setText(conn_type)
        else:
            self.disconnectedLabel.setText("Primeiro, remova a conexão existente com esse usuário")
            
    def removeConnection(self):
        """
        Remove connection between the users / Remove edge from graph
        """
        self.disconnectedLabel.setText("")
        if self.userAccount == self.userProfile:
            self.disconnectedLabel.setText("Conexão inválida. Esse é o seu perfil.")
            return
        conn_type = self.SNet.getConnection(self.userAccount, self.userProfile)
        if conn_type: 
            if conn_type == "Amigo":
                self.SNet.removeFriendship(self.userAccount, self.userProfile)
            elif conn_type == "Conhecido":
                self.SNet.removeAcquaintance(self.userAccount, self.userProfile)
            elif conn_type == "Família":
                self.SNet.removeFamily(self.userAccount, self.userProfile)
            else:
                self.SNet.removeClient(self.userAccount, self.userProfile)
            self.connLabel_2.setText("Nenhuma")
        else:
            self.disconnectedLabel.setText("Não existe conexão com esse usuário")    

class ProfileOWin(QMainWindow, ProfileO_MainWindow):
    def __init__(self, SNet, userAccount, userProfile, parent=None):
        """
        Profile window (personal)
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instances (users)
        self.SNet = SNet
        self.userAccount = userAccount #User who is accessing the profile (person or organization)
        self.userProfile = userProfile #User whose profile is being accessed (organization)
        
        #Setup
        self.label_2.setText(self.userProfile.key)
        lEdits = dict(zip(["name", "email", "city", "cnpj", "segment"],
                          [self.namelabel, self.emaillabel, self.citylabel, self.cnpjlabel, self.segmlabel]))
        for field in self.userProfile.value["private"].keys():
            lEdits[field].setText("INFORMAÇÃO PRIVADA")
        for field, value in self.userProfile.value["public"].items():
            lEdits[field].setText(value)        
        connection = self.SNet.getConnection(userAccount, userProfile)
        if connection:
            self.connlabel.setText(connection)
        else:
            self.connlabel.setText("Nenhuma")
       
        #Setup
        self.ConnectpushButton_2.pressed.connect(self.addConnection)
        self.DisconnectpushButton_2.pressed.connect(self.removeConnection)
    
    def addConnection(self):
        """
        Create connection between the users / Add edge to graph
        """
        if self.userAccount == self.userProfile:
            self.label.setText("Conexão inválida. Esse é o seu perfil.")
        elif not self.SNet.getConnection(self.userAccount, self.userProfile): 
            self.SNet.addClient(self.userAccount, self.userProfile)
            self.connlabel.setText("Cliente")
        else:
            self.label.setText("Primeiro, remova a conexão existente com esse usuário")
            
    def removeConnection(self):
        """
        Remove connection between the users / Remove edge from graph
        """
        conn_type = self.SNet.getConnection(self.userAccount, self.userProfile)
        if conn_type: 
            self.SNet.removeClient(self.userAccount, self.userProfile)
            self.connlabel.setText("Nenhuma")
        else:
            self.label.setText("Não existe conexão com esse usuário")    

class SearchResultsWin(QMainWindow, UsrSearch_MainWindow):
    def __init__(self, SNet, user, matches, key, value, person, parent=None):
        """
        Search results (present users who match the search)
        """    
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user)
        self.SNet = SNet
        self.user = user
        
        #Search parameters
        self.matches = matches #list of users who match the smart search
        self.key = key #Type of data (name, email, username, etc)
        self.value = value #Data 
        self.person = person #Person or organization
        self.counter = 0 #Auxiliary counter
        
    def configure(self):
        """
        -Setup connections
        -Perform dumb search if no matches were found with BFS
        """
        self.SimpushButton.pressed.connect(self.foundUser)
        if self.matches:
            self.counter = 1
            self.label.setText(self.matches[0].key)
            self.NaopushButton.pressed.connect(self.nextUser)
            return True
        else:
            self.matches = self.SNet.dumbSearch(self.key, self.value, self.person)
            if self.matches:
                self.NaopushButton.pressed.connect(self.nextUserDumb) 
                self.nextUserDumb()
                return True
            else:
                return False
    
    def notFound(self):
        """
        No more matches
        Go back to search window
        """
        self.search = SearchWin(self.SNet, self.user, True, self)
        self.search.show()
        self.close()
 
    def nextUser(self):
        """
        -Display next matching user
        -Perform dumb search if no more matches were found with BFS
        -Cease search when there are no more matches
        """
        if self.counter <  len(self.matches):
            self.label.setText(self.matches[self.counter].key)
            self.counter+=1
        else:
            dumb = self.SNet.dumbSearch(self.key, self.value, self.person) 
            self.matches = [i for i in dumb if i not in self.matches]
            if self.matches:
                self.NaopushButton.pressed.disconnect(self.nextUser)
                self.NaopushButton.pressed.connect(self.nextUserDumb)
                self.label.setText(self.matches[0].key)
                self.counter = 1
            else:
                self.notFound()
            
    def nextUserDumb(self):
        """
        -Display net matching user
        -Cease search when there are no more matches
        """
        if self.counter <  len(self.matches):
            self.label.setText(self.matches[self.counter].key)
            self.counter +=1
        else:
            self.notFound()
            
    def foundUser(self):
        """
        Open user profile and close this window
        """
        person = self.matches[self.counter-1].value["person"]
        if person:
            self.usrProfile = ProfilePWin(self.SNet, self.user, self.matches[self.counter-1])
            self.usrProfile.show()
            self.close()
        else:
            self.usrProfile = ProfileOWin(self.SNet, self.user, self.matches[self.counter-1])
            self.usrProfile.show()
            self.close()        
            
class SearchWin(QMainWindow, Search_MainWindow):
    def __init__(self, SNet, user, notFound = False, usrSWin = None, parent=None):
        """
        Search window
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user)
        self.SNet = SNet
        self.user = user
        
        #Setup - notFound will be set to True when SearchResultWin opens a SearchWin
        if notFound:
            self.notFoundLabel.setText("Usuário não encontrado")
        
        #Connections
        self.pushButton.pressed.connect(self.searchUser)
    
    def searchUser(self):
        """
        - Use BFS to search for user
        - Open userSearchWin with resulting matches 
        """
        person = self.PersonradioButton.isChecked()
        if person:
            field = self.PersoncomboBox.currentText()
        else:
            field = self.OrgcomboBox.currentText()
        translate_field = {"Usuário": "user", "Nome": "name", "E-mail": "email", "Data de nascimento": "born",
                           "Segmento": "segment", "Cidade": "city", "CPF": "cpf", "CNPJ": "cnpj"}
        value = self.lineEdit.text()
        userSearch = self.SNet.smartSearch(self.user.key, translate_field[field], value, person)
        self.userSearchWin = SearchResultsWin(self.SNet, self.user, userSearch, translate_field[field], value, person)
        if self.userSearchWin.configure():
            self.userSearchWin.show()
            self.close()
        else:
            self.notFoundLabel.setText("Usuário não encontrado")

class GraphWin(QMainWindow, Graph_MainWindow):
    def __init__(self, SNet, user, parent=None):
        """
        Window for graph visualization
        """
        #Setup
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(stylesheet)
        
        #SimpleNet instance and Vertex instance (user)
        self.SNet = SNet
        self.user = user
        
        #Connections
        self.pushButton.pressed.connect(self.plotSubGraph)
        self.pushButton_2.pressed.connect(self.plotGraph)
    
    def plotSubGraph(self):
        """
        Plot subgraph with x levels from current user
        """
        self.SNet.saveGraphImg(self.user, "graph.png", self.spinBox.value())
        pixmap = QPixmap('graph.png')
        self.label_2.setPixmap(pixmap)
    
    def plotGraph(self):
        """
        Plot whole graph
        """
        self.SNet.saveGraphImg(self.user, "graph.png")
        pixmap = QPixmap('graph.png')
        self.label_2.setPixmap(pixmap)
      

def MyAppExec():
    """
    Main execution
    """
    SNet = SimpleNet()
#     SNet.fromEmptyGraph()
    SNet.fromPkl("mysocialnet2.pkl")
    app = QApplication(sys.argv)
    font = QFont()
    font.setFamily("Jamrul")
    font.setPointSize(10)
    font.setBold(False)
    font.setItalic(False)
    font.setWeight(50)
    app.setFont(font)
    win = SignInWin(SNet)
    win.show()
    app.exec()
    SNet.dumpToPkl("mysocialnet2.pkl")
        
if __name__ == "__main__":
    #Stylesheet for all windows
    stylesheet = """
        QMainWindow {
            background-image: url("/home/amanda/Área de Trabalho/FURG/2/AEDii/TrabalhoGrafos/back.png"); 
            background-repeat: no-repeat; 
         }
     """
    sys.exit(MyAppExec())  
    
