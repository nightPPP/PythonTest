def print_info(name, gender=True):

    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print(name + gender_text)

print_info("张三", False)