'''
 0   Unnamed: 0    3650 non-null   int64  
 1   Date          3650 non-null   object 
 2   AveragePrice  3650 non-null   float64
 3   Total Volume  3650 non-null   float64
 4   4046          3650 non-null   float64
 5   4225          3650 non-null   float64
 6   4770          3650 non-null   float64
 7   Total Bags    3650 non-null   float64
 8   Small Bags    3650 non-null   float64
 9   Large Bags    3650 non-null   float64
 10  XLarge Bags   3650 non-null   float64
 11  type          3650 non-null   object 
 12  year          3650 non-null   int64  
 13  region        3650 non-null   object

Fecha: la fecha de la observación
Precio promedio: el precio promedio de un solo aguacate
tipo - convencional u orgánico
año - el año
Región - la ciudad o región de la observación.
Volumen total - número total de aguacates vendidos
4046 - Número total de aguacates con PLU 4046 vendidos
4225 - Número total de aguacates con PLU 4225 vendidos
4770 - Número total de aguacates con PLU 4770 vendidos
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def dataset_info(dataset, hist=False):
    '''Muestra la información básica del dataset'''
    print(dataset)
    print(dataset.info())
    print(dataset.describe())
    for column in dataset:
        if dataset[column].dtypes == object:
            print(dataset[column].value_counts())
    if hist:
        dataset.hist()
        plt.show()

def dataset_train_test_spit(dataset, generalize, bins, labels, hist=False):
    #dataset['index'] = pd.cut(dataset['AveragePrice'], bins=[0.,0.5,1.,1.5,2.,2.5,3.,np.inf], labels=[1,2,3,4,5,6,7])
    dataset['index'] = pd.cut(dataset[generalize], bins=bins, labels=labels)
    if hist:
        dataset['index'].hist(bins=7)
        plt.show()
    from sklearn.model_selection import StratifiedShuffleSplit
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(dataset, dataset['index']):
        train_set = dataset.loc[train_index]
        test_set = dataset.loc[test_index]
    for set_ in (train_set, test_set):
        set_.drop('index', axis=1, inplace=True)
    return train_set, test_set

def dataset_search_corr(dataset, generalize, attributes):
    corr_matrix = avocado.corr()
    print(corr_matrix[generalize].sort_values(ascending=False))
    from pandas.plotting import scatter_matrix
    scatter_matrix(dataset)
    plt.show()

def avocado_transform(dataset, objects):
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import OneHotEncoder
    numerical = dataset.drop(objects, axis=1)
    standard_scaler = StandardScaler()
    numerical_standar = standard_scaler.fit_transform(numerical)
    cat_encoder = OneHotEncoder()
    cat_hot = cat_encoder.fit_transform(dataset[objects])
    return np.c_[numerical_standar, cat_hot.toarray()]

def dataset_rmse(model, dataset_input, dataset_labels):
    from sklearn.metrics import mean_squared_error
    dataset_predictions = model.predict(dataset_input)
    lin_mse = mean_squared_error(dataset_labels, dataset_predictions)
    lin_rmse = np.sqrt(lin_mse)
    return lin_rmse

def dataset_display_scores(scores):
    print("Scores: ", scores)
    print("Mean: ", scores.mean())
    print("Standar deviation: ", scores.std())

avocado = pd.read_csv('./avocado.csv')
#dataset_info(avocado, False)
avocado_train_set, avocado_test_set = dataset_train_test_spit(avocado, 'AveragePrice', [0.,0.5,1.,1.5,2.,2.5,3.,np.inf], [1,2,3,4,5,6,7])
#dataset_search_corr(avocado, 'AveragePrice', ['year', 'XLarge Bags', 'Large Bags', 'Small Bags', 'Total Bags', 'Total Volume'])
#avocado.plot(x='Total Volume', y='AveragePrice', kind='scatter', alpha=0.4, s=(avocado['year'] - 2015) * 8, label='Año', c='Total Bags', cmap=plt.get_cmap('jet'), colorbar=True)
#plt.show()
avocado_labels = avocado_train_set['AveragePrice'].copy()
avocado_train = avocado_train_set.drop('AveragePrice', axis=1)
avocado_prepared = avocado_transform(avocado_train,['Date', 'type', 'region'])

#Traing models
'''from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(avocado_prepared, avocado_labels)
print(dataset_rmse(lin_reg, avocado_prepared, avocado_labels))

from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(avocado_prepared, avocado_labels)
print(dataset_rmse(tree_reg, avocado_prepared, avocado_labels))

from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, avocado_prepared, avocado_labels, scoring="neg_mean_squared_error", cv=10)
tree_rmse_scores = np.sqrt(-scores)
dataset_display_scores(tree_rmse_scores)

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

param_grid = [{'n_estimators':[3,10,30], 'max_features':[2,4,6,8]}, {'bootstrap':[False], 'n_estimators':[3,10], 'max_features':[2,3,4]}]
forest_reg = RandomForestRegressor()

grid_search = RandomizedSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error', return_train_score=True)
grid_search.fit(avocado_prepared, avocado_labels)
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres["mean_test_score"], cvres['params']):
    print(np.sqrt(-mean_score), params)'''

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
forest_reg = RandomForestRegressor()
forest_reg.fit(avocado_prepared, avocado_labels)
forest_scores = cross_val_score(forest_reg, avocado_prepared, avocado_labels, scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
dataset_display_scores(forest_rmse_scores)

final_model = forest_reg

y_test = avocado_test_set['AveragePrice'].copy()
X_test = avocado_test_set.drop('AveragePrice', axis=1)
X_test_prepared = avocado_transform(X_test, ['Date', 'type', 'region'])
dataset_rmse(final_model, X_test_prepared, y_test)

import joblib
joblib.dump(final_model, "avocado_model.pkl")