import multiprocessing


def down_from_web(q):
    """下载数据"""
    # 模拟从网上下载数据
    data = [11, 22, 33, 44]
    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("已经下载完成数据并存入队列中")


def analysis_data(q):
    """数据处理"""
    waiting_analysis_data = list()
    # 从队列中取数据
    while True:
        data = q.get()
        waiting_analysis_data.append(data)
        if q.empty():
            break

    print(waiting_analysis_data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()

    # 创建多个进程,将队列的引用当作实参进行传递到里面
    p1 = multiprocessing.Process(target=down_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()