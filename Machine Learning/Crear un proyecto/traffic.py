import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import *
from sklearn.base import *
from sklearn.pipeline import *
from sklearn.preprocessing import *
from sklearn.compose import *
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.metrics import *
from sklearn.ensemble import *

dataset = pd.read_csv('/home/leonel/Downloads/Metro_Interstate_Traffic_Volume.csv')
#http://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume

def traffic_info(X, categorical=False, hist=False):
    print(X.info())
    print(X.describe())
    if (categorical):
        print(X['holiday'].value_counts())
        print(X['weather_main'].value_counts())
        print(X['weather_description'].value_counts())
    if (hist):
        X.hist(bins=50)
        plt.show()

traffic_info(dataset)

def traffic_split(X):
    X['traffic_cat'] = pd.cut(X['traffic_volume'], bins = [-1., 1000., 2000., 3000., 4000., 5000., 6000., 7000., np.inf], labels=[1,2,3,4,5,6,7,8])
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(X, X['traffic_cat']):
        train = X.loc[train_index]
        test = X.loc[test_index]
    return train, test

traffic_train, traffic_test = traffic_split(dataset)

def traffic_plot_bar(X, column):
    a = X[column].value_counts()
    objects = tuple(a.index)
    y_pos = np.arange(len(objects))
    plt.barh(y_pos, a, tick_label=objects)
    plt.show()

def traffic_plot_box(X, column):
    fig, ax = plt.subplots()
    ax.set_title(column)
    ax.boxplot(X[column])
    plt.show()

def traffic_describe(X, bar = None, box = None):
    if bar:
        for b in bar:
            traffic_plot_bar(X, b)
    if box:
        for b in box:
            traffic_plot_box(X, b)

#traffic_describe(traffic_train, bar=['holiday', 'weather_main', 'weather_description'], box=['temp', 'rain_1h', 'snow_1h', 'clouds_all', 'traffic_volume'])
#traffic_describe(traffic_train, box=['temp', 'rain_1h'])

def traffic_corr(X):
    print(X.corr())
    scatter_matrix(X[['traffic_volume', 'temp', 'rain_1h', 'snow_1h', 'clouds_all']])
    plt.show()

def traffic_clear(X):
    X = X.drop(X[X.temp < 200].index)
    X = X.drop(X[X.rain_1h > 2000].index)
    return X

traffic_train = traffic_clear(traffic_train)

#traffic_corr(traffic_train)

traffic_labels = traffic_train['traffic_volume']
traffic_train = traffic_train.drop('traffic_volume', axis=1)

class DateTimeAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        a = pd.to_datetime(X['date_time'], errors='coerce')
        X = np.c_[a.dt.year, a.dt.month, a.dt.day, a.dt.hour]
        return X

num_pipeline = Pipeline([('std_scaler', StandardScaler())])
cat_pipeline = Pipeline([('hot_encoder', OneHotEncoder())])
date_pipeline = Pipeline([('date_adder', DateTimeAttributesAdder()), ('std_scaler', StandardScaler())])

full_pipeline = ColumnTransformer([
    ('num', num_pipeline, ['temp', 'rain_1h', 'snow_1h', 'clouds_all']),
    ('cat', cat_pipeline, ['holiday', 'weather_main', 'weather_description']),
    ('date', date_pipeline, ['date_time'])
])

traffic_prepared = full_pipeline.fit_transform(traffic_train)

def traffic_scores(model, name, dt_prepared, dt_labels):
    X_predictions = model.predict(dt_prepared)
    print(name, ": ", np.sqrt(mean_squared_error(dt_labels, X_predictions)))
    scores = np.sqrt(-cross_val_score(model, dt_prepared, dt_labels, scoring="neg_mean_squared_error", cv=10))
    print("Scores: ", scores)
    print("Mean: ", scores.mean())
    print("Standar deviation: ", scores.std())

#Linear regression
'''lin_reg = LinearRegression()
lin_reg.fit(traffic_prepared, traffic_labels)
traffic_scores(lin_reg, "Linear_regresion", traffic_prepared, traffic_labels)''' #1833.9563

#Decision tree
'''tree_reg = DecisionTreeRegressor()
tree_reg.fit(traffic_prepared, traffic_labels)
traffic_scores(tree_reg, "Decision tree", traffic_prepared, traffic_labels)''' #1107.0095

#Random forest
forest_reg = RandomForestRegressor(max_features=20, n_estimators=60)
forest_reg.fit(traffic_prepared, traffic_labels)
'''traffic_scores(forest_reg, "Random forest", traffic_prepared, traffic_labels) #300.7993

param_grid = [{'n_estimators':[40,50,60], 'max_features':[20, 25, 30]}]
grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error', return_train_score=True)
grid_search.fit(traffic_prepared, traffic_labels)
cvres = grid_search.cv_results_
for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
    print(np.sqrt(-mean_score), params)

Random forest :  300.79934897225
Scores:  [816.76328305 850.37962116 813.37335169 810.53433807 799.42831043
 838.72409716 842.76585627 801.48615072 802.06384049 787.14540875]
Mean:  816.2664257780242
Standar deviation:  19.90848114374631

792.8609182453243 {'max_features': 20, 'n_estimators': 40}
793.4900520122419 {'max_features': 20, 'n_estimators': 50}
788.0983850489744 {'max_features': 20, 'n_estimators': 60}
791.6850137208478 {'max_features': 25, 'n_estimators': 40}
790.5793316767389 {'max_features': 25, 'n_estimators': 50}
787.0544685158745 {'max_features': 25, 'n_estimators': 60}
794.1059198591207 {'max_features': 30, 'n_estimators': 40}
794.1906013968405 {'max_features': 30, 'n_estimators': 50}
792.0853049434867 {'max_features': 30, 'n_estimators': 60}
'''

traffic_test_labels = traffic_test['traffic_volume']
traffic_test = traffic_test.drop('traffic_volume', axis=1)

traffic_test_prepared = full_pipeline.transform(traffic_test)
traffic_test_predictions = forest_reg.predict(traffic_test_prepared)
print("Error: ", np.sqrt(mean_squared_error(traffic_test_labels, traffic_test_predictions)))

for i in range(len(traffic_test_predictions)):
    print(traffic_test_predictions[i], traffic_test_labels.iloc[i])
