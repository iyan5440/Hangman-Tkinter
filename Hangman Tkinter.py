import tkinter as tk
from tkinter import messagebox
import random as r
app = tk.Tk()
app.title("Hangman")

app.rowconfigure(1, pad=20)
app.rowconfigure(2, pad=20)
app.rowconfigure(3, pad=50)

words=['AZURE','DIRNDI','LYMPH','BUFFOON','PLAIN','DUPLEX','ZILCH','EMBEZZLE','SPHINX','ESPIONAGE','EUOUAE',]
word=r.choice(words)
taken=" "
misses=0 #controls hangman pics shown
hits=0 #determines if you win

def go():
    #variables are needed from the outside
    global word, words, taken, misses, hits
    #read in guess & convert to uppercase
    guess=txtlet.get().upper()
    #clear out the guess box
    txtlet.delete(0,tk.END)

    #if guess is > 1 letter or already picked
    if len(guess) !=1:
        messagebox.showinfo("ERROR #3190","GUESS ONE LETTER AT A TIME")
        return #leave
    elif taken.find(guess) >=0:
        messagebox.showinfo("ERROR #3049","YOU HAVE PICKED THAT LETTER")
        return
    #if we get to here we have a valid guess so add it to list
    taken += guess + ", "
    lbltaken.config(text=taken)

    #if guess isn't in word?
    if word.find(guess) == -1:
        #count it as a miss and update the image
        misses+= 1
        lblman.config(image=pics[misses])
        #is it over?
        if misses == 6:
            messagebox.showinfo("Game Over","You Lost")
            btn.grid_remove() #take away submit button
            btnres.grid(row=2,column=0)
        return
    #scan word for letter
    for x in range(0,len(word)):
        if guess==word[x]: #match
            #make letter white to reveal it
            labels[x].config(fg='white')
            hits+=1 #count as hit

    #when you get all letters
            if hits==len(word):
                messagebox.showinfo("Good Job!","You Win!")
                btn.grid_remove()
                btnres.grid(row=2,column=0)
            
def reset():
    global word, words, taken, misses, hits
    for x in range(0,len(word)):
        labels[x].config(bg='black')
        labels[x].grid_remove()
    word=r.choice(words)
    for x in range(0,len(word)):
        labels[x].grid(row=1,column=x)
        labels[x].config(font=("Arial",40),bg='black',fg='black',text=word[x])
        labels[x].config(width=3)
    lbltaken.config(text=' ')
    misses=0
    hits=0
    taken=" "
    lblman.config(image=pics[0])
    btnres.grid_remove()
    btn.grid(row=2,column=0)


#list of up to 10 labels used for letters of a word
labels=[tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label(),tk.Label()]
pics=[]
pics.append(tk.PhotoImage(file="pic0.gif"))
pics.append(tk.PhotoImage(file="pic1.gif"))
pics.append(tk.PhotoImage(file="pic2.gif"))
pics.append(tk.PhotoImage(file="pic3.gif"))
pics.append(tk.PhotoImage(file="pic4.gif"))
pics.append(tk.PhotoImage(file="pic5.gif"))
pics.append(tk.PhotoImage(file="pic6.gif"))
#btn and entry to submit a guess
btn=tk.Button(text="Submit",command=go)
btnres=tk.Button(text="Play Again",command=reset)
txtlet=tk.Entry(width=5)

#labels to show list of taken letters
lbll=tk.Label(text="Picked: ")
lbltaken=tk.Label(text=' ',bg='black',fg='white',width=30)

lblman = tk.Label(image=pics[0])

#config and place up to 10 labels on the grid, row 1
for x in range(0,len(word)):
    app.columnconfigure(x,pad=5)
    labels[x].config(font=("Arial",40),bg='black',fg='black',text=word[x])
    labels[x].config(width=3)
    labels[x].grid(row=1,column=x)
                     

#step 4 place widgets on grid
txtlet.grid(row=2, column=1) 
btn.grid(row=2, column=0)
lbll.grid(row=2, column=2)
lbltaken.grid(row=2, column=3,columnspan=3)
lblman.grid(row=3, column=3,columnspan=2)

