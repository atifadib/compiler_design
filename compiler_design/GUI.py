from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter
from textblob import TextBlob
import character_recognition
import adjective_extraction
import main_script
import character_development

filename=""
def adj():
	if(filename!=""):
		x,y=adjective_extraction.getAdj(filename)
		textPad.delete("1.0",END)
		out.delete("1.0",END)
		textPad.insert(END,"POSITIVE:")
		
		textPad.insert(END,x+"\n")
		
		textPad.insert(END,"NEGATIVE:")		
		textPad.insert(END,y+"\n")
		out.insert(END,"Adj_Extraction")
		
	else:
		out.insert(END,"PICK A FILE")
def char():
	if(filename!=""):
		chars=character_recognition.char_rec(filename)
		textPad.delete("1.0",END)
		out.delete("1.0",END)
		for x,y in chars.items():
			textPad.insert(END,x+" "+y+"\n")
		out.insert(END,"Adj_Extraction")		
	else:
		out.insert(END,"PICK A FILE")
		
def sentiment():
	main_script.main()
	
def char_dev():
	character_development.char_dev()
	


def pick():
	global filename
	filename = askopenfilename()
	f=open(filename,"r")
	l=f.readlines()
	if(len(l)>100):
		out.delete("1.0",END)
		textPad.delete("1.0",END)
		out.insert(END,"FILE OK")
		for i in l:
			textPad.insert(END,i)
	else:
		out.insert(END,"FILE TOO SMALL")
	
class BTN(Frame):
	def __init__(self,root):
		Frame.__init__(self, root)
		btn=Button(self,text="Pick File",command=pick)
		btn1=Button(self,text="Adjective Extract",command=adj)
		btn2=Button(self,text="Character Extract",command=char)
		btn3=Button(self,text="Sentiment Extract",command=sentiment)
		btn4=Button(self,text="Character Development",command=char_dev)
		btn5=Button(self,text="Exit",command=root.destroy)
		btn.grid(row=0,column=0)
		btn1.grid(row=0,column=1)
		btn2.grid(row=0,column=2)
		btn3.grid(row=0,column=3)
		btn4.grid(row=0,column=4)
		btn5.grid(row=0,column=5)
		
root=Tk()
root.title("Compiler Design Project")
lb=Label(root,text="Sentimental Analysis of a Text Document using a Lexical Analyser")

lb1=Label(root,text="Output Window")
textPad = ScrolledText(root, width=120, height=20)
#btn=Button(root,text="PICK FILE",command=pick)
#btn1=Button(root,text="Generate Reports",command=gen_report)
out=Text(root,width=120,height=1)
lb.pack()
lb1.pack()
textPad.pack()
layout=BTN(root)
layout.pack()
#btn.grid(row=0,column=0)
#btn1.grid(row=0,column=1)
#btn.pack()
#btn1.pack()
out.pack()
root.mainloop()
