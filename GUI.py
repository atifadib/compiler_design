from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter
from textblob import TextBlob
import character_recognition
import adjective_extraction
import main_script
import character_development

chars=[]
adj_pos=[]
adj_neg=[]
filename=""
def adj():
	if(filename!=""):
		global adj_pos
		global adj_neg
		x,y=adjective_extraction.getAdj(filename)
		adj_pos=x
		adj_neg=y
		textPad.delete("1.0",END)
		out.delete("1.0",END)
		textPad.insert(END,"POSITIVE: ")
		
		for i in x:
			textPad.insert(END,i)
			textPad.insert(END,",")
			
		textPad.insert(END,"\n")
		textPad.insert(END,"NEGATIVE: ")		
		for i in y:
			textPad.insert(END,i)
			textPad.insert(END,",")
		out.insert(END,"Adj_Extraction")
		
	else:
		out.insert(END,"PICK A FILE")
def char():
	if(filename!=""):
		global chars
		chars=character_recognition.char_rec(filename)
		textPad.delete("1.0",END)
		out.delete("1.0",END)
		for x,y in chars.items():
			textPad.insert(END,x+" "+str(y)+"\n")
		out.insert(END,"char_recognition")		
	else:
		out.insert(END,"PICK A FILE")
		
def sentiment():
	global chars
	global adj_pos
	global adj_neg	
	if(filename!="" and len(chars)>0 and len(adj_pos)>0 and len(adj_neg)>0):
		regs=main_script.main(chars,adj_pos,adj_neg,filename)
		textPad.delete("1.0",END)
		for i in regs:
			textPad.insert(END,i)
			textPad.insert(END,"\n")
	else:
		if(filename==""):
			out.delete("1.0",END)
			out.insert("1.0","PICK A FILE")
		if(len(chars)<=0):
			out.delete("1.0",END)
			out.insert("1.0","Character Extraction required")
		if(len(adj_pos)<=0 or len(adj_neg)<=0):
			out.delete("1.0",END)
			out.insert("1.0","Adjective Extraction required")			
def char_dev():
	def char_dev_fire():
		global filename
		global chars
		global adj_pos
		global adj_neg
		c=t1.get()
		if(c in chars.keys()):
			if(len(adj_neg)>0 and len(adj_pos)>0):
				s=character_development.char_dev(c,adj_pos,adj_neg,filename)
				out.delete("1.0",END)
				out.insert("1.0","regex: "+s)
			else:
				out.delete("1.0",END)
				out.insert("1.0","First Extract the adjectives from text")
		else:
			out.delete("1.0",END)
			out.insert("1.0","INVALID CHARACTER NAME")
	r1=Toplevel()
	label1=Label(r1,text="Enter Character Name")
	t1=Entry(r1)
	label1.pack()
	t1.pack()
	btn=Button(r1,text="OK",command=char_dev_fire)
	btn.pack()
	root.wait_window(r1)
	


def pick():
	global filename
	filename = askopenfilename()
	f=open(filename,"r")
	l=f.readlines()
	if(len(l)>10):
		out.delete("1.0",END)
		textPad.delete("1.0",END)
		out.insert(END,"FILE OK "+filename)
		for i in l:
			textPad.insert(END,i)
	else:
		out.insert(END,"FILE TOO SMALL "+filename)
	
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
out=Text(root,width=120,height=1)

lb.pack()
lb1.pack()
textPad.pack()
layout=BTN(root)
layout.pack()

out.pack()
root.mainloop()
