import matplotlib.pyplot as plt
from collections import Counter
from knock36 import load_cleaned_articles, get_all_tokens

# 1. コーパス読み込みと全語抽出（補助記号は除去済み）
articles = load_cleaned_articles()
tokens = get_all_tokens(articles)

# 2. 頻度カウント
counter = Counter(tokens)
freqs = sorted(counter.values(), reverse=True)  # 頻度順に並べる

# 3. 順位リストを作成（1位〜）
ranks = list(range(1, len(freqs) + 1))

# ========== 🔹 通常スケールのグラフ ==========
plt.figure(figsize=(8, 6))
plt.plot(ranks, freqs)
plt.xlabel("Rank of word")
plt.ylabel("Frequency")
plt.title("Word Frequency vs Rank (Linear Scale)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("zipf_linear.png")
print("✅ 通常スケールグラフを 'zipf_linear.png' に保存しました。")

# ========== 🔹 両対数グラフ（Zipf） ==========
plt.figure(figsize=(8, 6))
plt.plot(ranks, freqs)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Rank of word (log)")
plt.ylabel("Frequency (log)")
plt.title("Zipf's Law: Word Frequency vs Rank (Log-Log Scale)")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("zipf_loglog.png")
print("✅ 両対数グラフを 'zipf_loglog.png' に保存しました。")