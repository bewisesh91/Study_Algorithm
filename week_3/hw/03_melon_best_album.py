genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    n = len(genre_array)
    genre_each_total = {}
    genre_index_play = {}
    for i in range(n) :
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_each_total :
            genre_each_total[genre] = play
            genre_index_play[genre] = [[i, play]]
        else :
            genre_each_total[genre] += play
            genre_index_play[genre].append([i, play])

    genre_each_total = sorted(genre_each_total.items(), key=lambda item:item[1], reverse=True)
    print(genre_each_total)
    return genre_index_play

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!