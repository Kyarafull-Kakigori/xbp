from utils import suumo
import importlib
importlib.reload(suumo)

text = """
名称、カテゴリー、アドレス、アクセス
路線、駅、バス停、
MMまで、バス、徒歩、車、合計時間
築年数、構造、階数、
家賃、管理費、敷金、礼金
間取り、面積、URL
"""

# データの読み込み
df = suumo.read_csv("./data/yokohama_kawasaki.csv", index_col=0, encoding="utf-8")

# データ分析
#df.n_rooms("徒歩")
#df.n_rooms_by_line(["東急東横線", "みなとみらい線"], "徒歩")

df.average_bar("家賃", "徒歩")
df.average_bar_by_line(["東急東横線", "みなとみらい線"], "家賃", "徒歩")

#df.scatter_line("徒歩", "合計時間")
#df.scatter_station(["東急東横線", "みなとみらい線"], "", "合計時間")
