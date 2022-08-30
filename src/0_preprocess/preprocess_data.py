#%%
import pandas as pd
import pickle
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

#%%
PROJECT_PATH = Path().cwd()
DATA_PATH = PROJECT_PATH.joinpath('data')

data = pd.read_csv(DATA_PATH.joinpath('raw','train.csv'))
#%%
data = data[['Survived','Pclass','Sex','Age','Parch','Fare','Cabin','Embarked']]

data.select_dtypes('object')
#%%

data.Cabin = data.Cabin.str.extract(r'(^\w)')

#%%
def encode_column(column:pd.Series):
    values = list(column.unique())
    v2i = {v : idx for idx, v in enumerate(values)}
    i2v = {v : k for k, v in v2i.items()}
    
    return column.replace(v2i), v2i, i2v

encoders = {}
data.Cabin, _, encoders['Cabin'] = encode_column(data.Cabin)
data.Sex, _, encoders['Sex'] = encode_column(data.Sex)
data.Embarked, _, encoders['Embarked'] = encode_column(data.Embarked)
#%%
# Minmax Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

#%%
with open(DATA_PATH.joinpath('processed','data.pkl'),'wb') as f:
    pickle.dump(scaled_data, f)