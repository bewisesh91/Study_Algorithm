from collections import deque

c = 11
b = 2


# 코니
# 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 이동
# 속도 : 0 1 2 3 4 5
# 위치 : 11 12 14 17 21 26

# 브라운
# b-1, b+1, b*2
# 1초 후 1, 3, 4
# 2초 후 1인 경우, 0, 2, 4 / 3인 경우, 2, 4, 4 / 4인 경우, 3, 5, 8
# 경우의 수가 너무 많다.
# 경우의 수가 많은 경우 -> BFS를 사용하자!
# 각 시간 마다 갈 수 있는 위치를 저장

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 브라운의 위치와 시간을 담는다.
    visited = [{} for _ in range(200001)]  # 200000개의 딕셔너리를 만든다.

    while cony_loc <= 200000:
        cony_loc += time

        if time in visited[cony_loc]:
            return time

        for i in range(len(queue)):
            current_position, current_time = queue.popleft()
            # 새로운 시간
            new_time = current_time + 1

            # 새로운 위치
            new_position = current_position - 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1


print(catch_me(c, b))
