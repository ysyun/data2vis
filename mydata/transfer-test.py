
import pandas

# df = pandas.read_csv('./test-2018-07_08.csv')
df = pandas.read_csv('./part-00000.csv')
df['date'] = pandas.to_datetime(df['dtts'], unit='ms').astype(str)

df['separator'] = df['step'].map(lambda x: '_')
df['lot_wafer'] = df['lot'] + df['separator'].astype(str) + df['wafer']
df.sort_values(['step', 'idx'], ascending=[1, 1])
df['step_idx'] = df['step'].astype(str) + df['separator'].astype(str) + df['idx'].astype(str)
# step_size = df.groupby(['step']).size()
# print(step_size[0])
# print(step_size[3])



# del df['dtts']
# del df['separator']
# del df['module']
# del df['recipe']
# del df['param']
# del df['lot']
# del df['wafer']
