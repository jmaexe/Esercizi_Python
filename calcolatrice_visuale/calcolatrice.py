#prima inserire i due numeri e poi cliccare sull'operazione desiderata
#gestione controllo errori nel caso non siano numeri, nel caso si inserisca 0 come secondo numero nella divisione
import tkinter as tk

window = tk.Tk()
window.geometry('1280x720')
window.title("prova")
window.resizable(True, True)
window.configure(background="black")

def calcola(operazione) : 
    if numBox1.get() == "" or numBox2.get() == "":
        risultato_label.config(text="Devi inserire due numeri")
        return
    try:
        num1 = float(numBox1.get())
        num2 = float(numBox2.get())
    except ValueError:
        return
    if operazione == '+':
        risultato = num1 + num2
    elif operazione == '-':
        risultato = num1 - num2
    elif operazione == 'x':
        risultato = num1 * num2
    elif operazione == '/':
        if num2 == 0:
            risultato = "Non puoi dividere per zero"
            risultato_label.config(text="Non puoi dividere per zero")
            return  
        else:
            risultato = num1 / num2
    else:
        risultato = "Operazione non valida"
    risultato_label.config(text="Risultato: " + str(risultato))

label1 = tk.Label(window, text="Inserisci il primo numero:",)
label1.grid(row=0, column=0)
numBox1 = tk.Entry(window)
numBox1.grid(row=1, column=0)

label2 = tk.Label(window, text="Inserisci il secondo numero:")
label2.grid(row=0, column=3)
numBox2 = tk.Entry(window)
numBox2.grid(row=1, column=3)
bottoni = ['x','/','+','-']

i = 4
for bottone in bottoni : 
    bottone = tk.Button(window, text=bottone, command= lambda operazione=bottone: calcola(operazione))
    bottone.grid(row=0, column=i)
    i+=1



risultato_label = tk.Label(window, text="Risultato:")
risultato_label.grid(row=1, column=4)


if __name__ == "__main__":
    window.mainloop()

