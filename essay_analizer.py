import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtWidgets import QLabel, QLineEdit, QFileDialog, QInputDialog

def sortByLength(inputStr):
    return len(inputStr)


class Tricker(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        uic.loadUi('ui.ui', self)
        self.main_button.clicked.connect(self.find_repetitions)
        self.second_button.clicked.connect(self.find_mistakes)
        self.third_button.clicked.connect(self.help_to_improve)
        self.inp = open("roots.txt")
        self.inp2 = open("russian.txt", encoding="windows-1251")
        self.inp3 = open("russian_surnames.txt", encoding="windows-1251")
        self.roots = sorted(self.inp.read().split("\n"), key=sortByLength, reverse=True)
        self.words = self.inp2.read().split("\n")
        self.surnames = self.inp3.read().split("\n")
        self.inp.close()
        self.inp.close()
        self.inp.close()

    def find_repetitions(self):
        self.text = self.PlaceForText.text().split(".")
        for i in range(len(self.text)):
            self.used_roots = []
            self.previous_words = []
            self.text[i] = self.text[i].split()
            for elem in self.text[i]:
                if elem in self.previous_words:
                    add = "Слова " + elem + " в предложении " + str(i) + " повторяется"
                    self.PlaceForAnswer.setText(self.PlaceForAnswer.text() + "\n" + add)
                else:
                    for root in self.roots:
                        if root in elem:
                            if root in self.used_roots:
                                add = "\n" + "Слова" + elem + ", "\
                                      + self.previous_words[self.used_roots.index(root)]\
                                      + " в предложении " + str(i)
                                self.PlaceForAnswer.setText(self.PlaceForAnswer.text() + add)
                            else:
                                self.used_roots.append(root)
                                self.previous_words.append(elem)

    def find_mistakes(self):
        self.text = self.PlaceForText.text().split(".")
        for i in range(len(self.text)):
            for elem in self.text[i]:
                if elem not in self.words and elem not in self.surnames:
                    add = "Слово " + elem + " в предложении " + str(i)
                    self.PlaceForAnswer.setText(self.PlaceForAnswer.text() + "\n" + add)

    def help_to_improve(self):
        self.text = self.PlaceForText.text().split(".")
        for i in range(len(self.text)):
            for elem in self.text[i]:
                if elem not in self.words:
                    add = "Слово " + elem + " в предложении " + str(i)
                    add += "\n" + "Предлагаемые варианты:"
                    for word in self.words:
                        count = 0
                        for j in range(len(word)):
                            if word[j] == elem[j]:
                                count += 1
                        if count >= len(elem) - 2:
                            add += "\n" + word
                    for surname in self.surnames:
                        count = 0
                        for j in range(len(surname)):
                            if surname[j] == elem[j]:
                                count += 1
                        if count >= len(elem) - 2:
                            add += "\n" + surname
                    self.PlaceForAnswer.setText(self.PlaceForAnswer.text() + "\n" + add)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tricker()
    ex.show()
    sys.exit(app.exec())
