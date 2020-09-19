
import traceback
class BException(Exception):  #继承Exception基类
    pass

class CException(BException):  #继承BException基类
    pass

class DException(CException):  #继承CException基类
    pass

for cls in [BException, CException, DException]:
    # try:
    #     raise cls()  #抛出异常
    # except DException:
    #     print("D")
    # except CException:
    #     print("C")
    # except BException:
    #     print("B")
    #
    try:
        raise BException()  # 抛出异常
    except (BException, DException) as err:
        print("D")
        traceback.print_exc()
        print(err.args)  # 打印异常的参数元组
    except:
        print("处理全部其它异常")  # 处理全部其它异常
    else:
        print("没有异常发生")  # 没有异常发生
    finally:
        print("你们绕不过我，必须执行")  # 必须执行的代码