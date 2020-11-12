def time():
    currentDT = datetime.datetime.now()
    string = currentDT.strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)