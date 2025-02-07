import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import threading

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira um link do YouTube.")
        return
    
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return  # Usuário cancelou a seleção de pasta

    try:
        yt = YouTube(url, on_progress_callback=update_progress)
        if quality_var.get() == "Melhor Qualidade":
            stream = yt.streams.get_highest_resolution()
        elif quality_var.get() == "Apenas Áudio":
            stream = yt.streams.get_audio_only()
        else:
            stream = yt.streams.get_lowest_resolution()
        
        progress_bar["value"] = 0
        status_label.config(text="Baixando...")
        root.update_idletasks()

        threading.Thread(target=lambda: download_thread(stream, folder_selected)).start()
    
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao obter vídeo: {e}")

def download_thread(stream, folder_selected):
    try:
        stream.download(output_path=folder_selected)
        status_label.config(text="Download concluído!")
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro no download: {e}")

def update_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    progress_bar["value"] = percent
    root.update_idletasks()

# Criando a interface
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x300")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True, fill="both")

ttk.Label(frame, text="Insira o link do vídeo:").pack(anchor="w")
url_entry = ttk.Entry(frame, width=50)
url_entry.pack(pady=5)

ttk.Label(frame, text="Escolha a qualidade:").pack(anchor="w")
quality_var = tk.StringVar(value="Melhor Qualidade")
quality_options = ["Melhor Qualidade", "Apenas Áudio", "Qualidade Baixa"]
quality_menu = ttk.Combobox(frame, textvariable=quality_var, values=quality_options, state="readonly")
quality_menu.pack(pady=5)

download_button = ttk.Button(frame, text="Baixar", command=download_video)
download_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, length=300, mode="determinate")
progress_bar.pack(pady=5)

status_label = ttk.Label(frame, text="", foreground="blue")
status_label.pack()

root.mainloop()
