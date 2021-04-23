import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    current_day_index = 0
    max_heap = []

    while stock < k :       # 재고가 목표 일자까지 버틸 수 있는 정도만 필요하기 때문
        for date_index in range(current_day_index, len(dates)) :  # 공급 가능한 일자만큼 반복
            if dates[date_index] <= stock :    # 공급 가능한 일자 중에서 재고 보다 적은 경우에만 heap 구조에 최댓 값으로 넣는다.
                heapq.heappush(max_heap, -supplies[date_index])   # 우리는 주어진 조건을 충족하는 것 중에서 최댓 값만 필요
            else :
                current_day_index = date_index   # current_day_index를 update 해준다.
                break
        answer += 1
        stock += -heapq.heappop(max_heap)

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))