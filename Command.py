import Code, time, threading, datetime
from keyboard import *
from tkinter import *
from Code import register_point, Logs, Permission


class Commands:
    def __init__(self, location):
        # Connexion
        self.connexion = False

        # Location
        self.locate = location

        # Globale
        self.location = Tk()
        self.location.title("Accueil")
        self.location.geometry("760x560")
        self.location.minsize(760, 560)
        self.location.maxsize(760, 560)
        self.location.config(background="#000000")

        # Import
        from Sub import Subs
        self.sub_game = Subs.Sub_game(self.location, self.connexion, self.locate)
        self.sub_points = Subs.Sub_points(self.location, self.connexion, self.locate)
        self.sub_music = Subs.Sub_music(self.location, self.connexion, self.locate)
        self.sub_youtube = Subs.Sub_youtubeur(self.location, self.connexion, self.locate)
        self.sub_programmation = Subs.Sub_programmation(self.location, self.connexion, self.locate)
        self.sub_apprendre = Subs.Sub_apprendre(self.location, self.connexion, self.locate)
        self.sub_other = Subs.Sub_other(self.location, self.connexion, self.locate)
        self.sub_scroll_bar = Subs.Sub_scroll_bar(self.location, self.locate, self.change)
        self.sub_bienvenue = Subs.Sub_bienvenue(self.location, self.locate)

        self.subs = [self.sub_game.game, self.sub_points.point, self.sub_music.music, self.sub_youtube.youtube, self.sub_programmation.programmation, self.sub_apprendre.apprendre, self.sub_other.other]

        # Thread
        self.thread1 = threading.Thread(target=self.threading_one)
        self.thread2 = threading.Thread(target=self.threading_two)
        self.thread1.start()
        self.thread2.start()
        self.sub_scroll_bar.scroll_bar.pack()
        self.sub_bienvenue.bienvenue.pack()
        self.location.protocol("WM_DELETE_WINDOW", self.caption)
        self.location.mainloop()

    def threading_one(self):
        timer = 0
        while True:
            try:
                self.sub_youtube.points.set("Points : " + str(register_point(self.locate)))
                self.sub_game.points.set("Points : " + str(register_point(self.locate)))
            except:
                Logs().Error(text="Points not initialized.", locate=self.locate)
            try:
                Permission().find_unpermission_element(self.locate)
            except:
                Logs().Error(text="Impossible de fermer les fenêtres.", locate=self.locate)
            try:
                Permission().permission_youtube(self.locate)
            except:
                Logs().Error(text="Impossible de fermer YouTube.", locate=self.locate)
            try:
                if Permission().permission_game(self.locate):
                    timer += 1
                if timer == 120:
                    timer = 0
                    Code.timer(self.locate)
                    self.sub_game.restant_time.set(str(open(f"{self.locate}/Time.txt", "r").readlines()[0]))
            except:
                Logs().Error(text="Le temps de jeu ne défile pas.", locate=self.locate)
            time.sleep(0.47)

    def threading_two(self):
        while True:
            if is_pressed("Ctrl"):
                if is_pressed("a"):
                    self.location.deiconify()
                elif is_pressed("s"):
                    self.location.withdraw()
                elif is_pressed("y"):
                    """Enregistrement vocal"""
            time.sleep(0.1)

    def caption(self):
        self.location.withdraw()

    def change(self, number):
        self.sub_bienvenue.bienvenue.pack_forget()
        for n in range(0, 7):
            if n == number:
                self.subs[n].pack()
            else:
                self.subs[n].pack_forget()