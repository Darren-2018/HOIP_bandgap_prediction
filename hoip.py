import element_feature as ef
import combination_generator as cg
import preprocessing as pre
import feature_selection as fs
import test_ratio_selection as trs
import raw_plot as rp
import EDA as e
import gbr as g
import gpr as gp
import krr as k
import svr as s
import decision_tree as dt
import MLP as mlp
import os

data_directory = 'D:\\PycharmProjects\\HOIP_bandgap_prediction\\data'
model_directory = 'D:\\PycharmProjects\\HOIP_bandgap_prediction\\model'

os.chdir(data_directory)

# 初始数据集去重
# ef.raw_drop_duplicates()

# 分离ABX离子特征
# ef.element_feature()

# 生成特征组合的全集和补集
# cg.combination_generator()
# cg.unknown_combination_seperator()

# 初始数据集和归一化后初始数据集的特征统计描述
# e.raw_data_describe()
# e.pre_processing_data_describe()

# 初始数据集特征对标签的分布
# rp.raw_feature_plot('T_f')

# 考察测试集比例对模型精度的影响
# trs.ratio_test()

# 数据柱状图
# e.bar_plot()

os.chdir(model_directory)

# 不同方法做每次舍弃最差的特征筛选
# feature_selection_gbr_reg_list = fs.feature_selector_ensemble('gbr', data_directory)
# feature_selection_rfr_reg_list = fs.feature_selector_ensemble('rfr', data_directory)
# feature_selection_abr_reg_list = fs.feature_selector_ensemble('abr', data_directory)
# feature_selection_etr_reg_list = fs.feature_selector_ensemble('etr', data_directory)

# 考察PCA降维的影响
# feature_selection_mlp_reg_list = fs.feature_selector_pca(X_train, X_test, y_train, y_test, features)

feature_4 = ['P_A', 'P_B', 'X_p-electron', 'VE_B']
feature_5 = ['P_A', 'r_B_s+p', 'IE_B', 'X_p-electron', 'VE_B']

# Gradient Boosting R
# g.gbr(data_directory, feature_4)

# Gaussian Process R
# gp.gpr(data_directory, feature_4)

# Kernel Ridge R
# k.krr(data_directory, feature_4)

# Support Vector R
s.svr(data_directory, feature_4)

# Decision Tree R
# dt.DT()

# MLP R
# mlp.MLP()
