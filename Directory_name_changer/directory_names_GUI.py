from PyQt5.QtWidgets import *
import os


class Widgets(QWidget):
    def __init__(self, **kwargs):
        super(Widgets, self).__init__()

        self.vlayout = QVBoxLayout()

        self.hlayout_4 = QHBoxLayout()

        self.l4 = QLabel()
        self.l4.setText('''Paste path to the main directory where are LVL2 directories (main_LVL1\LVL2\LVL3_A)\n
Program changes directory names inside LVL2 directories, for example (LVL2\LVL3_A -> LVL2\LVL3_B)
                        ''')
        self.hlayout_4.addWidget(self.l4)

        self.vlayout.addLayout(self.hlayout_4)

        self.setLayout(self.vlayout)


        self.hlayout_1 = QHBoxLayout()

        self.l1 = QLabel()
        self.l1.setText("Old name \t")
        self.hlayout_1.addWidget(self.l1)

        self.t1 = QLineEdit()
        self.hlayout_1.addWidget(self.t1)

        self.vlayout.addLayout(self.hlayout_1)


        self.hlayout_2 = QHBoxLayout()

        self.l2 = QLabel()
        self.l2.setText("New name\t")
        self.hlayout_2.addWidget(self.l2)

        self.t2 = QLineEdit()
        self.hlayout_2.addWidget(self.t2)

        self.vlayout.addLayout(self.hlayout_2)

        self.setLayout(self.vlayout)


        self.hlayout_3 = QHBoxLayout()

        self.l3 = QLabel()
        self.l3.setText("Path to directories   ")
        self.hlayout_3.addWidget(self.l3)

        self.t3 = QLineEdit()
        self.hlayout_3.addWidget(self.t3)

        self.vlayout.addLayout(self.hlayout_3)

        self.setLayout(self.vlayout)


        self.bttn = QPushButton("Change names")
        self.bttn.clicked.connect(self.onclick)
        self.bttn.setGeometry(200, 150, 100, 40)
        self.vlayout.addWidget(self.bttn)
        self.setLayout(self.vlayout)

    def onclick(self):
        self.old_name = self.t1.text()
        self.new_name = self.t2.text()
        self.path_to_dirs = self.t3.text()

        self.list_dirs = self.get_dir_names(self.path_to_dirs)
        self.go_through_dirs(self.old_name, self.new_name, self.list_dirs)





    def get_dir_names(self, path_to_dirs=""):
        os.chdir(path_to_dirs)
        list_dir_prep = os.listdir()
        list_dir_post = []

        for i in list_dir_prep:
            if "." not in i:
                list_dir_post.append(i)
        return list_dir_post

    def change_dirs_name(self, old="", new_name=""):
        os.rename(old, new_name)

    def go_through_dirs(self,old_name, new_name, list_of_dirs=[]):
        for dir in list_of_dirs:
            os.chdir(dir)
            self.change_dirs_name(old_name, new_name)
            os.chdir("..")


def window():
    app = QApplication([])

    wig = Widgets()
    wig.resize(500,250)
    wig.setWindowTitle("Directory name changer")

    wig.show()
    app.exec_()


if __name__ == "__main__":
    window()