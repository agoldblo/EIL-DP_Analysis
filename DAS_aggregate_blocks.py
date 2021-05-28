
"""

Census Data DAS Analysis: Part 2
5/21/21

- for all states, take DAS data for each ε level and join to 2010 block
  data with comparable variables
- export joined data for each state in csv and shp format

"""

import pandas as pd
import geopandas as gpd
import maup
import os

def checkDataFrame(df):
    ''' 
    
    take a data frame and find all columns with null values
    
    return all null columns

    '''

    df.isnull().values.any()
    null_columns=df.columns[df.isnull().any()]
    print("Null Columns: ", str(len(null_columns)))
    print(null_columns)
    return null_columns


def checkPopEquivalence(df, dist_col, pop_col):
    '''
    
    take a data frame for a state in any sub-district level
    group into specified district assingment and 
    compute population and deviation for each district
    
    '''

    
    if dist_col in df.columns:
        print("Grouping by {0}".format(dist_col))
        print("Using population from {0}".format(pop_col))
        grouped = df.groupby(dist_col, as_index=True).sum()
        max_pop = max(grouped[pop_col])
        min_pop = min(grouped[pop_col])
        print("Min pop: {0}".format(min_pop))
        print("Max pop: {0}".format(max_pop))
        ideal_pop = sum(grouped[pop_col])/len(grouped[pop_col])
        print("Ideal pop: {0}".format(ideal_pop))
        # positive and negative deviations
        dev_pos = round((((max_pop - ideal_pop)/ideal_pop) * 100), 4)
        dev_neg = round((((ideal_pop - min_pop)/ideal_pop) * 100), 4)
        print("Positive deviation: {0}%".format(str(dev_pos)))
        print("Negative deviation: {0}%".format(str(dev_neg)))
    else:
        print("Column not found - can't group by this assignment column")
    
def aggregateData(blocks_join, dp_type, st_name):
    
    '''
    take a joined dataframe of joined census 2010 blocks and DP data blocks
    calculate additional columns
    rename columns
    subset and write to file
    
    return the geodataframe of aggregated blocks written to file

    '''
    dp_name = dp_type.replace('_','.')
    print ('Beginning ε={0} for {1}'.format(dp_name, st_name))
    
    #### TESTING
    
    # check total populations at block level for DP and 2010 data
    print('total pop (2010): {0}'.format(blocks_join['tot'].sum()))        
    print('total pop (DP): {0}'.format(blocks_join['totDP'].sum()))       
    print('total BPOP (2010): {0}'.format(blocks_join['NHbla_alo'].sum())) 
    print('total BPOP (DP): {0}'.format(blocks_join['NHbla_aloDP'].sum()))
    print('total VAP (2010): {0}'.format(blocks_join['totVAP'].sum()))
    print('total VAP (DP): {0}'.format(blocks_join['totVAPDP'].sum()))        
    print('total BVAP (2010): {0}'.format(blocks_join['NHbla_alo_'].sum()))     
    print('total BVAP (DP): {0}'.format(blocks_join['NHBVAP_aloDP'].sum()))     
    
    # create columns for each race alone (hispanic and nonhispanic combined)
    blocks_join['whi_alo'] = blocks_join['NHwhi_alo'] + blocks_join['Hwhi_alo']
    blocks_join['bla_alo'] = blocks_join['NHbla_alo'] + blocks_join['Hbla_alo']
    blocks_join['nat_alo'] = blocks_join['NHnat_alo'] + blocks_join['Hnat_alo']
    blocks_join['asi_alo'] = blocks_join['NHasi_alo'] + blocks_join['Hasi_alo']
    blocks_join['pci_alo'] = blocks_join['NHpci_alo'] + blocks_join['Hpci_alo']
    blocks_join['sor_alo'] = blocks_join['NHsor_alo'] + blocks_join['Hsor_alo']
    blocks_join['2mo'] = blocks_join['NH2mo'] + blocks_join['H2mo']
    
    # rename columns
    blocks_join.rename(columns={'whi_alo_VA':'whi_alo_VAP',
                                'bla_alo_VA':'bla_alo_VAP',
                                'nat_alo_VA':'nat_alo_VAP',
                                'asi_alo_VA':'asi_alo_VAP',
                                'pci_alo_VA':'pci_alo_VAP',
                                'sor_alo_VA':'sor_alo_VAP',
                                'NHwhi_alo_':'NHwhi_alo_VAP',
                                'NHbla_alo_':'NHbla_alo_VAP',
                                'NHnat_alo_':'NHnat_alo_VAP',
                                'NHasi_alo_':'NHasi_alo_VAP',
                                'NHpci_alo_':'NHpci_alo_VAP',
                                'NHsor_alo_':'NHsor_alo_VAP',
                                'bla_com_VA':'bla_com_VAP',
                                'NHbla_com_':'NHbla_com_VAP'}, inplace=True)
    
    # subset of columns to save
    subsetcols = ['tot','totDP','totVAP', 'totVAPDP',  # totals
                  'Htot', 'HtotDP', 'NHtot', 'NHtotDP','HVAP', 'HVAPDP','NHVAP', 'NHVAPDP',  # hispanic/nonhispanic
                  'whi_alo','whi_aloDP','bla_alo','bla_aloDP', 'nat_alo','nat_aloDP', 
                  'asi_alo','asi_aloDP', 'pci_alo','pci_aloDP', 'sor_alo','sor_aloDP', '2mo','2moDP', #  each race alone
                  'NHwhi_alo','NHwhi_aloDP','NHbla_alo','NHbla_aloDP','NHnat_alo','NHnat_aloDP',
                  'NHasi_alo','NHasi_aloDP','NHpci_alo','NHpci_aloDP','NHsor_alo','NHsor_aloDP', 'NH2mo','NH2moDP',# NH each race alone
                  'whi_alo_VAP','WVAP_aloDP','bla_alo_VAP','BVAP_aloDP','nat_alo_VAP', 'natVAP_aloDP', 
                  'asi_alo_VAP','AVAP_aloDP','pci_alo_VAP','pciVAP_aloDP','sor_alo_VAP', 'sorVAP_aloDP','2mo_VAP', '2moVAPDP',# each race alone VAP
                  'NHwhi_alo_VAP', 'NHWVAP_aloDP', 'NHbla_alo_VAP', 'NHBVAP_aloDP', 'NHnat_alo_VAP', 'NHnatVAP_aloDP',
                  'NHasi_alo_VAP','NHAVAP_aloDP','NHpci_alo_VAP','NHpciVAP_aloDP','NHsor_alo_VAP', 'NHsorVAP_aloDP','NH2mo_VAP', 'NH2moVAPDP'] # NHeach race alone VAP
    
    
    blocks_join[subsetcols] = blocks_join[subsetcols].fillna(0)
    
    # save subset and shapefile subset
    blocks_subset = blocks_join[['GEOID10', 'STATEFP10', 'COUNTYFP10', 'TRACTCE10', 'BLOCKCE10'] + subsetcols]
    blocks_subset_geo = blocks_join[['GEOID10', 'STATEFP10', 'COUNTYFP10', 'TRACTCE10', 'BLOCKCE10', 'geometry'] + subsetcols]
    
    
    blocks_subset.to_csv('D:/Census/Joined States/CSV/{0}/{1}_blocks_join_DP{2}.csv'.format(dp_name, st_name, dp_type))
    print('D:/Census/Joined States/CSV/{0}/{1}_blocks_join_DP{2}.csv'.format(dp_name, st_name, dp_type))
    
    blocks_subset_geo.to_file('D:/Census/Joined States/SHP/{0}/{1}_blocks_join_DP{2}.shp'.format(dp_name, st_name, dp_type))
    print('D:/Census/Joined States/SHP/{0}/{1}_blocks_join_DP{2}.shp'.format(dp_name, st_name, dp_type))
    
    print('done with ε={0} for {1}'.format(dp_name, state_name))
    
    return blocks_subset_geo
    
    
    
#######################################################################
#### AGGREGATE DATA FOR SPECIFIED STATES
#######################################################################

# list state to aggregate
st_list = ['AK', 'AL', 'AZ', 'FL', 'GA', 'MA', 'MI', 'MT', 'NC', 'NE', 'NJ', 'OH', 'OK', 'PA', 'TX', 'UT', 'VA', 'WI']

for state_name in st_list:

    print('beginning {0}'.format(state_name))
        
    #### IMPORTS
    
    # DP data at block level
    block_DP_4_5 = pd.read_csv('D:/Census/CensusDP_{0}_4_5.csv'.format(state_name))
    block_DP_12_2 = pd.read_csv('D:/Census/CensusDP_{0}_12_2.csv'.format(state_name))
    
    # blocks
    blocks = gpd.read_file('D:/GIS data/{0}/Shapefiles/{0}_blocks_dec10.shp'.format(state_name))

    # fix geoid columns
    block_DP_4_5.dtypes
    
    block_DP_4_5['GEOID'].head()
    block_DP_12_2['GEOID'].head()
    
    block_DP_4_5['GEOID'] = block_DP_4_5['GEOID'].map(lambda x:(str(x).zfill(15)))
    block_DP_12_2['GEOID'] = block_DP_12_2['GEOID'].map(lambda x:(str(x).zfill(15)))
    
    blocks['GEOID10'].head()
        
    # Join populated blocks (DP) to blocks shapefile (2010)
    
    # 4.5
    blocks_join4_5 = blocks.merge(block_DP_4_5, left_on='GEOID10', right_on='GEOID', how='left')
    # 12.2
    blocks_join12_2 = blocks.merge(block_DP_12_2, left_on='GEOID10', right_on='GEOID', how='left')
    

    ##### ε = 4.5
    agg_blocks4_5 = aggregateData(blocks_join4_5, '4_5', state_name)
    
    ##### ε = 12.2
    agg_blocks12_2 = aggregateData(blocks_join12_2, '12_2', state_name)
    

    
    
    
    
    
    