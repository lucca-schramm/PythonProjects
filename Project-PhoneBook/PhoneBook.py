import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

co0 = "#2e2d2b"  # Preta
co1="#ffffff"
global txt_edit
def open_file():
    global txt_edit
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit=eval(text)
    window.title(f"Cadastro de Lista Telefônica - {filepath}")
    mostrar()


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = str(txt_edit)
        output_file.write(text)
    window.title(f"Cadastro de Lista Telefônica - {filepath}")
    mostrar()
    
def salvar():
    nome=NameEntry.get()
    telefone=TelEntry.get()
    if (nome=='') or (telefone == ''):
        raise ValueError("Erro! Você esqueceu de inserir alguma informação!")
    else:
        txt_edit[nome]=telefone
    mostrar()

window = tk.Tk()
window.title("Cadastro de Lista Telefônica")
window.geometry('500x400')
window.resizable(False, False)

frameCima = tk.Frame(window, width=500, height=40,  relief="flat")
frameCima.grid(row=0, column=0)
txt_edit={}
btn_open = tk.Button(frameCima, text="Open", command=open_file)
btn_save = tk.Button(frameCima, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frameMeio = tk.Frame(window,width=500, height=110, pady=0, relief="flat", bg=co1)
frameMeio.grid(row=1, column=0,pady=0, padx=0, sticky="NSEW")
NameLb = tk.Label(frameMeio, text = 'Nome*', bg = '#ffffff')
NameLb.place(x = 30, y = 0.01)
NameEntry = tk.Entry(frameMeio, bg='#f7f7f7')
NameEntry.place(x = 30, y = 25, width = 200, height = 25)       
TelLB = tk.Label(frameMeio,text = 'Telefone', bg = '#ffffff')
TelLB.place(x = 250, y = 0.01)
TelEntry = tk.Entry(frameMeio, bg = '#f7f7f7')
TelEntry.place(x = 250, y = 25, width = 200, height = 25)
SubmitBtn = tk.Button(frameMeio, text = 'Cadastrar', command=salvar)
SubmitBtn.place(x = 180, y = 58, width = 105, height = 35) 

frameDireita = tk.Frame(window,width=500, height=200, relief="flat")
frameDireita.grid(row=2, column=0, sticky="NSEW")

def mostrar():
    tabela_head = ['Nome',  'Telefone']
    global txt_edit
    tree = ttk.Treeview(frameDireita, selectmode="extended",columns=tabela_head, show="headings")
    vsb=ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)

    tree.grid(column=0, row=0, sticky='NSEW')
    tree.configure(yscrollcommand=vsb.set)
    
    vsb.grid(column=1,row=0,sticky='ns')
    

    hd=["center","center"]
    h=[240,240]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor="center")

        tree.column(col, width=h[n],anchor=hd[n])

        n+=1
    
    for i in txt_edit:
        tree.insert("","end",values=(i,txt_edit[i]))

mostrar()
window.mainloop()