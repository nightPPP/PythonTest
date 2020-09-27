xiaoming_dict = {"name":"小明",
            "age":18,
            "gender":True,
            "height":1.75}

print(xiaoming_dict)

# 通过键找值
print(xiaoming_dict["name"])

xiaoming_dict["age"] = 20
print(xiaoming_dict)

tem_dict = {"age": 50,
            "weight": 300}
xiaoming_dict.update(tem_dict)
print(xiaoming_dict)

for key in xiaoming_dict:
    print("%s --- %s" %(key, xiaoming_dict[key]))

xiaoming_dict.clear()
print(xiaoming_dict)