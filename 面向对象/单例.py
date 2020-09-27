class MusicPlayer(object):

    # 是否创建过的标记
    instance = None
    # 是否初始化过
    init_flag = False
    # 如果没有创建过对象实例就创建一个，有就直接拿过来用
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("初始化")
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)