#HJogAP

from Tkinter import *
import tkMessageBox

#-------------------------------------------------------#
top = Tk()
top.wm_title('Innskraning')
#-------------------------------------------------------#
L1 = Label(top, text="Notandanafn:")
L1.pack(side = 'top')
E1 = Entry(top, bd =5)
E1.pack(side = 'top')
L2 = Label(top, text="Lykilord:")
L2.pack()
E2 = Entry(top, bd =5, show='*')
E2.pack()
#-------------------------------------------------------#
logintries = 0
#-------------------------------------------------------#
def logxin():
	global logintries
	passwordinput = E2.get()
	usernameinput = E1.get()
	with open('passwords.txt', 'r') as my_file:
		if (usernameinput+':'+passwordinput+'\n') in my_file.read():
			tkMessageBox.showinfo("Forrit", "Velkominn, " + E1.get())
		elif usernameinput == 'deleteall' and passwordinput == '0000':
			with open('passwords.txt', 'w') as my_file:
				my_file.write('')
			with open('passwords.txt', 'r') as my_file:
				print my_file.read()
		elif usernameinput == 'displayall' and passwordinput == '0000':
			with open('passwords.txt', 'r') as my_file:
				print my_file.read()
		else:
			logintries += 1
			if logintries < 3:
				tkMessageBox.showinfo('INVALID', "Vitlaust notandanafn eda lykilord!.")
			else:
				tkMessageBox.showinfo('INVALID', "Thu hefur engar tilraunir eftir!")
				wataman = 1
				while wataman == 1:
					tkMessageBox.showinfo('ERROR', "ERROR")
#-------------------------------------------------------#
def buatilnotanda():
	password = E2.get()
	username = E1.get()
	if len(password) != 0 and len(username) != 0:
		if username != 'deleteall' and username != 'displayall': #Til ad koma i veg fyrir ad deleteall commandid haettir ad virka
			with open('passwords.txt', 'a') as my_file:
				my_file.write(username+':'+password+'\n')
			with open('passwords.txt', 'r') as my_file:
				print my_file.read()
	else:
		tkMessageBox.showinfo('Error', 'Notandanafn eda Lykilord vantar!')
#-------------------------------------------------------#
takki2 = Button(top, activebackground='Pale Green', bg = 'Royal Blue', width ='17' ,height='1', bd = '2', text="Innskra", command = logxin)
takki1 = Button(top, activebackground='Pale Green', bg = 'Royal Blue', width ='17' ,height='1', bd = '2', text="Nyskraning", command = buatilnotanda)
takki2.pack()
takki1.pack()
#-------------------------------------------------------#
top.mainloop()
#-------------------------------------------------------#
