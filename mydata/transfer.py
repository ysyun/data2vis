import pandas

# df = pandas.read_csv('./test-2018-07_08.csv')
df = pandas.read_csv('./part-00000.csv')
df['date'] = pandas.to_datetime(df['dtts'], unit='ms').astype(str)

# df['separator'] = df['step'].map(lambda x: '_')
# df['lot_wafer'] = df['lot'] + df['separator'].astype(str) + df['wafer']
df.sort_values(['step', 'idx'], ascending=[True, True], inplace=True)
df['step_idx'] = df['step'].astype(str) + '_' + df['idx'].astype(str)
i=-1
def increase(x):
    global i
    i += 1
    # return x[0:x.find('_')] + '_' + str(i)
    return i


df['count'] = df['step_idx'].map(lambda x: increase(x))
# df['wafer_step_count'] = df['wafer'] + '_' + df['step'].astype(str) + '_' + df['count'].astype(str)
del df['dtts']
# del df['separator']
# del df['module']
# del df['recipe']
# del df['param']
# del df['lot']
# del df['wafer']

# {
#     "wafer": "LOT180731-082159.542.1",
#     "step": 0,
#     "idx": 0,
#     "point": 54.2368291482,
#     "lot": "LOT180731-082159.542",
#     "recipe": "COND_HSE_IDP",
#     "date": "2018-07-30 23:24:08.452",
#     "lot_wafer": "LOT180731-082159.542_LOT180731-082159.542.1",
#     "step_idx": "0_0",
#     "count": 0,
#     "step_count": "0_0"
# }
# cols = ['wafer', 'step', 'idx', 'count', 'point', 'lot', 'recipe', 'date', 'lot_wafer', 'step_idx', 'step_count']
# df = df[cols]

# with open('./test-2018-07_08.json', 'w') as f:
with open('./step_point.json', 'w') as f:
    f.write(df.to_json(orient='records'))
