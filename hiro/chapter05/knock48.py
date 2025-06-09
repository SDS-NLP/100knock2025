import os
from dotenv import load_dotenv
from google import genai
import random
import re
import statistics
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from google.genai.types import GenerateContentConfig
import pandas as pd

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# 適当なお題リスト
topics = [
    "プログラミング",
    "コーヒー",
    "雨の日",
    "通勤電車",
    "リモートワーク",
    "スマートフォン",
    "猫",
    "お正月",
    "桜",
    "夏祭り"
]

# ランダムにお題を選択
selected_topic = random.choice(topics)
print(f"お題: {selected_topic}")
print("=" * 30)

# 川柳を3個作成するプロンプト（頑健性テストのため少なめに変更）
prompt = f"""
お題「{selected_topic}」で川柳を3個作成してください。
各川柳には番号を付けて、以下の形式で出力してください：

1. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

2. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

3. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

ユーモアや風刺を込めた川柳を作成してください。
"""

# システム指示を設定
config = GenerateContentConfig(
    system_instruction=[
        "あなたは経験豊かな俳句・川柳の専門家です。",
        "5-7-5の音律（語数ではない）を正確に守り、季語や心情を巧みに表現する才能があります。",
        "日本の伝統的な川柳の技法を理解し、現代的な感性も取り入れることができます。",
        "ユーモアや風刺、人生の機微を短い言葉で表現することが得意です。",
        "音数を正確に数え、美しい日本語で川柳を作成してください。"
    ]
)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=prompt,
    config=config
)

print("【生成された川柳】")
print(response.text)
print("\n" + "=" * 50)

# 川柳を抽出する関数
def extract_senryu(text):
    """生成されたテキストから川柳を抽出する"""
    senryus = []
    lines = text.split('\n')
    current_senryu = []
    current_number = None
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_senryu and len(current_senryu) == 3:
                senryus.append({
                    'number': current_number,
                    'senryu': '\n'.join(current_senryu)
                })
            current_senryu = []
            current_number = None
            continue
            
        # 番号で始まる行を検出
        number_match = re.match(r'^(\d+)\.?\s*(.+)', line)
        if number_match:
            # 前の川柳を保存
            if current_senryu and len(current_senryu) == 3:
                senryus.append({
                    'number': current_number,
                    'senryu': '\n'.join(current_senryu)
                })
            current_number = number_match.group(1)
            current_senryu = [number_match.group(2)]
        elif current_senryu and len(current_senryu) < 3:
            current_senryu.append(line)
    
    # 最後の川柳を保存
    if current_senryu and len(current_senryu) == 3:
        senryus.append({
            'number': current_number,
            'senryu': '\n'.join(current_senryu)
        })
    
    return senryus

# 川柳を評価する関数（温度設定対応版）
def evaluate_senryu(senryu_text, topic, temperature=0.7):
    """川柳の面白さを10段階で評価する"""
    evaluation_prompt = f"""
以下の川柳をお題「{topic}」に対する作品として評価してください。

川柳:
{senryu_text}

評価基準:
1. ユーモア・面白さ（4点満点）
2. お題との関連性（3点満点）
3. 川柳としての技法・表現力（3点満点）

合計10点満点で評価し、以下の形式で回答してください：

【評価点】: X/10点
【評価理由】: 具体的な評価理由を簡潔に記述
"""
    
    evaluation_config = GenerateContentConfig(
        system_instruction=[
            "あなたは川柳の専門評価者です。",
            "ユーモア、表現技法、お題との関連性を総合的に評価してください。",
            "公平で建設的な評価を心がけてください。",
            "評価は1-10の整数で行い、理由も簡潔に述べてください。"
        ],
        temperature=temperature
    )
    
    try:
        eval_response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=evaluation_prompt,
            config=evaluation_config
        )
        return eval_response.text
    except Exception as e:
        return f"評価エラー: {str(e)}"

# スコアを抽出する関数
def extract_score(evaluation_text):
    """評価テキストからスコアを抽出する"""
    score_match = re.search(r'(\d+)/10', evaluation_text)
    if score_match:
        return int(score_match.group(1))
    return None

# 頑健性テスト：同じ川柳を複数回評価
def robustness_test(senryu_text, topic, num_evaluations=10, temperature=0.7):
    """同じ川柳を複数回評価して頑健性をテストする"""
    print(f"\n川柳を{num_evaluations}回評価中...")
    scores = []
    evaluations = []
    
    for i in range(num_evaluations):
        print(f"評価 {i+1}/{num_evaluations}", end=" ")
        evaluation = evaluate_senryu(senryu_text, topic, temperature=temperature)
        score = extract_score(evaluation)
        
        if score is not None:
            scores.append(score)
            evaluations.append(evaluation)
            print(f"スコア: {score}")
        else:
            print("スコア抽出失敗")
    
    if scores:
        return {
            'scores': scores,
            'evaluations': evaluations,
            'mean': statistics.mean(scores),
            'variance': statistics.variance(scores) if len(scores) > 1 else 0,
            'std_dev': statistics.stdev(scores) if len(scores) > 1 else 0,
            'min': min(scores),
            'max': max(scores),
            'range': max(scores) - min(scores),
            'cv': (statistics.stdev(scores)/statistics.mean(scores))*100 if len(scores) > 1 and statistics.mean(scores) > 0 else 0
        }
    else:
        return None

# 統計分析関数
def analyze_robustness(result, senryu_number):
    """スコアの統計分析を行う"""
    if not result:
        print("有効なスコアがありません")
        return None
    
    print(f"\n【川柳{senryu_number}の頑健性分析】")
    print(f"評価回数: {len(result['scores'])}回")
    print(f"平均スコア: {result['mean']:.2f}")
    print(f"分散: {result['variance']:.2f}")
    print(f"標準偏差: {result['std_dev']:.2f}")
    print(f"最小スコア: {result['min']}")
    print(f"最大スコア: {result['max']}")
    print(f"スコア範囲: {result['range']}")
    print(f"変動係数 (CV): {result['cv']:.2f}%")
    print(f"スコア分布: {dict(sorted([(score, result['scores'].count(score)) for score in set(result['scores'])]))}")
    
    # 頑健性の判定
    if result['std_dev'] < 0.8:
        consistency = "非常に高い"
    elif result['std_dev'] < 1.2:
        consistency = "高い"
    elif result['std_dev'] < 1.8:
        consistency = "中程度"
    else:
        consistency = "低い"
    
    print(f"評価の一貫性: {consistency}")
    
    return result

# 可視化関数
def visualize_robustness(all_results, selected_topic):
    """頑健性テストの結果を可視化する"""
    try:
        plt.style.use('default')
    except:
        pass
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'LLM評価の頑健性分析 (お題: {selected_topic})', fontsize=16)
    
    # 各川柳の結果を処理
    senryu_keys = list(all_results.keys())
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # 1. 各川柳のスコア分布（ヒストグラム）
    ax1 = axes[0, 0]
    for i, (senryu_key, result) in enumerate(all_results.items()):
        if result:
            ax1.hist(result['scores'], bins=range(1, 12), alpha=0.6, 
                    label=f'川柳{senryu_key}', color=colors[i % len(colors)], density=True)
    
    ax1.set_title('各川柳のスコア分布')
    ax1.set_xlabel('スコア')
    ax1.set_ylabel('密度')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. 箱ひげ図
    ax2 = axes[0, 1]
    box_data = []
    labels = []
    for senryu_key, result in all_results.items():
        if result:
            box_data.append(result['scores'])
            labels.append(f'川柳{senryu_key}')
    
    if box_data:
        bp = ax2.boxplot(box_data, labels=labels, patch_artist=True)
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.6)
    
    ax2.set_title('各川柳の評価ばらつき')
    ax2.set_xlabel('川柳')
    ax2.set_ylabel('スコア')
    ax2.grid(True, alpha=0.3)
    
    # 3. 標準偏差の比較
    ax3 = axes[1, 0]
    std_devs = []
    labels = []
    for senryu_key, result in all_results.items():
        if result:
            std_devs.append(result['std_dev'])
            labels.append(f'川柳{senryu_key}')
    
    if std_devs:
        bars = ax3.bar(labels, std_devs, color=colors[:len(std_devs)], alpha=0.7)
        ax3.set_title('各川柳の標準偏差')
        ax3.set_xlabel('川柳')
        ax3.set_ylabel('標準偏差')
        ax3.grid(True, alpha=0.3)
        
        # 値をバーの上に表示
        for bar, std_dev in zip(bars, std_devs):
            height = bar.get_height()
            ax3.annotate(f'{std_dev:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    # 4. 変動係数の比較
    ax4 = axes[1, 1]
    cvs = []
    labels = []
    for senryu_key, result in all_results.items():
        if result:
            cvs.append(result['cv'])
            labels.append(f'川柳{senryu_key}')
    
    if cvs:
        bars = ax4.bar(labels, cvs, color=colors[:len(cvs)], alpha=0.7)
        ax4.set_title('各川柳の変動係数')
        ax4.set_xlabel('川柳')
        ax4.set_ylabel('変動係数 (%)')
        ax4.grid(True, alpha=0.3)
        
        # 値をバーの上に表示
        for bar, cv in zip(bars, cvs):
            height = bar.get_height()
            ax4.annotate(f'{cv:.1f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f'robustness_analysis_{selected_topic}.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_summary_visualization(all_results, selected_topic):
    """統計サマリーの可視化"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f'頑健性統計サマリー (お題: {selected_topic})', fontsize=16)
    
    # データ整理
    means = []
    std_devs = []
    labels = []
    
    for senryu_key, result in all_results.items():
        if result:
            means.append(result['mean'])
            std_devs.append(result['std_dev'])
            labels.append(f'川柳{senryu_key}')
    
    # 1. 平均スコア vs 標準偏差の散布図
    ax1 = axes[0]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    for i, (mean, std_dev, label) in enumerate(zip(means, std_devs, labels)):
        ax1.scatter(mean, std_dev, s=150, alpha=0.7, 
                   c=colors[i % len(colors)], label=label)
        ax1.annotate(label, (mean, std_dev), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    ax1.set_xlabel('平均スコア')
    ax1.set_ylabel('標準偏差')
    ax1.set_title('平均スコア vs 評価ばらつき')
    ax1.grid(True, alpha=0.3)
    
    # 理想的な領域を示す
    ax1.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='標準偏差1.0')
    ax1.legend()
    
    # 2. 評価回数とスコア分布
    ax2 = axes[1]
    all_scores = []
    for result in all_results.values():
        if result:
            all_scores.extend(result['scores'])
    
    if all_scores:
        ax2.hist(all_scores, bins=range(1, 12), alpha=0.7, color='skyblue', edgecolor='black')
        ax2.set_title('全評価スコアの分布')
        ax2.set_xlabel('スコア')
        ax2.set_ylabel('頻度')
        ax2.grid(True, alpha=0.3)
        
        # 統計情報を追加
        mean_all = statistics.mean(all_scores)
        std_all = statistics.stdev(all_scores) if len(all_scores) > 1 else 0
        ax2.axvline(mean_all, color='red', linestyle='-', label=f'平均: {mean_all:.2f}')
        ax2.axvline(mean_all - std_all, color='red', linestyle='--', alpha=0.7, label=f'±1σ: {std_all:.2f}')
        ax2.axvline(mean_all + std_all, color='red', linestyle='--', alpha=0.7)
        ax2.legend()
    
    plt.tight_layout()
    plt.savefig(f'robustness_summary_{selected_topic}.png', dpi=300, bbox_inches='tight')
    plt.show()

# 川柳を抽出
senryus = extract_senryu(response.text)

print("【川柳評価結果】")
print("=" * 50)

# 通常の評価（従来通り）
total_score = 0
evaluated_count = 0

for senryu_data in senryus:
    print(f"\n川柳 {senryu_data['number']}:")
    print(senryu_data['senryu'])
    print("-" * 30)
    
    # 通常の評価を1回実行
    evaluation = evaluate_senryu(senryu_data['senryu'], selected_topic, temperature=0.7)
    print(evaluation)
    
    # 評価点を抽出して集計
    score_match = re.search(r'(\d+)/10', evaluation)
    if score_match:
        score = int(score_match.group(1))
        total_score += score
        evaluated_count += 1
    
    print("=" * 50)

# 平均評価を表示
if evaluated_count > 0:
    average_score = total_score / evaluated_count
    print(f"\n【通常評価の総合結果】")
    print(f"評価対象川柳数: {evaluated_count}個")
    print(f"平均評価点: {average_score:.1f}/10点")
    print(f"お題: {selected_topic}")

print("\n" + "=" * 70)
print("【頑健性分析開始】")
print("=" * 70)

# 頑健性テストの実行
all_robustness_results = {}

for senryu_data in senryus:
    print(f"\n川柳 {senryu_data['number']} の頑健性テスト:")
    print(f"テキスト: {senryu_data['senryu']}")
    print("-" * 50)
    
    # 頑健性テストを実行
    result = robustness_test(senryu_data['senryu'], selected_topic)
    
    # 統計分析
    analyzed_result = analyze_robustness(result, senryu_data['number'])
    all_robustness_results[senryu_data['number']] = analyzed_result

# 全体的な頑健性分析
print("\n" + "=" * 70)
print("【全体的な頑健性サマリー】")

all_std_devs = []
all_cvs = []
all_means = []

for senryu_key, result in all_robustness_results.items():
    if result:
        all_std_devs.append(result['std_dev'])
        all_cvs.append(result['cv'])
        all_means.append(result['mean'])

if all_std_devs:
    print(f"全体平均スコア: {statistics.mean(all_means):.2f}")
    print(f"全体平均標準偏差: {statistics.mean(all_std_devs):.3f}")
    print(f"全体平均変動係数: {statistics.mean(all_cvs):.2f}%")
    
    # 頑健性の評価
    overall_avg_std = statistics.mean(all_std_devs)
    if overall_avg_std < 0.8:
        robustness_level = "非常に高い"
    elif overall_avg_std < 1.2:
        robustness_level = "高い"
    elif overall_avg_std < 1.8:
        robustness_level = "中程度"
    else:
        robustness_level = "低い"
    
    print(f"\n【最終結論】")
    print(f"LLM評価の頑健性: {robustness_level}")
    
    # 最も安定した川柳を特定
    if all_robustness_results:
        best_senryu = min(all_robustness_results.keys(), 
                         key=lambda k: all_robustness_results[k]['std_dev'] if all_robustness_results[k] else float('inf'))
        print(f"最も評価が安定した川柳: 川柳{best_senryu} (標準偏差: {all_robustness_results[best_senryu]['std_dev']:.3f})")
    
    # 評価の推奨事項
    if overall_avg_std > 1.5:
        print("⚠️  評価のばらつきが大きいため、複数回評価の平均を取ることを推奨します。")
    elif overall_avg_std < 1.0:
        print("✅ 評価は比較的安定しており、単回評価でも信頼性があります。")
    else:
        print("📊 評価の安定性は中程度です。重要な評価では複数回実施を検討してください。")

# 可視化
print("\n頑健性分析の可視化を生成中...")
try:
    visualize_robustness(all_robustness_results, selected_topic)
    create_summary_visualization(all_robustness_results, selected_topic)
    print("✅ 可視化ファイルが生成されました。")
except Exception as e:
    print(f"可視化エラー: {e}")

print("\n" + "=" * 70)
print("頑健性分析完了")
print("=" * 70)