class MyError(Exception):
    def __init__(self):
        print('Error is raised')


def demo():
    raise MyError


try:
    demo()
except MyError:
    print('Error is raise')
