import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import numpy as np
pd.set_option('display.max_columns', 500)

data = pd.read_csv("C:\\Users\\Maria\\PycharmProjects\\dataprojectbr\\venv\\Include\\houserentals.sp.csv.csv")


def unique_cities():
    unique_cities = sorted ((data ['city'].unique()))
    return unique_cities


def get_rent_min_max():
    max_min = 'From %s until %s rent' % (data.rent.min(), data.rent.max())
    return max_min


def get_rent_mean():
    rent_mean = data['rent'].mean()
    return rent_mean


def get_frequency():
    frequency = data.value_counts()
    return frequency


def get_mode():
    n = data.shape[0]
    return n/2


def get_median():
    data_median = data.median()
    return data_median


def first_plot():
    ax = sns.distplot(data.rent)
    ax.figure.set_size_inches(12,6)
    ax.set_title("House rentals", fontsize=18)
    ax.set_xlabel("Price", fontsize=14)
    data.rent.hist(bins = 20, figsize= (12,6))
    return plt.show()
    #see if it needs a return


def rent_over_5mins():
    min_wage = 1045
    total_data = len(data)
    rent_over_5 = data.rent > 5 * min_wage
    rent_over_perc = rent_over_5 / total_data * 100
# (normalize=True)
    return rent_over_perc


def describe_rent():
    rent_desc = data['rent'].describe()
    return rent_desc

def correlation():
    pearsoncorr = data.corr(method ='pearson')
# 'kendall' #'spearman' #‘pearson’
    return pearsoncorr
# pearson correlation = data['rent'].corr(data['rooms'])(method ='pearson')

def get_heatmap_corr():
    plt.title('Pearson Correlation - Rental Houses', fontsize =20)
    sns.heatmap(pearsoncorr,
                xticklabels=pearsoncorr.columns,
                yticklabels=pearsoncorr.columns,
                cmap='RdBu_r', #"YlGnBu", #'RdBu_r'
                annot=True,
                linewidth=0.3,
                edgecolor='blue',
                linecolor='black',
            )
    return plt.show()

