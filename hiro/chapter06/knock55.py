import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(script_dir, 'ans54.txt')
df = pd.read_csv(txt_path, sep=" ", header=None)
print((df[3] == df[4]).sum() / len(df))