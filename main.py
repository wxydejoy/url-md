# import tkinter
from tkinter import *



root = Tk()  # 建立根窗口 自定义的Tk对象名称，也可以取其它名称
root.title("url-md")
root.config(bg='#FFEDDF')
root.iconbitmap("hhh.ico")  # 不知道为什么，png和bmp无法显示，或许是我图片问题，但就先这样吧


def mwindow():
    screenWidth = root.winfo_screenwidth()  # 屏幕宽度
    screenHeight = root.winfo_screenheight()  # 屏幕高度
    w = 300  # 窗口宽
    h = 160  # 窗口高
    x = (screenWidth - w) / 2  # 窗口左上角x轴位置
    y = (screenHeight - h) / 2  # 窗口左上角y轴位置
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # 表示距离屏幕左上角(400,200)
    # +x表示窗口左侧距离屏幕左侧距离, -x表示窗口右侧距离屏幕右侧的距离
    # +y与-y的含义类似，窗口上侧(下侧)距离屏幕上侧(下侧)的距离
    # 练习改函数


def windowset():
    # label = Label(root,text="前缀")
    # label.pack()
    label = Label(root, text="前缀", fg="black", bg="#FFEDDF")
    label.pack(anchor=N, side=LEFT, padx=10, pady=10)
    label = Label(root, text="后缀", fg="black", bg="#FFEDDF")
    label.pack(anchor=N, side=LEFT, padx=50, pady=10)
    label = Label(root, text="自动序号", fg="black", bg="#FFEDDF")
    label.pack(anchor=N, side=LEFT, padx=0, pady=10)
    label = Label(root, text="-wxy", fg="blue", bg="#FFEDDF")
    label.pack(side=BOTTOM, padx=10, pady=10)
    btn = Button(root, padx=0, pady=0, bd=2,relief=GROOVE, bg="white", text="转换", command=get_url)
    # btn.pack(side=BOTTOM,padx=10,pady=10)
    btn.place(x=130, y=120)
    global former, latter, main,var
    former = Entry(root,width=6,bd=2,relief=GROOVE)
    latter = Entry(root,width=6,bd=2,relief=GROOVE)
    main = Text(root,width=6,bd=2,relief=GROOVE)
    former.place(x=45,y=10)
    latter.place(x=133, y=10)
    main.place(x=50,y=40,width=200,height=60)
    var =IntVar()
    select = Checkbutton(root,bg="#FFEDDF",variable=var)
    select.place(x=230,y=8)
    root.mainloop()  # 让程序继续运行，同时进入等待与处理窗口事件，放在程序最后一行1


def get_url():
    urlformer = former.get()
    urllatter = latter.get()
    url = main.get(1.0,END)
    if url[-2] == '\n':
        url = url[0:-1]
    # 这里有点迷

    md = ''
    if var.get() == 0:
        md = urlformer + url.replace('\n', urllatter + '\n' + urlformer)
        l = len(urlformer)
        main.delete(1.0, END)
        main.insert(END, md[0:-l])
    else:
        md = urlformer + url.replace('\n', urllatter + '\n' + urlformer)
        ran = md.count('$')
        for i in range(ran):
            md = md.replace('$',str(i),1)
        l = len(urlformer)
        main.delete(1.0, END)
        main.insert(END, md[0:-l])








mwindow()
windowset()






'''
f = open('main.txt')
lines = f.readlines()
f.close()
print(lines)
for i in range(len(lines)):
    #lines[i] = "![](" + lines[i].replace('\n','') + ')' + '\n'
    #lines[i] = "- ![" + lines[i].replace('\n','') + "](" + lines[i].replace('\n','') + ')' +'\n'
    lines[i] = "- " + lines[i].replace('\n','') +'\n'
f = open('main.txt','w')
f.writelines(lines)

'''







