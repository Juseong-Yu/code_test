def solution(genres, plays):
    answer = []
    genre_dict = {} # 각 노래가 얼마나 재생되었는지 저장
    play_dict = {} # 각 장르가 얼마나 재생되었는지 저장
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_dict:
            genre_dict[genre] = []
            play_dict[genre] = 0
        genre_dict[genre].append((i, play))
        play_dict[genre] += play
        
    sorted_genres = sorted(play_dict.items(), key = lambda x : x[1], reverse = True) #장르 재생횟수별 정렬
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_dict[genre], key = lambda x : (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    return answer