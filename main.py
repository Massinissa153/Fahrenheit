# Write a python GUI program using tkinter module to input temperature in entry widget that is in a text box and convert to temperature in celsius
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Celsius to fahrenheit")
    window.geometry("375x200")
    # create a label with text Enter Miles
    label1 = tk.Label(window, text="Enter Temperature in celsius:")
    # create a label with text Kilometers:
    label2 = tk.Label(window, text="Fahrenheit:")
    # place label1 in window at position x,y
    label1.place(x=50, y=30)
    # create an Entry widget (text box)
    textbox1 = tk.Entry(window, width=12)
    # place textbox1 in window at position x,y
    textbox1.place(x=220, y=35)
    # place label2 in window at position x,y
    label2.place(x=50, y=100)
    # create a label3 with empty text:
    label3 = tk.Label(window, text=" ")
    # place label3 in window at position x,y
    label3.place(x=180, y=100)

    def btn1_click():
        Celsius = round(float(textbox1.get()) * 9 / 5 + 32)
        label3.configure(text=str(Celsius) + ' C')

    def btn2_click():
        window.destroy()

    # create a button with text Button 1
    btn1 = tk.Button(window, text="Click Me To Convert", command=btn1_click)
    # place this button in window at position x,y
    btn1.place(x=90, y=150)
    btn2 = tk.Button(window, text="Exit", command=btn2_click)
    btn2.place(x=250, y=150)
    window.mainloop()

main()
