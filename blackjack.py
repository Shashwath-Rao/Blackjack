from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QInputDialog, QMessageBox
from PyQt6.QtGui import QPixmap
import math
import random


class Ui_Dialog:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 794)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 700, 60, 32))
        self.pushButton.setMaximumSize(QtCore.QSize(750, 300))
        self.pushButton.setObjectName("pushButton")
        self.splitter_2 = QtWidgets.QSplitter(parent=Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(10, 340, 1000, 300))
        self.splitter_2.setMaximumSize(QtCore.QSize(1003, 300))
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label6 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label6.setMinimumSize(QtCore.QSize(195, 300))
        self.label6.setMaximumSize(QtCore.QSize(195, 300))
        self.label6.setText("")
        self.label6.setScaledContents(True)
        self.label6.setObjectName("label6")
        self.label7 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label7.setMinimumSize(QtCore.QSize(195, 300))
        self.label7.setMaximumSize(QtCore.QSize(195, 300))
        self.label7.setText("")
        self.label7.setScaledContents(True)
        self.label7.setObjectName("label7")
        self.label8 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label8.setMinimumSize(QtCore.QSize(195, 300))
        self.label8.setMaximumSize(QtCore.QSize(195, 300))
        self.label8.setText("")
        self.label8.setScaledContents(True)
        self.label8.setObjectName("label8")
        self.label9 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label9.setMinimumSize(QtCore.QSize(195, 300))
        self.label9.setMaximumSize(QtCore.QSize(195, 300))
        self.label9.setText("")
        self.label9.setScaledContents(True)
        self.label9.setObjectName("label9")
        self.label10 = QtWidgets.QLabel(parent=self.splitter_2)
        self.label10.setMinimumSize(QtCore.QSize(195, 300))
        self.label10.setMaximumSize(QtCore.QSize(195, 300))
        self.label10.setText("")
        self.label10.setScaledContents(True)
        self.label10.setObjectName("label10")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(507, 700, 71, 32))
        self.pushButton_2.setMaximumSize(QtCore.QSize(750, 300))
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter = QtWidgets.QSplitter(parent=Dialog)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 1000, 300))
        self.splitter.setMaximumSize(QtCore.QSize(1003, 300))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label1 = QtWidgets.QLabel(parent=self.splitter)
        self.label1.setMinimumSize(QtCore.QSize(195, 300))
        self.label1.setMaximumSize(QtCore.QSize(195, 300))
        self.label1.setText("")
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(parent=self.splitter)
        self.label2.setMinimumSize(QtCore.QSize(195, 300))
        self.label2.setMaximumSize(QtCore.QSize(195, 300))
        self.label2.setText("")
        self.label2.setScaledContents(True)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(parent=self.splitter)
        self.label3.setMinimumSize(QtCore.QSize(195, 300))
        self.label3.setMaximumSize(QtCore.QSize(195, 300))
        self.label3.setText("")
        self.label3.setScaledContents(True)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(parent=self.splitter)
        self.label4.setMinimumSize(QtCore.QSize(195, 300))
        self.label4.setMaximumSize(QtCore.QSize(195, 300))
        self.label4.setText("")
        self.label4.setScaledContents(True)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(parent=self.splitter)
        self.label5.setMinimumSize(QtCore.QSize(195, 300))
        self.label5.setMaximumSize(QtCore.QSize(195, 300))
        self.label5.setText("")
        self.label5.setScaledContents(True)
        self.label5.setObjectName("label5")
        self.result = QtWidgets.QLabel(parent=Dialog)
        self.result.setGeometry(QtCore.QRect(10, 670, 650, 30))
        self.result.setText("")
        self.result.setObjectName("result")
        self.win = QtWidgets.QLabel(parent=Dialog)
        self.win.setGeometry(QtCore.QRect(700, 665, 194, 40))
        self.win.setText("Computer : 0 \t Player : 0")
        self.win.setObjectName("win")
        self.win.setStyleSheet("border: 2px dotted black;")

        self.splitter.raise_()
        self.splitter_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.result.raise_()
        self.win.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Black Jack"))
        self.pushButton.setText(_translate("Dialog", "Hit"))
        self.pushButton_2.setText(_translate("Dialog", "Stand"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    playing = True
    chip = 100
    highscore = 0
    while True:
        uname, ok = QInputDialog.getText(None, "User Name", "Please enter your name")
        if ok and uname != "":
            break

    table = {'Computer': 0, 'Player': 0}
    suits = ('hearts', 'diamonds', 'spades', 'clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    class Card:

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return self.rank + " of " + self.suit


    class Deck:

        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))

        def shuffle(self):
            random.shuffle(self.deck)

        def remove_one(self):
            return self.deck.pop(0)


    def print_some(computer, player):
        ui.label1.setPixmap(QPixmap("png/"+computer[1].rank+"_of_"+computer[1].suit+".png"))
        ui.label2.setPixmap(QPixmap("png/not.png"))
        ui.label6.setPixmap(QPixmap("png/"+player[0].rank+"_of_"+player[0].suit+".png"))
        ui.label7.setPixmap(QPixmap("png/"+player[1].rank+"_of_"+player[1].suit+".png"))
        players_total(player)


    def print_all(computer, player):
        i = 1
        for card in range(len(computer)):
            if i == 1:
                ui.label1.setPixmap(QPixmap("png/"+computer[card].rank+"_of_"+computer[card].suit+".png"))
            elif i == 2:
                ui.label2.setPixmap(QPixmap("png/"+computer[card].rank+"_of_"+computer[card].suit+".png"))
            elif i == 3:
                ui.label3.setPixmap(QPixmap("png/"+computer[card].rank+"_of_"+computer[card].suit+".png"))
            elif i == 4:
                ui.label4.setPixmap(QPixmap("png/"+computer[card].rank+"_of_"+computer[card].suit+".png"))
            elif i == 5:
                ui.label5.setPixmap(QPixmap("png/"+computer[card].rank+"_of_"+computer[card].suit+".png"))
            i += 1

        dealers_total(computer)

        i = 1
        for card in range(len(player)):
            if i == 1:
                ui.label6.setPixmap(QPixmap("png/"+player[card].rank+"_of_"+player[card].suit+".png"))
            elif i == 2:
                ui.label7.setPixmap(QPixmap("png/"+player[card].rank+"_of_"+player[card].suit+".png"))
            elif i == 3:
                ui.label8.setPixmap(QPixmap("png/"+player[card].rank+"_of_"+player[card].suit+".png"))
            elif i == 4:
                ui.label9.setPixmap(QPixmap("png/"+player[card].rank+"_of_"+player[card].suit+".png"))
            elif i == 5:
                ui.label10.setPixmap(QPixmap("png/"+player[card].rank+"_of_"+player[card].suit+".png"))
            i += 1

        players_total(player)


    def dealers_total(computer):
        ui.result.setText(f"Computer's Total: {check_ace(computer)}")


    def players_total(player):
        ui.result.setText(ui.result.text() + f" Player's Total: {check_ace(player)}")


    def check_ace(hand):
        ace_count = 0
        ace_adjusted_total = 0

        for card in range(len(hand)):
            ace_adjusted_total += hand[card].value

            if hand[card].value == 11:
                ace_count += 1

        if ace_adjusted_total > 21 and ace_count > 0:
            for card in range(ace_count):
                ace_adjusted_total -= 10
            return ace_adjusted_total

        else:
            return ace_adjusted_total


    def hit(computer_cards, player_cards, player_deck):
        while True:
            a1 = check_ace(player_cards)

            if a1 <= 21:
                player_cards.append(player_deck.pop(0))
                return player_cards
            else:
                player_lose(computer_cards, player_cards)
                break


    def hit_stand(computer_cards, player_cards, player_deck):
        stand = False
        global playing

        def s():
            nonlocal stand
            stand = True

        def h():
            player_card = hit(computer_cards, player_cards, player_deck)

            if player_card is None:
                return

            if check_ace(player_card) <= 21:
                print_all(computer_cards, player_card)

            else:
                player_lose(computer_cards, player_card)

        ui.pushButton.clicked.connect(h)
        ui.pushButton_2.clicked.connect(s)

        while True:
            QtGui.QGuiApplication.processEvents()
            if not playing or stand:
                ui.pushButton.disconnect()
                ui.pushButton_2.disconnect()
                break


    def play_dealer(computer_cards, player_cards, computer_deck):
        while True:
            comp_total = check_ace(computer_cards)
            player_total = check_ace(player_cards)

            if comp_total > player_total:
                player_lose(computer_cards, player_cards)
                break

            elif comp_total <= 17:
                computer_cards.append(computer_deck.pop(0))

                if check_ace(computer_cards) <= 21:
                    print_all(computer_cards, player_cards)

                else:
                    dealer_lose(computer_cards, player_cards)
                    break

            elif comp_total == player_total:
                print_all(computer_cards, player_cards)
                ui.result.setText("It's a tie!!!")
                table['Computer'] += 1
                table['Player'] += 1
                disp_record()
                break

            else:
                dealer_lose(computer_cards, player_cards)
                break


    def store_highscore():
        if highscore > 100:
            with open("highscore.txt", "a") as f:
                f.write(f"{uname} : {highscore} \n")


    def player_lose(computer_cards, player_cards):
        global playing, chip
        chip -= bet
        table['Computer'] += 1
        print_all(computer_cards, player_cards)
        ui.result.setText(f"Computer has won!!! Player has lost! Total chips remaining: {chip}\n"
                          f"Computer total: {check_ace(computer_cards)} Players total: {check_ace(player_cards)}")
        disp_record()
        QtGui.QGuiApplication.processEvents()
        if chip == 0:
            x = QMessageBox()
            x.setWindowTitle("Game Over !!!")
            x.setText(f"You have run out of chips !!! Game Over !!! \n High Score : {highscore}")
            x.exec()
            store_highscore()
            sys.exit()
        playing = False


    def dealer_lose(computer_cards, player_cards):
        global playing, chip, highscore
        print_all(computer_cards, player_cards)
        chip += bet
        table['Player'] += 1
        ui.result.setText(f"Player has won!!! Computer has lost!  Total chips remaining: {chip}\n"
                          f"Computer total: {check_ace(computer_cards)} Players total: {check_ace(player_cards)}")
        disp_record()
        highscore = max(highscore, chip)
        playing = False


    def disp_record():
        record = ""
        cw = table['Computer'] * 100 / (table['Computer'] + table['Player'])
        pw = table['Player'] * 100 / (table['Computer'] + table['Player'])
        perc = {'Computer': str(math.trunc(cw)) + "%", 'Player': str(math.trunc(pw)) + "%"}
        for key in table:
            record += key + " : " + str(table[key]) + "\t"
        record += "\n"
        for key in perc:
            record += key + " : " + str(perc[key]) + "   "
        ui.win.setText(record)

    def run_logic():
        deck = Deck()
        deck.shuffle()

        computer_deck = []
        player_deck = []

        com_cards = []
        player_cards = []

        for x in range(26):
            computer_deck.append(deck.remove_one())
            player_deck.append(deck.remove_one())

        com_cards.extend([computer_deck.pop(0), computer_deck.pop(1)])
        player_cards.extend([player_deck.pop(0), player_deck.pop(1)])

        print_some(com_cards, player_cards)
        hit_stand(com_cards, player_cards, player_deck)

        if playing:
            play_dealer(com_cards, player_cards, computer_deck)


    def chip_bet():
        global playing
        playing = True
        ui.label1.setPixmap(QPixmap())
        ui.label2.setPixmap(QPixmap())
        ui.label3.setPixmap(QPixmap())
        ui.label4.setPixmap(QPixmap())
        ui.label5.setPixmap(QPixmap())
        ui.label6.setPixmap(QPixmap())
        ui.label7.setPixmap(QPixmap())
        ui.label8.setPixmap(QPixmap())
        ui.label9.setPixmap(QPixmap())
        ui.label10.setPixmap(QPixmap())

        while True:
            global chip
            bet, okay = QInputDialog.getInt(None, f"Hello - Chips remaining {chip}",
                                            f"Welcome to Blackjack please enter your bet (1 to {chip}): ", 1, 1, chip, 1)
            if bet <= chip and okay:
                ui.result.setText("")
                return bet

    while True:
        bet = chip_bet()
        run_logic()
        text, ok = QInputDialog.getText(None, "Hello", "Do you want to continue to play BlackJack (y or n):")
        if text == "n" and ok:
            ui.result.setText(f"Game Over !!! Your High Score is {highscore}")
            store_highscore()
            break

    app.exec()
