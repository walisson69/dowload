from pytube import YouTube
from tkinter import messagebox
import tkinter

class DownloadVideos():
    def __init__(self):
        self.main_window()

    def download_video(self):
        try:
            self.url = self.input.get()
            self.youtube = YouTube(self.url)
            self.video = self.youtube.streams.get_highest_resolution()
            messagebox.INFO('Tudo certo', 'Fazendo o download')
            self.video.download()
            messagebox.INFO('Tudo certo', 'Download concluido')

        except Exception as e:
            self.button = tkinter.Button(self.window, text="Fazer download", command=self.download_video)


    def main_window(self):
        self.window = tkinter.Tk()
        self.window.title('Download de videos')
        self.window.geometry("400x200")  
        self.window.resizable(False, False)

        self.input = tkinter.Entry(self.window, width=40)
        self.input.pack(pady=20)

        self.button = tkinter.Button(self.window, text="Fazer download", command=self.download_video)
        self.button.pack(pady=10)

        self.window.mainloop()


if __name__ == '__main__':
    init = DownloadVideos()