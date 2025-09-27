import turtle
import tkinter as tk
import time

# Janela

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.tracer(0)
screen.title("Geometry")
root = turtle.getcanvas().winfo_toplevel()

# Referenciais

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-1000, 0)
t.pendown()
t.goto(1000, 0)
t.penup()
t.goto(0, 1000)
t.pendown()
t.goto(0, -1000)
t.penup()
t.goto(2, -11)
t.pendown()
t.write(arg="o")
t.penup()
t.goto(5, 370)
t.pendown()
t.write(arg="y,z")
t.penup()
t.goto(285, -15)
t.pendown()
t.write(arg="x")
t.penup()

objects = []


def object_list():
    def destroy():
        ok.destroy()
        refresh.destroy()
        listbox.destroy()
        list1.destroy()
        list_button.pack(side="right", anchor="s")

    list1 = tk.Toplevel(root)
    listbox = tk.Listbox(list1, width=100, height=20)
    listbox.grid(row=0, column=0, rowspan=2)
    ok = tk.Button(list1, text="Exit", command=destroy)
    ok.grid(row=0, column=1)

    def update_list():
        for item in objects:
            listbox.insert(tk.END, item)

    update_list()
    refresh = tk.Button(list1, text="Refresh", command=update_list)
    refresh.grid(row=1, column=1)


def add_inf_line():
    name_inf_line = screen.textinput(prompt="Name", title="New Infinite Line")
    inf_line_dot1_x = screen.numinput(prompt="X of dot 1: ", title="New Infinite Line")
    inf_line_dot1_y = screen.numinput(prompt="Y of dot 1: ", title="New Infinite Line")
    inf_line_dot1_z = screen.numinput(prompt="Z of dot 1: ", title="New Infinite Line")
    inf_line_dot2_x = screen.numinput(prompt="X of dot 2: ", title="New Infinite Line")
    inf_line_dot2_y = screen.numinput(prompt="Y of dot 2: ", title="New Infinite Line")
    inf_line_dot2_z = screen.numinput(prompt="Z of dot 2: ", title="New Infinite Line")
    inf_line_dot1_x = -inf_line_dot1_x * 30
    inf_line_dot1_y = -inf_line_dot1_y * 30
    inf_line_dot1_z = inf_line_dot1_z * 30
    inf_line_dot2_x = -inf_line_dot2_x * 30
    inf_line_dot2_y = -inf_line_dot2_y * 30
    inf_line_dot2_z = inf_line_dot2_z * 30
    t.penup()
    t.goto(inf_line_dot1_x, inf_line_dot1_y)
    t.pendown()
    t.dot(4)
    t.penup()
    t.goto(inf_line_dot1_x, inf_line_dot1_z)
    t.pendown()
    t.dot(4)
    t.penup()
    t.goto(inf_line_dot2_x, inf_line_dot2_y)
    t.pendown()
    t.dot(4)
    t.penup()
    t.goto(inf_line_dot2_x, inf_line_dot2_z)
    t.pendown()
    t.dot(4)
    t.penup()
    if inf_line_dot1_x == inf_line_dot2_x:
        declive_line_1 = "Inf."
        declive_line_2 = "Inf."
        t.penup()
        t.goto(inf_line_dot1_x, 0)
        t.pendown()
        t.goto(inf_line_dot1_x, 10000)
        t.penup()
        t.goto(inf_line_dot2_x, 0)
        t.pendown()
        t.goto(inf_line_dot2_x, -10000)
        t.penup()
        t.goto(inf_line_dot1_x + 2, 0)
        t.pendown()
        t.dot(4)
        t.write("F1" + name_inf_line, font=('Arial', 7, 'normal'))
        t.dot(4)
        t.penup()
        t.goto(inf_line_dot1_x + 2, -15)
        t.pendown()
        t.write("H2" + name_inf_line, font=('Arial', 7, 'normal'))
        t.penup()
        t.goto(inf_line_dot1_x + 2, 300)
        t.pendown()
        t.write(arg=name_inf_line + "1≡" + name_inf_line + "2", font=('Arial', 8, 'normal'))
    else:
        declive_line_1 = (inf_line_dot1_y - inf_line_dot2_y) / (inf_line_dot1_x - inf_line_dot2_x)
        declive_line_2 = (inf_line_dot1_z - inf_line_dot2_z) / (inf_line_dot1_x - inf_line_dot2_x)
        objects.append(
            "Inf.Line: " + name_inf_line + "((" + str(inf_line_dot1_x / 30) + "," + str(inf_line_dot1_y / 30) + ","
            + str(inf_line_dot1_z / 30) + ")->(" + str(inf_line_dot2_x / 30) + "," + str(inf_line_dot2_y / 30)
            + "," + str(inf_line_dot2_z / 30) + ")), " + "Declive(" + name_inf_line + ")1: "
            + str(declive_line_1) + "; Declive(" + name_inf_line + ")2: " + str(declive_line_2))

        def inf_line(name, onex, oney, onez, twox, twoy, twoz):
            t.width(1)
            t.color(0, 0, 0)
            t.penup()
            t.goto(onex - (1 * 10000), oney + (-declive_line_1 * 10000))
            t.pendown()
            t.goto(twox + (1 * 10000), twoy + (declive_line_1 * 10000))
            t.penup()
            t.goto(onex - (1 * 10000), onez + (-declive_line_2 * 10000))
            t.pendown()
            t.goto(twox + (1 * 10000), twoz + (declive_line_2 * 10000))
            t.penup()
            t.goto(onex - (1 * 50), oney + (-declive_line_1 * 50))
            t.pendown()
            t.write(arg=name + "1", font=('Arial', 8, 'normal'))
            t.penup()
            t.goto(onex - (1 * 50), onez + (-declive_line_2 * 50))
            t.pendown()
            t.write(arg=name + "2", font=('Arial', 8, 'normal'))
            t.penup()
            # --------------------------------------------------------------------------------------------------------------
            # Pontos de interseção da reta com plano horizontal e o plano frontal
            # --------------------------------------------------------------------------------------------------------------
            # Descobrir B1
            b1 = oney - (declive_line_1 * onex)
            # Descobrir B2
            b2 = twoz - (declive_line_2 * twox)
            if declive_line_1 != 0:
                # X quando y = 0 1
                x1 = (0 - b1) / declive_line_1
                # F1
                t.penup()
                t.goto(x1, 0)
                t.pendown()
                t.dot(4)
                t.write("F1" + name, font=('Arial', 7, 'normal'))
                t.penup()
                # Descobrir Y2 f2 quando x1 = 0
                y2 = declive_line_2 * x1 + b2
                # F2
                t.goto(x1, y2)
                t.pendown()
                t.dot(4)
                t.write("F2" + name, font=('Arial', 7, 'normal'))
                t.fillcolor("#33cc8c")
                t.penup()
                t.goto(x1, 0)
                t.pendown()
                t.goto(x1, y2)
                t.penup()
            if declive_line_2 != 0:
                # X quando y = 0  2
                x2 = (0 - b2) / declive_line_2
                # H2
                t.penup()
                t.goto(x2, 0)
                t.pendown()
                t.dot(4)
                t.write("H2" + name, font=('Arial', 7, 'normal'))
                t.penup()
                # Descobrir quando y2 = 0
                y1 = declive_line_1 * x2 + b1
                # H1
                t.penup()
                t.goto(x2, y1)
                t.pendown()
                t.dot(4)
                t.write("H1" + name, font=('Arial', 7, 'normal'))
                t.penup()
                t.goto(x2, 0)
                t.pendown()
                t.goto(x2, y1)
                t.penup()
            # Draw the lines between H1, H2; F1, F2

        inf_line(name_inf_line, inf_line_dot1_x, inf_line_dot1_y, inf_line_dot1_z, inf_line_dot2_x, inf_line_dot2_y,
                 inf_line_dot2_z)


def add_line():
    name_line = screen.textinput(prompt="Name: ", title="New line")
    line_dot1_x = screen.numinput(prompt="X of dot 1: ", title="New Line")
    line_dot1_y = screen.numinput(prompt="Y of dot 1: ", title="New Line")
    line_dot1_z = screen.numinput(prompt="Z of dot 1: ", title="New Line")
    line_dot2_x = screen.numinput(prompt="X of dot 2: ", title="New Line")
    line_dot2_y = screen.numinput(prompt="Y of dot 2: ", title="New Line")
    line_dot2_z = screen.numinput(prompt="Z of dot 2: ", title="New Line")
    line_dot1_x = -(line_dot1_x * 30)
    line_dot1_y = -(line_dot1_y * 30)
    line_dot1_z = line_dot1_z * 30
    line_dot2_x = -(line_dot2_x * 30)
    line_dot2_y = -(line_dot2_y * 30)
    line_dot2_z = line_dot2_z * 30

    def line(name, onex, oney, onez, twox, twoy, twoz):
        t.penup()
        t.goto(onex, oney)
        t.pendown()
        t.goto(twox, twoy)
        t.write(name + "1")
        t.penup()
        t.goto(onex, onez)
        t.pendown()
        t.goto(twox, twoz)
        t.write(name + "2")
        t.penup()

    line(name_line, line_dot1_x, line_dot1_y, line_dot1_z, line_dot2_x, line_dot2_y, line_dot2_z)


def add_button():
    name_dot = screen.textinput(prompt="Name: ", title="New Dot")
    x_coordinate = screen.numinput(prompt="Abcissa: ", title="New Dot")
    y_coordinate = screen.numinput(prompt="Afastamento: ", title="New Dot")
    z_coordinate = screen.numinput(prompt="Cota: ", title="New Dot")
    x_coordinate = -(x_coordinate * 30)
    y_coordinate = -(y_coordinate * 30)
    z_coordinate = z_coordinate * 30

    def point(name, x, y, z):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(4)
        t.write(arg=name + "1", font=('Arial', 7, 'normal'))
        t.penup()
        t.goto(x, z)
        t.pendown()
        t.dot(4)
        t.write(arg=name + "2", font=('Arial', 7, 'normal'))

    point(name_dot, x_coordinate, y_coordinate, z_coordinate)


addition_button = tk.Button(root, text="Add Dot", command=add_button)
addition_button_line = tk.Button(root, text="Add Line", command=add_line)
addition_button_inf_line = tk.Button(root, text="Add Infinite Line", command=add_inf_line)
list_button = tk.Button(root, text="List of Objects", command=object_list)
addition_button.pack(side="left", anchor="s")
addition_button_line.pack(side="left", anchor="s")
addition_button_inf_line.pack(side="left", anchor="s")
list_button.pack(side="right", anchor="s")
turtle.mainloop()
