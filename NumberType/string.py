'''
list_string = []
dict_string = {}
i = 1
while i <= 3:
    lists = input("请输入第"+str(i)+"字符：\n")
    list_string.append(lists)
    i += 1
print(list_string)
'''

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

cole = [row[2] for row in M]
print(cole)

dicts = {}
