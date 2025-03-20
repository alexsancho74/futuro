import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Visual")
        
        self.text_input = tk.StringVar()
        self.operator = ""
        
        self.display = tk.Entry(master, textvariable=self.text_input, font=('Arial', 20, 'bold'),
                                bd=30, insertwidth=4, width=14, borderwidth=4, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', 'C', '=', '/'
        ]
        
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, padx=20, pady=20,
                               font=('Arial', 20, 'bold'),
                               command=lambda bt=button_text: self.button_click(bt))
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        if value == 'C':
            self.operator = ""
            self.text_input.set("")
        elif value == "=":
            try:
                result = str(eval(self.operator))
                self.text_input.set(result)
                self.operator = result
            except Exception:
                self.text_input.set("Error")
                self.operator = ""
        else:
            self.operator += str(value)
            self.text_input.set(self.operator)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()