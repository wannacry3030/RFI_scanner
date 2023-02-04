import tkinter as tk
from tkinter import ttk

#root window
root = tk.Tk()
root.geometry('300x120')
root.title('Demo da GUI')

root.grid()

#criando a barra de progresso, 280 pixels e modo indeterminado
pb = ttk.Progressbar(
  root,
  orient='horizontal',
  mode='indeterminate',
  length=280
)
#organizando visualmente
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

#passando o metodo progressbar.start pro botao de start
start_button = ttk.Button(
  root,
  text='Start',
  command=pb.start
)
#organizando visualmente
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

#passando o metodo stop pro botao stop
stop_button = ttk.Button(
  root,
  text='Stop',
  command=pb.stop
)
#organizando visualmente
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

root.mainloop()