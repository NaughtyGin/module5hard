from time import sleep


class User:


    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:


    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'


class UrTube:
    current_user = None
    users = []
    videos = []

    def __init__(self):
        self.data = []

    def __contains__(self, item):
        self.data = UrTube()
        return item in self.data

    def log_in(self, nickname, password, age):
        for user in UrTube.users:
            if nickname == user[0]:
                if hash(password) == user[1]:
                    UrTube.log_out(self.current_user)
                    UrTube.current_user = User(nickname, hash(password), age)
                else:
                    print('Имя пользователя или пароль введены неверно')

    def register(self, nickname, password, age):
        for i in UrTube.users:
            if nickname == i[0]:
                return print(f'Пользователь {nickname} уже существует')
            else:
                UrTube.users.append([nickname, hash(password), age])
                break
        else:
            UrTube.users.append([nickname, hash(password), age])
        UrTube.log_in(self, nickname, password, age)

    def log_out(self):
        UrTube.current_user = None

    def add(self, *args):
        for i in args:
            if i not in UrTube.videos:
                UrTube.videos.append([i.title, i.duration, i.time_now, i.adult_mode])
            else:
                print(f'Видео {i} уже существует')

    def get_videos(self, search_term):
        self.search_term = search_term
        found_video = []
        for i in UrTube.videos:
            if search_term.upper() in i[0].upper():
                found_video.append(i[0])
        return found_video

    def watch_video(self, title):
        self.title = title
        if UrTube.current_user is None:
            return print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in UrTube.videos:
                if i[0] == title and (i[3] is False or (i[3] is True and self.current_user.age >= 18)):
                    for t in range(1, i[1]+1):
                        print(t, end=' ')
                        sleep(0.2)
                    print('Конец видео')
                if i[3] is True and self.current_user.age < 18:
                    return print('Вам нет 18 лет, пожалуйста, покиньте страницу')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

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
