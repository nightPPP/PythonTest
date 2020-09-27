class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息，让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        cls.top_score += 1
        print("历史记录 %d" %cls.top_score)

    def start_game(self):
        print("%s 开始游戏了,最高分%d" %(self.player_name, self.top_score))

# 查看游戏的帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")
game.start_game()