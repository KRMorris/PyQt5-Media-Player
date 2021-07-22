import urllib
import vlc
import os
import random
from urllib import parse
import re

#ext_list = ['.mp4','.wmv', '.mp3']#music
#ext_list = ['.mkv', '.avi', '.flv', '.mov', '.wmv', '.vob','.mpg','.3gp']#vid
#path=music
class PlaylistInst():
        #self.path=path
        #self.ext_list=ext_list
        def __init__(self):
            self.instance = vlc.Instance('--play-and-exit')

        #ToDo: improve dir search
        def fileToPlaylist(self,path,ext_list):
            #ext_list = ['.mp4','.wmv', '.mp3']
            url1=path#"C:\\Users\\Ross\\Google Drive\\Car\\app\\GUI\\Infotainment\\"+path
            url=[]
            for file in os.listdir(url1):
                if file.endswith(tuple(ext_list)):
                    url.append(os.path.join(url1,file))
            print(url)
            url.sort()
            self.media_list = self.instance.media_list_new(url)
            list_player = self.instance.media_list_player_new()
            list_player.set_media_list(self.media_list)
            return list_player

        def fileToPlaylist11(self,path,ext_list):
            media_player =vlc.MediaListPlayer()
            player=vlc.Instance()
            media_list=vlc.MediaList()
            #ext_list = ['.mp4','.wmv', '.mp3']
            url1=path
            url=[]
            #C:\Users\Ross\Google Drive\Car\app\
            for file in os.listdir(url1):
                if file.endswith(tuple(ext_list)):
                    url.append(os.path.join(url1,file))
                    media1=player.media_new(os.path.join(url1,file))
                    media_list.add_media(media1)
            print(url)

            Media_list = self.instance.media_list_new(url)
            list_player = self.instance.media_list_player_new()
            list_player.set_media_list(Media_list)
            #return list_player
            print(media_list.item_at_index(0))
            media_player.set_media_list(media_list)
            return (media_player,media_list)

        def vidtest(self,path,ext_list):
            # creating vlc media player object
            media_player = vlc.MediaPlayer()

            # media object
            media = vlc.Media(path)

            # setting media to the media player
            media_player.set_media(media)
            return media_player

        def setVideoLst(self, path, ext_list):
            url=self.fileToPath(path, ext_list)
            url.sort()
            vid_list = self.instance.media_list_new(url)
            return vid_list

        #Search dir and return path to files
        def fileToPath(self,path,ext_list):
            #ext_list = ['.mp4','.wmv', '.mp3']
            url1=path#"C:\\Users\\Ross\\Google Drive\\Car\\app\\GUI\\Infotainment\\"+path
            url=[]
            #C:\Users\Ross\Google Drive\Car\app\
            for file in os.listdir(url1):
                if file.endswith(tuple(ext_list)):
                    url.append(os.path.join(url1,file))
            return url

        #Add url to new medialistplayer
        def pathToPlaylist(self,url):
                self.media_list = self.instance.media_list_new(url)
                list_player = self.instance.media_list_player_new()
                list_player.set_media_list(self.media_list)
                #list_player.play()
                return list_player
        #
        #ToDo shuffle everything but currently playing song or search for faster way to shuffle list
        #
        def shuffle(self,url):#search for faster way to shuffle list
                random.shuffle(url)
                return url

        def shuffle1(self,url,data,path):
            #ToDo stop(),setlist,insert current playing at 0,play
            random.shuffle(url)
            pa = self.splitUrl(path,data)
            sl="\\"

            print(pa)
            if url[0]==pa:#data:#check if item in first index match data
                #url.pop(0)
                #url.insert(0,path+data)
                print('url[0]==data')
                #return url
            elif url[1]==pa:
                url.pop(1)
                url.insert(0, data)
                print('url[1] == data')

            else:
                url.insert(0, data)#insert path at index 0
                #search n remove similar occurence?no..what if same song added twice to list?
                print("else insert")
            return url

        def splitUrl(self,path,data):#getFname
            upurl = urllib.parse.unquote(data)
            res = re.split("/", upurl)
            data = res[-1]
            print(data)
            return data

        def unshuffle(self,title,path,ext_list):
            #ToDO:
            #reinitialize instance/exit
            #play music from current index/item onwards
            #get index?
            #idx=self.searchIndex(mpl, title)
            list_player = self.fileToPlaylist(path, ext_list)
            #getmpl
            idx = self.searchIndex(self.getMediaList(), title,path)
            #list_player.play_item_at_index(idx)
            return list_player,idx

        def getArtist(self,player):
            artist=player.get_media_player().get_media().get_meta(1)
            if artist is None:
                artist=""
            return artist

        def getTitle(self,player):
            title=player.get_media_player().get_media().get_meta(0)
            if title is None:
                title=""
            return title
        #ToDo.....thought process-find index base on title(on_click listview), return index,play song from that index DONE
        #lv.data
        def searchIndex(self,mpl, title,path):
            for i in range(mpl.count()):
                z = mpl.item_at_index(i).get_mrl()
                z=self.splitUrl(path,z)
                print(z+"\n")
                if z == title:
                    print("found:{} index:{}".format(z, i))#index
                    return i

        def getMediaList(self):
            return self.media_list

        def mediaListCheck(self,mlp,ml):
            if ml==None:
                #time.sleep(1)
                self.getTitle()
                return self.getMediaList()
            else:
                return ml

        def album(self):
            from itertools import groupby
            l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 1, 2, 1]
            l.sort()
            [list(j) for i, j in groupby(l)]
            # save group to diff plst