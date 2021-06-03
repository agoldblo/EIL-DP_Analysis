import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import os

# change path to local path to dataset
# base_path = '/Users/hwheelen/Downloads/Subjurisdictions'

#specify details about each jurisdiction

az_apache = pd.read_csv('D:/Census/Localities/AZ/AZ_Apache_BOS.csv')
az_apache_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Apache_BOS_blocks.csv')
az_apache['map'] = 'AZ Apache BOS'
az_apache['state'] = 'AZ'
az_apache['dist_type'] = 'County BOS'
az_apache_blocks['map'] = 'AZ Apache BOS'
az_apache_blocks['state'] = 'AZ'
az_apache_blocks['dist_type'] = 'County BOS'

az_cochise = pd.read_csv('D:/Census/Localities/AZ/AZ_Cochise_Bisbee.csv')
az_cochise_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Cochise_Bisbee_blocks.csv')
az_cochise['map'] = 'AZ Cochise Bisbee'
az_cochise['state'] = 'AZ'
az_cochise['dist_type'] = 'City'
az_cochise_blocks['map'] = 'AZ Cochise Bisbee'
az_cochise_blocks['state'] = 'AZ'
az_cochise_blocks['dist_type'] = 'City'

az_coconino = pd.read_csv('D:/Census/Localities/AZ/AZ_Coconino_BOS.csv')
az_coconino_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Coconino_BOS_blocks.csv')
az_coconino['map'] = 'AZ Coconino BOS'
az_coconino['state'] = 'AZ'
az_coconino['dist_type'] = 'County BOS'
az_coconino_blocks['map'] = 'AZ Coconino BOS'
az_coconino_blocks['state'] = 'AZ'
az_coconino_blocks['dist_type'] = 'County BOS'

az_gila = pd.read_csv('D:/Census/Localities/AZ/AZ_Gila_Comm.csv')
az_gila_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Gila_Comm_blocks.csv')
az_gila['map'] = 'AZ Gila Comm'
az_gila['state'] = 'AZ'
az_gila['dist_type'] = 'County Comm'
az_gila_blocks['map'] = 'AZ Gila Comm'
az_gila_blocks['state'] = 'AZ'
az_gila_blocks['dist_type'] = 'County Comm'

az_gila_globe = pd.read_csv('D:/Census/Localities/AZ/AZ_Gila_Globe.csv')
az_gila_globe_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Gila_Globe_blocks.csv')
az_gila_globe['map'] = 'AZ Gila Globe'
az_gila_globe['state'] = 'AZ'
az_gila_globe['dist_type'] = 'City'
az_gila_globe_blocks['map'] = 'AZ Gila Globe'
az_gila_globe_blocks['state'] = 'AZ'
az_gila_globe_blocks['dist_type'] = 'City'

az_navajo = pd.read_csv('D:/Census/Localities/AZ/AZ_Navajo_BOS.csv')
az_navajo_blocks = pd.read_csv('D:/Census/Localities/AZ/AZ_Navajo_BOS_blocks.csv')
az_navajo['map'] = 'AZ Navajo BOS'
az_navajo['state'] = 'AZ'
az_navajo['dist_type'] = 'County BOS'
az_navajo_blocks['map'] = 'AZ Navajo BOS'
az_navajo_blocks['state'] = 'AZ'
az_navajo_blocks['dist_type'] = 'County BOS'

ca_hanford = pd.read_csv('D:/Census/Localities/CA/CA_Kings_Hanford_Elem.csv')
ca_hanford = ca_hanford.loc[ca_hanford['local_id'] > 0]
ca_hanford_blocks = pd.read_csv('D:/Census/Localities/CA/CA_Kings_Hanford_Elem_blocks.csv')
ca_hanford_blocks = ca_hanford_blocks.loc[ca_hanford_blocks['local_id'] > 0]
ca_hanford['map'] = 'CA Hanford Elem'
ca_hanford['state'] = 'CA'
ca_hanford['dist_type'] = 'S.D.'
ca_hanford_blocks['map'] = 'CA Hanford Elem'
ca_hanford_blocks['state'] = 'CA'
ca_hanford_blocks['dist_type'] = 'S.D.'

ca_riverdale = pd.read_csv('D:/Census/Localities/CA/CA_Kings_Riverdale_SD.csv')
ca_riverdale = ca_riverdale.loc[ca_riverdale['local_id'] > 0]
ca_riverdale_blocks = pd.read_csv('D:/Census/Localities/CA/CA_Kings_Riverdale_SD_blocks.csv')
ca_riverdale_blocks = ca_riverdale_blocks.loc[ca_riverdale_blocks['local_id'] > 0]
ca_riverdale['map'] = 'CA Riverdale S.D.'
ca_riverdale['state'] = 'CA'
ca_riverdale['dist_type'] = 'S.D.'
ca_riverdale_blocks['map'] = 'CA Riverdale S.D.'
ca_riverdale_blocks['state'] = 'CA'
ca_riverdale_blocks['dist_type'] = 'S.D.'

ca_merced = pd.read_csv('D:/Census/Localities/CA/CA_Merced_Weaver_SD.csv')
ca_merced = ca_merced.loc[ca_merced['local_id'] > 0]
ca_merced_blocks = pd.read_csv('D:/Census/Localities/CA/CA_Merced_Weaver_SD_blocks.csv')
ca_merced_blocks = ca_merced_blocks.loc[ca_merced_blocks['local_id'] > 0]
ca_merced['map'] = 'CA Weaver S.D. (Merced County)'
ca_merced['state'] = 'CA'
ca_merced['dist_type'] = 'S.D.'
ca_merced_blocks['map'] = 'CA Weaver S.D. (Merced County)'
ca_merced_blocks['state'] = 'CA'
ca_merced_blocks['dist_type'] = 'S.D.'

fl_collier = pd.read_csv('D:/Census/Localities/FL/FL_Collier_SD.csv')
fl_collier_blocks = pd.read_csv('D:/Census/Localities/FL/FL_Collier_SD_blocks.csv')
fl_collier['map'] = 'FL Collier S.D.'
fl_collier['state'] = 'FL'
fl_collier['dist_type'] = 'S.D.'
fl_collier_blocks['map'] = 'FL Collier S.D.'
fl_collier_blocks['state'] = 'FL'
fl_collier_blocks['dist_type'] = 'S.D.'

fl_hendry = pd.read_csv('D:/Census/Localities/FL/FL_Hendry_Comm.csv')
fl_hendry_blocks = pd.read_csv('D:/Census/Localities/FL/FL_Hendry_Comm_blocks.csv')
fl_hendry['map'] = 'FL Hendry Comm'
fl_hendry['state'] = 'FL'
fl_hendry['dist_type'] = 'County Comm'
fl_hendry_blocks['map'] = 'FL Hendry Comm'
fl_hendry_blocks['state'] = 'FL'
fl_hendry_blocks['dist_type'] = 'County Comm'

sd_charles = pd.read_csv('D:/Census/Localities/SD/SD_Charles_Mix_Comm.csv')
sd_charles_blocks = pd.read_csv('D:/Census/Localities/SD/SD_Charles_Mix_Comm_blocks.csv')
sd_charles['map'] = 'SD Charles Mix Comm'
sd_charles['state'] = 'SD'
sd_charles['dist_type'] = 'County Comm'
sd_charles_blocks['map'] = 'SD Charles Mix Comm'
sd_charles_blocks['state'] = 'SD'
sd_charles_blocks['dist_type'] = 'County Comm'

sd_shannon = pd.read_csv('D:/Census/Localities/SD/SD_Shannon_Comm.csv')
sd_shannon_blocks = pd.read_csv('D:/Census/Localities/SD/SD_Shannon_Comm_blocks.csv')
sd_shannon['map'] = 'SD Shannon Comm'
sd_shannon['state'] = 'SD'
sd_shannon['dist_type'] = 'County Comm'
sd_shannon_blocks['map'] = 'SD Shannon Comm'
sd_shannon_blocks['state'] = 'SD'
sd_shannon_blocks['dist_type'] = 'County Comm'

sd_todd = pd.read_csv('D:/Census/Localities/SD/SD_Todd_Comm.csv')
sd_todd_blocks = pd.read_csv('D:/Census/Localities/SD/SD_Todd_Comm_blocks.csv')
sd_todd['map'] = 'SD Todd Comm'
sd_todd['state'] = 'SD'
sd_todd['dist_type'] = 'County Comm'
sd_todd_blocks['map'] = 'SD Todd Comm'
sd_todd_blocks['state'] = 'SD'
sd_todd_blocks['dist_type'] = 'County Comm'


# combine all jurisdictions
jurisdictions_az = [az_apache, az_cochise, az_coconino, az_gila, az_gila_globe, az_navajo]
jurisdictions_ca = [ca_hanford, ca_riverdale, ca_merced]
jurisdictions_fl = [fl_collier, fl_hendry]
jurisdictions_sd = [sd_charles, sd_shannon, sd_todd]

jurisdictions = jurisdictions_az + jurisdictions_ca + jurisdictions_fl + jurisdictions_sd
all_data = pd.concat(jurisdictions)
all_data = all_data.loc[all_data['local_id'] > 0]

# combine all blocks
blocks_az = [az_apache_blocks, az_cochise_blocks, az_coconino_blocks, az_gila_blocks, az_gila_globe_blocks, az_navajo_blocks]
blocks_ca = [ca_hanford_blocks, ca_riverdale_blocks, ca_merced_blocks]
blocks_fl = [fl_collier_blocks, fl_hendry_blocks]
blocks_sd = [sd_charles_blocks, sd_shannon_blocks, sd_todd_blocks]

blocks = blocks_az + blocks_ca + blocks_fl + blocks_sd
all_blocks = pd.concat(blocks)

# checking length of all blocks
all_blocks['GEOID10'].nunique()
    
    
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
    maps = all_data.map.unique()
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 16})
    ax.yaxis.set_major_formatter(PercentFormatter(decimals = 1))
    plt.ylim([-5.25, 5.25])
    for i in maps:
        # subset the data by district only in the ith political level
        df = all_data[all_data["map"] == i]
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
    plt.legend(prop={'size': 9}, frameon = True, loc = 'upper right', bbox_to_anchor=(1.6,1.))
    plt.savefig("D:/Census/Localities/Figures/{} VAP Relative Distance.png".format(minority_title), bbox_inches='tight')
    plt.show()

#make figures
relative_distance_figure(all_data, "NHbla_alo_VAP", "NHBVAP_aloDP", "totVAP", "NH Black VAP", "Black")
relative_distance_figure(all_data, "NHnat_alo_VAP", "NHnatVAP_aloDP", "totVAP", "NH American Indian VAP", "American Indian")
relative_distance_figure(all_data, "NHasi_alo_VAP", "NHAVAP_aloDP", "totVAP", "NH Asian VAP", "Asian")
relative_distance_figure(all_data, "HVAP", "HVAPDP", "totVAP", "Hispanic VAP", "Hispanic")
relative_distance_figure(all_data, "tot", "totDP", "tot", "total population", "Total Population")

#make table
maps = all_data.map.unique()
total_df = pd.DataFrame(columns=['jurisdiction','district type', 'num of districts', 
                                 'num of blocks', 'mean blocks per dist', 'max blocks per dist',
                                 'num of pop blocks', 'pct blocks populated', 'mean pop blocks per dist', 'max pop blocks per dist',
                                 'max abs difference', 'mean abs difference', 'mean difference', 'abs standard deviation', 'standard deviation',
                                 'total map pop 2010', 'mean pop per dist 2010', 'max pop per dist 2010', 'stdev pop per dist 2010'])

for i in maps:
    print(i)
    
    # subset the district data only in the ith political level
    df = all_data[all_data["map"] == i]
    
    # subset the block data only in the ith political level
    blocks_df = all_blocks[all_blocks["map"] == i]
    blocks_df_grouped = blocks_df[['geoid', 'local_id']].groupby('local_id').count()
    
    # subset the populated block data only in the ith political level
    blocks_df_pop = blocks_df.loc[blocks_df['tot'] > 0]
    blocks_df_pop_grouped = blocks_df_pop[['geoid', 'local_id']].groupby('local_id').count()
    
    # Census Bureau Relative Distance Measure defined as the difference of the 
    # minority VAP in the 2010 Census data with and without differential privacy applied
    # as a fraction of the total VAP in the 2010 Census.
    df['relative_dist'] = ((df['totDP'] - df['tot']) / df['tot']) * 100
    
    # append entry for ith political level to table
    total_df = total_df.append({'jurisdiction':i, 
                                'district type':df['dist_type'].unique()[0],
                                'num of districts':len(df),
                                'num of blocks':len(blocks_df),
                                'mean blocks per dist':np.average(blocks_df_grouped['geoid']),
                                'max blocks per dist':max(blocks_df_grouped['geoid']),
                                'num of pop blocks':len(blocks_df_pop),
                                'pct blocks populated':(len(blocks_df_pop)/len(blocks_df))*100,
                                'mean pop blocks per dist':np.average(blocks_df_pop_grouped['geoid']),
                                'max pop blocks per dist':max(blocks_df_pop_grouped['geoid']),
                                'max abs difference':max(abs(df['relative_dist'])),
                                'mean abs difference':np.average(abs(df['relative_dist'])),
                                'mean difference':np.average((df['relative_dist'])),
                                'abs standard deviation':np.std(abs(df['relative_dist'])),
                                'standard deviation':np.std(df['relative_dist']),
                                'total map pop 2010':np.sum(df['tot']),
                                'mean pop per dist 2010':np.average(df['tot']),
                                'max pop per dist 2010':max(df['tot']),
                                'stdev pop per dist 2010':np.std(df['tot'])
                                }, ignore_index=True)

# save table
total_df.to_csv(r'D:/Github/EIL-DP_Analysis/DOJ Jurisdictions/Analysis/DOJ_jurisdictions_AZ_CA_FL_SD.csv')



### final stats about districts by type

# demographics by district type
all_data_sort = all_data.groupby('dist_type').mean()

# number of blocks and populated blocks by district type
all_blocks_sort = all_blocks[['geoid', 'dist_type']].groupby('dist_type').count()

all_blocks_pop = all_blocks.loc[all_blocks['tot']>0]
all_blocks_pop_sort = all_blocks_pop[['geoid', 'dist_type']].groupby('dist_type').count()

all_blocks_join = all_blocks_sort.merge(all_blocks_pop_sort, on='dist_type')
all_blocks_join['pct_populated'] = (all_blocks_join['geoid_y'] / all_blocks_join['geoid_x']) * 100


