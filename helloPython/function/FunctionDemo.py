
def def_param_fun(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# def_param_fun('Do you really want to quit?')

# def_param_fun('Do you really want to quit?', 2)
#
# def_param_fun('Do you really want to quit?', 2, 'Please, yes or no!')

def variable_fun(kind,*arguments,**keywords):
    print("friend : ", kind , ";")
    print("-"*40)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw, ":" ,keywords[kw])

# variable_fun("xiaoming",
#              "hello xiaoming", "nice to meet you!",
#             mother="xiaoma",
#             father="xiaoba",
#             son="see you")
list01 = ["hello xiaoming", "nice to meet you!"]
dict01 = {'mother': 'xiaoma', 'father': 'xiaoba', 'son': 'see you'}
# variable_fun("xiaoming", *list01, **dict01)

def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This key_fun wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# key_fun(1000)                                          # 1 positional argument
# key_fun(voltage=1000)                                  # 1 keyword argument
# key_fun(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# key_fun(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# key_fun('a million', 'bereft of life', 'jump')         # 3 positional arguments
key_fun('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
