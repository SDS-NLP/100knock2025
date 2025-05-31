# 東急大井町線（自由が丘 → 大井町）の駅順
stations = [
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

# 急行が停車する駅（自由が丘～大井町方向）
express_stops = {"自由が丘", "大岡山", "旗の台", "大井町"}

# 出発地点
start_station = "自由が丘"

# ステップ1：自由が丘から急行に乗ったとして、次の停車駅を探す
start_index = stations.index(start_station)

# 急行で自由が丘の次に停まる駅を見つける
for i in range(start_index + 1, len(stations)):
    if stations[i] in express_stops:
        missed_station = stations[i]
        break

print(f"つばめちゃんが間違えて降りた駅は: {missed_station}")

# ステップ2：そこから逆方向（各停）で1駅戻る
missed_index = stations.index(missed_station)
destination_index = missed_index - 1
destination_station = stations[destination_index]

print(f"つばめちゃんの目的地は: {destination_station}駅")
