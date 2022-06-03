from threading import Thread
import tornado;
import tornado.web;
import tornado.ioloop;
import tornado.template;
import os;
import sys;
from urllib import parse
#from gpioController import *

cookieSecret='aaDa23dsf@#$!'



    
class IHandler(tornado.web.RequestHandler):
    pass
    
class RootHandler(IHandler):
    def get(self):
        if not self.get_secure_cookie("user"):
            self.redirect("/login")
            return;
        if not self.isAdmin():
            self.clear_all_cookies();
            self.set_status(400)
            self.finish("<html><body>Error while logging in. Check your login and password</body></html>")
        self.redirect("/list");

class ControlPanelHandler(IHandler):
    def get(self):
        songsList = create_list(path_to_music);
        uploadMessage = "";

        self.render("tree.html", songs=songsList);

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
        action = self.get_argument('Action',  None)
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

def create_list(path):
    list = dict(name="Songs listing", songs=[])
    lst = os.listdir(path)
    for name in lst:
        fullpath = os.path.join(path, name)

        if os.path.isdir(fullpath):
            pass
        else:
            list['songs'].append(dict(name=name))    
    return list


#arguments - [pathToCerts] [pathToMusic]
if (len(sys.argv) != 3):
    print('Bad arguments! Usage - server.py [pathToCerts] [pathToMusic]')
    exit();
data_dir = sys.argv[1]
path_to_music = sys.argv[2]

application = tornado.web.Application([
    (r"/", RootHandler),
    (r"/panel", ControlPanelHandler),

], cookie_secret=cookieSecret)

http_server = tornado.httpserver.HTTPServer(application, ssl_options={
"certfile": os.path.join(data_dir, "linsw.lab4.crt"),
"keyfile": os.path.join(data_dir, "linsw.lab4.key"),
})

http_server.listen(5001)
http_server.start(0)
tornado.ioloop.IOLoop.current().start()
