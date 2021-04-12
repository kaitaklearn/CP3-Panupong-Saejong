from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import ttk


def ConvertRate(event):
    result = float(money_input.get()) * currency_rate.get_rate(list_currency_first.get(), list_currency_second.get())
    result_label.configure(text=str(round(result, 2)))


currency_rate = CurrencyRates()
#create_GUI
main_window = Tk()
main_window.option_add("*Font", "consolas 15")
main_window.geometry("350x200")
main_window.title("อัตราแลกเปลี่ยนเงินตรา")
#label_first
label_first = Label(main_window, text="สกุลเงิน")
label_first.grid(row=0, column=0)
list_currency_first = ttk.Combobox(main_window,
                                   value=list(currency_rate.get_rates("").keys()),
                                   width=8, state="readonly")
list_currency_first.current(10)
list_currency_first.grid(row=0, column=1)
#input_money
money_label = Label(main_window, text="จำนวนเงิน")
money_label.grid(row=1, column=0)
money_input = Entry(main_window, width=10, bg="#FFFFCC")
money_input.grid(row=1, column=1)
#label_second
label_second = Label(main_window, text="แปลงเป็น")
label_second.grid(row=2, column=0)
list_currency_second = ttk.Combobox(main_window,
                                    value=list(currency_rate.get_rates("").keys()),
                                    width=8, state="readonly")
list_currency_second.current(29)
list_currency_second.grid(row=2, column=1)
#button
convert_button = Button(main_window, text="คำนวณ")
convert_button.grid(row=3, column=0)
convert_button.bind("<Button-1>", ConvertRate)
#result
result_label = Label(main_window, text="ผลลัพธ์")
result_label.grid(row=3, column=1)

main_window.mainloop()