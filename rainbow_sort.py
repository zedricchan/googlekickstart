#n cards on a table
def test():
    N = input()
    num_list = N.split(' ')
    appeared = []
    for i in range(len(num_list)):
        if num_list[i] not in appeared:
            appeared.append(num_list[i])
        elif num_list[i] in appeared and (num_list[i] != num_list[i-1]):
            return 'IMPOSSIBLE'
    return appeared

#main
T = input()
for i in range(T):
    print(test())
