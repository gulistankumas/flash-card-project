from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card=[]
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data=pandas.read_csv("data/french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records") 

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_word, text = current_card["French"] , fill="black")
    canvas.itemconfig(card_title, text = "French", fill="black" )
    canvas.itemconfig(card_back, image= front_img)
    flip_timer = window.after(3000,func=flip_card)
    

def flip_card():
   
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word, text= current_card["English"], fill="white")
    # back image
    canvas.itemconfig(front_img,image=card_back)
    #!!!!!!! flipden sonra beyaz arka plana dönme!!!!!!

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(data))
    next_card()
    

 



window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas=Canvas(width=800, height=526)
# card_front.png images içinde olduğu için images\card_front.png

# back image
card_back=PhotoImage(file="images\card_back.png")

card_front=PhotoImage(file="images\card_front.png")
front_img = canvas.create_image(400,263,image=card_front)

card_title = canvas.create_text(400,150, text="", font=("Ariel", 40 , "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60 , "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2,)


#BUTTONS

check_image = PhotoImage(file="images\check.png")
known_button = Button(image=check_image, highlightthickness=0,command=is_known)
known_button.grid(column=1,row=1)

cross_image = PhotoImage(file="images\wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(column=0,row=1)





next_card()

window.mainloop()


