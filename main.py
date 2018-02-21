import urllib
class youtube(object):
    def __init__(self, channel):
        self.info = {}
        self.channel = channel
        self.videos = "https://www.youtube.com/channel/" +self.channel+ "/videos"
        self.search = '<h3 class="yt-lockup-title ">'
        socket = urllib.urlopen(self.videos)
        self.source = socket.readlines()
    def getstr(self, source, tag):
        tagstart = source.find(tag)
        start = source.find('"', tagstart) + 1
        end = source.find('"', start +1)
        return source[start:end]
    def tag(self, source, tag):
        start = source.find(tag) + len(tag)
        end = source.find(self.join(tag), start)
        return source[start:end]
    def join(self, tag, j=""):
        for test in tag:
            if tag.index(test) is 1:
                j = j + "/"
            j = j + test
        return j
    def views(self):
        for test in self.source:
            if test.find(self.search) is not -1:
                title = self.getstr(test[test.find(self.search)+len(self.search):], "title")
                metainfo = self.source[self.source.index(test)+5]
                views = self.tag(metainfo, "<li>")
                if views.find("views") is -1:
                    views = "not views"
                self.info.update({"title":title, "views":views})
        return self.info

get = youtube("UCRx5NnTE3bK_gMXm0-lKlpw")
print get.views()
