import sys
from Tkinter import *
import tkMessageBox
import sqlite3
import string



#-----------------------------------------------------------------------------------------------------------------------------------------

def second2():
	window = Tk()
	window.title('\t monthly entries')
	window.geometry("1300x750")

	
	global e0
	global e1
	global e2
	global e3
	global e4
	global e5
	global e6
	global e7
	global e8
	global e9
	global e10
	global e11
	global e12
	global e13
	global e14
	
	s1 = Label(window,text="\n* GANESH GOLDSMITH *",font =(None, 25)).grid(column = 4, row = 1)
	s2 = Label(window,text="\n* LABOUR BILL *",font =(None, 18)).grid(column = 6, row = 1)

	s3 = Label(window,text="Address:-922,Ravivar peth,Guruprasd apts,shop no-7,pune-2",font =(None, 10)).grid(column = 4, row = 2)

	s4= Label(window,text="\n State:- Maharashtra         State code:- 27",font =(None, 10)).grid(column = 4, row = 3)

	s5 = Label(window,text="\n* GST No :- 27CSBPS7265J1Z5 *",font =(None, 11)).grid(column = 4, row = 4)

	s6 = Label(window,text="\n INVOICE NO. :-",font =(None, 11)).grid(column = 2, row = 4)
	e0 = Entry(window)
	e0.grid(column = 3, row =4)

	s7 = Label(window,text="--------------------------------------------------------------",font =(None, 9)).grid(column = 3, row = 5)
	s9 = Label(window,text="------------------------------------------------------------------------------------------------------",font =(None, 9)).grid(column = 4, row = 5)
	s8 = Label(window,text="-----------------------------------------------------",font =(None, 9)).grid(column = 5, row = 5)
	ss1 = Label(window,text="--------------------------------------------------",font =(None, 9)).grid(column = 6, row = 5)

	ss2 = Label(window,text="\n INVOICE DATE :- ",font =(None, 11)).grid(column = 5, row = 3)
	e1 = Entry(window)
	e1.grid(column = 6, row =3)

	ss3 = Label(window,text="\n PLACE OF SUPPLY :-",font =(None, 11)).grid(column = 2, row = 6)
	e2 = Entry(window)
	e2.grid(column = 3, row =6)

	ss4 = Label(window,text="\n CUSTOMER NAME:-",font =(None, 11)).grid(column = 3, row = 7)

	lst1 = ['CHANDUKAKA SARAF & SONS','M/s MAHALAXMI GOLDSMITH','SHRIPAD CHANDRAKANT BELWALKAR']
	var1=StringVar()
	e3 = Spinbox(window,values=lst1, textvariable=var1,font =(None, 12),width=35)
	e3.grid(column = 4, row =7)

	ss5 = Label(window,text="\n ADDRESS :-",font =(None, 11)).grid(column = 3, row = 9)

	lst2 = ['S.No 32/1/B/5 GUNAWADI RD BARAMATI','PORWAL HOUSE,255GANESH PETH PUNE-2','SHOP-4 1045 SADASHIV PETH PUNE-30']
	var2=StringVar()
	e4 = Spinbox(window,values=lst2, textvariable=var2,font =(None, 12),width=35)
	e4.grid(column = 4, row =9)
	
	ss6 = Label(window,text="\n GSTIN NO :-",font =(None, 11)).grid(column = 3, row = 11)

	lst3 = ['27AAAFC8675R1ZM','27AOOPP4413N1ZD','27ABBPB2828D1Z9']
	var3=StringVar()
	e5 = Spinbox(window,values=lst3, textvariable=var3,font =(None, 12),width=35)
	e5.grid(column = 4, row =11)

	ss7 = Label(window,text="\n DESCRIPTION OF GOODS :-",font =(None, 11)).grid(column = 3, row = 13)
	e6 = Entry(window,width=42)
	e6.grid(column = 4, row =13)

	ss8 = Label(window,text="\n HSN code :-",font =(None, 11)).grid(column = 5, row = 6)
	e7 = Entry(window)
	e7.grid(column = 6, row =6)

	ss9 = Label(window,text="\n NET Wt. :-",font =(None, 11)).grid(column = 5, row = 7)
	e8 = Entry(window)
	e8.grid(column = 6, row =7)

	ss10 = Label(window,text="\n FINE Wt. :-",font =(None, 11)).grid(column = 5, row = 8)
	e9 = Entry(window)
	e9.grid(column = 6, row =8)

	ss11= Label(window,text="\n AMOUNT :-",font =(None, 11)).grid(column = 5, row = 9)
	e10 = Entry(window)
	e10.grid(column = 6, row =9)

	ss12 = Label(window,text="------------------------------------------------------",font =(None, 9)).grid(column = 5, row = 10)
	ss13 = Label(window,text="--------------------------------------------------",font =(None, 9)).grid(column = 6, row = 10)

	ss14 = Label(window,text="\n SGST :-",font =(None, 11)).grid(column = 5, row = 11)
	e11 = Entry(window)
	e11.grid(column = 6, row =11)

	ss15 = Label(window,text="\n CGST :-",font =(None, 11)).grid(column = 5, row = 12)
	e12 = Entry(window)
	e12.grid(column = 6, row =12)

	ss16 = Label(window,text="\n IGST :-",font =(None, 11)).grid(column = 5, row = 13)
	e13 = Entry(window)
	e13.grid(column = 6, row =13)

	ss17 = Label(window,text="\n TOTAL :-",font =(None, 11)).grid(column = 5, row = 14)
	e14 = Entry(window)
	e14.grid(column = 6, row =14)


	bb1=Button(window,text='\n\n PRINT',font =(None, 12)).grid(column = 3, row =16)

	bb2=Button(window,text='\n\n SAVE',font =(None, 12),command=lambda: print2(e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14))
	bb2.grid(column = 4, row =16)

	bb3=Button(window,text='\n\n TOTAL',font =(None, 12)).grid(column = 5, row =16)

	ss18 = Label(window,text="\nCustomer Signature ",font =(None, 11)).grid(column = 2, row = 17)

	ss19 = Label(window,text="\nSupplier Signature ",font =(None, 11)).grid(column = 6, row = 17)


#-----------------------------------------------------------------------------------------------------------------------------------------

def print2(ee0,ee1,ee2,ee3,ee4,ee5,ee6,ee7,ee8,ee9,ee10,ee11,ee12,ee13,ee14):	
	
	zz="M"+ee0.get()
	invoice_no=zz
	invoice_date=ee1.get()
	place=ee2.get()
	name=ee3.get()
	addr=ee4.get()
	gstin1=ee5.get()
	describe1=ee6.get()
	hsn1=ee7.get()
	net=ee8.get()
	fine=ee9.get()
	amount=ee10.get()
	sgst=ee11.get()
	cgst=ee12.get()
	igst=ee13.get()
	total=ee14.get()

	newl="\n"

	f=open(invoice_no+".txt","a+")

	f.write("\n\n\n\t\t\t\t **  GANESH GOLDSMITH  **")
	f.write("\n\t\t\t\t-------------------------")
	
	f.write("\n\n\n\n\t\tAddress:-922,Ravivar peth,Guruprasd apts,shop no-7,pune-2")

	f.write("\n\n\t\t\t State:- Maharashtra         State code:- 27")

	f.write("\n----------------------------------------------------------------------------------")

	f.write("\n\n\t\t\t\t* GST No :- 27CSBPS7265J1Z5 *")

	f.write("\n\n----------------------------------------------------------------------------------")

	f.write("\n\n\n\n INVOICE No:- "+invoice_no)
	f.write("\t\t\t\t INVOICE DATE  :- "+invoice_date)
		
	f.write(newl)

	f.write("\n\n PLACE   :- "+place)

	f.write("\n\n----------------------------------------------------------------------------------")

	f.write("\n\n\n\n NAME    :- "+name)
	f.write("\n\n\t\t\t\t\t\t\t NET  :- "+net)

	f.write("\n\n ADDRESS :- "+addr)
	f.write("\n\n\t\t\t\t\t\t\t FINE  :- "+fine)

	f.write("\n\n GST IN  :- "+gstin1)
	f.write("\n\n\t\t\t\t\t\t\t AMOUNT     :- "+amount)

	f.write("\n\n DESCRIPTION :- "+describe1)
	f.write("\n\n\n\t\t\t\t\t\t\t SGST     :- "+sgst)

	f.write("\n\n\n HSN  :- "+hsn1)
	f.write("\t\t\t\t\t\t CGST    :- "+cgst)

	f.write("\n\n\n\t\t\t\t\t\t\t IGST     :- "+igst)
	f.write("\n\n\n\t\t\t\t\t\t\t TOTAL   :- "+total)
		

	f.write("\n\n\n\n\n\n Customer signature")
	f.write("\t\t\t\t\t Supplier signature")


	f.write(newl)


	f.close()


	conn = sqlite3.connect('stud1.db')
	print "\nNew data stored in Month table";
	
	cur = conn.cursor()

	cur.execute("INSERT INTO month VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ee0.get(),ee1.get(),ee2.get(),ee3.get(),ee4.get(),ee5.get(),ee6.get(),ee7.get(),ee8.get(),ee9.get(),ee10.get(),ee11.get(),ee12.get(),ee13.get(),ee14.get()))
	
	conn.commit()



#-----------------------------------------------------------------------------------------------------------------------------------------

def second1():
		window = Tk()
		window.title('\t Entry page')
		window.geometry("1300x750")

		global t0
		global t1
		global t2
		global t3
		global t4
		global t5
		global t6
		global t7
		global t8
		global t9
		global t10
		global t11
		global t12
		global t13
		global t14
		global ts15

		var2=IntVar()
		varss=StringVar()
		varss1=StringVar()

		l1 = Label(window,text="\n* GANESH GOLDSMITH *",font =(None, 25)).grid(column = 4, row = 1)

		l2 = Label(window,text="Address:-922,Ravivar peth,Guruprasd apts,shop no-7,pune-2",font =(None, 10)).grid(column = 4, row = 2)

		l3 = Label(window,text="\n State:- Maharashtra         State code:- 27",font =(None, 10)).grid(column = 4, row = 3)

		l4 = Label(window,text="\n* GST No :- 27CSBPS7265J1Z5 *",font =(None, 12)).grid(column = 4, row = 4)

		l5 = Label(window,text="\n CHALLAN NO. :-",font =(None, 12)).grid(column = 2, row = 4)
		t0 = Entry(window)
		t0.grid(column = 3, row =4)

		l6 = Label(window,text="--------------------------------------------------------------",font =(None, 9)).grid(column = 3, row = 5)
		l66 = Label(window,text="------------------------------------------------------------------------------------------------------",font =(None, 9)).grid(column = 4, row = 5)
		l666 = Label(window,text="----------------------------------------------------",font =(None, 9)).grid(column = 5, row = 5)

		l55 = Label(window,text=" DATE :- ",font =(None, 12)).grid(column = 5, row = 3)
		t1 = Entry(window)
		t1.grid(column = 6, row =3)
		
		l11 = Label(window,text=" PLACE OF SUPPLY :-",font =(None, 11)).grid(column = 2, row = 6)
		t2 = Entry(window)
		t2.grid(column = 3, row =6)
	
		l22 = Label(window,text="  CUSTOMER NAME :-",font =(None, 11)).grid(column = 3, row = 7)
		
		lst1 = ['CHANDUKAKA SARAF & SONS','M/s MAHALAXMI GOLDSMITH','SHRIPAD CHANDRAKANT BELWALKAR']
		var1=StringVar()
		t3 = Spinbox(window,values=lst1, textvariable=var1,font =(None, 11),width=32)
		t3.grid(column = 4, row =7)


		l33 = Label(window,text=" ADDRESS :-",font =(None, 11)).grid(column = 3, row = 9)

		lst2 = ['S.No 32/1/B/5 GUNAWADI RD BARAMATI','PORWAL HOUSE,255GANESH PETH PUNE-2','SHOP-4 1045 SADASHIV PETH PUNE-30']
		var2=StringVar()
		t4 = Spinbox(window,values=lst2, textvariable=var2,font =(None, 11),width=32)
		t4.grid(column = 4, row =9)
		

		l44 = Label(window,text=" GST IN NUMBER :-",font =(None, 11)).grid(column = 3, row = 11)
		lst3 = ['27AAAFC8675R1ZM','27AOOPP4413N1ZD','27ABBPB2828D1Z9']
		var3=StringVar()
		t5 = Spinbox(window,values=lst3, textvariable=var3,font =(None, 11),width=32)
		t5.grid(column = 4, row =11)

		l0 = Label(window,text=" DESCRIPTION OF GOODS :-",font =(None, 11)).grid(column = 3, row = 13)
		t6 = Entry(window,width=42)
		t6.grid(column = 4, row =13)
		
		l55 = Label(window,text=" HSN CODE :-",font =(None, 11)).grid(column = 5, row = 6)
		t7 = Entry(window)
		t7.grid(column = 6, row =6)
	
		l66 = Label(window,text="\n QUANTITY :-",font =(None, 11)).grid(column = 5, row = 7)
		t8 = Entry(window)
		t8.grid(column = 6, row =7)
	
		l7 = Label(window,text="\n GROSS wt. :-",font =(None, 11)).grid(column = 5, row = 8)
		t9 = Entry(window)
		t9.grid(column = 6, row =8)
	
		l8 = Label(window,text="\n NET wt. :-",font =(None, 11)).grid(column = 5, row = 9)
		t10 = Entry(window)
		t10.grid(column = 6, row =9)
	
		l9 = Label(window,text="\n FINE wt. :-",font =(None, 11)).grid(column = 5, row = 10)
		t11 = Entry(window)
		t11.grid(column = 6, row =10)

		ls = Label(window,text="\n CARAT :-",font =(None, 11)).grid(column = 5, row = 11)
		t12 = Entry(window)
		t12.grid(column = 6, row =11)
	
		l77 = Label(window,text="\n RATE :-",font =(None, 11)).grid(column = 5, row = 12)
		t13 = Entry(window)
		t13.grid(column = 6, row =12)
	
		l88 = Label(window,text="\n WASTAGE :-",font =(None, 11)).grid(column = 5, row = 13)
		t14 = Entry(window)
		t14.grid(column = 6, row =13)
	
		varss=t14.get()
		l99 = Label(window,text="\n ESTIMATE AMOUNT :-",font =(None, 11)).grid(column = 5, row = 14)
		t15 = Entry(window,text=varss1)
		varss1.set(varss)
		t15.grid(column=6, row=14)
	
	
		b1=Button(window,text='\n\n PRINT',font =(None, 12))
		b1.grid(column = 3, row =16)
	
		b2=Button(window,text='\n\n SAVE',font =(None, 12),command=lambda: print1(t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15))

		b2.grid(column = 4, row =16)
	
		b3=Button(window,text='\n\n TOTAL',font =(None, 12),command=lambda: cal1(t11,t12,t13,t14))
		b3.grid(column = 5, row =16)
	
		l70 = Label(window,text="\nCustomer Signature ",font =(None, 11)).grid(column = 2, row = 17)
	
		l80 = Label(window,text="\nSupplier Signature ",font =(None, 11)).grid(column = 6, row = 17)

		window.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------

def cal1(tt11,tt12,tt13,tt14):
	fine=float(tt11.get())			
	carat=float(tt12.get())
	rate=float(tt13.get())
	w=float(tt14.get())

	total1=fine*carat*rate*w

	cal11(total1)

def cal11(total11):
		window = Tk()
		window.title('\t total')
		window.geometry("230x80")

		l70 = Label(window,text=total11,font =(None, 30)).grid(column = 2, row = 2)

#-----------------------------------------------------------------------------------------------------------------------------------------

def print1(tt0,tt1,tt2,tt3,tt4,tt5,tt6,tt7,tt8,tt9,tt10,tt11,tt12,tt13,tt14,tt15):	
	
	ch_no=tt0.get()
	date1=tt1.get()
	place1=tt2.get()
	name1=tt3.get()
	addr1=tt4.get()
	gstin=tt5.get()
	describe=tt6.get()
	hsn=tt7.get()
	Q=tt8.get()
	gross=tt9.get()
	net=tt10.get()
	fine=tt11.get()
	carat=tt12.get()
	rate=tt13.get()
	wastage=tt14.get()
	estimate=tt15.get()

	newl="\n"

	f=open(ch_no+".txt","a+")

	f.write("\n\n\n\t\t\t\t **  GANESH GOLDSMITH  **")
	f.write("\n\t\t\t\t-------------------------")
	
	f.write("\n\n\n\n\t\tAddress:-922,Ravivar peth,Guruprasd apts,shop no-7,pune-2")

	f.write("\n\n\t\t\t State:- Maharashtra         State code:- 27")

	f.write("\n----------------------------------------------------------------------------------")

	f.write("\n\n\t\t\t\t* GST No :- 27CSBPS7265J1Z5 *")

	f.write("\n\n----------------------------------------------------------------------------------")

	f.write("\n\n\n\n CHALLAN No:- "+ch_no)
	f.write("\t\t\t\t\t DATE  :- "+date1)
		
	f.write(newl)

	f.write("\n\n PLACE   :- "+place1)

	f.write("\n\n----------------------------------------------------------------------------------")

	f.write("\n\n\n\n NAME    :- "+name1)
	f.write("\n\n\t\t\t\t\t\t\t QUANTITY  :- "+Q)

	f.write("\n\n ADDRESS :- "+addr1)
	f.write("\n\n\t\t\t\t\t\t\t GROSS  :- "+gross)

	f.write("\n\n GST IN  :- "+gstin)
	f.write("\n\n\t\t\t\t\t\t\t NET     :- "+net)

	f.write("\n\n DESCRIPTION :- "+describe)
	f.write("\n\n\n\t\t\t\t\t\t\t FINE     :- "+fine)

	f.write("\n\n\n HSN  :- "+hsn)
	f.write("\t\t\t\t\t\t CARAT    :- "+carat)

	f.write("\n\n\n\t\t\t\t\t\t\t RATE     :- "+rate)
	f.write("\n\n\n\t\t\t\t\t\t\t WASTAGE   :- "+wastage)
	f.write("\n\n\n\t\t\t\t\t\t\t ESTIMATE  :- "+estimate)
		

	f.write("\n\n\n\n\n\n Customer signature")
	f.write("\t\t\t\t\t Supplier signature")


	f.write(newl)


	f.close()


	conn = sqlite3.connect('stud1.db')
	print "\nNew data stored in Day table";
	
	cur = conn.cursor()
	cur.execute("INSERT INTO day VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(tt0.get(),tt1.get(),tt2.get(),tt3.get(),tt4.get(),tt5.get(),tt6.get(),tt7.get(),tt8.get(),tt9.get(),tt10.get(),tt11.get(),tt12.get(),tt13.get(),tt14.get(),tt15.get()))
	
	conn.commit()


#-----------------------------------------------------------------------------------------------------------------------------------------

def next1():
	if((entry1.get()=='ss') & (entry2.get()=='ss')):
		second1()
	else:
		tkMessageBox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
#-----------------------------------------------------------------------------------------------------------------------------------------

def next2():
	
 	if((entry1.get()=='s') & (entry2.get()=='s')):
		second2()
	else:
		tkMessageBox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
#-----------------------------------------------------------------------------------------------------------------------------------------
def next3():
	
 	if((entry1.get()=='ss') & (entry2.get()=='ss')):
		next33()
	else:
		tkMessageBox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
#-----------------------------------------------------------------------------------------------------------------------------------------
def next4():
	
 	if((entry1.get()=='s') & (entry2.get()=='s')):
		next44()
	else:
		tkMessageBox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")
#-----------------------------------------------------------------------------------------------------------------------------------------

def next33():	
	window = Tk()
	window.title('\t search day')
	window.geometry("1300x750")

	data=readdata()	

        for index, dat in enumerate(data):
            Label(window, text=dat[0]).grid(row=index+1, column=0)
            Label(window, text=dat[1]).grid(row=index+1, column=1)
            Label(window, text=dat[2]).grid(row=index+1, column=2)
	    Label(window, text=dat[3]).grid(row=index+1, column=3)
            Label(window, text=dat[4]).grid(row=index+1, column=4)
            Label(window, text=dat[5]).grid(row=index+1, column=5)
	    Label(window, text=dat[6]).grid(row=index+1, column=6)
            Label(window, text=dat[7]).grid(row=index+1, column=7)
            Label(window, text=dat[8]).grid(row=index+1, column=8)
	    Label(window, text=dat[9]).grid(row=index+1, column=9)
            Label(window, text=dat[10]).grid(row=index+1, column=10)
            Label(window, text=dat[11]).grid(row=index+1, column=11)
	    Label(window, text=dat[12]).grid(row=index+1, column=12)
            Label(window, text=dat[13]).grid(row=index+1, column=13)
            Label(window, text=dat[14]).grid(row=index+1, column=14)
            Label(window, text=dat[15]).grid(row=index+1, column=15)
	

def readdata():
	conn = sqlite3.connect('stud1.db')
	
	cur = conn.cursor()
	cur.execute("select * from day")
	return cur.fetchall()	
	
	conn.commit()

#-----------------------------------------------------------------------------------------------------------------------------------------

def next44():	
	window = Tk()
	window.title('\t search month')
	window.geometry("1300x750")

	data=readdata2()	

        for index, dat in enumerate(data):
            Label(window, text=dat[0]).grid(row=index+1, column=0)
            Label(window, text=dat[1]).grid(row=index+1, column=1)
            Label(window, text=dat[2]).grid(row=index+1, column=2)
	    Label(window, text=dat[3]).grid(row=index+1, column=3)
            Label(window, text=dat[4]).grid(row=index+1, column=4)
            Label(window, text=dat[5]).grid(row=index+1, column=5)
	    Label(window, text=dat[6]).grid(row=index+1, column=6)
            Label(window, text=dat[7]).grid(row=index+1, column=7)
            Label(window, text=dat[8]).grid(row=index+1, column=8)
	    Label(window, text=dat[9]).grid(row=index+1, column=9)
            Label(window, text=dat[10]).grid(row=index+1, column=10)
            Label(window, text=dat[11]).grid(row=index+1, column=11)
	    Label(window, text=dat[12]).grid(row=index+1, column=12)
            Label(window, text=dat[13]).grid(row=index+1, column=13)
            Label(window, text=dat[14]).grid(row=index+1, column=14)
	

def readdata2():
	conn = sqlite3.connect('stud1.db')
	
	cur = conn.cursor()
	cur.execute("select * from month")
	return cur.fetchall()	
	
	conn.commit()

#-----------------------------------------------------------------------------------------------------------------------------------------


window = Tk()
window.title('\tlogin page')
window.geometry("1300x750")

global Lable1
global Lable2
global entry1
global entry2


Label11 = Label(window).grid(column = 4, row = 1)
Label12 = Label(window).grid(column = 4, row = 2)
Label13 = Label(window).grid(column = 4, row = 3)
Label14 = Label(window).grid(column = 4, row = 4)


Lable1 = Label(window,text = 'USERNAME:- ',font =(None, 15))
Lable1.grid(column = 12, row = 5)
entry1 = Entry(window,font =(None, 12))
entry1.grid(column = 13, row = 5)

Label14 = Label(window).grid(column = 4, row = 6)

Lable2 = Label(window,text = 'PASSWORD:- ',font =(None, 15))
Lable2.grid(column = 12, row = 7)
entry2 = Entry(window,font =(None, 12))
entry2.grid(column = 13, row = 7)


b=Button(text='\n\n Daily Entry',font =(None, 15),command=lambda: next1()).grid(column = 13, row = 8)

bb=Button(text='\n\n Each month entry',font =(None, 15),command=lambda: next2()).grid(column = 15, row = 8)

Label14 = Label(window).grid(column = 4, row = 9)

bbb=Button(text='\n\n SEARCH DAY',font =(None, 15),command=lambda: next3()).grid(column = 13, row = 10)

bbbb=Button(text='\n\n SEARCH MONTH',font =(None, 15),command=lambda: next4()).grid(column = 15, row = 10)
	
window.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------

 
