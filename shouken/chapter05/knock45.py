# 東急大井町線（溝の口方面 → 自由が丘 → 大井町方面）の駅リスト
stations = [
    "溝の口",
    "高津",
    "二子新地",
    "二子玉川",
    "上野毛",
    "等々力",
    "尾山台",
    "九品仏",
    "自由が丘",
    "緑が丘",
    "大岡山",
    "北千束",
    "旗の台",
    "荏原町",
    "中延",
    "戸越公園",
    "下神明",
    "大井町"
]

# 急行が停まる駅（上り・下り共通）
express_stops = {"自由が丘", "二子玉川", "大井町", "旗の台", "大岡山"}

# 出発地点
start_station = "自由が丘"
destination_station = "緑が丘"

# ステップ1：反対方向（溝の口方面）に急行に乗ってしまった場合
start_index = stations.index(start_station)

# 急行で次に停車する駅（進行方向における）
for i in range(start_index - 1, -1, -1):
    if stations[i] in express_stops:
        mistaken_stop = stations[i]
        break

print(f"つばめちゃんが間違えて降りた駅: {mistaken_stop}")

# ステップ2：そこから各駅停車で目的地「緑が丘」までの駅数を数える
mistaken_index = stations.index(mistaken_stop)
destination_index = stations.index(destination_station)

# 各駅停車で乗り直す（上り方向）
num_stops = 0
for i in range(mistaken_index + 1, destination_index + 1):
    num_stops += 1

print(f"{mistaken_stop}から各駅停車で{num_stops}駅目が目的地「{destination_station}」です。")
