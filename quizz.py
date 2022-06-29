from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:
	def __init__(self):
		self.qno=0
		self.disp_title()
		self.disp_ques()
		self.opt_sel=IntVar()
		self.opts=self.radio_buttons()
		self.disp_opt()
		self.buttons()
		self.total_ques=len(question)
		self.correct=0

	def disp_res(self):
		
		wrong_count = self.total_ques - self.correct
		correct = f"\nCorrectly Answered : {self.correct}"
		wrong = f"\nWrongly Answered : {wrong_count}"
		
		score = int(self.correct / self.total_ques * 100)
		result = f"Total Score: {score}%"
		
		mb.showinfo("Your Final Score is", f"{result}\n{correct}\n{wrong}")

        


	def check_ans(self, qno):
		
		if self.opt_sel.get() == answer[qno]:
			return True


	def next_btn(self):
		
		if self.check_ans(self.qno):
			self.correct += 1
		
		self.qno += 1
		
		if self.qno==self.total_ques:
			self.disp_res()
			ws.destroy()
		else:
			self.disp_ques()
			self.disp_opt()


	def buttons(self):
		
		next_button = Button(
            ws, 
            text="Next",
            command=self.next_btn,
            width=10,
            bg="#F2780C",
            fg="white",
            font=("ariel",16,"bold")
            )
		
		next_button.place(x=w_width-300,y=w_height-200)
		
		quit_button = Button(
            ws, 
            text="End the Test", 
            command=ws.destroy,
            width=10,
            bg="red",
            fg="white",
            font=("ariel",16," bold")
            )
		
		quit_button.place(x=w_width-200,y=120)


	def disp_opt(self):
		val=0
		self.opt_sel.set(0)
		
		for option in options[self.qno]:
			self.opts[val]['text']=option
			val+=1

	def disp_ques(self):
		
		qno = Label(
            ws, 
            text=question[self.qno], 
            width=60,
            font=( 'ariel' ,34,'bold'), 
            anchor= 'w',
			wraplength=1300,
			justify='center'
            )
		
		qno.place(x=250,y=250)


	def disp_title(self):
		
		title = Label(
            ws, 
            text="MCQ Test",
            height='2',
            bg="#33F0FF",
            fg="white",
            justify="center",
            padx=w_width/2-100,
            font=("ariel", 30,'bold')
            )
		
		title.place(x=0, y=2)


	def radio_buttons(self):
		
		q_list = []
		
		y_pos = 320
		
		while len(q_list) < 4:
			
			radio_btn = Radiobutton(
                ws,
                text=" ",
                variable=self.opt_sel,
                value = len(q_list)+1,
                font = ("ariel",30)
                )
			q_list.append(radio_btn)
			
			radio_btn.place(x = 300, y = y_pos)
			
			y_pos += 60
		
		return q_list

ws = Tk()
w_width= ws.winfo_screenwidth()
w_height= ws.winfo_screenheight()
ws.geometry("%dx%d" % (w_width,w_height))

ws.title("MCQ Test")

with open('data.json') as f:
	data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

quiz = Quiz()

ws.mainloop()
