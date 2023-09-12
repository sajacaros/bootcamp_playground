from collections import deque
from typing import List


# https://leetcode.com/problems/keys-and-rooms
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    empty = [True] * len(rooms)
    q = deque()
    q.append(0)
    empty[0] = False
    while q:
        node = q.popleft()
        for child_node in rooms[node]:
            if empty[child_node] == True:
                empty[child_node] = False
                q.append(child_node)
    return sum(empty) == 0


print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
