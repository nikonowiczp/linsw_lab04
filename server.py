from threading import Thread
import tornado;
import tornado.web;
import tornado.ioloop;
import tornado.template;
import os;
import sys;
from urllib import parse

cookieSecret='aaDa23dsf@#$!'

mpdFileActions=["add-to-playlist", "play-now", "pause", "start"]

    
class IHandler(tornado.web.RequestHandler):
    pass
    
class RootHandler(IHandler):
    def get(self):
        self.redirect("/panel");

class ControlPanelHandler(IHandler):
    def get(self):
        data = create_data(path_to_music);
        uploadMessage = "";

        self.render("controlPanel.html", data=data);

class UploadHandler(IHandler):
    def post(self):
        inputFile = self.request.files['inputFile'][0];
        fileName = inputFile['filename']
        try:
            outputFile = open(path_to_music + fileName, 'wb+')
        except:
            print('Upload failed')
            return;
        outputFile.write(inputFile['body'])
        outputFile.close();

        self.redirect("/panel");

class MpdAction(IHandler):
    def post(self):
        filename=self.get_argument('filename', None)
        action = self.get_argument('action-type',  None)
        if not filename:
            self.write({"error":"File name is empty"})
            return
        if not action:
            self.write({"error":"Action is empty"})
            return
        if action == 1:
            pass
        elif action == 2:
            pass

def create_data(path):
    list = {
        "playlist":[],
        "songs":[]
    }
    lst = os.listdir(path)
    for name in lst:
        fullpath = os.path.join(path, name)

        if os.path.isdir(fullpath):
            pass
        else:
            list['songs'].append(dict(name=name))
    mpdClient.connect("localhost",6600);
    playlist = mpdClient.playlistinfo();
    mpdClient.disconnect();
    print(playlist)
    return list


#arguments - [pathToCerts] [pathToMusic]
if (len(sys.argv) != 3):
    print('Bad arguments! Usage - server.py [pathToMusic] [pathToCerts]')
    exit();
data_dir = sys.argv[2]
path_to_music = sys.argv[1]

#
from gpioController import *


application = tornado.web.Application([
    (r"/", RootHandler),
    (r"/panel", ControlPanelHandler),
    (r"/upload", UploadHandler),
    (r"/action", MpdAction),
], cookie_secret=cookieSecret)

http_server = tornado.httpserver.HTTPServer(application, ssl_options={
"certfile": os.path.join(data_dir, "linsw.lab4.crt"),
"keyfile": os.path.join(data_dir, "linsw.lab4.key"),
})

http_server.listen(5001)
http_server.start(0)
tornado.ioloop.IOLoop.current().start()