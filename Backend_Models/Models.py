

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib

# Load the data
data = pd.read_csv("C:/Users/akish/Downloads/Home Prediction/Backend_Models/MLS.csv")

# Drop missing values
data.dropna(inplace=True)

# Separate features and target variable
x = data.drop(['CompBenchmark'], axis=1)
y = data['CompBenchmark']

# Split data into training and testing sets
x_train_comp, x_test_comp, y_train_comp, y_test_comp = train_test_split(x, y, test_size=0.2, random_state=42)

# Preprocess training data
train_data = x_train_comp.join(y_train_comp)
epsilon = 1e-10  # A small positive number
train_data['SFDetachBenchmark'] = np.log(train_data['SFDetachBenchmark'].apply(lambda x: max(x, epsilon)) + 1)
train_data['THouseYoYChange'] = np.log(train_data['THouseYoYChange'].apply(lambda x: max(x, epsilon)) + 1)
train_data['ApartYoYChange'] = np.log(train_data['ApartYoYChange'].apply(lambda x: max(x, epsilon)) + 1)
train_data = train_data.join(pd.get_dummies(train_data.Location, dtype=int)).drop(['Location'], axis=1)

# Preprocess test data
test_data = x_test_comp.join(y_test_comp)
test_data['SFDetachBenchmark'] = np.log(test_data['SFDetachBenchmark'].apply(lambda x: max(x, epsilon)) + 1)
test_data['THouseYoYChange'] = np.log(test_data['THouseYoYChange'].apply(lambda x: max(x, epsilon)) + 1)
test_data['ApartYoYChange'] = np.log(test_data['ApartYoYChange'].apply(lambda x: max(x, epsilon)) + 1)
test_data = test_data.join(pd.get_dummies(test_data.Location, dtype=int)).drop(['Location'], axis=1)


# Prepare features and target for model fitting
x_train_comp = train_data.drop(['CompBenchmark'], axis=1)
y_train_comp = train_data['CompBenchmark']
x_test_comp = test_data.drop(['CompBenchmark'], axis=1)
y_test_comp = test_data['CompBenchmark']

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder()
x_train_comp['Date'] = date_encoder.fit_transform(x_train_comp[['Date']])
x_test_comp['Date'] = date_encoder.transform(x_test_comp[['Date']])
scaler = StandardScaler()
x_train_comp_s = scaler.fit_transform(x_train_comp)
x_test_comp_s = scaler.transform(x_test_comp)


# Fit the Random forest_comp model
forest_comp = RandomForestRegressor()
forest_comp.fit(x_train_comp, y_train_comp)
print(f'Random forest_comp R^2 score: {forest_comp.score(x_test_comp, y_test_comp)}')

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
x_train_comp['Date'] = date_encoder.fit_transform(x_train_comp[['Date']])
x_test_comp['Date'] = date_encoder.transform(x_test_comp[['Date']])
scaler = StandardScaler()
x_train_comp_s = scaler.fit_transform(x_train_comp)
x_test_comp_s = scaler.transform(x_test_comp)





# Prepare features and target for model fitting
x_train_SFDetach = train_data.drop(['SFDetachBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_train_SFDetach = train_data['SFDetachBenchmark']
x_test_SFDetach = test_data.drop(['SFDetachBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_test_SFDetach = test_data['SFDetachBenchmark']

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder()
x_train_SFDetach['Date'] = date_encoder.fit_transform(x_train_SFDetach[['Date']])
x_test_SFDetach['Date'] = date_encoder.transform(x_test_SFDetach[['Date']])
scaler = StandardScaler()
x_train_SFDetach_s = scaler.fit_transform(x_train_SFDetach)
x_test_SFDetach_s = scaler.transform(x_test_SFDetach)


# Fit the Random forest_comp model
forest_SFDetach = RandomForestRegressor()
forest_SFDetach.fit(x_train_SFDetach, y_train_SFDetach)
print(f'Random forest_comp R^2 score: {forest_SFDetach.score(x_test_SFDetach, y_test_SFDetach)}')

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
x_train_SFDetach['Date'] = date_encoder.fit_transform(x_train_SFDetach[['Date']])
x_test_SFDetach['Date'] = date_encoder.transform(x_test_SFDetach[['Date']])
scaler = StandardScaler()
x_train_SFDetach_s = scaler.fit_transform(x_train_SFDetach)
x_test_SFDetach_s = scaler.transform(x_test_SFDetach)





# Prepare features and target for model fitting
x_train_SFAttach = train_data.drop(['SFAttachBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_train_SFAttach = train_data['SFAttachBenchmark']
x_test_SFAttach = test_data.drop(['SFAttachBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_test_SFAttach = test_data['SFAttachBenchmark']

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder()
x_train_SFAttach['Date'] = date_encoder.fit_transform(x_train_SFAttach[['Date']])
x_test_SFAttach['Date'] = date_encoder.transform(x_test_SFAttach[['Date']])
scaler = StandardScaler()
x_train_SFAttach_s = scaler.fit_transform(x_train_SFAttach)
x_test_SFAttach_s = scaler.transform(x_test_SFAttach)


# Fit the Random forest_comp model
forest_SFAttach = RandomForestRegressor()
forest_SFAttach.fit(x_train_SFAttach, y_train_SFAttach)
print(f'Random forest_comp R^2 score: {forest_SFAttach.score(x_test_SFAttach, y_test_SFAttach)}')

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
x_train_SFAttach['Date'] = date_encoder.fit_transform(x_train_SFAttach[['Date']])
x_test_SFAttach['Date'] = date_encoder.transform(x_test_SFAttach[['Date']])
scaler = StandardScaler()
x_train_SFAttach_s = scaler.fit_transform(x_train_SFAttach)
x_test_SFAttach_s = scaler.transform(x_test_SFAttach)











# Prepare features and target for model fitting
x_train_THouse = train_data.drop(['THouseBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_train_THouse = train_data['THouseBenchmark']
x_test_THouse = test_data.drop(['THouseBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','ApartIndex','ApartBenchmark','ApartYoYChange'], axis=1)
y_test_THouse = test_data['THouseBenchmark']

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder()
x_train_THouse['Date'] = date_encoder.fit_transform(x_train_THouse[['Date']])
x_test_THouse['Date'] = date_encoder.transform(x_test_THouse[['Date']])
scaler = StandardScaler()
x_train_THouse_s = scaler.fit_transform(x_train_THouse)
x_test_THouse_s = scaler.transform(x_test_THouse)


# Fit the Random forest_comp model
forest_THouse = RandomForestRegressor()
forest_THouse.fit(x_train_THouse, y_train_THouse)
print(f'Random forest_comp R^2 score: {forest_THouse.score(x_test_THouse, y_test_THouse)}')

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
x_train_THouse['Date'] = date_encoder.fit_transform(x_train_THouse[['Date']])
x_test_THouse['Date'] = date_encoder.transform(x_test_THouse[['Date']])
scaler = StandardScaler()
x_train_THouse_s = scaler.fit_transform(x_train_THouse)
x_test_THouse_s = scaler.transform(x_test_THouse)














# Prepare features and target for model fitting
x_train_Apart = train_data.drop(['ApartBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange'], axis=1)
y_train_Apart = train_data['ApartBenchmark']
x_test_Apart = test_data.drop(['ApartBenchmark','CompIndex','CompBenchmark','CompYoYChange','SFDetachIndex','SFDetachBenchmark','SFDetachYoYChange','SFAttachIndex','SFAttachBenchmark','SFAttachYoYChange','THouseIndex','THouseBenchmark','THouseYoYChange'], axis=1)
y_test_Apart = test_data['ApartBenchmark']

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder()
x_train_Apart['Date'] = date_encoder.fit_transform(x_train_Apart[['Date']])
x_test_Apart['Date'] = date_encoder.transform(x_test_Apart[['Date']])
scaler = StandardScaler()
x_train_Apart_s = scaler.fit_transform(x_train_Apart)
x_test_Apart_s = scaler.transform(x_test_Apart)

# Fit the Random forest_comp model
forest_Apart = RandomForestRegressor()
forest_Apart.fit(x_train_Apart, y_train_Apart)
print(f'Random forest_comp R^2 score: {forest_Apart.score(x_test_Apart, y_test_Apart)}')

# Encode 'Date' column and scale features
date_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
x_train_Apart['Date'] = date_encoder.fit_transform(x_train_Apart[['Date']])
x_test_Apart['Date'] = date_encoder.transform(x_test_Apart[['Date']])
scaler = StandardScaler()
x_train_Apart_s = scaler.fit_transform(x_train_Apart)
x_test_Apart_s = scaler.transform(x_test_Apart)

joblib.dump(forest_comp, 'forest_comp_model.pkl')
joblib.dump(forest_SFDetach, 'forest_SFDetach_model.pkl')
joblib.dump(forest_SFAttach, 'forest_SFAttach_model.pkl')
joblib.dump(forest_THouse, 'forest_THouse_model.pkl')
joblib.dump(forest_Apart, 'forest_Apart_model.pkl')
joblib.dump(date_encoder, 'date_encoder.pkl')

joblib.dump(x_train_comp.columns, 'x_train_comp_columns.pkl')

# Similarly for other models
joblib.dump(x_train_SFDetach.columns, 'x_train_SFDetach_columns.pkl')
joblib.dump(x_train_SFAttach.columns, 'x_train_SFAttach_columns.pkl')
joblib.dump(x_train_THouse.columns, 'x_train_THouse_columns.pkl')
joblib.dump(x_train_Apart.columns, 'x_train_Apart_columns.pkl')