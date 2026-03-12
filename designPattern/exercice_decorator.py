import time

def quack():
    print('quack')
    time.sleep(1)
    print('quack')

def log_time(func):
    def inner_log_time():
        start = time.time_ns()
        func()
        end = time.time_ns()
        print(end - start)
    return inner_log_time
    
quack = log_time(quack)

if __name__ == '__main__':
    print(type(quack))
    # quack
    # quack
    # 1
    quack()