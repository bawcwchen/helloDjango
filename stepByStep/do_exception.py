"""
  异常处理
"""
import logging

if __name__ == '__main__':
    try:
        10/0
        print("success")
    except ZeroDivisionError as e:
        print("除数为0", e)
        logging.exception(e)

    finally:
        print("finally")

    if True:
        raise Exception("raise exception")

