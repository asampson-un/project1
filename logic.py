from PyQt6.QtWidgets import *
from gui import *
import re

#ID must be made of 8 numbers
#txt file; (no #)
#ID: //id
#VOTED: //vote
#-----

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initialize window and make buttons usable
        """
        super().__init__()
        self.setupUi(self)

        self.submit_Button.clicked.connect(self.submit)
        self.candidate_Radio.setText("John")
        self.candidate2_Radio.setText("Jane")


    def submit(self) -> None:
        """
        Submit vote information if given choice and correct ID
        """
        try:
            _ID :int = int(self.ID_Entry.text())
            if _ID <= 9999999 or _ID > 99999999: raise TypeError
            if self.radio_Group.checkedButton() is None: raise KeyError
        except ValueError, TypeError:
            self.about_Label.setStyleSheet("color: red;")
            self.about_Label.setText("ID must be 8 digits")
        except KeyError:
            self.about_Label.setStyleSheet("color: orange;")
            self.about_Label.setText("No Choice Selected")
        else: #has good ID and selected a choice
            self.about_Label.setText("")

            #create file if not exist
            _file :object = open("voteinfo.txt", "a+")
            _file.close()

            #check if ID is already in file
            _exists :bool = False
            with open("voteinfo.txt", "r") as votefile:
                for line in votefile:
                    line.rstrip()
                    if re.search("ID:", line):
                        line :list = line.split()
                        if self.ID_Entry.text() == line[1]: #ID exists in file
                            _exists = True
                            self.about_Label.setStyleSheet("color: orange;")
                            self.about_Label.setText("Already Voted")


            if not _exists:
                with open("voteinfo.txt", "a") as voteinfo:
                    voteinfo.write(f"ID: {self.ID_Entry.text()}\n")
                    voteinfo.write(f"VOTED: {self.radio_Group.checkedButton().text()}\n")
                    voteinfo.write("------\n")
