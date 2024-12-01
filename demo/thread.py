import threading, time

def func():
    for i in range(10):
        print(time.strftime("%H:%M:%S"))
        time.sleep(1)

thread_pool = []
for i in range(10):
    thread_demo = threading.Thread(target=func)
    thread_demo.start()
    thread_pool.append(thread_demo)


# 开始机型线程守护
for i in thread_pool:
    i.join()

print("线程池调度完毕...")