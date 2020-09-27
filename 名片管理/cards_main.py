import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：").strip()
    # print("您选择的操作是 【%s】" %action_str)

    # 1,2,3是针对名片的操作
    # 0退出
    # 其他提示
    if "0" == action_str:
        print("欢迎再次使用【名片管理系统】")
        break
    elif (action_str in ["1", "2", "3"]):
        # 新增名片
        if "1" == action_str:
            cards_tools.new_card()
            pass
        # 显示全部
        elif "2" == action_str:
            cards_tools.show_all()
            pass

        # 查询名片
        elif "3" == action_str:
            cards_tools.search_card()
            pass
        else:

            pass
        print("选择的是 【%s】" %action_str)
        pass
    else:
        print(" 输入有误")