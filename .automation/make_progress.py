from pathlib import Path
from pprint import pprint
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import datetime


class User:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.progress = [0] * 10


def get_progress() -> List[User]:
    cur = Path(".")
    users = list(
        filter(lambda x: x.is_dir() and not is_ignored(
            x.name), sorted(cur.iterdir()))
    )

    progress = list()
    # user ごとの progress を取得する
    for user in users:
        u = User(user.name, user)
        for chap, max_cnt in enumerate(QUESTIONS):
            # user/chapterXX の path (章だけ 1-indexed なので num+1)
            chapter_path = Path(user / f"chapter{chap+1:02d}")
            # user/chapterXX に含まれる .py, .sh, .ipynb ファイルの数をカウント
            cnt = 0
            for ext in ["py", "sh", "ipynb"]:
                cnt += len(list(chapter_path.glob(f"*.{ext}")))
            # 問題数は max_cnt が上限で、それ以上のファイル数が含まれる場合は max_cnt にする
            solved_cnt = min(cnt, max_cnt)
            u.progress[chap] = solved_cnt
        progress.append(u)

    return progress


def plot_progress(users: np.array, scores: np.array):
    # 描画されるグラフのサイズを指定
    plt.figure(figsize=(8, 6))

    # 各章ごとに棒グラフを積み上げていく
    for chap in range(CHAPTER):
        label = f"chapter {chap+1:02d}"
        bottom = np.sum(scores[:, :chap], axis=1)
        plt.bar(
            users,
            scores[:, chap],
            bottom=bottom,
            align="center",
            tick_label=users,
            label=label,
        )
    today = datetime.date.today()
    date_list = list()
    # date_list.append(datetime.date(2025, 4, 14))
    date_list.append(datetime.date(2025, 4, 21))
    date_list.append(datetime.date(2025, 4, 28))
    # date_list.append(datetime.date(2025, 5, 5))
    date_list.append(datetime.date(2025, 5, 12))
    date_list.append(datetime.date(2025, 5, 19))
    date_list.append(datetime.date(2025, 5, 26))
    date_list.append(datetime.date(2025, 6, 2))
    date_list.append(datetime.date(2025, 6, 9))
    date_list.append(datetime.date(2025, 6, 16))
    date_list.append(datetime.date(2025, 6, 23))
    date_list.append(datetime.date(2025, 6, 30))
    # print(date_list)
    d = [date for date in date_list if today >= date]
    # print(date_list)
    # print(d)
    # print(len(d))
    xmin, xmax = plt.xlim()
    if len(d) != 10 and len(d) != 0:
        label = "{}Border".format(str(date_list[len(d)])[5:])
        plt.hlines((len(d)+1) * 10, xmin, xmax, linewidth=2,
                   linestyle='dashed', color="gray", label=label)
        plt.xlim(xmin, xmax)

    if len(d) != 0:
        label = "{}Border".format(str(d[-1])[5:])
        plt.hlines(len(d) * 10, xmin, xmax, linewidth=4,
                   color="red", label=label)

    plt.xlim(xmin, xmax)

    # グラフの設定
    plt.xticks(rotation=30, fontsize=10)
    # 縦軸のラベルを 10 問刻みにする
    whole = sum(QUESTIONS)
    plt.ylim(0, whole+1)
    plt.yticks(np.arange(0, whole + 1, 10))
    # 凡例をグラフの外側に表示する
    plt.legend(bbox_to_anchor=(1.28, 1.0))
    plt.subplots_adjust(right=0.8)
    # グラフを書き出す
    plt.savefig("progress.png")


def main():
    data = get_progress()
    users = np.array([user.name for user in data])
    scores = np.array([user.progress for user in data])

    if scores.size:
        plot_progress(users, scores)


if __name__ == "__main__":
    sns.set()
    # 章数と各章の問題数
    CHAPTER = 10
    QUESTIONS = [10] * CHAPTER
    # progress bar に表示しないディレクトリ名
    IGNORE = [""]
    def is_ignored(name): return name in IGNORE or name.startswith(".")

    main()
