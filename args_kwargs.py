

            # 1st
# def show_names(a, b, c, d):
#     print(a, b, c, d)

# show_names("Amit", "Rohan", "Joga", "Bitan")

            # 2nd
# def show_name(*args):
#     print(args[1])
#     print(args[2])
# show_name("Amit", "Rohan", "Joga", "Bitan")


           # 3rd

# def show_name(normal, *args):
#     for item in args:
#         print(item, end=" ")
#     print("\n", normal)
#
# lst = ["Anindya", "Niloy", "Rohan", "Goda "]
# normal = 124
# show_name(normal, *lst)

        # 4th
#
# def show_name(normal, *args, **kwargs):
#     for item in args:
#         print(item, end=" ")
#
#     print("\n", normal)
#
#     for key, value in kwargs.items():
#         print(key, value)
#
# lst = ["Anindya", "Niloy", "Rohan", "Goda "]
# normal = 124
# kw = {"1.": "Java", "2.": "C++", "3.": "Python", "4.": ".Net"}
# show_name(normal, *lst, **kw)

   # 5th

def show(n, *lst, **dic):
    print(n)
    for i in lst:
        print(i, end= " ")
    print("\n")
    for k, v in dic.items():
        print(f"{k} is the best {v}")

lst = [1, 2, 3, 4, 5, 10, 20, 30, 40]
dic = {"1": "Java", "2": "C++", "3": "Python", "4": ".Net"}
n = "Coding is the best thing"
show(n, *lst, **dic)