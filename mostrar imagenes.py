def Images_show():
    result = filedialog.askopenfile(initialdir=os.getcwd() + "/dataset_images/", title="Select file",
                                    filetypes=(("text", ".jpg"), ("all file", "*.*")))
    img = os.path.abspath(result.name)
    print(img)
    top = Toplevel()
    top.title("harish")
    bt1 = Button(top, text="Exit", bg='red', command=top.destroy)
    bt1.pack(side=BOTTOM)
    cv_img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
    height, width, no_channels = cv_img.shape
    canvas = Canvas(top, width=width, height=height)
    canvas.pack()
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
    canvas.create_image(0, 0, image=photo, anchor=NW)
    top.mainloop()