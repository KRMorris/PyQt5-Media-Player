# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setEnabled(False)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget.addWidget(self.widget_2)
        self.musicplayer_menu = QtWidgets.QWidget()
        self.musicplayer_menu.setObjectName("musicplayer_menu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.musicplayer_menu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonBack_songs = QtWidgets.QPushButton(self.musicplayer_menu)
        self.pushButtonBack_songs.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBack_songs.setIcon(icon)
        self.pushButtonBack_songs.setFlat(True)
        self.pushButtonBack_songs.setObjectName("pushButtonBack_songs")
        self.gridLayout_2.addWidget(self.pushButtonBack_songs, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonSongs = QtWidgets.QPushButton(self.musicplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSongs.sizePolicy().hasHeightForWidth())
        self.pushButtonSongs.setSizePolicy(sizePolicy)
        self.pushButtonSongs.setObjectName("pushButtonSongs")
        self.horizontalLayout_6.addWidget(self.pushButtonSongs)
        self.pushButtonPlaylts = QtWidgets.QPushButton(self.musicplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlaylts.sizePolicy().hasHeightForWidth())
        self.pushButtonPlaylts.setSizePolicy(sizePolicy)
        self.pushButtonPlaylts.setFlat(False)
        self.pushButtonPlaylts.setObjectName("pushButtonPlaylts")
        self.horizontalLayout_6.addWidget(self.pushButtonPlaylts)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButtonAlbums = QtWidgets.QPushButton(self.musicplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAlbums.sizePolicy().hasHeightForWidth())
        self.pushButtonAlbums.setSizePolicy(sizePolicy)
        self.pushButtonAlbums.setObjectName("pushButtonAlbums")
        self.horizontalLayout_7.addWidget(self.pushButtonAlbums)
        self.pushButtonGenre = QtWidgets.QPushButton(self.musicplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGenre.sizePolicy().hasHeightForWidth())
        self.pushButtonGenre.setSizePolicy(sizePolicy)
        self.pushButtonGenre.setObjectName("pushButtonGenre")
        self.horizontalLayout_7.addWidget(self.pushButtonGenre)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.musicplayer_menu)
        self.mediaplayer_menu = QtWidgets.QWidget()
        self.mediaplayer_menu.setObjectName("mediaplayer_menu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mediaplayer_menu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButtonSongMenu = QtWidgets.QPushButton(self.mediaplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSongMenu.sizePolicy().hasHeightForWidth())
        self.pushButtonSongMenu.setSizePolicy(sizePolicy)
        self.pushButtonSongMenu.setObjectName("pushButtonSongMenu")
        self.horizontalLayout_14.addWidget(self.pushButtonSongMenu)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButtonVideoMenu = QtWidgets.QPushButton(self.mediaplayer_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonVideoMenu.sizePolicy().hasHeightForWidth())
        self.pushButtonVideoMenu.setSizePolicy(sizePolicy)
        self.pushButtonVideoMenu.setObjectName("pushButtonVideoMenu")
        self.horizontalLayout_15.addWidget(self.pushButtonVideoMenu)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.pushButtonBack_MP = QtWidgets.QPushButton(self.mediaplayer_menu)
        self.pushButtonBack_MP.setEnabled(False)
        self.pushButtonBack_MP.setText("")
        self.pushButtonBack_MP.setFlat(True)
        self.pushButtonBack_MP.setObjectName("pushButtonBack_MP")
        self.gridLayout_3.addWidget(self.pushButtonBack_MP, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.mediaplayer_menu)
        self.musicplayer_ui_main = QtWidgets.QWidget()
        self.musicplayer_ui_main.setObjectName("musicplayer_ui_main")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.musicplayer_ui_main)
        self.gridLayout_11.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButtonBack_music = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButtonBack_music.setText("")
        self.pushButtonBack_music.setIcon(icon)
        self.pushButtonBack_music.setFlat(True)
        self.pushButtonBack_music.setObjectName("pushButtonBack_music")
        self.gridLayout_9.addWidget(self.pushButtonBack_music, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.nowplaying_label = QtWidgets.QLabel(self.musicplayer_ui_main)
        self.nowplaying_label.setText("")
        self.nowplaying_label.setObjectName("nowplaying_label")
        self.gridLayout_9.addWidget(self.nowplaying_label, 1, 0, 1, 1)
        self.listViewSongs = QtWidgets.QListView(self.musicplayer_ui_main)
        self.listViewSongs.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewSongs.setObjectName("listViewSongs")
        self.gridLayout_9.addWidget(self.listViewSongs, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.positionSlider = QtWidgets.QSlider(self.musicplayer_ui_main)
        self.positionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.positionSlider.setObjectName("positionSlider")
        self.horizontalLayout_8.addWidget(self.positionSlider)
        self.labelMediaTime = QtWidgets.QLabel(self.musicplayer_ui_main)
        self.labelMediaTime.setObjectName("labelMediaTime")
        self.horizontalLayout_8.addWidget(self.labelMediaTime)
        self.gridLayout_9.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_Prev = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButton_Prev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/prev.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Prev.setIcon(icon1)
        self.pushButton_Prev.setObjectName("pushButton_Prev")
        self.horizontalLayout_21.addWidget(self.pushButton_Prev)
        self.pushButtonPlayPause = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButtonPlayPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonPlayPause.setIcon(icon2)
        self.pushButtonPlayPause.setObjectName("pushButtonPlayPause")
        self.horizontalLayout_21.addWidget(self.pushButtonPlayPause)
        self.pushButton_Next = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButton_Next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Next.setIcon(icon3)
        self.pushButton_Next.setObjectName("pushButton_Next")
        self.horizontalLayout_21.addWidget(self.pushButton_Next)
        self.pushButtonLoop = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButtonLoop.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/loop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLoop.setIcon(icon4)
        self.pushButtonLoop.setObjectName("pushButtonLoop")
        self.horizontalLayout_21.addWidget(self.pushButtonLoop)
        self.pushButtonShuffle = QtWidgets.QPushButton(self.musicplayer_ui_main)
        self.pushButtonShuffle.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/shuffle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonShuffle.setIcon(icon5)
        self.pushButtonShuffle.setObjectName("pushButtonShuffle")
        self.horizontalLayout_21.addWidget(self.pushButtonShuffle)
        self.volSlider = QtWidgets.QSlider(self.musicplayer_ui_main)
        self.volSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volSlider.setObjectName("volSlider")
        self.horizontalLayout_21.addWidget(self.volSlider, 0, QtCore.Qt.AlignRight)
        self.gridLayout_9.addLayout(self.horizontalLayout_21, 4, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.musicplayer_ui_main)
        self.agp_ui = QtWidgets.QWidget()
        self.agp_ui.setObjectName("agp_ui")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.agp_ui)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_back_list_playlist = QtWidgets.QPushButton(self.agp_ui)
        self.pushButton_back_list_playlist.setText("")
        self.pushButton_back_list_playlist.setIcon(icon)
        self.pushButton_back_list_playlist.setFlat(True)
        self.pushButton_back_list_playlist.setObjectName("pushButton_back_list_playlist")
        self.gridLayout_10.addWidget(self.pushButton_back_list_playlist, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.listView = QtWidgets.QListView(self.agp_ui)
        self.listView.setIconSize(QtCore.QSize(60, 60))
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setObjectName("listView")
        self.gridLayout_10.addWidget(self.listView, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.agp_ui)
        self.widget = QtWidgets.QWidget()
        self.widget.setEnabled(False)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget.addWidget(self.widget)
        self.musicplayer_ui_sec = QtWidgets.QWidget()
        self.musicplayer_ui_sec.setObjectName("musicplayer_ui_sec")
        self.gridLayout = QtWidgets.QGridLayout(self.musicplayer_ui_sec)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.nowplaying_label_2 = QtWidgets.QLabel(self.musicplayer_ui_sec)
        self.nowplaying_label_2.setText("")
        self.nowplaying_label_2.setObjectName("nowplaying_label_2")
        self.gridLayout_5.addWidget(self.nowplaying_label_2, 1, 0, 1, 1)
        self.listViewSongs_2 = QtWidgets.QListView(self.musicplayer_ui_sec)
        self.listViewSongs_2.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewSongs_2.setObjectName("listViewSongs_2")
        self.gridLayout_5.addWidget(self.listViewSongs_2, 2, 0, 1, 1)
        self.pushButtonBack_music_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButtonBack_music_2.setText("")
        self.pushButtonBack_music_2.setIcon(icon)
        self.pushButtonBack_music_2.setFlat(True)
        self.pushButtonBack_music_2.setObjectName("pushButtonBack_music_2")
        self.gridLayout_5.addWidget(self.pushButtonBack_music_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.pushButton_Prev_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButton_Prev_2.setText("")
        self.pushButton_Prev_2.setIcon(icon1)
        self.pushButton_Prev_2.setObjectName("pushButton_Prev_2")
        self.horizontalLayout_22.addWidget(self.pushButton_Prev_2)
        self.pushButtonPlayPause_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButtonPlayPause_2.setText("")
        self.pushButtonPlayPause_2.setIcon(icon2)
        self.pushButtonPlayPause_2.setObjectName("pushButtonPlayPause_2")
        self.horizontalLayout_22.addWidget(self.pushButtonPlayPause_2)
        self.pushButton_Next_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButton_Next_2.setText("")
        self.pushButton_Next_2.setIcon(icon3)
        self.pushButton_Next_2.setObjectName("pushButton_Next_2")
        self.horizontalLayout_22.addWidget(self.pushButton_Next_2)
        self.pushButtonLoop_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButtonLoop_2.setText("")
        self.pushButtonLoop_2.setIcon(icon4)
        self.pushButtonLoop_2.setObjectName("pushButtonLoop_2")
        self.horizontalLayout_22.addWidget(self.pushButtonLoop_2)
        self.pushButtonShuffle_2 = QtWidgets.QPushButton(self.musicplayer_ui_sec)
        self.pushButtonShuffle_2.setText("")
        self.pushButtonShuffle_2.setIcon(icon5)
        self.pushButtonShuffle_2.setObjectName("pushButtonShuffle_2")
        self.horizontalLayout_22.addWidget(self.pushButtonShuffle_2)
        self.volSlider_2 = QtWidgets.QSlider(self.musicplayer_ui_sec)
        self.volSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.volSlider_2.setObjectName("volSlider_2")
        self.horizontalLayout_22.addWidget(self.volSlider_2, 0, QtCore.Qt.AlignRight)
        self.gridLayout_5.addLayout(self.horizontalLayout_22, 4, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.positionSlider_2 = QtWidgets.QSlider(self.musicplayer_ui_sec)
        self.positionSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.positionSlider_2.setObjectName("positionSlider_2")
        self.horizontalLayout_9.addWidget(self.positionSlider_2)
        self.labelMediaTime_2 = QtWidgets.QLabel(self.musicplayer_ui_sec)
        self.labelMediaTime_2.setObjectName("labelMediaTime_2")
        self.horizontalLayout_9.addWidget(self.labelMediaTime_2)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.musicplayer_ui_sec)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonSongs.setText(_translate("MainWindow", "Songs"))
        self.pushButtonPlaylts.setText(_translate("MainWindow", "Playlist"))
        self.pushButtonAlbums.setText(_translate("MainWindow", "Album"))
        self.pushButtonGenre.setText(_translate("MainWindow", "Genre"))
        self.pushButtonSongMenu.setText(_translate("MainWindow", "Music"))
        self.pushButtonVideoMenu.setText(_translate("MainWindow", "Video"))
        self.labelMediaTime.setText(_translate("MainWindow", "00:00"))
        self.labelMediaTime_2.setText(_translate("MainWindow", "00:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
