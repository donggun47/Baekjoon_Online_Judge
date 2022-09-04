king, queen, rook, bishop, knight, pawn = map(int, input().split())

list1 = [1, 1, 2, 2, 2, 8]
list2 = [king, queen, rook, bishop, knight, pawn]

add_list = [list1[i] - list2[i] for i in range(len(list1))]
print(*add_list) # *(애스터리스크)리스트or튜플 = unpacking
