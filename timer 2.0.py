import time
from tkinter import CENTER, Button, Tk, StringVar, Entry
from tkinter import messagebox


clockwindow = Tk()
clockwindow.geometry('500x500')
clockwindow.title('countdown timer')
clockwindow.configure(background= 'orange')

hourstring = StringVar()
minutestring = StringVar()
secondstring = StringVar()

hourstring.set('00')
minutestring.set('00')
secondstring.set('00')

hourtextbox = Entry(clockwindow, width= 3, font =('calibri'), textvariable=hourstring)
minutetextbox = Entry(clockwindow, width= 3, font =('calibri'), textvariable=minutestring)
secondtextbox = Entry(clockwindow, width= 3, font =('calibri'), textvariable=secondstring)

hourtextbox.place(x=170, y=180)
minutetextbox.place(x=220, y=180)
secondtextbox.place(x=270, y=180)


def runtimer():
    try:
        clocktime = int(hourstring.get())*3600 + int(minutestring.get())*60 
        + int(secondstring.get())
    except:  # noqa: E722
        print('incorrect values')
    while(clocktime > -1):

        totalminutes, totalseconds = divmod(clocktime, 60)

        totalhours = 0
        if(totalminutes == 60):
            totalhours, totalminutes = divmod(totalminutes, 60)


            hourstring.set('{0:2d}'.format(totalhours))
            minutestring.set('{0:2d}'.format(totalminutes))
            secondstring.set('{0:2d}'.format(totalseconds))


            clockwindow.update()
            time.sleep(1)



            if(clocktime == 0):
                messagebox.showinfo('time expired', 'your time has expired')


            clocktime -= 1



settimebutton = Button(clockwindow, text = 'set time', bd = '5', command = runtimer)
settimebutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)


clockwindow.mainloop()