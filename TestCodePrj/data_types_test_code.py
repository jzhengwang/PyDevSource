# math_form = 'print("max how are you?"*5)'
# exec(math_form)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_person(name, age):
    print("There was a man named " + name)
    print("he was " + age + " years old")


def print_logo(position, size):
    print_str = "^"
    print_str = print_str.zfill(position + size)
    print_str = print_str.replace('0', ' ')
    print(print_str)
    print_str = print_str.replace('^', '|')
    mid_index = print_str.index('|')
    max_repl = position + size
    while size > 0:
        tm_print_str = print_str[:mid_index - 1] + '/' + print_str[mid_index:]
        print(tm_print_str)
        size -= 1
        mid_index -= 1
    tm_print_str = print_str[:mid_index - 1] + '/' + print_str[mid_index:]
    tm_print_str = tm_print_str.replace(' ', '_', max_repl)
    tm_print_str = tm_print_str.replace('_', ' ', mid_index - 1)
    print(tm_print_str)

def testmain_list():
    friends = ["Kevin", "Karen", "Jim", "Joseph", "Toby"]
    print(friends[0])  ## Access element with index
    print(friends[-1])  ## Access element with backward
    print(friends[-2])  ## same as above
    print(friends[2:])  ## Acess elements after index include
    print(friends[:2])  ## Access elements before index include
    ## List method, function
    print(friends)
    friends.append("Max")
    friends.insert(1, "Nancy")
    friends.extend(["Tom"])
    print(friends)
    friends.reverse()
    print(friends)
    friends.sort()
    print(friends)
    # friends.clear()
    friends.pop()
    print(friends)
    friends2 = friends.copy()
    print(friends2)


def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


def monthConversion(month):  # dictionary
    monthCon = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }
    print("The {month} is " + monthCon[month])


def test_loop(upToNum):
    i = 1
    while i < upToNum:
        if (i % 5) == 0:
            print("one 5 factor found is " + str(i))
        i += 1
    print("Done with while loop")

    for unit in range(1, upToNum):
        if (unit % 5) == 0:
            print("Unit hit 5 factors: unit = " + str(unit))
    print("Done with for loop")


def guess_game(in_word):
    secret_word = "giraffe"
    while guess != "secret_word":
        guess = input("Enter guess: ")


# Conversion	Meaning
# %[flags][width][.precision]type
# d	Signed integer decimal.
# i	Signed integer decimal.
# o	Unsigned octal.
# u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
# x	Unsigned hexadecimal (lowercase).
# X	Unsigned hexadecimal (uppercase).
# e	Floating point exponential format (lowercase).
# E	Floating point exponential format (uppercase).
# f	Floating point decimal format.
# F	Floating point decimal format.
# g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
# G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
# c	Single character (accepts integer or single character string).
# r	String (converts any python object using repr()).
# s	String (converts any python object using str()).
# %	No argument is converted, results in a "%" character in the result.
def test_print_format():
    print("Only one percentage sign: %% " % ())


def TwoDimensionList():
    number_grid = [
        [10, 20, 30],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]

    for row in number_grid:
        print(row)
        for col in row:
            print(col)


# def translate(phrase):

def test_error_handle():
    try:
        number = int(input("Enter a number:"))
        dividorN = int(input("Enter a dividor:"))
        print(number / dividorN)
    except ZeroDivisionError as err:
        print(err)
        print("Divided by Zero error")
    except ValueError as err:
        print(err)
        print("Invalid input")


def test_file_op():
    print("File operation test")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
