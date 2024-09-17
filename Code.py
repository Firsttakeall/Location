import os, win32gui, win32con, time, threading, requests, os, shutil, pygame.mixer, subprocess, datetime, urllib.request, tkinter, pyautogui, keyboard
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from pydub import AudioSegment
from pytube import YouTube, Channel
from PIL import Image

text = ""


def timer(locate):
    file_time = int(open(f"{locate}/Time.txt", "r").readlines()[0]) - 1
    final_time = open(f"{locate}/Time.txt", "w")
    final_time.write(f"{locate}/{str(file_time)}")
    final_time.close()


def date_change(date):
    date = str(date)
    date = date[0:10]
    return date


def time_change(time):
    hours = int(time / 3600)
    minutes = int(time / 60) - (hours * 60)
    seconds = time - (hours * 3600) - (minutes * 60)
    if 0 <= seconds < 10:
        seconds = "0" + str(seconds)
    if 0 <= minutes < 10:
        minutes = "0" + str(minutes)
    if not hours == 0:
        time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    else:
        time = str(minutes) + ":" + str(seconds)
    return time


def bytes_to_megabytes(byte_size):
    megabytes_size = str(byte_size / (1024 ** 2))
    megabytes_size = megabytes_size.split(".")[0]
    megabytes_size = int(megabytes_size)
    return megabytes_size


def sub_running(game, locate):
    file = open(f"{locate}/Game.bat", "w")
    file2 = open(f"{locate}/Game.vbs", "w")
    if game[len(game)-4:len(game)] == ".lnk" or game[len(game)-4:len(game)] == ".url":
        file.write(f'start /D "{locate}/Links" {game}')
    else:
        if game[len(game)-4:len(game)] == ".n64":
            file.write(fr'start {locate}/Emulators/Projet_64/Project64.exe "{locate}/Links/{game}"')
        elif game[len(game)-4:len(game)] == ".nds":
            file.write(fr'start {locate}/Emulators/Desmume/DeSmuME_0.9.13_x64.exe "{locate}/Links/{game}"')
        elif game[len(game)-4:len(game)] == ".gbc":
            file.write(fr'start {locate}/Emulators/TGB_dual/TGB_Dual.exe "{locate}/Links/{game}"')
        elif game[len(game)-4:len(game)] == ".iso":
            file.write(fr'start {locate}/Emulators/Dolphin/Dolphin.exe "--exec={locate}/Links/{game}" --batch')
    file2.write(f"""Set wsc = CreateObject("WScript.Shell")\nwsc.Run "{locate}/Game.bat", 0""")
    file.close()
    file2.close()
    os.system(f"{locate}/Game.vbs")


def running(game, locate):
    thread = threading.Thread(target=lambda : sub_running(game, locate))
    thread.start()


def register_point(locate):
    while True:
        try:
            file = open(f"{locate}/Points.txt", "r")
            read_file = file.readlines()
            points = read_file[len(read_file)-1]
            break
        except:
            pass
    return points


class Musique:
    def __init__(self, locate):
        self.locate = locate
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('-profile')
        self.options.add_argument(r'C:\Users\W7\AppData\Roaming\Mozilla\Firefox\Profiles\dk96i2vu.default-release-1')
        self.driver = webdriver.Firefox(options=self.options)

    def listen_musique_online(self, link):
        self.driver.get(link)

    def download_music(self, link, name=None):
        video = YouTube(link)
        stream = video.streams.get_audio_only()
        if name is None:
            stream.download(output_path=f"{self.locate}/Musics", filename=f"{stream.default_filename[0:len(stream.default_filename)-4]}.mp3")
            self.mp3_to_way(f"{stream.default_filename[0:len(stream.default_filename)-4]}.mp3")
            os.remove(f"{self.locate}/Musics/{stream.default_filename[0:len(stream.default_filename)-4]}.mp3")
        else:
            stream.download(output_path=f"{self.locate}/Musics", filename=f"{name}.mp3")
            self.mp3_to_way(f"{name}.mp3")
            os.remove(f"{self.locate}/Musics/{name}.mp3")

    def search(self, keywords):
        keywords = keywords.split(" ")
        search = "https://youtube.com/search?q="
        for n in keywords:
            search = search + n + "+"
        search = search[0:len(search)-1]
        response = requests.get(search)
        data = str(response.content).split('"')
        result = ""
        for ligne in data:
            if ligne[0:6] == "/watch":
                result = f"https://youtube.com/watch?v={ligne[9:20]}"
                break
        return result

    def search_and_download(self, link):
        audio = self.search(link)
        self.download_music(audio)

    def unsafe_search(self, entry):
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=option)
        result = ""
        if entry == "":
            driver.get("https://www.youtube.com/")
        else:
            entry = entry.split(" ")
            link = ""
            for n in entry:
                link = link + n + "+"
            driver.get(f"https://www.youtube.com/search?q={link}")
        while True:
            if driver.current_url[0:len(driver.current_url)-11] == "https://www.youtube.com/watch?v=":
                result = driver.current_url
                break
        driver.quit()
        return result

    def unsafe_search_and_download(self, entry):
        link = self.unsafe_search(entry)
        self.download_music(link)

    def play_song(self, link_song):
        link = f"{self.locate}/Musics/" + link_song
        sound = pygame.mixer.Sound(link)
        sound.set_volume(0.5)
        sound.play()

    def mp3_to_way(self, filename):
        subprocess.call(['ffmpeg', '-i', f'{self.locate}/Musics/{filename}',
                         f'{self.locate}/Musics/{filename[0:len(filename)-4]}.wav'])


class Permission:
    def destroy(self, object_name):
        handle = win32gui.FindWindow(None, fr'{object_name}')
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)

    def reduce_youtube(self):
        keyboard.press_and_release("Windows+m")

    def permission_youtube(self, locate):
        windows = None
        for window in pyautogui.getAllWindows():
            if len(window.title) >= 25:
                if window.title[-25:len(window.title)] == "YouTube — Mozilla Firefox--":
                    self.destroy(window.title)
                    windows = window.title

    def permission_game(self, locate):
        windows = None
        for window in pyautogui.getAllWindows():
            if len(window.title) >= 12:
                if window.title[0:12] == "Dolphin 2407":
                    if int(open("Time.txt", "r").readlines()[0]) <= 0:
                        self.destroy(window.title)
                        windows = window.title
                    else:
                        return True
            if len(window.title) >= 28:
                if window.title[-28:len(window.title)] == "Project64 3.0.1.5664-2df3434":
                    if int(open("Time.txt", "r").readlines()[0]) <= 0:
                        self.destroy(window.title)
                        windows = window.title
                    else:
                        return True
            if len(window.title) >= 23:
                if window.title[0:23] == "DeSmuME 0.9.13 x64 SSE2":
                    if int(open("Time.txt", "r").readlines()[0]) <= 0:
                        self.destroy(window.title)
                        windows = window.title
                    else:
                        return True
            if len(window.title) >= 10:
                if window.title[0:10] == "BlueStacks":
                    if int(open("Time.txt", "r").readlines()[0]) <= 0:
                        self.destroy(window.title)
                        windows = window.title
                    else:
                        return True
        if windows is not None:
            Logs().Message(text=f"Plus de temps de jeu: Interdiction d'ouvrir: {windows}", locate=locate)
        else:
            return None

    def find_unpermission_element(self, locate):
        windows = None
        permission = open("Permission.txt", "r", encoding="utf-8").readlines()
        for window in pyautogui.getAllWindows():
            for ligne in permission:
                if window.title == ligne:
                    self.destroy(window.title)
                    windows = window.title
        if windows is not None:
            Logs().Message(text=f"Interdiction d'ouvrir la fenêtre suivante: {windows}", locate=locate)


class Data:
    def __init__(self, locate):
        self.number = {}
        self.list_youtube = []
        self.new_content = {}
        self.all = []
        self.locate = locate

        self.init_youtubeurs()
        self.initialising()
        self.check()
        self.take_videos()
        self.timer()
        self.miniature(self.locate)

    @staticmethod
    def progress_func(stream, chunk, bytes_remaining):
        current = stream.filesize - bytes_remaining
        text = "Téléchargement : " + str(bytes_to_megabytes(current)) + " Mégabytes sur " + str(
            bytes_to_megabytes(stream.filesize)) + " ; Temps restant : " + str(
            round((bytes_to_megabytes(stream.filesize) - bytes_to_megabytes(current)) / 1.8)) + " secondes."

    def init_youtubeurs(self):
        data = open(f"{self.locate}/Liste_Youtubeurs.txt", "r")
        count = False
        for ligne in data:
            self.all.append(ligne[0:len(ligne) - 1])
            count = not count
            if count is False:
                self.list_youtube.append(self.all)
                self.all = []

    def initialising(self):
        for youtubeur in self.list_youtube:
            if not os.path.exists(f"{self.locate}/Videos/{youtubeur[0]}"):
                os.mkdir(f"{self.locate}/Videos/{youtubeur[0]}")

    def check(self):
        for youtubeur in self.list_youtube:
            new_content = 0
            urls = []
            url = f"https://www.youtube.com/{youtubeur[0]}/videos"
            response = requests.get(url)
            for ligne in str(response.content).split('"'):
                if ligne[0:7] == "/watch?":
                    if not os.path.exists(f"{self.locate}/Videos/{youtubeur[0]}/{ligne[9:len(ligne)]}.txt"):
                        urls.append(ligne[9:len(ligne)])
                        new_content += 1
                    else:
                        break
            self.new_content[youtubeur[0]] = [new_content, urls]

    def take_videos(self):
        for youtubeur in self.list_youtube:
            if self.new_content[youtubeur[0]][0] > 0:
                Logs().Message(text=f"{youtubeur[0]}: {self.new_content[youtubeur[0]][0]} new video(s).", locate=self.locate)
            videos = []
            new_content = self.new_content[youtubeur[0]]
            for number in range(0, new_content[0]):
                link = "https://www.youtube.com/watch?v=" + new_content[1][number]
                minia = f"https://i.ytimg.com/vi/{new_content[1][number]}/hqdefault.jpg"
                video = YouTube(link)
                videos.append([link, minia, video.title, time_change(video.length), date_change(video.publish_date)])
            number = 0
            for vid in videos:
                if os.path.isdir(f"{self.locate}/Videos/--{youtubeur[0]}"):
                    shutil.rmtree(f"{self.locate}/Videos/{youtubeur[0]}")
                    os.rename(f"{self.locate}/Videos/--{youtubeur[0]}", f"{self.locate}/Videos/{youtubeur[0]}")
                shutil.copytree(f"{self.locate}/Videos/{youtubeur[0]}", f"{self.locate}/Videos/--{youtubeur[0]}")
                fichier = open(f"{self.locate}/Videos/{youtubeur[0]}/{new_content[1][number]}.txt", "w", encoding="utf-8")
                fichier.write(vid[0] + "\n" + vid[1] + "\n" + vid[2] + "\n" + vid[3] + "\n" + vid[4])
                fichier.close()
                number += 1
                shutil.rmtree(f"{self.locate}/Videos/--{youtubeur[0]}")

    def timer(self):
        for youtubeur in os.listdir(f"{self.locate}/Videos"):
            if youtubeur[0:1] == "@":
                for content in os.listdir(f"{self.locate}/Videos/{youtubeur}"):
                    video = open(f"{self.locate}/Videos/{youtubeur}/{content}", "r", encoding="utf-8").readlines()
                    if not os.path.exists(f"{self.locate}/Videos/Time/{video[4]}"):
                        os.mkdir(f"{self.locate}/Videos/Time/{video[4]}")
                    if not os.path.exists(f"{self.locate}/Videos/Time/{video[4]}/{content}"):
                        shutil.copy(f"{self.locate}/Videos/{youtubeur}/{content}", f"{self.locate}/Videos/Time/{video[4]}/{content}")

    @staticmethod
    def miniature(locate):
        for youtubeur in os.listdir(f"{locate}/Videos"):
            if youtubeur[0:1] == "@":
                for video in os.listdir(f"{locate}/Videos/{youtubeur}"):
                    link = f"https://i.ytimg.com/vi/{video[0:len(video) - 4]}/hqdefault.jpg"
                    if not os.path.exists(f"{locate}/Miniatures/{video[0:len(video) - 4]}.png"):
                        for _ in range(1, 6):
                            try:
                                urllib.request.urlretrieve(link, filename=f"{locate}/Miniatures/{video[0:len(video) - 4]}.jpg")
                                im = Image.open(f'{locate}/Miniatures/{video[0:len(video) - 4]}.jpg')
                                x, y = im.size
                                im.crop((0, 45, x, y - 45)).save(f"{locate}/Miniatures/{video[0:len(video) - 4]}.png")
                                os.remove(f'{locate}/Miniatures/{video[0:len(video) - 4]}.jpg')
                                break
                            except:
                                pass

    @staticmethod
    def load(texte):
        while not text == "Terminate":
            if not text == "":
                texte.set(text)

    @staticmethod
    def get_video(link, locate):
        global text
        video = YouTube(link, on_progress_callback=Data.progress_func)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=f"{locate}/Videos/Download_Videos")
        text = "Terminate"
        Data.load(text)

    @staticmethod
    def search(entry):
        driver = webdriver.Chrome(options=webdriver.ChromeOptions())
        result, link = "", ""
        if len(entry) == 0:
            driver.get("https://www.youtube.com/")
        else:
            for n in entry.split(" "):
                link = link + n + "+"
            driver.get(f"https://www.youtube.com/search?q={link}")
        while True:
            if driver.current_url[0:len(driver.current_url) - 11] == "https://www.youtube.com/watch?v=":
                result = driver.current_url
                break
        driver.quit()
        return result

    @staticmethod
    def search_and_download(entry, locate):
        link = Data.search(entry)
        Data.get_video(link, locate)


class Logs:
    def Message(self, text, locate):
        logs = open(f"{locate}/Logs.txt", "a", encoding="utf-8")
        logs.write(f"{datetime.datetime.now()}      {text}\n")
        logs.close()

    def Error(self, text, locate):
        logs = open(f"{locate}/Logs.txt", "a", encoding="utf-8")
        logs.write(f"{datetime.datetime.now()}      Error: {text}\n")
        logs.close()
