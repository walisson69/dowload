import yt_dlp
import tkinter as tk
from tkinter import messagebox as msg
import instaloader as ig

def baixar_instagram():
    loader = ig.Instaloader()

    url_post = entrada_insta.get()

    shortcode = url_post.split("/")[-2]

    try:
        post = ig.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target="downloads")
        msg.showinfo('Tudo certo', 'Download concluido')

    except Exception as e:
        msg.showerror('Erro!!', 'Cuidado essa parte so faz download de links de videos do insta')


def baixar_youtube():
    try:
        url = entrada_link_yt.get() 
        if url:  
            ydl_opts = {
                'format': 'best',  
                'outtmpl': '%(title)s.%(ext)s',
                'merge_output_format': 'mp4',  
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    except:
        msg.showerror('ERRO!!', 'Cuidado essa parte so faz download de links de videos do youtube')

janela = tk.Tk()
janela.title('Tela inicial')
janela.minsize(300, 250)
janela.resizable(False, False)

entrada_link_yt = tk.Entry(janela)
entrada_link_yt.pack(pady=10)

baixaryoutube = tk.Button(janela, text='Youtube', command=baixar_youtube)
baixaryoutube.pack(pady=10)

entrada_insta = tk.Entry(janela)
entrada_insta.pack(pady=10)

baixarintagram = tk.Button(janela, text='Instagram', command=baixar_instagram)
baixarintagram.pack(pady=10)


janela.mainloop()