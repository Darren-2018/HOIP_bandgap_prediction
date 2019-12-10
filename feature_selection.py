from sklearn.ensemble import GradientBoostingRegressor as GBR
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA
from sklearn.neural_network import MLPRegressor
import pandas as pd
import numpy as np

def __gbr_test(X_train, X_test, y_train, y_test):
    reg = GBR(random_state=1)
    reg.fit(X_train, y_train)
    return reg, reg.score(X_test, y_test), reg.feature_importances_

def feature_selector_gbr(X_tr, X_te, y_tr, y_te, feature, cwd):
    reg_list = []
    X_train, X_test, y_train, y_test = X_tr, X_te, y_tr, y_te
    local_feature = feature
    df = pd.DataFrame(columns=['number','reg_score','adj. r**2','feature_list'])
    while len(local_feature) > 1:
        reg, score, weight = __gbr_test(X_train, X_test, y_train, y_test)
        reg_list.append(reg)
        df = df.append(pd.DataFrame([[len(local_feature),score,1-(1-score*score)*(40)/(40-len(local_feature)),np.array(local_feature)]],columns=df.columns), ignore_index=True)
        low = np.argmin(weight)
        del local_feature[low]
        X_train = np.delete(X_train, low, axis=1)
        X_test = np.delete(X_test, low, axis=1)
    df.to_csv(cwd+'feature_selection_gbr.csv', index=False)
    return reg_list

def __mlp_test(X_train, X_test, y_train, y_test):
    reg = MLPRegressor(hidden_layer_sizes=(20,),max_iter=10000,random_state=1)
    reg.fit(X_train, y_train)
    return reg, reg.score(X_test, y_test)

def feature_selector_mlp(X_tr, X_te, y_tr, y_te, feature, cwd):
    reg_list = []
    X_train, X_test, y_train, y_test = X_tr, X_te, y_tr, y_te
    local_feature = feature
    df = pd.DataFrame(columns=['number','reg_score','feature_list'])
    while len(local_feature) > 1:
        reg, score, weight = __mlp_test(X_train, X_test, y_train, y_test)
        reg_list.append(reg)
        low = np.argmin(weight)
        del local_feature[low]
        df = df.append(pd.DataFrame([[len(local_feature),score,np.array(local_feature)]],columns=df.columns), ignore_index=True)
        X_train = np.delete(X_train, low, axis=1)
        X_test = np.delete(X_test, low, axis=1)
    df.to_csv(cwd+'feature_selection_mlp.csv', index=False)
    return reg_list

def __pca_test(dem, X_tr, X_te, y_train, y_test):
    reg = KernelPCA(kernel='linear',n_components=dem, random_state=1)
    re = reg.fit(np.vstack((X_tr, X_te)))
    X_train = re.transform(X_tr)
    X_test = re.transform(X_te)
    reg, score = __mlp_test(X_train, X_test, y_train, y_test)
    print(score)
    return reg, score

def feature_selector_pca(X_tr, X_te, y_tr, y_te, feature, cwd):
    reg_list = []
    X_train, X_test, y_train, y_test = X_tr, X_te, y_tr, y_te
    local_feature = feature
    df = pd.DataFrame(columns=['number','reg_score','adj. r**2'])
    for i in range(2,len(local_feature)+1):
        reg, score = __pca_test(i, X_train, X_test, y_train, y_test)
        df = df.append(pd.DataFrame([[i,score,1-(1-score*score)*(40)/(40-i)]],columns=df.columns), ignore_index=True)
    df.to_csv(cwd+'feature_selection_pca.csv', index=False)
    return reg_list


