# 记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.输入名片信息
    name_str = input("请输入姓名：").strip()
    phone_str = input("请输入电话：").strip()
    qq_str = input("请输入QQ：").strip()
    email_str = input("请输入email：").strip()
    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}
    # 3.将名片添加到字典中
    card_list.append(card_dict)
    print(card_list)
    # 4.添加名片成功
    print("添加 %s 的名片成功" %name_str)
    print("-" * 50)

def show_all():
    """显示全部名片"""
    print("-" * 50)
    print("显示全部名片")

    # 判定是否有名片
    if 0 == len(card_list):
        print("无记录，请新增名片")
        # return下方的代码不执行
        return

    # 打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name, end="\t\t")

    print("")
    print("="*50)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
                                             card_dict["phone"],
                                             card_dict["qq"],
                                             card_dict["email"]))
    print("-" * 50)

def search_card():
    """"搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" %(card_dict["name"],
                                           card_dict["phone"],
                                           card_dict["qq"],
                                           card_dict["email"]))

            # 针对找到的名片字典删除或修改操作
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到 %s" %find_name)

    print("-" * 50)

def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作 1-修改 2-删除 0-返回上一级目录")
    if "1" == action_str:
        find_dict["name"] = input_card_info(find_dict["name"], "请输入修改的姓名")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入修改的电话")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入修改的QQ")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入修改的email")
        print("修改名片")
    elif "2" == action_str:
        card_list.remove(find_dict)
        print("删除名片成功")

def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value