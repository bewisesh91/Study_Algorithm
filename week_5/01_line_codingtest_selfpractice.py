from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0
    queue = deque()
    queue.append((brown_loc, time))
    brown_possible_loc = []
    for i in range(200000) :
        brown_possible_loc.append({})

    while cony_loc <= 200000 :
        cony_loc += time

        if time in brown_possible_loc[cony_loc]:
            return time

        for i in range(len(queue)) :
            brown_current_loc, brown_current_time = queue.popleft()

            new_brown_time = brown_current_time + 1

            new_brown_loc = brown_current_loc - 1
            if new_brown_loc >= 0 and new_brown_time not in brown_possible_loc[new_brown_loc] :
                brown_possible_loc[new_brown_loc][new_brown_time] = True
                queue.append((new_brown_loc, new_brown_time))

            new_brown_loc = brown_current_loc + 1
            if new_brown_loc >= 0 and new_brown_time not in brown_possible_loc[new_brown_loc]:
                brown_possible_loc[new_brown_loc][new_brown_time] = True
                queue.append((new_brown_loc, new_brown_time))

            new_brown_loc = brown_current_loc * 2
            if new_brown_loc >= 0 and new_brown_time not in brown_possible_loc[new_brown_loc]:
                brown_possible_loc[new_brown_loc][new_brown_time] = True
                queue.append((new_brown_loc, new_brown_time))

        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!