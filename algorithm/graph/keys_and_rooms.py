from collections import deque
from typing import List


# https://leetcode.com/problems/keys-and-rooms
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    is_locked = [True] * len(rooms)
    q = deque()
    q.append(0)
    is_locked[0] = False
    while q:
        node = q.popleft()
        for child_node in rooms[node]:
            if is_locked[child_node] == True:
                is_locked[child_node] = False
                q.append(child_node)
    return sum(is_locked) == 0


print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
