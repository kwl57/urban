


import time
import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_passw(password)  # хеширование пароля
        self.age = age

    def hash_passw(self, password): # Функция хеширования пароля.
        return hashlib.sha256(password.encode()).hexdigest()

    def __eq__(self, other):
        # Функция проверки пользователя по имени пользователя.
        return self.nickname == other.nickname

    def __str__(self):
        # Функция строкового представления имени пользователя.
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration,time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now  # Текущее время просмотра видео (секунда остановки (изначально 0))
        self.adult_mode = adult_mode

    # Функция проверки видео по заголовку.
    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    # Функция строкового представления параметров видео.
    def __str__(self):
        return (f"Video(title ='{self.title}',time_now = {self.time_now}, duration = {self.duration}, "
                f"adult_mode = {self.adult_mode})")


class UrTube:
    def __init__(self):
        self.users = []  # Список зарегистрированных пользователей
        self.videos = []  # Список доступных видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user    # Если user пользователь найден, то current_user меняется
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
        print("Проверьте введенные данные: неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("В системе нет активного пользователя.")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()   # Перевод слова в нижний регистр.
        # Возвращает список названий всех видео, содержащих поисковое слово
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:  # Воспроизводит видео, если пользователь вошёл в систему
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    # Воспроизводит видео, если пользователь имеет право на просмотр
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                # Воспроизведение видео:
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush = True)
                    time.sleep(1)  # Просмотр по одной секунде
                index_video = self.videos.index(video)
                video.time_now = 0  # Сбрасывается время остановки после полного просмотра
                self.videos[index_video] =  video
                print("Конец видео")
                return


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года',200)
v2 = Video('Для чего девушкам парень программист?', 10,3, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
