import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    # 完成文件的copy
    # print("模拟copy文件---%s---从%s-----》 %s" %(file_name, old_folder_name, new_folder_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 拷贝完就向队列放消息
    q.put(file_name)


def main():
    # 获取要copy的文件夹名字如：A
    old_folder_name = input("输入要copy的名字")
    # 创建新的文件夹如：B
    try:
        new_folder_name = old_folder_name + "[附件]"
        os.mkdir(new_folder_name)
    except:
        pass
    # 获取A文件夹中所有的待copy的名字
    file_names = os.listdir(old_folder_name)
    print(file_names)
    # 创建进程池
    po = multiprocessing.Pool(2)

    # 进度条
    # 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 向进程池中添加copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()

    # 所有的文件个数
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print("已经copy完成----%s" %file_name)
        copy_ok_num += 1
        print("\r进度----%.2f%%" % (copy_ok_num / all_file_num * 100), end="")
        if all_file_num <= copy_ok_num:
            break

    print()
    # 复制原文件夹中的文件到新文件夹中的文件去


if __name__ == "__main__":
    main()