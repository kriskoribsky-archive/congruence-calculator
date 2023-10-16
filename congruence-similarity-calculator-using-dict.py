import tkinter as tk            #tkinter
from tkinter import font        #tkinter font

WIDTH = 700
HEIGHT = 500

#definition for triangle comparisons

def start_comparison():

    inputs = {"a": None, "b": None, "c":None, "x":None, "y":None, "z":None, "A":None, "B":None, "C":None, "X":None, "Y":None, "Z":None}   #all inputs dictionary
    f = {}                                                                                                                                #float only inputs dictionary
    
    inputs["a"] = is_float(a_entry.get())
    inputs["b"] = is_float(b_entry.get())
    inputs["c"] = is_float(c_entry.get())

    inputs["x"] = is_float(x_entry.get())
    inputs["y"] = is_float(y_entry.get())
    inputs["z"] = is_float(z_entry.get())

    inputs["A"] = is_float(uhol_A.get())
    inputs["B"] = is_float(uhol_B.get())
    inputs["C"] = is_float(uhol_C.get())

    inputs["X"] = is_float(uhol_X.get())
    inputs["Y"] = is_float(uhol_Y.get())
    inputs["Z"] = is_float(uhol_Z.get())

    print(str(inputs))
    
    for x, y in inputs.items():
        if y != None:
            f[x] = y

    print(f)

    comparison_output.delete(1.0, tk.END)

    #KONTROLA SPRÁVNOSTI UHLOV (MUSIA BYŤ MENEJ AKO 180°)
    if all (x in f for x in ("A","B","C")):
        if f["A"] + f["B"] + f["C"] == 180:
            pass
        else:
            comparison_output.insert(tk.INSERT, "Súčet uhlov trojuholníkov nie je 180°.")
            return
    
    if all (x in f for x in ("X","Y","Z")):
        if f["X"] + f["Y"] + f["Z"] == 180:
            pass
        else:
            comparison_output.insert(tk.INSERT, "Súčet uhlov trojuholníkov nie je 180°.")
            return

    #ZHODNOSŤ TROJUHOLNÍKOV
        #veta (sss)
    if all (x in f for x in ("a","b","c","x","y","z")):
        
        if f["a"] == f["x"] and f["b"] == f["y"] and f["c"] == f["z"]:
            comparison_output.insert(tk.INSERT, "Trojuholníky sú zhodné podľa vety (sss)")
        else:
            pass

        #veta (sus)
    if ()




#definition for entry-to-float conversion

def is_float(entry):
    
    try:
        float(entry)
        return float(entry)
    except:
        return

  


#tkinter GUI
window = tk.Tk()
window.resizable(False, False)
window.title("Zhodnosť a podobnosť trojuholníkov")

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="D:/Programovanie/Python - programy/Matematika/Zhodnosť a podobnosť trojuholníkov/background_image.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

#first frame (first triangle on the left, angle inputs)
first_frame = tk.Frame(window, bg="#aeaeb5")
first_frame.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.4, anchor="nw")

first_label = tk.Label(first_frame, text="Prvý trojuholník (▲ABC)", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
first_label.place(relx=0.5, rely=0.01, relwidth=0.6, relheight=0.13, anchor="n")

first_triangle = tk.Canvas(first_frame, bg="#aeaeb5")
first_triangle.place(relx=0.5, rely=0.55, relwidth=0.8, relheight=0.8, anchor="c")
first_triangle.create_polygon(20,150, 205,150, 115,14, fill="#aeaeb5", outline="black", width=2) 

first_instruction = tk.Label(first_frame, text="Uhly v stupňoch:", font=("Calibri Light",8), bg="#aeaeb5")
first_instruction.place(relx=0.28, rely=0.3, relwidth=0.28, relheight=0.1, anchor="c")

uhol_A = tk.Entry(first_triangle, font=("Calibri Light", 11))
uhol_A.place(relx=0.08, rely=0.8, relwidth=0.15, relheight=0.15)

uhol_B = tk.Entry(first_triangle, font=("Calibri Light", 11))
uhol_B.place(relx=0.76, rely=0.8, relwidth=0.15, relheight=0.15)

uhol_C = tk.Entry(first_triangle, font=("Calibri Light", 11))
uhol_C.place(relx=0.515, rely=0.1, relwidth=0.15, relheight=0.15, anchor="c")

a_triangle = tk.Label(first_triangle, text="a", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
a_triangle.place(relx=0.7, rely=0.35, relwidth=0.05, relheight=0.1)

b_traingle = tk.Label(first_triangle, text="b", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
b_traingle.place(relx=0.25, rely=0.35, relwidth=0.05, relheight=0.1)

c_triangle = tk.Label(first_triangle, text="c", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
c_triangle.place(relx=0.5, rely=0.8, relwidth=0.05, relheight=0.1)

#second frame (second triangle on the right, angle inputs)
second_frame = tk.Frame(window, bg="#aeaeb5")
second_frame.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4, anchor="nw")

second_label = tk.Label(second_frame, text="Druhý trojuholník (▲XYZ)", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
second_label.place(relx=0.5, rely=0.01, relwidth=0.6, relheight=0.13, anchor="n")

second_triangle = tk.Canvas(second_frame, bg="#aeaeb5")
second_triangle.place(relx=0.5, rely=0.55, relwidth=0.8, relheight=0.8, anchor="c")
second_triangle.create_polygon(20,150, 205,150, 115,14, fill="#aeaeb5", outline="black", width=2) 

second_instruction = tk.Label(second_frame, text="Uhly v stupňoch:", font=("Calibri Light",8), bg="#aeaeb5")
second_instruction.place(relx=0.28, rely=0.3, relwidth=0.28, relheight=0.1, anchor="c")

uhol_X = tk.Entry(second_triangle, font=("Calibri Light", 11))
uhol_X.place(relx=0.08, rely=0.8, relwidth=0.15, relheight=0.15)

uhol_Y = tk.Entry(second_triangle, font=("Calibri Light", 11))
uhol_Y.place(relx=0.76, rely=0.8, relwidth=0.15, relheight=0.15)

uhol_Z = tk.Entry(second_triangle, font=("Calibri Light", 11))
uhol_Z.place(relx=0.515, rely=0.1, relwidth=0.15, relheight=0.15, anchor="c")

x_triangle = tk.Label(second_triangle, text="x", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
x_triangle.place(relx=0.7, rely=0.35, relwidth=0.05, relheight=0.1)

y_triangle = tk.Label(second_triangle, text="y", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
y_triangle.place(relx=0.25, rely=0.35, relwidth=0.05, relheight=0.1)

z_triangle = tk.Label(second_triangle, text="z", font=("Arial Rounded MT Bold", 10), bg="#aeaeb5")
z_triangle.place(relx=0.5, rely=0.8, relwidth=0.05, relheight=0.1)

#third frame (sides of triangle ABC input, instructions)
third_frame = tk.Frame(window, bg="#aeaeb5")
third_frame.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.14, anchor="nw")

third_label = tk.Label(third_frame, bg="#aeaeb5", text="Zadajte známe strany 1. trojuholníka:", font=("Arial Rounded MT Bold", 10))
third_label.place(relx=0, rely=0, relwidth=1, relheight=0.5, anchor="nw")

a_label = tk.Label(third_frame, bg="#aeaeb5", text="a=", font=("Arial Rounded MT Bold", 10))
a_label.place(relx=0.1, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

a_entry = tk.Entry(third_frame, font=("Calibri Light", 11))
a_entry.place(relx=0.2, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

b_label = tk.Label(third_frame, bg="#aeaeb5", text="b=", font=("Arial Rounded MT Bold", 10))
b_label.place(relx=0.4, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

b_entry = tk.Entry(third_frame, font=("Calibri Light", 11))
b_entry.place(relx=0.5, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

c_label = tk.Label(third_frame, bg="#aeaeb5", text="c=", font=("Arial Rounded MT Bold", 10))
c_label.place(relx=0.7, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

c_entry = tk.Entry(third_frame, font=("Calibri Light", 11))
c_entry.place(relx=0.8, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

#fourth frame (sides of triangle XYZ input, instructions)
fourth_frame = tk.Frame(window, bg="#aeaeb5")
fourth_frame.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.14, anchor="nw")

fourth_label = tk.Label(fourth_frame, bg="#aeaeb5", text="Zadajte známe strany 2.trojuholníka:", font=("Arial Rounded MT Bold", 10))
fourth_label.place(relx=0, rely=0, relwidth=1, relheight=0.5, anchor="nw")

x_label = tk.Label(fourth_frame, bg="#aeaeb5", text="x=", font=("Arial Rounded MT Bold", 10))
x_label.place(relx=0.1, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

x_entry = tk.Entry(fourth_frame, font=("Calibri Light", 11))
x_entry.place(relx=0.2, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

y_label = tk.Label(fourth_frame, bg="#aeaeb5", text="y=", font=("Arial Rounded MT Bold", 10))
y_label.place(relx=0.4, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

y_entry = tk.Entry(fourth_frame, font=("Calibri Light", 11))
y_entry.place(relx=0.5, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

z_label = tk.Label(fourth_frame, bg="#aeaeb5", text="z=", font=("Arial Rounded MT Bold", 10))
z_label.place(relx=0.7, rely=0.75, relwidth=0.05, relheight=0.5, anchor="c")

z_entry = tk.Entry(fourth_frame, font=("Calibri Light", 11))
z_entry.place(relx=0.8, rely=0.75, relwidth=0.14, relheight=0.3, anchor="c")

#fifth frame (compare button, degree of similarity output)
fifth_frame = tk.Frame(window, bg="#aeaeb5")
fifth_frame.place(relx=0.05, rely=0.7, relwidth=0.6, relheight=0.25, anchor="nw")

comparison_output = tk.Text(fifth_frame, font=("Bahnschrift", 12))
comparison_output.place(relx=0.01, rely=0.95, relwidth=0.98, relheight=0.65, anchor="sw")

convert_button = tk.Button(fifth_frame, bg="#aeaeb5", text="Porovnaj trojuholníky", font=("Arial Rounded MT Bold", 10), command=lambda: start_comparison())
convert_button.place(relx=0.01, rely=0.02, relwidth=0.4, relheight=0.25, anchor="nw")

window.mainloop()
