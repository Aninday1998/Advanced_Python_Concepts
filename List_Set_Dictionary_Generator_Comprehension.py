# List Comprehension, Dictionary Comprehension, Set Comprehension,

        # 1st
#
# lst = []
# for i in range(100):
#     if i % 3 == 0:
#         lst.append(i)
# print(lst)

        # 2nd           List Comprehension
#
# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)


        # 3rd Dictionary Comprehension

# dic = {i: f"item{i}" for i in range(30) if i % 3 == 0}
#
# dic = {value: key for key, value in dic.items()}
#
# print(dic)


        # 4th  Set Comprehension

# dress = {dress for dress in ['D1', 'D2', 'D3', 'D4', 'D1', 'D1']}
# print(dress)


        # 5th Generator Comprehension

num = (i for i in range(25) if i % 3 == 0)
print(type(num))
for j in num:
    print(j)
