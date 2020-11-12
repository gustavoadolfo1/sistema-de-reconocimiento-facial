def Attendance_count():
    os.chdir(os.getcwd())
    wordcount = {}
    top = Toplevel()
    top.title("attendance count")
    bt1 = Button(top, text="Exit", bg='red', command=top.destroy)
    bt1.pack(side=BOTTOM)
    top.geometry("400x400+150+150")
    text_area = Text(top, undo=True)
    text_area.pack(fill=BOTH, expand=1)
    newlist = []
    files_list = []
    for all_files in glob.glob("*.csv"):
        af = all_files
        files_list.append(af)

    print(files_list)

    for files in files_list:
        # d=datetime.date.today()
        # file_name=d.strftime("%B")
        # print(file_name)
        print(files)
        pk = re.search(r'\d\d\w(?:Jan|Feb|March|April|May|June|Jul|Aug|Sep|Oct|Nov|December).(?:csv)', files)
        if pk == None:
            print("files not found")
        else:
            mk = pk.group()
            print(mk)
            file = open(mk, "r+")
            new = file.read().split(',')

            for l in range(1, len(new), 3):
                p = new[l]
                newlist.append(p)

    print(newlist)
    for word in newlist:
        if word not in wordcount:
            wordcount[word] = 1

        else:
            wordcount[word] += 1

    print(wordcount)

    # for l in range(0,len(wordcount)+1):
    # k = wordcount[l]
    for k, v in wordcount.items():
        # print (k , v)

        text_area.insert(INSERT, k)
        text_area.insert(INSERT, "=")
        text_area.insert(INSERT, v)
        text_area.insert(INSERT, "\n")