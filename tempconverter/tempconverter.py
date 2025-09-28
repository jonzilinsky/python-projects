import tkinter as tk

window = tk.Tk()
window.title("Temp Converter")
window.option_add("*Font", ("Arial", 15))

answer = 0
temp = ["celsius to fahrenheit",
        "celsius to kelvin",
        "fahrenheit to celsius",
        "fahrenheit to kelvin"]

dropdown = tk.StringVar()
dropdown.set("fahrenheit to celsius")
drop = tk.OptionMenu(window, dropdown, *temp)

output = tk.Label(window,text=answer)
entry = tk.Entry(window)

def submit(event=None):
  uinput = entry.get()
  try:
    answer = float(uinput)
  except ValueError:
    output.config(text="Invalid"); return
  if dropdown.get() == "celsius to fahrenheit":
    answer = (float(uinput) * 9/5) + 32
    output.config(text=round(answer,4))
  elif dropdown.get() == "fahrenheit to celsius":
    answer = (float(uinput) - 32) * 5/9
    output.config(text=round(answer,4))
  elif dropdown.get() == "fahrenheit to kelvin":
    answer = (float(uinput) - 32) * 5/9 + 273.15
    output.config(text=round(answer,4))
  elif dropdown.get() == "celsius to kelvin":
    answer = (float(uinput) + 273.15)
    output.config(text=round(answer,4))
  else:
    output.config(text="Error: cannot convert")

button = tk.Button(window,text='Submit',
  command=submit,
  activebackground='green')

entry.pack(padx=30, pady=10)
drop.pack(padx=30, pady=10)
output.pack(padx=30, pady=10)
button.pack(padx=30, pady=10)

entry.focus_set()
window.bind("<Return>", submit)
window.bind("<KP_Enter>", submit)

window.mainloop()
