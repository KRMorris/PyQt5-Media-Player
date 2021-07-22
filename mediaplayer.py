#import sys, traceback
import os
import platform
#import random
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import QTimer
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
import MainWindow
from vlcInst import PlaylistInst
#import time
#import subprocess
#from functools import partial
import vlc
#import itertools
import logging
#from logging import exception
from playlist_creator_parser import PlaylistCP
from dirwatcher import StartObserver


class Player(QtWidgets.QWidget, MainWindow.Ui_MainWindow):

    # ToDo: view only display correct file type (mp3 etc)
    # ToDo: shuffle highlight get index from medialistplayer and compare to QModelIndex like QModelIndex index=
    # ToDo: Function/ui to add songs, sync (from external device?)
    # Todo: newmodel=Player.model newmodel in highlight
    # Todo: vlc mrl cant be found error handling
    def __init__(self, gui, *args, **kwargs):
        #super(Player, self).__init__(*args, **kwargs)
        #threadpool = QThreadPool()
        Player.logf = open("error.log", "w+")

        # win.currentTrackTime=0
        Player.currentTrackTime = 0
        Player.is_paused = False
        Player.lst = []
        Player.NXT = False
        Player.is_shuffle = False
        # Set up vlc
        Player.ext_list = ['.mp4', '.wmv', '.mp3']  # music
        Player.path = 'media/music'
        #Player.plstPath = 'media/playlist/'
        # vlc Playlist instance
        Player.pli = PlaylistInst()
        # Playlist creator
        Player.dis_plst = PlaylistCP()
        # watchdog
        Player.dir_snap = StartObserver()

        self.vlen = 0
        self.vidCount = 0

        Player.org_ui = True
        Player.currentUi = gui.listViewSongs
        Player.current_nowplaying = gui.nowplaying_label
        Player.current_slider = gui.positionSlider

        # class wide uri lisr
        Player.uri_lst = []

        # fpi
        Player.list_player = Player.pli.fileToPlaylist(
            Player.path, Player.ext_list)
        Player.ref_to_list_player = Player.list_player
        # Media Player Main view
        Player.model = QtWidgets.QFileSystemModel()
        Player.model.setRootPath(os.getcwd())
        Player.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        gui.listViewSongs.setModel(Player.model)
        # "music"))#os.getcwd()+"\music"))
        gui.listViewSongs.setRootIndex(Player.model.index(Player.path))
        Player.perIdx = Player.model.persistentIndexList()

        gui.listViewSongs.clicked[QtCore.QModelIndex].connect(Player.on_click)
        gui.listViewSongs_2.clicked[QtCore.QModelIndex].connect(
            Player.on_click)
        gui.listViewSongs.clicked[QtCore.QModelIndex].connect(
            lambda i: Player.on_test(i, gui))
        # Media Player - Songs Button
        gui.pushButtonPlayPause.clicked.connect(
            Player.playpause)  # vlcmusic.playpause)
        gui.pushButton_Prev.clicked.connect(lambda: Player.prev(gui))
        gui.pushButton_Next.clicked.connect(lambda: Player.next(gui))
        # self.pushButtonLoop.setCheckable(True)
        gui.pushButtonLoop.clicked.connect(
            Player.loop)  # (Player.loop)#partial
        gui.pushButtonShuffle.clicked.connect(Player.shuffle)  # test

        # Media Player - Songs Button
        gui.pushButtonPlayPause_2.clicked.connect(
            Player.playpause)  # vlcmusic.playpause)
        gui.pushButton_Prev_2.clicked.connect(lambda: Player.prev(gui))
        gui.pushButton_Next_2.clicked.connect(lambda: Player.next(gui))
        # self.pushButtonLoop.setCheckable(True)
        gui.pushButtonLoop_2.clicked.connect(
            Player.loop)  # (Player.loop)#partial
        gui.pushButtonShuffle_2.clicked.connect(Player.shuffle)  # test

        # Media Player - Playlist
        # List view onClick
        # Player.testin(i,self))
        gui.listView.clicked.connect(lambda i: Player.displayPlaylist(i, gui))
        gui.listView.clicked.connect(lambda i: Player.currentIn(i, gui))
        #self.listViewSongs_2.clicked.connect(lambda i:Player.currentIn(i,self))

        # Sliders
        # self.positionSlider.setFocusPolicy(Qt.NoFocus)
        gui.positionSlider.sliderMoved.connect(lambda: Player.setPosition(gui))
        gui.positionSlider.sliderPressed.connect(
            lambda: Player.setPosition(gui))
        gui.positionSlider_2.sliderMoved.connect(
            lambda: Player.setPosition(gui))
        gui.positionSlider_2.sliderPressed.connect(
            lambda: Player.setPosition(gui))
        # QTimer
        Player.timer = QTimer()  # Player.startTimer(
        Player.timer.setInterval(1000)  # 1000
        Player.timer.timeout.connect(lambda: Player.updateUI(gui))

        Player.snap_timer = QTimer()
        Player.snap_timer.setInterval(100)  # 30000)
        Player.snap_timer.timeout.connect(Player.dir_snap.dir_snap)

        #Player.videoframe = gui.videoframe
        # gui.videofram
        # Player.dir_snap.run()

        # VLC Event Manager
        Player.lp_events = Player.list_player.event_manager()
        Player.lp_events.event_attach(
            vlc.EventType.MediaListPlayerNextItemSet, lambda _: Player.nextSongUI(gui))
        # MediaPlayerEndReached
        #self.vp_events = self.video_lst.event_manager()
        #self.vp_events.event_attach(vlc.EventType.MediaPlayerEndReached, lambda _:Player.videoPlayer(gui))

    def on_test(self, ui):
        '''itms=self.listViewSongs.selectedIndexes()
        for data in itms:
            print(data.row())'''
        print("---------]]]")
        print(self)
        print("row:{} row{} col{}".format(
            Player.model.fileName(self), self.row(), self.column()))
        a = Player.model.index(
            "music\\2038[kb]061_trumpety-organy-swing.mp3", 0)
        print(a)
        print(a.row())
        print(ui.listViewSongs.rectForIndex(a))
        print(a.column())
        print(Player.perIdx)

    def testin(x, self):
        print(x.data())
        entries = ['one', 'two', 'three']

        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def playpause():
        # ToDo: add another cond isPaused
        """Toggle play/pause status
        """
        if Player.list_player.is_playing():
            Player.list_player.pause()
            # playbutton.setText("Play")
            print("Play")
            #isPaused = True
        else:
            if Player.list_player.play() == -1:
                # selectFile()
                print("can't play")
                return
            Player.list_player.play()

            # playbutton.setText("Pause")
            # timer.start()
            Player.timer.start()
            print("pause")
            #isPaused = False
    # Previous song

    def prev(self):
        Player.NXT = False
        Player.list_player.previous()
        Player.prevSongHl(self)

    def next(self):
        Player.list_player.next()

    def rel():
        Player.list_player.release()

    def test():
        # MainWindow.__init__()
        pass

    @QtCore.pyqtSlot()
    def updateUI(self):

        # Player.list_player.get_media_player().get_media().get_meta(0)#Title
        # Player.list_player.get_media_player().get_media().get_meta(1)#Artist ##4-Album ##8-Year
        # index_of_item
        # print("########################call update ui#################################")
        """updates the user interface"""
        try:

            # setting the slider to the desired position
            Player.current_slider.setValue(
                Player.list_player.get_media_player().get_position() * 100.0)
            #self.positionSlider_2.setValue(Player.list_player.get_media_player().get_position() * 100.0)
            # get current time
            Player.currentTrackTime = Player.list_player.get_media_player().get_time()
            # convert to h:m:s
            # Player.list_player.get_media_player().get_time())
            conv = Player.hms_conversion(self, Player.currentTrackTime)
            # print(conv)

            # Player.list_player.get_media_player().get_time()))
            Player.current_labelMediaTime.setText(str(conv))
            # ToDO try-catch / error check
            # Player.list_player.get_media_player().get_media().get_meta(1)
            artist = Player.pli.getArtist(Player.list_player)
            title = Player.pli.getTitle(Player.list_player)
            if artist == "":
                Player.current_nowplaying.setText(str(title))
            else:
                Player.current_nowplaying.setText(str(artist +
                                                      " - "+title))
        except Exception as e:
            print("Error can't read file info")
            logging.exception("Error can't read file meta %s", e)
            print(e)

        if not Player.list_player.is_playing():

            Player.timer.stop()
            print('stop')
            '''if not Player.is_paused():
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it

                Player.list_player.stop()
                print("if not")'''
            pass
        # print("{}:".format(Player.list_player.get_media_player().get_media().get_mrl()))#.index_of_item("2038[kb]061_trumpety-organy-swing.mp3"))

    @QtCore.pyqtSlot('QItemSelection')
    def nextSongUI(self):
        #global NXT
        print("ws0ng ui")
        # print(Player.list_player.get_media_player().get_media().get_mrl())
        # print(Player.model.index(Player.list_player.get_media_player().get_media().get_mrl(),0))
        if Player.NXT == False:  # dont move on first next
            Player.NXT = True
        elif Player.is_shuffle == True:
            print("----------------Shuffle--------")

            index = Player.model.index(
                Player.list_player.get_media_player().get_media().get_mrl(), 0)
            print(index)
            Player.currentUi.selectionModel().select(
                index, QItemSelectionModel.ClearAndSelect)
            Player.currentUi.selectionModel().setCurrentIndex(
                index, QtCore.QItemSelectionModel.SelectCurrent)
        else:
            index = Player.currentUi.moveCursor(
                QtWidgets.QAbstractItemView.MoveNext, QtCore.Qt.NoModifier)
            Player.currentUi.selectionModel().setCurrentIndex(
                index, QtCore.QItemSelectionModel.SelectCurrent)

    def prevSongHl(self):  # highlight
        index = Player.currentUi.moveCursor(
            QtWidgets.QAbstractItemView.MovePrevious, QtCore.Qt.NoModifier)
        Player.currentUi.selectionModel().setCurrentIndex(
            index, QtCore.QItemSelectionModel.SelectCurrent)

    def hms_conversion(self, ms):
        ms = int(ms)
        if ms < 60000:
            sec = int((ms/1000) % 60)
            return("%d:%d:%02d" % (0, 0, sec))
        else:
            sec = int((ms/1000) % 60)
            mins = int((ms/(1000*60)) % 60)
            hr = int((ms/(1000*60*60)) % 24)
            return("%d:%d:%02d" % (hr, mins, sec))

    def hms_conversion2(self, ms):
        ms = int(ms)
        if ms < 60000:
            sec = int((ms/1000) % 60)
            return("%d:%d:%d" % (0, 0, sec))
        else:
            sec = int((ms/1000) % 60)
            mins = int((ms/(1000*60)) % 60)
            hr = int((ms/(1000*60*60)) % 24)
            return(hr, mins, sec)

    # @QtCore.pyqtSlot(bool)
    # Toggle play_back mode
    def loop(self):  # toggle):
        global a
        global b

        if self == True:  # .isChecked():
            if a == 0:
                Player.list_player.set_playback_mode(vlc.PlaybackMode.loop)
                print(self)
                a = a+1
                print("loop")
            elif a == 2:
                Player.list_player.set_playback_mode(vlc.PlaybackMode.default)
                a = 0
                print("default")
        elif self == False and a == 1:
            # change icon
            Player.list_player.set_playback_mode(vlc.PlaybackMode.repeat)
            print("repeat")
            print(self)
            print(a)
            a = 2
        elif self == False and a == 0:
            Player.list_player.set_playback_mode(vlc.PlaybackMode.loop)
            print(self)
            a = a+1
            print("loop fal")
        print(a)

    # ToDo improve shuffle
    @QtCore.pyqtSlot()
    def shuffle(self):
        # ToDo if not playing mrl
        print("shuffle!")
        cp = Player.list_player.get_media_player(
        ).get_media().get_mrl()  # currentplayingTitle
        Player.currentTrackTimeShuf = Player.list_player.get_media_player().get_time()
        # Toggle shuffle
        if Player.is_shuffle == False:
            Player.is_shuffle = True
            # wait then play
            Player.stop()  # fix
            # Player.rel()
            # Player.pli.pathToPlaylist(Player.pli.shuffle(Player.pli.fileToPath(Player.path, Player.ext_list)))
            lp = Player.pli.pathToPlaylist(Player.pli.shuffle1(
                Player.pli.fileToPath(Player.path, Player.ext_list), cp, Player.path))
            Player.list_player = lp
            Player.list_player.play()
            # if not found, check index?
            #
            # seek to current time Player.currentTrackTime
            Player.list_player.get_media_player().set_time(Player.currentTrackTimeShuf)

        else:
            Player.is_shuffle = False
            # call default media 0,1,2....
            #
            Player.stop()
            print("shuffle off")
            title = Player.pli.getTitle(Player.list_player)
            # unshuffle(self, url, data, path)
            unshuff = Player.pli.unshuffle(title, path, ext_list)
            Player.list_player = unshuff[0]
            indx = unshuff[1]
            Player.list_player.play_item_at_index(indx)
            # seek to current time Player.currentTrackTime
            Player.list_player.get_media_player().set_time(Player.currentTrackTimeShuf)

    def stop():
        Player.list_player.stop()

    # Song select/click
    def on_click(self):
        try:
            Player.NXT = False
            global tog
            global a
            a = 0
            print("w")
            medl = Player.pli.getMediaList()
            print(self.row())
            # match .data with list_player index
            print("DATA:{} MEDL:{}".format(self.data(), medl))
            sIndx = Player.pli.searchIndex(medl, self.data(), Player.path)
            print("S INDEX:{}".format(sIndx))
            if Player.uri_lst != [] and Player.org_ui == False:
                print("Player.uri_lst !=[] and Player.org_ui == False")
                Player.list_player.stop()
                Player.list_player = Player.pli.pathToPlaylist(Player.uri_lst)
            if Player.org_ui == True:
                if Player.list_player.is_playing():
                    Player.list_player.stop()
                    # list_player from file sys
                    Player.list_player = Player.ref_to_list_player
            try:
                if Player.is_shuffle:
                    print("on_click shuffle")
                    if Player.list_player.is_playing():
                        Player.list_player.stop()
                        Player.list_player.play_item_at_index(sIndx)
                        #    Player.pli.searchIndex(medl,self.data()))
                    else:
                        Player.list_player.play_item_at_index(sIndx)
                        #    Player.pli.searchIndex(medl, self.data()))
                        print("ELSE IS SHUFFLE")
                else:

                    if Player.list_player.is_playing():
                        Player.list_player.stop()
                        print("mml")
                        Player.list_player.play_item_at_index(self.row())
                    else:
                        Player.list_player.play_item_at_index(self.row())
            except Exception as e:
                logging.exception("mpl Unexpected exception! %s", e)
                # Player.logf.write(str(e))
                # Player.logf.close()
        except VLCException as ex:
            print("VLC Error:{}".format(ex))
        Player.timer.start()

    # slider position
    def setPosition(self):
        Player.timer.stop()
        Player.list_player.get_media_player().set_position(
            self.positionSlider.value()/100.0)
        # player 2
        Player.list_player.get_media_player().set_position(
            self.positionSlider_2.value() / 100.0)
        Player.timer.start()

    #
    # Playlist model: load playlist,genre or album
    #
    def playlist_model(self, ui):

        try:

            Player.logf = open("error.log", "w+")
            Player.plst_model = QtWidgets.QFileSystemModel()
            Player.plst_model.setRootPath(os.getcwd())
            Player.plst_model.setFilter(
                QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
            ui.listView.setModel(Player.plst_model)
            # "media/playlist"))  # os.getcwd()+"\music"))
            ui.listView.setRootIndex(Player.plst_model.index(Player.plstPath))
            ui.listView.setViewMode(QListView.IconMode)
            # self.list_playlists

        except Exception as e:
            logging.exception("mpl Unexpected exception! %s", e)

    # Add content of playlist to listview
    def displayPlaylist(self, ui):

        try:
            uri = Player.dis_plst.getUri(self.data(), Player.plstPath)
            print(uri)
            # Player.list_player=Player.pli.pathToPlaylist(uri)
            Player.uri_lst = uri
            model = QtGui.QStandardItemModel()
            # ui.listViewPlC.setModel(model)
            ui.listViewSongs_2.setModel(model)
            # Split uri
            uri = [Player.pli.splitUrl(None, i) for i in uri]

            for i in uri:
                item = QtGui.QStandardItem(i)
                model.appendRow(item)
        except Exception as e:
            logging.exception("mpl Unexpected exception! %s", e)

        # Player.list_player.play()
    # ?
    def setPlayerType(self, pt):
        Player.pt = pt
    # Set current mediainfo to media player 2

    def currentIn(i, self):
        Player.org_ui = False
        print("Current Index:{}".format(self.stackedWidget.currentIndex()))
        Player.currentUi = self.listViewSongs_2
        Player.current_nowplaying = self.nowplaying_label_2
        Player.current_slider = self.positionSlider_2
        Player.current_labelMediaTime = self.labelMediaTime_2
    # base state media player ui, change media info to mediaplayer 1

    def orgUi(i, self):
        print("orgUi")
        # Check if original player is in view
        Player.org_ui = True
        Player.currentUi = self.listViewSongs
        Player.current_nowplaying = self.nowplaying_label
        Player.current_slider = self.positionSlider
        Player.current_labelMediaTime = self.labelMediaTime

    def setAGPPath(self, button, ui):

        if button.text() == 'Album':
            print("album......")
            Player.plstPath = 'media/album/'
            Player.playlist_model(self, ui)
        elif button.text() == 'Genre':
            print("genre")
            Player.plstPath = 'media/genre/'
            Player.playlist_model(self, ui)
        elif button.text() == 'Playlist':
            Player.plstPath = 'media/playlist/'
            Player.playlist_model(self, ui)
        # print(button.text())

    #############################################
    ##############VIDEO PLAYER###
    ##############################################
    # Add video to frame
    def videoPlayer(self):
        # pushButtonVideoMenu
        # add media to player list videolsr
        # r'C:\Users\Ross\Videos\gym\declinebench.mp4'
        vpath = r'C:\Users\Ross\Videos\gym'
        vext = ['.avi', '.mp4']
        # video_lst=Player.pli.fileToPlaylist(vpath,vext)
        video_lst = self.vMediapl  # Player.pli.vidtest(vpath,vext)
        #
        vt = video_lst.get_media_player().get_media()
        if platform.system() == 'Linux':
            video_lst.set_xwindow(int(Player.videoframe.winId()))

        elif platform.system() == 'Windows':
            video_lst.set_hwnd(int(Player.videoframe.winId()))

        video_lst.play()
    # Get files from folder, add to list(vlist)

    def setupVideoPlayer(self):
        # ml=vl.media_list
        # ml.count()
        # mediap=vlc.MediaPlayer()
        # mind=ml.item_at_index(1)  mind.get_mrl()  med=vlc.Media(mind.get_mrl()) mediap.set_media(med)  mediap.play()
        # MediaPlayerEndReached
        # vid count
        #
        #video_lst = Player.pli.fileToPlaylist(vpath, vext)
        self.vlist = Player.pli.setVideoLst(vpath, vext)
        # get len (mlist)
        self.vlen = vlist.count()
        #vlist_ind = vlist.item_at_index(self.vcount)
        # self.vmrl=vlist_ind.get_mrl()

    def vMedia(self):
        vlist_ind = self.vlist.item_at_index(self.vindx)
        self.vmrl = vlist_ind.get_mrl()
        self.vMediapl = vlc.MediaPlayer()
        self.vMediapl.set_media(self.vmrl)
        # return self.vMediapl

    def nextVid(self):
        self.vindx = self.vindx+1
        self.vMedia()
