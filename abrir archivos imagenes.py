def open_file():
    result = filedialog.askopenfile(initialdir=os.getcwd(), title="Select file",
                                    filetypes=(("Attendance files", ".csv"), ("all file", "*.*")))
    dir_ = os.path.basename(result.name)
    print(dir_)
    txt = result.read()
    top = Toplevel()
    top.title(dir_)
    bt1 = Button(top, text="Exit", bg='red', command=top.destroy)
    bt1.pack(side=BOTTOM)
    top.geometry("400x400+150+150")
    text_area = Text(top, undo=True)
    text_area.pack(fill=BOTH, expand=1)
    if (result != None):
        i = 1
        for c in txt:
            text_area.insert(END, c)

        exit_file = result.name
    result.close()