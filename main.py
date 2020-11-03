from tkinter import *
from tkinter import messagebox
import time

tk = Tk()
app_running = True

size_canvas_x = 800
size_canvas_y = 800
kletok_po_x = kletok_po_y = 7
step_x = size_canvas_x // kletok_po_x
step_y = size_canvas_y // kletok_po_y
size_canvas_x = step_x * kletok_po_x
size_canvas_y = step_y * kletok_po_y

menu_x = 250


def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Ты чё уже уходишь?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Игра Морско  бой")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_y, size_canvas_y, fill="#fafaf1")
canvas.pack()
tk.update()


def draw_table():
    for i in range(0, kletok_po_x + 1):
        canvas.create_line(step_x * i, 0, step_y * i, size_canvas_y)

    for i in range(0, kletok_po_x + 1):
        canvas.create_line(0, step_y * i, size_canvas_y, step_x * i)


draw_table()


def button_shou_enemy():
    pass


def button_begin_again():
    pass


b0 = Button(tk, text="Показать корабли противника", command=button_shou_enemy)
b0.place(x=size_canvas_x + 20, y=30)

b1 = Button(tk, text="Начать заново", command=button_begin_again)
b1.place(x=size_canvas_x + 20, y=100)


def add_to_all(event):
    _type = 0  # ЛКМ
    if event.num == 3:
        _type = 1  # ПКМ
    #print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    #print(mouse_x, mouse_y)
    idp_x = mouse_x // step_x
    idp_y = mouse_y // step_y
    print(idp_x, idp_y, "_type", _type)


canvas.bind_all("<Button-1>", add_to_all)  # левая кнопка мыши
canvas.bind_all("<Button-3>", add_to_all)  # правая кнопка мыши

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
