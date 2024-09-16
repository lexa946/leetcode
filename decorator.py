from functools import wraps

def func_index():
    print("Index")




ex_list = [(IndexError, func_index), (KeyError, lambda _: print("Key")), (TypeError, lambda _: print("Typniak"))]


def decorator(ex_list):
    @wraps
    def wrap_1(func):
        def wrap(*args, **kwargs):

            try:
                res = func(*args, **kwargs)
            except Exception as ex:
                for ex_tuple in ex_list:
                    ex_type, ex_func = ex_tuple
                    if isinstance( ex, ex_type):
                        ex_func("1")

                raise ex

            return res
        return wrap

    return wrap_1






@decorator(ex_list=ex_list)
def my_func(arr=None):
    if not arr:
        arr = []

    for i in range(10):
        print(arr[i])



@decorator(ex_list=ex_list)
def my_key_func(dict_=None):
    return dict_['Index']






# my_func()

my_key_func(dict_={"123": 123})

