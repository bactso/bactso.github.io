#! coding:utf-8

def html(f_name,title,audio):
  f = open(f_name)  # 歌词文件
  o_name = f_name.split('.')[0]+'.html'
  o = open(o_name,'w')
  header = '''<html lang="en">
  <head>
    <title></title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <link rel="stylesheet" href="bootstrap.css">
    <link rel="stylesheet" href="bubugao.css">
    <script src="jquery.js"></script>
    <script src="bootstrap.js"></script>
  </head>
  <body>
    <div class="container">
      <h3>%s</h3>
      <div class="slidecontainer">
        <input type="range" min="1" max="20" value="3" class="slider" id="myRange">
      </div>
      <div>
        Repeat <span id="demo"> times.</span>
      </div>
      <audio id="audio-player" src="%s" controls="controls"></audio>
      <div class="slidecontainer">
        <input type="range" min="10" max="30" value="10" class="slider" id="rate">
      </div>
      <div>
        Speed x<span id="trate"></span>
      </div>
      <div>
        <input type="checkbox" id="nob">
        <label for="nob">Autoplay</label>
      </div>
      <table class="table">
         <tbody>
'''%(title,audio)

  footer = '''        </tbody>
      </table>
    </div>
  </body>
  <script src="bubugao.js"></script>
</html>
'''

  def to_second(ts):
    hms,ms = ts.split(',')
    h,m,s = hms.split(':')
    h,m,s = map(int,(h,m,s))
    return str(h*60*60+m*60+s)+'.'+ms


  o.write(header)
  lines = [line.rstrip() for line in f.readlines()]
  cnt = len(lines)
  j = 1
  for i in xrange(0,cnt,4):
    s,t = lines[i+1][:12], lines[i+1][-12:]
    s,t = to_second(s), to_second(t)
    lrc = lines[i+2]
    o.write('''            <tr data-start="%s" data-end="%s" id="p%d">
               <td>%s</td>
            </tr>
'''%(s,t,j,lrc))
    j += 1
  o.write(footer)
  o.close()


from Tkinter import *
class App(Frame):
    def createWidgets(self):
        self.l1 = Label(self, text="srt文件名(例1.srt)").grid(row=1)
        self.e1 = Entry(self)
        self.e1.grid(row=1,column=1)
        self.sname = StringVar()
        self.l2 = Label(self, text="音频文件名(例1.mp3)").grid(row=2)
        self.e2 = Entry(self)
        self.e2.grid(row=2,column=1)
        self.aname = StringVar()
        self.l3 = Label(self, text="标题(例 延世1-1)").grid(row=0)
        self.e3 = Entry(self)
        self.e3.grid(row=0,column=1)
        self.title = StringVar()
        self.e1["textvariable"] = self.sname
        self.e2["textvariable"] = self.aname
        self.e3["textvariable"] = self.title

        self.b = Button(self)
        self.b['text'] = '生成网页'
        self.b.grid(row=3,column=1)
        self.b["command"] = self.say_hi
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def say_hi(self):
        f_name = self.sname.get().encode("utf-8")
        audio = self.aname.get().encode("utf-8")
        title = self.title.get().encode("utf-8")
        html(f_name,title,audio)

root = Tk()
root.title("bubugao")
app = App(master=root)
app.mainloop()
