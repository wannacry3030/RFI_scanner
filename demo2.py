import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#root window
root = tk.Tk()
root.geometry('300x120')
root.title('Demo da GUI')


#definindo a função progresso
def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='Progresso concluido!')

#defindo a função stop
def stop():
    pb.stop()
    value_label['text'] = update_progress_label()

#criando a barra de progresso, 280 pixels e modo indeterminado
pb = ttk.Progressbar(
  root,
  orient='horizontal',
  mode='determinate',
  length=280
)

#definindo o progress_label
def update_progress_label():
    return f"Progresso atual: {pb['value']}%"

#criando a label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)
        
#organizando visualmente
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

#passando o metodo progressbar.start pro botao de start
start_button = ttk.Button(
  root,
  text='Progresso',
  command=progress
)
#organizando visualmente
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

#passando o metodo stop pro botao stop
stop_button = ttk.Button(
  root,
  text='Stop',
  command=pb.stop
)
#organizando visualmente
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

root.mainloop()