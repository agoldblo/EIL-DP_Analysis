import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import os

# change path to local path to dataset
path_to_data = r'/Users/ari/Documents/PGP/Differential Privacy/Epsilon12.2Data.xlsx'
all_data = pd.read_excel(path_to_data)


def relative_distance_figure(all_data, census_col, dp_col, total_col, race_eth, minority_title):
    """
    relative_distance_figure consumes a dataset of districts and Census demographic variables.
    The function consumes column names for a selected minority group's 
    voting age population (VAP) to plot the Census Bureau's Relative Distance measure 
    against the total voting age population. It produces and saves this figure within the function.

    Parameters
    ----------
    all_data : pandas.DataFrame
        Pandas dataframe with columns representing the political level (Congress, House, ...)
        and Census demographic data both in the 2010 Census and the 2010 Census with 
        differential privacy applied. Each row represents a single district.
    census_col : String
        Column name representing the selected minority's VAP in the 2010 Census.
        For example, an input could be "NHbla_alo_VAP" which represents Black VAP in the 2010 Census.
    dp_col : String
        Column name representing the selected minority's population in the 2010 Census with differential
        privacy applied.
        For example, an input could be "NHBVAP_aloDP" which represents Black VAP
        in the 2010 Census with differential privacy applied.
    total_col : String
        Column name representing the total voting age population in the 2010 Census.
        For example, an input could be "totVAP" which represents the total VAP in the 2010 Census.
    race_eth : String
        Formal name of demographic group that will be used in the x-axis label.
    minority_title : String
        Informal name of demographic group that will be used in the title and figure filename.

    Returns
    -------
    None.

    """
    # set of political levels represented in the dataset
    levels = ["School", "House", "Senate", "Congress"]
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 16})
    ax.yaxis.set_major_formatter(PercentFormatter(decimals = 1))
    plt.ylim([-1.05, 1.05])
    for i in levels:
        # subset the data by district only in the ith political level
        df = all_data[all_data["Political Level"] == i]
        # 2010 Census minority data
        x = df[census_col]
        # 2010 Census minority data with differential privacy added
        y = df[dp_col]
        diff = y - x
        # Census Bureau Relative Distance Measure defined as the difference of the 
        # minority VAP in the 2010 Census data with and without differential privacy applied
        # as a fraction of the total VAP in the 2010 Census.
        relative_dist = diff / df[total_col] * 100
        plt.scatter(x, relative_dist, alpha = 0.5, label = i)
    plt.xlabel("{} in 2010 Census".format(race_eth))
    plt.ylabel("Census Bureau Relative Distance")
    plt.title(minority_title)
    plt.legend(prop={'size': 13}, frameon = True)
    plt.savefig("{} VAP Relative Distance.png".format(minority_title), bbox_inches='tight')
    plt.show()


relative_distance_figure(all_data, "NHbla_alo_VAP", "NHBVAP_aloDP", "totVAP", "NH Black VAP", "Black")
relative_distance_figure(all_data, "NHnat_alo_VAP", "NHnatVAP_aloDP", "totVAP", "NH American Indian VAP", "American Indian")
relative_distance_figure(all_data, "NHasi_alo_VAP", "NHAVAP_aloDP", "totVAP", "NH Asian VAP", "Asian")
relative_distance_figure(all_data, "HVAP", "HVAPDP", "totVAP", "Hispanic VAP", "Hispanic")





