def Search_Attendance():
    hk1 = simpledialog.askstring("Input string", "Enter Search name")
    os.chdir(os.getcwd())
    wordcount = {}
    d = {}
    newlist = []
    files_list = []
    for all_files in glob.glob("*.csv"):
        af = all_files
        files_list.append(af)
    print(files_list)
    for files in files_list:
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

    for word in newlist:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    for k, v in wordcount.items():
        d[k] = str(v)

    if hk1 in d:
        messagebox.showinfo("Attendance Count", "Successfully count\n\n" + "         " + d[hk1])
    else:
        messagebox.showerror("Error", '   ' + hk1 + "\nName Not Found")


