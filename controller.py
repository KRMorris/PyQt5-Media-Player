
import sys
import MainWindow
from mediaplayer import Player
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.Qt import Qt


class Controller(Player, MainWindow.Ui_MainWindow):
    def __init__(self):
        # super().__init__(self)
        self.ex = MainWindow.Ui_MainWindow

    def nav(self, gui):

        # gui.pushButton_mediaplayer.clicked.connect(lambda:gui.stackedWidget.setCurrentIndex(2))#mediaplayer
        gui.pushButtonSongMenu.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(1))  # music
        gui.pushButtonSongs.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(3))  # songs
        gui.listView.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(6))  # player2
        gui.pushButtonPlaylts.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(4))  # playlists
        gui.pushButtonAlbums.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(4))  # Albums
        gui.pushButtonGenre.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(4))  # Genre
        # gui.pushButton_revCam.clicked.connect(lambda: gui.stackedWidget.setCurrentIndex(5))#camera/webview
        gui.pushButtonVideoMenu.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(7))  # video player
        gui.pushButtonSongs.clicked.connect(lambda i: Player.orgUi(i, gui))

        # Back buttons
        gui.pushButtonBack_songs.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(2))  # from songs
        gui.pushButtonBack_music.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(1))
        gui.pushButtonBack_MP.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(0))
        gui.pushButton_back_list_playlist.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(1))
        gui.pushButtonBack_music_2.clicked.connect(
            lambda: gui.stackedWidget.setCurrentIndex(4))
        #gui.pushButtonBack_web.clicked.connect(lambda: gui.stackedWidget.setCurrentIndex(0))

        # display album, genre or playlist
        # swich controls to respective widgets(player1 and player2) qlabel etc
        # args:button, gui
        gui.pushButtonPlaylts.clicked.connect(
            lambda i: Player.setAGPPath(i, gui.pushButtonPlaylts, gui))
        gui.pushButtonAlbums.clicked.connect(
            lambda i: Player.setAGPPath(i, gui.pushButtonAlbums, gui))
        gui.pushButtonGenre.clicked.connect(
            lambda i: Player.setAGPPath(i, gui.pushButtonGenre, gui))

        gui.pushButtonPlaylts.clicked.connect(
            lambda i: Player.playlist_model(i, gui))
        # Misc
        #gui.pushButton_mediaplayer.clicked.connect(lambda i: Controller.tshot(i, Player))
        gui.pushButtonSongMenu.clicked.connect(
            lambda i: Controller.tshot(Player))
        #  gui.pushButton_mediaplayer.clicked.connect(Window.loadMP)
        gui.pushButtonVideoMenu.clicked.connect(Player.videoPlayer)

    def currentIn(i, self):
        print("Current Index:{}".format(self.stackedWidget.currentIndex()))

    def tshot(pl):
        print("tshot")
        pl.snap_timer.start()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        # Call navigation
        controller = Controller()
        controller.nav(self.ui)
        # Call player
        Player(self.ui)

    def keyPressEvent(self, event):
        print("key press")
        print(event.text())
        if event.key() == Qt.Key_Space:
            print("Space")

    def rObv():
        print("SINGLESHOT!")

    def loadMP(self):
        Player(self.ui)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # sdir=StartObserver()
    MainWindow = Window()
    # sdir.run()
    MainWindow.show()
    sys.exit(app.exec_())
