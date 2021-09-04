# 멜론에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 한다.
# 노래는 인덱스 구분하며, 노래를 수록하는 기준은 다음과 같다.
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록한다.
# (단, 각 장르에 속한 노래의재생 수 총합은 모두 다르다.)
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록한다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록한다.
# 노래의 장르를 나타내는 문자열 배열 genres와
# 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 인덱스를 순서대로 반환하시오.


# 장르 별로(key) 우선 재생된 횟수(value)를 저장해야 한다
# 장르 별로 곡의 정보(인덱스, 재생 횟수) 배열로 묶어 저장한다.


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
    # print(genre_total_play_dict)
    # print(genre_index_play_array_dict)

    # 람다 : 특정 인자를 받아서 어떤 값으로 돌려줄 건지를 간단한 수식으로 표현
    # items() : 딕셔너리 키, 값 쌍 얻기 / 딕셔너리 값 반복 시 접근이 유용함
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_genre_play_array)
    result = []
    for genre, value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_by_play_and_index_play_index_array)):
            if i > 1:  # 상위 2개까지만 저장되도록
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0])
    return result


print(get_melon_best_album(genres, plays))  # [4, 1, 3, 0]
