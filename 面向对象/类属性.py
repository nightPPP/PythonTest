class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

tool2 = Tool("小小")
tool3 = Tool("中中")
tool1 = Tool("大大")

print(Tool.count)