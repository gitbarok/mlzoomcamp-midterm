import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

import warnings

warnings.filterwarnings("ignore")

# read data
df = pd.read_csv("data/clean_data.csv")

# split the data
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=42)

y_train = df_train["label"].values
y_val = df_val["label"].values
y_test = df_test["label"].values

del df_train["label"]
del df_val["label"]
del df_test["label"]

df_full_train = df_full_train.reset_index(drop=True)
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

## Initiate the model
dv = DictVectorizer(sparse=False)
model = RandomForestClassifier()

dict_train = df_train.to_dict(orient="records")
X_train = dv.fit_transform(dict_train)

dict_val = df_val.to_dict(orient="records")
X_val = dv.transform(dict_val)

##train the model
model.fit(X_train, y_train)

## export the model
model_name = f"model.bin"
with open(model_name, "wb") as f_out:
    pickle.dump((model, dv), f_out)
