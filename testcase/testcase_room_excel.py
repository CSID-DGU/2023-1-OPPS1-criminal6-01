import pandas as pd
from enum import Enum

class Genre(Enum):
    ADVENTURE = 0
    ANIMATION = 1
    COMEDY = 2
    FANTASY = 3
    ROMANCE = 4
    THRILLER = 5
    DRAMA = 6
    HORROR = 7
    SF = 8
    DOCUMENTARY = 9

class Level(Enum):
    HIGH = 2
    MEDIUM = 1
    LOW = 0

class Room:
    def __init__(self, genre, difficulty, horror, activity):
        self.genre = genre
        self.difficulty = difficulty
        self.horror = horror
        self.activity = activity

rooms = []

# 모든 조합 생성
for genre in Genre:
    for difficulty in Level:
        for horror in Level:
            for activity in Level:
                room = Room(genre, difficulty, horror, activity)
                rooms.append(room)

# 엑셀 파일 생성 및 데이터 저장
output_data = []
for room in rooms:
    output_data.append([room.genre.name, room.difficulty.value, room.horror.value, room.activity.value])

output_df = pd.DataFrame(output_data, columns=["장르", "난이도", "공포도", "활동성"])
output_df.to_excel("room_list.xlsx", index=False)
