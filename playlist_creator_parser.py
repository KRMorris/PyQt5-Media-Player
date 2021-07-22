import xml.etree.ElementTree as xml
from pymediainfo import MediaInfo
import os
import re


class PlaylistCP():  # hdh
    def __init__(self):
        self.srclst = []
        self.path = 'media/playlist/'
        self.cwd = os.getcwd()

    # parse xspf files
    def xspf_parse(self, p_lst):
        self.tree = xml.parse(p_lst)
        self.root = self.tree.getroot()
        text_lst = [x.text for x in self.tree.findall(".//")]
        text_lst = [i for i in text_lst if i != None]
        url = [text_lst[i] for i, s in enumerate(text_lst) if 'file' in s]
        return url

    # parse wpl files
    def wpl_parse(self, p_lst):
        self.tree = xml.parse(p_lst)
        self.root = self.tree.getroot()
        for pl in self.root.iter('media'):
            print(pl.get('src'))
            self.srclst.append(pl.get('src'))
        return self.srclst

    def searchExtention(self, filename):
        return re.compile(r'\b({0})\b'.format(filename), flags=re.IGNORECASE).search

    def getUri(self, pl, path):
        if self.searchExtention('xspf')(pl):
            print('xspf')
            uri = self.xspf_parse(path+pl)
            return uri
        elif self.searchExtention('wpl')(pl):
            print("wpl")
            uri = self.wpl_parse(path+pl)
            return uri

    # Function use to create playlist (xspf)
    def create_playlist(self, paths, title, save_path):
        playlist = Playlist_xspf()

        for path in paths:
            playlist.add_track(path)
            print("create playlist path:"+path)

        playlist_xml = playlist.get_playlist()
        with open(save_path+title+'.xspf', 'w') as mf:
            mf.write(xml.tostring(playlist_xml).decode('utf-8'))

    # Get album name (with mediainfo) from files in path folder, add to dict
    # First run?
    def get_album_meta(self, path):
        # run on another thread or on background
        albumlst = []
        alli = {}
        alli['Unknown'] = {}
        ext_list = ['.mp4', '.wmv', '.mp3']
        for file in os.listdir(path):
            if file.endswith(tuple(ext_list)):
                media_info = MediaInfo.parse(os.path.join(path, file))
                al = media_info.to_data()
                b1 = al.get('tracks')
                b11 = b1[0]
                b2 = b11.get('album')
                if b2 == None:
                    # albumlst.append('Unknown')
                    alli['Unknown'][b11.get('complete_name')] = b11.get(
                        'file_name')
                else:
                    # albumlst.append(b2)
                    abc = self.recursive_lookup(b2, alli)
                    if abc != None:

                        alli[b2][b11.get('complete_name')] = b11.get(
                            'complete_name')
                    else:
                        alli[b2] = {b11.get('complete_name')
                                            : b11.get('complete_name')}
        # print(albumlst)
        # print(alli)
        return alli

    # Search for keys in dictionary
    def recursive_lookup(self, k, d):
        if k in d:
            return d[k]
        for v in d.values():
            if isinstance(v, dict):
                a = self.recursive_lookup(k, v)
                if a is not None:
                    return a
        return None
    # Dictionary as input, search for keys, write to nested data to playlist

    def write_to_playlist(self, d):
        # get key n write to playlist
        print("write_to_playlist")
        albumtrk = []
        dkeys = d.keys()
        klst = [i for i in dkeys]
        for ky in klst:
            for x in d.get(ky):
                print('albumtrk:'+x)
                albumtrk.append('file:///' + x)
            print(";)()")  # write to playlist send ky as name
            self.create_playlist(albumtrk, ky)
            albumtrk = []
    # Todo: CHANGE EDIT PATH SO that is doesn't add working dir to uri with working dir
    # BUG!

    def edit_path(self, uri):
        for i in range(len(uri)):
            uri[i] = ('file:///' + self.cwd+"/"+uri[i]
                      ).replace('\\', '/').replace('./', '/')
        # for i in range(len(uri)):
        #    uri[i] = ('file:///' + os.path.join(uri[i])).replace('\\', '/')
        #print("edit path:{}".format(uri))
        return uri

    ##########################################
    ############BACKGROUND PLAYLIST##########
    ############PROCESSES####################
    #########################################
    # Get list from watchdog and extract meta
    # ag-album or genre string
    def get_album_meta_live(self, lfiles, ag):
        alli = {}
        alli['Unknown'] = {}
        ext_list = ['.mp4', '.wmv', '.mp3']
        for file in lfiles:
            print(file)
            if file.endswith(tuple(ext_list)):
                media_info = MediaInfo.parse(file)
                al = media_info.to_data()
                b1 = al.get('tracks')
                b11 = b1[0]
                b2 = b11.get(ag)  # ('album')
                if b2 == None:
                    # albumlst.append('Unknown')
                    alli['Unknown'][b11.get('complete_name')] = b11.get(
                        'file_name')
                else:
                    # albumlst.append(b2)
                    abc = self.recursive_lookup(b2, alli)
                    print(abc)
                    if abc != None:
                        print('!= None')
                        alli[b2][b11.get('complete_name')] = b11.get(
                            'complete_name')
                    else:
                        alli[b2] = {b11.get('complete_name')
                                            : b11.get('complete_name')}
        # print(albumlst)
        # print(alli)
        return alli

    # Bug:new file not appending to pl
    # bug;when uri already in pl n func run twice
    # e.g file:////home/pi/Documents/media player//home/pi/Documents/media player/media/music/01. Fireworks (Feat. Alicia Keys).mp3
    # Create album/add track to album
    # d-Dictionary uri key/value pair
    def is_newalbum(self, d, path):
        # append to playlist
        # check if file already exist
        # call get album live??
        # append to corresponding playlist
        print("is_new_album")
        path = path  # 'media/album/'
        plst = []
        # list of tracks
        albumtrk = []
        # temporay list of tracks
        albumtrk_temp = []
        # get keys in dict of file paths
        dkeys = d.keys()
        klst = [i for i in dkeys]
        # get playlists from folder(path)
        for file in os.listdir(path):
            if file.endswith(tuple('.xspf')):
                plst.append(file)
        #
        for ky in klst:
            sky = ky+".xspf"
            print(sky)
            # check if playlist exist
            if sky in plst:
                print("IF plst")
                # get files
                # write
                uri = self.getUri(sky, path)
                print("After getUri{}".format(uri))
                albumtrk = uri
                print("####After:{}".format(albumtrk))
                if d.get(ky) == {}:
                    pass
                else:
                    for x in d.get(ky):
                        # print(x)
                        # add new file path to temp list
                        albumtrk_temp.append(x)
                        # albumtrk.append(x)
                    # print(";)")
                    # edit new file path and combine
                    # temp album track with tracks already in list
                    albumtrk = albumtrk+self.edit_path(albumtrk_temp)

                    # write to playlist, send ky as name
                    self.create_playlist(
                        albumtrk, self.create_valid_name(ky), path)
                    albumtrk = []
            else:
                # print("Else")
                # new album/genre
                for x in d.get(ky):
                    print(x)
                    albumtrk.append(x)
                print('BEFORE EDIT{}'.format(albumtrk))
                print(";)")  # write to playlist send ky as name
                albumtrk = self.edit_path(albumtrk)
                print(albumtrk)
                self.create_playlist(
                    albumtrk, self.create_valid_name(ky), path)
                albumtrk = []

    def create_valid_name(self, s):
        return re.sub('[^\w_.)( -]', '', s)


    ###############
    # END
    ###########
'''
pcp=PlaylistCP()
>>> d=pcp.get_album_meta_live(['C:\\Users\\Ross\\Google Drive\\Car\\app\\GUI\\Infotainment\\media\\music\\02. Karaoke.mp3','C:\\Users\\Ross\\Google Drive\\Car\\app\\GUI\\Infotainment\\media\\music\\01. Fireworks (Feat. Alicia Keys).mp3'])
>>> pcp.is_newalbum(d)
'''


class Playlist_xspf:
    """Build xml playlist."""

    def __init__(self):
        # Defines basic tree structure.
        self.playlist = xml.Element('playlist')
        self.tree = xml.ElementTree(self.playlist)
        self.playlist.set('xmlns', 'http://xspf.org/ns/0/')
        self.playlist.set(
            'xmlns:vlc', 'http://www.videolan.org/vlc/playlist/ns/0/')
        self.playlist.set('version', '1')

        self.title = xml.Element('title')
        self.playlist.append(self.title)
        self.title.text = 'Playlist'

        self.trackList = xml.Element('trackList')
        self.playlist.append(self.trackList)

    def add_track(self, path):
        # Add tracks to xml tree (within trackList).
        track = xml.Element('track')
        location = xml.Element('location')
        location.text = path
        track.append(location)
        self.trackList.append(track)

    def get_playlist(self):
        # Return complete playlist with tracks.
        return self.playlist
