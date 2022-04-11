import tkinter as tk

def celsius_to_fahrenheit():
    """Convert the value for Celsius to Fahrenheit and insert the
    result into lbl_result.
    """
    celsius = ent_temperature.get()
    fahrenheit = (9 / 5) * float(celsius) + 32
    lbl_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=True, height=True)

# Create the Celsius entry frame with an Entry
# widget and label in it

text = tk.StringVar()
text.set(0)

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, textvariable = text, width=20, font=("Consolas", 25))
lbl_temp = tk.Label(master=frm_entry, font=("Consolas", 25), text="\N{DEGREE CELSIUS}")


# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit,
    font=("Consolas", 20)
)
lbl_result = tk.Label(master=window, font=("Consolas", 25), text="\N{DEGREE FAHRENHEIT}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=20)
lbl_result.grid(row=0, column=2, padx=30)

# Run the application
window.mainloop()