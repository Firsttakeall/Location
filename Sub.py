import os, shutil, tkinter, threading, urllib3
from tkinter import *
from PIL import Image, ImageTk
from Code import *
from datetime import date, timedelta
from pytube import YouTube


def pay(cost, locate):
    cost = int(cost)
    points = int(open(f"{locate}/Points.txt", "r").readlines()[0])
    if points >= cost:
        file = open(f"{locate}/Points.txt", "w")
        file.write(str(points - cost))
        file.close()
        return True
    else:
        return False


class Subs:
    class Sub_scroll_bar:
        def __init__(self, location, locate, change):
            self.change = change
            self.location = location
            self.scroll_bar = Canvas(self.location, width=760, height=85, bg="#181818", highlightthickness=0)
            self.image1 = PhotoImage(file=f"{locate}/Images/Jeux.png")
            self.image2 = PhotoImage(file=f"{locate}/Images/Points.png")
            self.image3 = PhotoImage(file=f"{locate}/Images/Musique.png")
            self.image4 = PhotoImage(file=f"{locate}/Images/Youtube.png")
            self.image5 = PhotoImage(file=f"{locate}/Images/Programmer.png")
            self.image6 = PhotoImage(file=f"{locate}/Images/Apprendre.png")
            self.image7 = PhotoImage(file=f"{locate}/Images/Autres.png")
            self.button1 = tkinter.Button(self.location, borderwidth=0, image=self.image1, command=lambda: self.change(0))
            self.button2 = tkinter.Button(self.location, borderwidth=0, image=self.image2, command=lambda: self.change(1))
            self.button3 = tkinter.Button(self.location, borderwidth=0, image=self.image3, command=lambda: self.change(2))
            self.button4 = tkinter.Button(self.location, borderwidth=0, image=self.image4, command=lambda: self.change(3))
            self.button5 = tkinter.Button(self.location, borderwidth=0, image=self.image5, command=lambda: self.change(4))
            self.button6 = tkinter.Button(self.location, borderwidth=0, image=self.image6, command=lambda: self.change(5))
            self.button7 = tkinter.Button(self.location, borderwidth=0, image=self.image7, command=lambda: self.change(6))
            self.sub_button1 = self.scroll_bar.create_window(20, 15, height=55, width=90, anchor="nw", window=self.button1)
            self.sub_button2 = self.scroll_bar.create_window(125, 15, height=55, width=90, anchor="nw", window=self.button2)
            self.sub_button3 = self.scroll_bar.create_window(230, 15, height=55, width=90, anchor="nw", window=self.button3)
            self.sub_button4 = self.scroll_bar.create_window(335, 15, height=55, width=90, anchor="nw", window=self.button4)
            self.sub_button5 = self.scroll_bar.create_window(440, 15, height=55, width=90, anchor="nw", window=self.button5)
            self.sub_button6 = self.scroll_bar.create_window(545, 15, height=55, width=90, anchor="nw", window=self.button6)
            self.sub_button7 = self.scroll_bar.create_window(650, 15, height=55, width=90, anchor="nw", window=self.button7)

    class Sub_bienvenue:
        def __init__(self, location, locate):
            self.location = location
            self.locate = locate
            self.bienvenue = Canvas(self.location, width=760, height=475, bg="#ffffff", highlightthickness=0)
            self.bienvenue_image = PhotoImage(file=f"{self.locate}/Images/Fond.png")
            self.bienvenue.create_image((380, 237), image=self.bienvenue_image)

    class Sub_apprendre:
        def __init__(self, location, connexion, locate):
            self.apprendre = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)

    class Sub_game:
        def __init__(self, location, connexion, locate):
            self.locate = locate
            self.game = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)
            self.affichage = Canvas(self.game, width=760, height=100, bg="#181818", highlightthickness=0)
            self.points = StringVar()
            self.points_counter = Label(self.affichage, bg="#181818", fg="#ffffff", borderwidth=4, justify="center", font=("Open Sans", 15), textvariable=self.points)
            self.affichage.create_window(150, 40, height=30, width=140, anchor="nw", window=self.points_counter)
            self.restant_time = StringVar()
            self.restant_time.set(str(open("Time.txt", "r").readlines()[0]))
            self.moretime = Button(self.affichage, bg="#EFEFEF", highlightthickness=0, borderwidth=0, text="+", command=lambda: self.more_time())
            self.affichage.create_window(434, 40, width=30, height=30, anchor="nw", window=self.moretime)
            self.time = Label(self.affichage, width=100, height=30, bg="#EFEFEF", highlightthickness=0, textvariable=self.restant_time)
            self.affichage.create_window(330, 40, width=100, height=30, anchor="nw", window=self.time)
            self.affichage.pack(side=TOP)
            self.all = Canvas(self.game, width=674, height=375, bg="#181818", highlightthickness=0)
            self.scrollbar = Scrollbar(self.game, orient=VERTICAL, command=self.all.yview, width=16)
            self.name = {"GeometryDashLite": "Geometry Dash",
                 "GeometryDashMeltdown": "Meltdown",
                 "GeometryDashSubZero": "SubZero",
                 "GeometryDashWorld": "World",
                 "LegendSlime": "Legend Slime",
                 "PocketChamps": "Pocket Champs",
                 "Pydroid3": "Pydroid 3",
                 "Rider": "Rider",
                 "SlimeWeaponMaster": "Slime Weapon",
                 "SimCity": "Sim City",
                 "Pokemon SoulSilver": "SoulSilver",
                 "Pokemon Platinum": "Platine",
                 "Link's Awakening": "Awakening",
                 "Mystery Dungeon Blue Rescue Team": "Blue Rescue",
                 "Mystery Dungeon Explorers of Sky": "Sky Explorers",
                 "Pokemon Blanche": "PKMN Blanc",
                 "Pokemon Diamond": "PKMN Diamant",
                 "Pokemon Emerald": "Emeraude",
                 "Pokemon Gold": "PKMN Gold",
                 "Pokemon White 2": "PKMN Blanc 2",
                 "The Wind Waker": "Wind Waker"}
            self.commande_1 = lambda: running("Link's Awakening.gbc", locate)
            self.commande_2 = lambda: running("Lolbeans.url", locate)
            self.commande_3 = lambda: running("Majora's Mask.n64", locate)
            self.commande_4 = lambda: running("Mystery Dungeon Blue Rescue Team.nds", locate)
            self.commande_5 = lambda: running("Mystery Dungeon Explorers of Sky.nds", locate)
            self.commande_6 = lambda: running("Ocarina of Time.n64", locate)
            self.commande_7 = lambda: running("Pokemon Blanche.nds", locate)
            self.commande_8 = lambda: running("Pokemon Diamond.nds", locate)
            self.commande_9 = lambda: running("Pokemon Emerald.gba", locate)
            self.commande_10 = lambda: running("Pokemon Gold.gbc", locate)
            self.commande_11 = lambda: running("Pokemon Gold.sa2", locate)
            self.commande_12 = lambda: running("Pokemon Gold.sav", locate)
            self.commande_13 = lambda: running("Pokemon Platinum.nds", locate)
            self.commande_14 = lambda: running("Pokemon SoulSilver.nds", locate)
            self.commande_15 = lambda: running("Pokemon White 2.nds", locate)
            self.commande_16 = lambda: running("Super Mario Galaxy (USA) (En,Fr,Es).rvz", locate)
            self.commande_17 = lambda: running("The Wind Waker.iso", locate)
            self.all_commands = [self.commande_1, self.commande_2, self.commande_3, self.commande_4, self.commande_5,
                                 self.commande_6, self.commande_7, self.commande_8, self.commande_9, self.commande_10,
                                 self.commande_11, self.commande_12, self.commande_13, self.commande_14,
                                 self.commande_15, self.commande_16, self.commande_17]
            lnk = 0
            self.all_game = []
            hauteur = 90
            for link in os.listdir(f"{locate}/Links"):
                if not (link == "Images" or link == "Unresponsable" or link[-4:len(link)] == ".sa2" or link[-4:len(link)] == ".sav"):
                    self.link = link
                    try:
                        self.photo = Image.open(f"{locate}/Links/Images/{self.link[0:len(self.link) - 4]}.png")
                        self.resize_photo = self.photo.resize((72, 72))
                        self.image = ImageTk.PhotoImage(self.resize_photo)
                        self.game_button_special = tkinter.Button(self.all, bg="#181818", borderwidth=0, justify="center", image=self.image, command=self.all_commands[lnk])
                    except:
                        self.game_button_special = tkinter.Button(self.all, bg="#181818", borderwidth=0, justify="center", command=self.all_commands[lnk])
                    try:
                        name = self.name[link[0:len(link) - 4]]
                    except:
                        name = link[0:len(link) - 4]
                    self.game_text = tkinter.Label(self.all, bg="#181818", fg="#ffffff", borderwidth=0, justify="center", font=("Helvetica", 10), text=name)
                    self.all.create_window((0 + 115 * (lnk % 6), hauteur + 76 + 130 * (lnk - (lnk % 6))/6), height=36, width=92, anchor="nw", window=self.game_text)
                    self.all.create_window((10 + 115 * (lnk % 6), hauteur + 130 * (lnk - (lnk % 6))/6), height=72, width=72, anchor="nw", window=self.game_button_special)
                    lnk += 1
                    self.all_game.append([self.link, self.photo, self.resize_photo, self.image, self.game_button_special, self.game_text])
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.all.pack(side=BOTTOM, padx=35)
            self.all.configure(yscrollcommand=self.scrollbar.set, scrollregion=self.all.bbox("all"))

        def more_time(self):
            time = int(open(f"{self.locate}/Time.txt", "r").readlines()[0])
            if pay(100, locate=self.locate):
                time += 15
                extend_time = open(f"{self.locate}/Time.txt", "w")
                extend_time.write(str(time))
                extend_time.close()
                self.restant_time.set(str(time))

    class Sub_music:
        def __init__(self, location, connexion, locate):
            self.music = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)
            self.utility = Canvas(self.music, width=760, height=100, bg="#181818", highlightthickness=0)
            self.sub_music = Canvas(self.music, width=760, height=375, bg="#181818", highlightthickness=0)
            self.scrollbar = Scrollbar(self.music, orient=VERTICAL, command=self.sub_music.yview, width=15)
            self.sub_music_one = Canvas(self.sub_music, width=745, height=100, bg="#899283", highlightthickness=0)
            self.sub_music_two = Canvas(self.sub_music, width=745, height=100, bg="#876547", highlightthickness=0)
            self.sub_music_three = Canvas(self.sub_music, width=745, height=100, bg="#faafaf", highlightthickness=0)
            self.sub_music_four = Canvas(self.sub_music, width=745, height=100, bg="#666fff", highlightthickness=0)
            self.sub_music_five = Canvas(self.sub_music, width=745, height=100, bg="#444aaa", highlightthickness=0)
            self.sub_music_five_try = self.sub_music.create_window(0, 0, anchor="nw", window=self.sub_music_five)
            self.sub_music_five.config(height=150)
            self.utility.pack()
            self.scrollbar.pack(side=RIGHT, fill=Y)
            self.sub_music.pack()
            self.sub_music.create_line(0, 0, 500, 1000)
            self.sub_music.configure(yscrollcommand=self.scrollbar.set, scrollregion=self.sub_music.bbox("all"))

    class Sub_other:
        def __init__(self, location, connexion, locate):
            self.other = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)

    class Sub_points:
        def __init__(self, location, connexion, locate):
            self.point = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)

    class Sub_programmation:
        def __init__(self, location, connexion, locate):
            self.programmation = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)

    class Sub_youtubeur:
        def __init__(self, location, connexion, locate):
            self.connexion, self.save, self.all_documents, self.location, self.locate, self.current_search, self.vid_player, self.img1, self.img2, self.img3, self.document_value, self.max_value = False, [], [], location, locate, "", "", "", "", "", 0, 0
            self.points, self.downloading, self.message = StringVar(), StringVar(), StringVar(self.location, "0 / 0")

            self.youtube = Canvas(location, width=760, height=475, bg="#181818", highlightthickness=0)

            self.searching_image = ImageTk.PhotoImage(Image.open(f"{self.locate}/Images/Search_bar.png"))
            self.searching = Label(self.youtube, bg="#181818", borderwidth=0, justify="center", image=self.searching_image)
            self.youtube.create_window(20, 0, height=40, width=175, anchor="nw", window=self.searching)

            self.search_bar = Entry(self.youtube, bg="#ffffff", fg="#000000", borderwidth=0, justify="left", font=("Open Sans", 14))
            self.youtube.create_window(35, 5, height=30, width=116, anchor="nw", window=self.search_bar)

            self.search_button = Button(self.youtube, bg="#ffffff", borderwidth=0, justify="center", text="🔎", font=("Open Sans", 12), command=lambda : self.caption())
            self.youtube.create_window(158, 5, height=30, width=30, anchor="nw", window=self.search_button)

            self.right_button = Button(self.youtube, bg="#000000", fg="#ffffff", borderwidth=0, justify="center", font=("Open Sans", 20), text=">", command=lambda : self.defile_list("+"))
            self.youtube.create_window(320, 3, height=30, width=30, anchor="nw", window=self.right_button)

            self.left_button = Button(self.youtube, bg="#000000", fg="#ffffff", borderwidth=0, justify="center", font=("Open Sans", 20), text="<", command=lambda: self.defile_list("-"))
            self.youtube.create_window(215, 3, height=30, width=30, anchor="nw", window=self.left_button)

            self.reload_search = Button(self.youtube, bg="#232322", fg="#ffffff", borderwidth=2, justify="center", font=("Open Sans", 15), text="↺", command=lambda: self.detect())
            self.youtube.create_window(360, 3, height=30, width=30, anchor="nw", window=self.reload_search)

            self.value_counter = Label(self.youtube, bg="#181818", fg="#ffffff", borderwidth=2, justify="center", font=("Open Sans", 15), textvariable=self.message)
            self.youtube.create_window(250, 3, height=30, width=65, anchor="nw", window=self.value_counter)

            self.search_youtube_bar = Entry(self.youtube, bg="#232322", fg="#ffffff", borderwidth=3, justify="center", font=("Open Sans", 10))
            self.youtube.create_window(550, 3, height=30, width=140, anchor="nw", window=self.search_youtube_bar)

            self.search_youtube_button = Button(self.youtube, bg="#232322", fg="#ffffff", borderwidth=3, justify="center", font=("Open Sans", 10), text="Youtube", command=lambda: self.search())
            self.youtube.create_window(695, 3, height=30, width=60, anchor="nw", window=self.search_youtube_button)

            self.points_counter = Label(self.youtube, bg="#181818", fg="#ffffff", borderwidth=4, justify="center", font=("Open Sans", 15), textvariable=self.points)
            self.youtube.create_window(400, 3, height=30, width=140, anchor="nw", window=self.points_counter)

            self.caption(text=f"last")

        def connect(self):
            file = open(f"{self.locate}/Connexion.txt", "w")
            https = urllib3.PoolManager()
            try:
                response = https.request("GET", "https://www.google.com")
                self.connexion = True
                file.write("True")
            except:
                self.connexion = False
                file.write("False")
            file.close()

        def pytube(self):
            try:
                os.mkdir(f"{self.locate}/test")
                video = YouTube(link)
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=f"{self.locate}/test")
                shutil.rmtree(f"{self.locate}/test")
                return True
            except:
                Logs().Error(text="Download with pytube not working", locate=self.locate)
                return False

        def thread_watch(self, documents):
            Permission().reduce_youtube()
            time.sleep(2)
            youtube = open("Youtube.html", "w").write(f'''<!DOCTYPE html>\n<html lang="fr">\n    <head>\n        <link rel="stylesheet" href="Youtube.css" />\n        <meta charset="utf-8">\n        <title>Youtube video player</title>\n    </head>\n    <body bgcolor="#181818">\n    <iframe class="positioned" width="600" height="370" src="{documents[3][0:24]}embed/{documents[3][32:43]}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n    </body>\n</html>''')
            os.system(f"{self.locate}/Youtube.vbs")

        def thread_download(self, documents):
            Data.get_video(documents[3], self.locate)

        def watch(self, documents):
            self.connect()
            if self.connexion:
                if pay(self.time_to_pieces(documents[2]), self.locate):
                    self.thread_watch(documents)
                    #thread = threading.Thread(target=lambda: self.thread_watch(documents))
                    #thread.start()

        def download(self, documents):
            if self.pytube():
                if pay(self.time_to_pieces(documents[2]), self.locate):
                    thread = threading.Thread(target=lambda: self.thread_download(documents))
                    thread.start()

        def detect(self):
            self.connect()
            if self.connexion:
                try:
                    self.location.withdraw()
                    data = Data(self.locate)
                    self.caption(text=self.current_search)
                    self.location.deiconify()
                except:
                    Logs().Error(text="YouTube == Connard", locate=self.locate)
            else:
                Logs().Error(text="No connexion", locate=self.locate)

        def search(self):
            text = self.search_youtube_bar.get()
            self.search_youtube_bar.delete(0, "end")
            action = lambda : Data.search_and_download(text, self.locate)
            thread = threading.Thread(target=action)
            thread.start()

        def caption(self, text=None):
            if text is None:
                text = self.search_bar.get()
            self.current_search = text
            self.search_bar.delete(0, "end")
            if len(text) == 0:
                pass
            elif text[0] == "@":
                self.modify_list("youtubeur", text)
            elif text == "last" or text == "Last":
                self.modify_list("time", str(os.listdir(f"{self.locate}/Videos/Time")[len(os.listdir(f"{self.locate}/Videos/Time")) - 1]))
            elif text == "amixem" or text == "Amixem":
                self.modify_list("youtubeur", "@Amixem")
            elif text == "bazar du grenier":
                self.modify_list("youtubeur", "@BazarduGrenier")
            elif text == "codebh" or text == "code bh":
                self.modify_list("youtubeur", "@codebh")
            elif text == "ego" or text == "Ego":
                self.modify_list("youtubeur", "@Ego_One")
            elif text == "fuzay" or text == "fuzay 2" or text == "Fuzay 2" or text == "Fuzay":
                self.modify_list("youtubeur", "@FuzayAuCarre")
            elif text == "fuze III" or text == "Fuze III" or text == "Fuze 3" or text == "fuze3" or text == "fuze 3":
                self.modify_list("youtubeur", "@FuzeIII")
            elif text == "fiouze":
                self.modify_list("youtubeur", "@FuzePlays")
            elif text == "henry tran" or text == "henri tran" or text == "Henry Tran":
                self.modify_list("youtubeur", "@HenryTran")
            elif text == "hihacks" or text == "Hihacks":
                self.modify_list("youtubeur", "@Hihacks")
            elif text == "jdg" or text == "JDG" or text == "Jdg" or text == "joueur du grenier":
                self.modify_list("youtubeur", "@joueurdugrenier")
            elif text == "kombo" or text == "Kombo":
                self.modify_list("youtubeur", "@Kombo000")
            elif text == "ninjaxx 2" or text == "ninjaxx2":
                self.modify_list("youtubeur", "@LeNinjaxx")
            elif text == "micode" or text == "Micode":
                self.modify_list("youtubeur", "@Micode")
            elif text == "mrbeast" or text == "Mr beast" or text == "Mrbeast" or text == "mr beast":
                self.modify_list("youtubeur", "@MrBeast")
            elif text == "ninjaxx" or text == "Ninjaxx":
                self.modify_list("youtubeur", "@Ninjaxx")
            elif text == "rayton 3.0" or text == "rayton":
                self.modify_list("youtubeur", "@rayton3.0_officiel")
            elif text == "squeezie" or text == "Squeezie":
                self.modify_list("youtubeur", "@Squeezie")
            elif text == "squeezie gaming" or text == "Squeezie gaming":
                self.modify_list("youtubeur", "@SqueezieGaming")
            elif text == "Kevin Tran" or text == "kevin tran":
                self.modify_list("youtubeur", "@superkevintran")
            elif text == "underscore" or text == "Underscore":
                self.modify_list("youtubeur", "@Underscore_")
            elif text == "tgr" or text == "Tgr" or text == "TGR" or text == "the great review":
                self.modify_list("youtubeur", "@TheGreatReview")
            elif text == "whatafail" or text == "what a fail":
                self.modify_list("youtubeur", "@WhataFail")
            elif text == "hier" or text == "Hier":
                self.modify_list("time", str(date.today() - timedelta(days=1)))
            elif text == "aujourd'hui" or text == "today" or text == "now" or text == "maintenant":
                self.modify_list("time", str(date.today() - timedelta(days=0)))
            else:
                self.modify_list("time", text)

        def modify_list(self, mode, list):
            self.document_value = 0
            self.all_documents = []
            if mode == "time":
                lk = f"{self.locate}/Videos/Time/{list}"
                if os.path.exists(lk):
                    for video in os.listdir(lk):
                        video_live = (open(f"{lk}/{video}", "r", encoding="utf-8")).readlines()
                        link = str(video_live[0])
                        list_video = [
                            f"{self.locate}/Miniatures/{link[len(video_live[0]) - 12:len(video_live[0]) - 1]}.png",
                            str(video_live[2].split("\n")[0]),
                            video_live[3][0: len(video_live[3]) - 1],
                            video_live[0]]
                        self.all_documents.append(list_video)
            else:
                lk = f"{self.locate}/Videos/{list}"
                all_documents = []
                if os.path.exists(lk):
                    for video in os.listdir(lk):
                        video_live = (open(f"{lk}/{video}", "r", encoding="utf-8")).readlines()
                        link = str(video_live[0])
                        list_video = [
                            f"{self.locate}/Miniatures/{link[len(video_live[0]) - 12:len(video_live[0]) - 1]}.png",
                            str(video_live[2].split("\n")[0]),
                            video_live[3][0: len(video_live[3]) - 1],
                            video_live[0],
                            video_live[4]]
                        all_documents.append(list_video)
                position = 0
                if os.path.exists(f"{self.locate}/Videos/Temporary"):
                    shutil.rmtree(f"{self.locate}/Videos/Temporary")
                if not os.path.exists(f"{self.locate}/Videos/Temporary"):
                    os.mkdir(f"{self.locate}/Videos/Temporary")
                for video in all_documents:
                    if not os.path.exists(f"{self.locate}/Videos/Temporary/{video[4]}"):
                        os.mkdir(f"{self.locate}/Videos/Temporary/{video[4]}")
                    if not os.path.exists(f"{self.locate}/Videos/Temporary/{video[4]}/{position}.txt"):
                        s = open(f"{self.locate}/Videos/Temporary/{video[4]}/{position}.txt", "w")
                        s.close()
                    position += 1
                liste = []
                for sus in os.listdir(f"{self.locate}/Videos/Temporary"):
                    for l in os.listdir(f"{self.locate}/Videos/Temporary/{sus}"):
                        liste.append(all_documents[int(l[0:len(l)-4])])
                liste.reverse()
                for element in liste:
                    self.all_documents.append(element)
                shutil.rmtree(f"{self.locate}/Videos/Temporary")
            if os.path.exists(lk):
                if len(os.listdir(lk)) % 3 == 0:
                    self.max_value = int((len(os.listdir(lk)) / 3)) - 1
                else:
                    self.max_value = int(len(os.listdir(lk)) / 3)
            else:
                self.max_value = 0
            if self.max_value == 0 and len(os.listdir(lk)) % 3 == 0 and not len(os.listdir(lk)) == 3:
                self.message.set(f"0 / 0")
            else:
                self.message.set(f"{self.document_value + 1} / {self.max_value + 1}")
            self.change_videos()

        def defile_list(self, norp):
            if norp == "+":
                if self.max_value == self.document_value:
                    self.document_value = 0
                else:
                    self.document_value += 1
            if norp == "-":
                if self.document_value == 0:
                    self.document_value = self.max_value
                else:
                    self.document_value -= 1
            if self.max_value == 0 and (len(self.all_documents) % 3) == 0 and not len(self.all_documents) == 3:
                self.message.set(f"0 / 0")
            else:
                self.message.set(f"{self.document_value + 1} / {self.max_value + 1}")
            self.change_videos()

        def time_to_pieces(self, time):
            if not time == "":
                time_split = time.split(":")
                pieces = 0
                if len(time_split) == 3:
                    pieces += int(time_split[0]) * 3600
                    pieces += int(time_split[1]) * 60
                    pieces += int(time_split[2])
                elif len(time_split) == 2:
                    pieces += int(time_split[0]) * 60
                    pieces += int(time_split[1])
                elif len(time_split) == 1:
                    pieces += int(time_split[0])
                return round(pieces / 10)
            else:
                return ""

        def change_videos(self):
            if self.max_value >= self.document_value:
                im = 0
                for n in [[0, 52, 6], [1, 193, 6], [2, 334, 6]]:
                    im += 1
                    try:
                        try:
                            image = Image.open(self.all_documents[self.document_value * 3 + n[0]][0])
                            resize_image = image.resize((240, 135))
                            if im == 1:
                                self.img1 = ImageTk.PhotoImage(resize_image)
                                i_youtube = Label(bg="#181818", image=self.img1)
                            elif im == 2:
                                self.img2 = ImageTk.PhotoImage(resize_image)
                                i_youtube = Label(bg="#181818", image=self.img2)
                            else:
                                self.img3 = ImageTk.PhotoImage(resize_image)
                                i_youtube = Label(bg="#181818", image=self.img3)
                            y_image = self.youtube.create_window(n[2], n[1], height=135, width=240, anchor="nw",
                                                                 window=i_youtube)
                        except:
                            pass
                        self.change_video(self.all_documents[3 * self.document_value + n[0]], n[1], n[2])
                    except:
                        self.change_video(hauteur=n[1], largeur=n[2])

        def change_video(self, documents=None, hauteur=None, largeur=None):
            if documents is None:
                title1 = Label(background="#181818", justify="center")
                self.youtube.create_window(largeur, hauteur, height=135, width=748, anchor="nw", window=title1)
            else:
                if len(documents[1]) < 70:
                    title = Label(background="#181818", text=documents[1], font=("sans-serif", 10, "bold"), fg="#ffffff", justify="left")
                    self.youtube.create_window(largeur + 240, hauteur + 7, height=20, width=514, anchor="nw", window=title)
                    sub_title = Label(background="#181818", justify="left")
                    self.youtube.create_window(largeur + 240, hauteur + 27, height=20, width=514, anchor="nw", window=sub_title)
                else:
                    title1 = Label(background="#181818", text=documents[1].split(" ")[0:9], font=("sans-serif", 10, "bold"), fg="#ffffff", justify="left")
                    self.youtube.create_window(largeur + 240, hauteur + 7, height=20, width=514, anchor="nw", window=title1)
                    title2 = Label(background="#181818", text=documents[1].split(" ")[9:len(documents[1].split(" "))], font=("sans-serif", 10, "bold"), fg="#ffffff", justify="left")
                    self.youtube.create_window(largeur + 240, hauteur + 27, height=20, width=514, anchor="nw", window=title2)
                time = Label(background="#000000", text=documents[2], font=("Arial", 9, "bold"), fg="#ffffff", justify="left")
                self.youtube.create_window(largeur + 187, hauteur + 112, height=20, width=50, anchor="nw", window=time)
                image_download = ImageTk.PhotoImage(Image.open(f"{self.locate}/Images/Download.png"))
                download = Button(bg="#181818", justify="center", borderwidth=0, image=image_download, command=lambda : self.download(documents))
                self.youtube.create_window(largeur + 262, hauteur + 89, height=40, width=150, anchor="nw", window=download)
                image_watch = ImageTk.PhotoImage(Image.open(f"{self.locate}/Images/Watch.png"))
                watch = Button(bg="#181818", justify="center", borderwidth=0, image=image_watch, command=lambda : self.watch(documents))
                self.youtube.create_window(largeur + 428, hauteur + 89, height=40, width=150, anchor="nw", window=watch)
                image_later = ImageTk.PhotoImage(Image.open(f"{self.locate}/Images/Later.png"))
                later = Button(bg="#181818", justify="center", borderwidth=0, image=image_later, command=lambda : self.download(documents))
                self.youtube.create_window(largeur + 594, hauteur + 89, height=40, width=150, anchor="nw", window=later)
                self.save.append(image_download)
                self.save.append(image_watch)
                self.save.append(image_later)