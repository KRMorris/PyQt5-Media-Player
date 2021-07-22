
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshot
from watchdog.observers.polling import PollingObserver
from playlist_creator_parser import PlaylistCP
import json
import ast


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.l = []
        self.tm = 30.0
        self.pcp = PlaylistCP()
        self.refSnap = DirectorySnapshot(
            path='./media/music/', recursive=False)

    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        # ass src_path to playlist
        print('=========================')
        self.l.append(event.src_path)
        print("on_created", event.src_path)
        print(self.l)
        self.newSnap = DirectorySnapshot(
            path='./media/music/', recursive=False)
        # if self.newSnap!=None:

    def on_deleted(self, event):
        print("on_deleted", event.src_path)

    def on_modified(self, event):
        print("on_modified", event.src_path)

    def on_moved(self, event):
        print("on_moved", event.src_path)

    def clearLst(self):
        self.pcp.is_newalbum(self.pcp.get_album_meta_live(
            self.l, 'album'), 'media/album/')
        self.l = []
        print("Clear")
        print("Format:{}".format(self.l))


# dirwatcherTC
class StartObserver():
    def __init__(self):
        self.refSnap = self.get_ref_snap()
        self.pcp = PlaylistCP()
        self.c = 0

    def run(self, ui):
        self.event_handler = MyHandler()
        observer = Observer()  # PollingObserver(2.5)
        # folder to observe for changes
        observer.schedule(self.event_handler,
                          path='./media/music/', recursive=False)
        observer.start()

    def get_ref_snap(self):
        try:
            #self.refSnap = dict()
            self.ref_log = open('log/ref_log.bin', 'r')
            rl = self.ref_log.read()
            self.refSnap = DirectorySnapshot(ast.literal_eval('"'+rl+'"'))
        except FileNotFoundError:
            self.write_dref()
        return self.refSnap

    def write_dref(self, nsnap=None):
        self.ref_log = open('log/ref_log.bin', 'w')
        if nsnap == None:
            # print('get_ref_snap')
            self.refSnap = DirectorySnapshot(
                path='./media/music/', recursive=False)
            # print(self.refSnap)
            self.ref_log.write(str(self.refSnap))
            self.ref_log.close()
        else:
            self.ref_log.write(str(nsnap))
            self.ref_log.close()

    def get_new_snap(self):
        # print('get_new_snap')
        self.newSnap = DirectorySnapshot(
            path='./media/music/', recursive=False)
        return self.newSnap

    def dir_snap(self):
        # get snapshot of directory
        self.newSnap = self.get_new_snap()
        # print(self.newSnap)
        # check for changes
        dif = self.newSnap - self.refSnap
        # media files extention list
        ext_list = ['.mp4', '.wmv', '.mp3']
        if dif.files_created == []:
            #print("No new files")
            pass
        else:
            diff_list = []
            for dfc in range(len(dif.files_created)):
                # check if files are media files
                if dif.files_created[dfc][-4:] in ext_list:  # '.mp3':
                    print('=========================endswith(.mp3)')
                    # for file_created in dif.files_created:
                    # print(dif.files_created)
                    diff_list.append(dif.files_created[dfc])

            # add files to albums
            self.pcp.is_newalbum(self.pcp.get_album_meta_live(
                diff_list, 'album'), 'media/album/')

            # organize files into genre
            self.pcp.is_newalbum(self.pcp.get_album_meta_live(
                diff_list, 'genre'), 'media/genre/')

            # update reference snapshop with new snapshot
            self.refSnap = self.newSnap
            self.write_dref(self.newSnap)
