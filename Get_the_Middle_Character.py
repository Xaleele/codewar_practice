s = 'test'
empty_list = []

for letter in s:
    empty_list.append(letter)
if len(empty_list) == 1:
    print(empty_list[0])

elif len(empty_list) % 2 != 0:
    print(str(empty_list[round(len(empty_list)/2)]))
else:
    print(str(empty_list[round(len(empty_list)/2)-1])+str(empty_list[round(len(empty_list)/2)]))
def get_middle(s):
    pass