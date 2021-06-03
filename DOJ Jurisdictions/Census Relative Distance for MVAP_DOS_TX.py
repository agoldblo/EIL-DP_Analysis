import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import os

# change path to local path to dataset
base_path = 'D:/Census/Localities/TX'

#specify details about each jurisdiction
tx_corp= pd.read_csv(base_path + '/TX_Ark_Kle_Nue_SanPat_Corpus_Christi.csv')
tx_corp['map'] = 'Corpus Christi'
tx_corp['state'] = 'TX'
tx_corp['dist_type'] = 'City'
tx_corp_blocks = pd.read_csv(base_path + '/TX_Ark_Kle_Nue_SanPat_Corpus_Christi_blocks.csv')
tx_corp_blocks['map'] = 'Corpus Christi'
tx_corp_blocks['state'] = 'TX'
tx_corp_blocks['dist_type'] = 'City'

tx_lytle= pd.read_csv(base_path + '/TX_Atascosa_Bexar_Medina_Lytle.csv')
tx_lytle['map'] = 'Lytle'
tx_lytle['state'] = 'TX'
tx_lytle['dist_type'] = 'City'
tx_lytle_blocks = pd.read_csv(base_path + '/TX_Atascosa_Bexar_Medina_Lytle_blocks.csv')
tx_lytle_blocks['map'] = 'Lytle'
tx_lytle_blocks['state'] = 'TX'
tx_lytle_blocks['dist_type'] = 'City'

tx_karne_city= pd.read_csv(base_path + '/TX_Atascosa_Karnes_City_ISD.csv')
tx_karne_city['map'] = 'Karnes City ISD'
tx_karne_city['state'] = 'TX'
tx_karne_city['dist_type'] = 'School District'
tx_karne_city_blocks = pd.read_csv(base_path + '/TX_Atascosa_Karnes_City_ISD_blocks.csv')
tx_karne_city_blocks['map'] = 'Karnes City ISD'
tx_karne_city_blocks['state'] = 'TX'
tx_karne_city_blocks['dist_type'] = 'School District'

tx_bexar= pd.read_csv(base_path + '/TX_Bexar_Comm_CT.csv')
tx_bexar['map'] = 'Bexar Comm Ct'
tx_bexar['state'] = 'TX'
tx_bexar['dist_type'] = 'Commissioners Court'
tx_bexar_blocks = pd.read_csv(base_path + '/TX_Bexar_Comm_CT_blocks.csv')
tx_bexar_blocks['map'] = 'Bexar Comm Ct'
tx_bexar_blocks['state'] = 'TX'
tx_bexar_blocks['dist_type'] = 'Commissioners Court'

tx_judson= pd.read_csv(base_path + '/TX_Bexar_Judson_ISD.csv')
tx_judson['map'] = 'Judson ISD'
tx_judson['state'] = 'TX'
tx_judson['dist_type'] = 'School District'
tx_judson_blocks = pd.read_csv(base_path + '/TX_Bexar_Judson_ISD_blocks.csv')
tx_judson_blocks['map'] = 'Judson ISD'
tx_judson_blocks['state'] = 'TX'
tx_judson_blocks['dist_type'] = 'School District'

tx_san_antonio= pd.read_csv(base_path + '/TX_Bexar_San_Antonio_ISD.csv')
tx_san_antonio['map'] = 'San Antonio ISD'
tx_san_antonio['state'] = 'TX'
tx_san_antonio['dist_type'] = 'School District'
tx_san_antonio_blocks = pd.read_csv(base_path + '/TX_Bexar_San_Antonio_ISD_blocks.csv')
tx_san_antonio_blocks['map'] = 'San Antonio ISD'
tx_san_antonio_blocks['state'] = 'TX'
tx_san_antonio_blocks['dist_type'] = 'School District'

tx_san_antonio_2= pd.read_csv(base_path + '/TX_Bexar_San_Antonio.csv')
tx_san_antonio_2['map'] = 'San Antonio City'
tx_san_antonio_2['state'] = 'TX'
tx_san_antonio_2['dist_type'] = 'City'
tx_san_antonio_2_blocks = pd.read_csv(base_path + '/TX_Bexar_San_Antonio_blocks.csv')
tx_san_antonio_2_blocks['map'] = 'San Antonio City'
tx_san_antonio_2_blocks['state'] = 'TX'
tx_san_antonio_2_blocks['dist_type'] = 'City'

tx_floresville= pd.read_csv(base_path + '/TX_Bexar_Wilson_Floresville_ISD.csv')
tx_floresville['map'] = 'Floresville ISD'
tx_floresville['state'] = 'TX'
tx_floresville['dist_type'] = 'School District'
tx_floresville_blocks = pd.read_csv(base_path + '/TX_Bexar_Wilson_Floresville_ISD_blocks.csv')
tx_floresville_blocks['map'] = 'Floresville ISD'
tx_floresville_blocks['state'] = 'TX'
tx_floresville_blocks['dist_type'] = 'School District'

tx_alvin= pd.read_csv(base_path + '/TX_Brazoria_Alvin.csv')
tx_alvin['map'] = 'Alvin City'
tx_alvin['state'] = 'TX'
tx_alvin['dist_type'] = 'City'
tx_alvin_blocks = pd.read_csv(base_path + '/TX_Brazoria_Alvin_blocks.csv')
tx_alvin_blocks['map'] = 'Alvin City'
tx_alvin_blocks['state'] = 'TX'
tx_alvin_blocks['dist_type'] = 'City'

tx_brewster= pd.read_csv(base_path + '/TX_Brewster_Comm_CT_CONS_JP.csv')
tx_brewster['map'] = 'Brewster Comm Ct/Con/JP'
tx_brewster['state'] = 'TX'
tx_brewster['dist_type'] = 'Comm Ct/Con/JP'
tx_brewster_blocks = pd.read_csv(base_path + '/TX_Brewster_Comm_CT_CONS_JP_blocks.csv')
tx_brewster_blocks['map'] = 'Brewster Comm Ct/Con/JP'
tx_brewster_blocks['state'] = 'TX'
tx_brewster_blocks['dist_type'] = 'Comm Ct/Con/JP'

tx_caldwell= pd.read_csv(base_path + '/TX_Caldwell_Comm_CT_JP.csv')
tx_caldwell['map'] = 'Caldwell Comm Ct/JP'
tx_caldwell['state'] = 'TX'
tx_caldwell['dist_type'] = 'Comm Ct/JP'
tx_caldwell_blocks = pd.read_csv(base_path + '/TX_Caldwell_Comm_CT_JP_blocks.csv')
tx_caldwell_blocks['map'] = 'Caldwell Comm Ct/JP'
tx_caldwell_blocks['state'] = 'TX'
tx_caldwell_blocks['dist_type'] = 'Comm Ct/JP'

tx_hayes= pd.read_csv(base_path + '/TX_Caldwell_Hayes_Travis_Hays_ISD.csv')
tx_hayes['map'] = 'Hayes ISD'
tx_hayes['state'] = 'TX'
tx_hayes['dist_type'] = 'School District'
tx_hayes_blocks = pd.read_csv(base_path + '/TX_Caldwell_Hayes_Travis_Hays_ISD_blocks.csv')
tx_hayes_blocks['map'] = 'Hayes ISD'
tx_hayes_blocks['state'] = 'TX'
tx_hayes_blocks['dist_type'] = 'School District'

tx_lockhart= pd.read_csv(base_path + '/TX_Caldwell_Lockhart_ISD.csv')
tx_lockhart['map'] = 'Lockhart ISD'
tx_lockhart['state'] = 'TX'
tx_lockhart['dist_type'] = 'School Districts'
tx_lockhart_blocks = pd.read_csv(base_path + '/TX_Caldwell_Lockhart_ISD_blocks.csv')
tx_lockhart_blocks['map'] = 'Lockhart ISD'
tx_lockhart_blocks['state'] = 'TX'
tx_lockhart_blocks['dist_type'] = 'School District'

tx_luling= pd.read_csv(base_path + '/TX_Caldwell_Luling.csv')
tx_luling['map'] = 'Luling'
tx_luling['state'] = 'TX'
tx_luling['dist_type'] = 'City'
tx_luling_blocks = pd.read_csv(base_path + '/TX_Caldwell_Luling_blocks.csv')
tx_luling_blocks['map'] = 'Luling'
tx_luling_blocks['state'] = 'TX'
tx_luling_blocks['dist_type'] = 'City'

tx_dimmitt= pd.read_csv(base_path + '/TX_Castro_Dimmitt.csv')
tx_dimmitt['map'] = 'Dimmit City'
tx_dimmitt['state'] = 'TX'
tx_dimmitt['dist_type'] = 'City'
tx_dimmitt_blocks = pd.read_csv(base_path + '/TX_Castro_Dimmitt_blocks.csv')
tx_dimmitt_blocks['map'] = 'Dimmit City'
tx_dimmitt_blocks['state'] = 'TX'
tx_dimmitt_blocks['dist_type'] = 'City'

tx_mckinney= pd.read_csv(base_path + '/TX_Collin_McKinney_ISD.csv')
tx_mckinney['map'] = 'McKinney ISD'
tx_mckinney['state'] = 'TX'
tx_mckinney['dist_type'] = 'School District'
tx_mckinney_blocks = pd.read_csv(base_path + '/TX_Collin_McKinney_ISD_blocks.csv')
tx_mckinney_blocks['map'] = 'McKinney ISD'
tx_mckinney_blocks['state'] = 'TX'
tx_mckinney_blocks['dist_type'] = 'School District'

tx_concho= pd.read_csv(base_path + '/TX_Concho_Comm_CT_CONS_JP.csv')
tx_concho['map'] = 'Concho Comm Ct/Cons/JP'
tx_concho['state'] = 'TX'
tx_concho['dist_type'] = 'Comm Ct/Cons/JP'
tx_concho_blocks = pd.read_csv(base_path + '/TX_Concho_Comm_CT_CONS_JP_blocks.csv')
tx_concho_blocks['map'] = 'Concho Comm Ct/Cons/JP'
tx_concho_blocks['state'] = 'TX'
tx_concho_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_ralls= pd.read_csv(base_path + '/TX_Crosby_Ralls_ISD.csv')
tx_ralls['map'] = 'Ralls ISD'
tx_ralls['state'] = 'TX'
tx_ralls['dist_type'] = 'School District'
tx_ralls_blocks = pd.read_csv(base_path + '/TX_Crosby_Ralls_ISD_blocks.csv')
tx_ralls_blocks['map'] = 'Ralls ISD'
tx_ralls_blocks['state'] = 'TX'
tx_ralls_blocks['dist_type'] = 'School District'

tx_dawson= pd.read_csv(base_path + '/TX_Dawson_Comm_CT_CONS_JP.csv')
tx_dawson['map'] = 'Dawson Comm Ct/Cons/JP'
tx_dawson['state'] = 'TX'
tx_dawson['dist_type'] = 'Comm Ct/Cons/JP'
tx_dawson_blocks = pd.read_csv(base_path + '/TX_Dawson_Comm_CT_CONS_JP_blocks.csv')
tx_dawson_blocks['map'] = 'Dawson Comm Ct/Cons/JP'
tx_dawson_blocks['state'] = 'TX'
tx_dawson_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_spur= pd.read_csv(base_path + '/TX_Dickens_Spur.csv')
tx_spur['map'] = 'Spur'
tx_spur['state'] = 'TX'
tx_spur['dist_type'] = 'City'
tx_spur_blocks = pd.read_csv(base_path + '/TX_Dickens_Spur_blocks.csv')
tx_spur_blocks['map'] = 'Spur'
tx_spur_blocks['state'] = 'TX'
tx_spur_blocks['dist_type'] = 'City'

tx_ector= pd.read_csv(base_path + '/TX_Ector_Comm_CT_CONS_JP.csv')
tx_ector['map'] = 'Ector Comm Ct/Cons/JP'
tx_ector['state'] = 'TX'
tx_ector['dist_type'] = 'Comm Ct/Cons/JP'
tx_ector_blocks = pd.read_csv(base_path + '/TX_Ector_Comm_CT_CONS_JP_blocks.csv')
tx_ector_blocks['map'] = 'Ector Comm Ct/Cons/JP'
tx_ector_blocks['state'] = 'TX'
tx_ector_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_houston= pd.read_csv(base_path + '/TX_FtBend_Harris_Houston_Comm_Coll_Dist.csv')
tx_houston['map'] = 'Houston Comm Coll Dist'
tx_houston['state'] = 'TX'
tx_houston['dist_type'] = 'Community College'
tx_houston_blocks = pd.read_csv(base_path + '/TX_FtBend_Harris_Houston_Comm_Coll_Dist_blocks.csv')
tx_houston_blocks['map'] = 'Houston Comm Coll Dist'
tx_houston_blocks['state'] = 'TX'
tx_houston_blocks['dist_type'] = 'Community College'

tx_gaines= pd.read_csv(base_path + '/TX_Gaines_Comm_CT_CONS_JP.csv')
tx_gaines['map'] = 'Gaines Comm Ct/Cons/JP'
tx_gaines['state'] = 'TX'
tx_gaines['dist_type'] = 'Comm Ct/Cons/JP'
tx_gaines_blocks = pd.read_csv(base_path + '/TX_Gaines_Comm_CT_CONS_JP_blocks.csv')
tx_gaines_blocks['map'] = 'Gaines Comm Ct/Cons/JP'
tx_gaines_blocks['state'] = 'TX'
tx_gaines_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_galviston= pd.read_csv(base_path + '/TX_Galveston_CONS_JP.csv')
tx_galviston['map'] = 'Galviston Cons/JP'
tx_galviston['state'] = 'TX'
tx_galviston['dist_type'] = 'Cons/JP'
tx_galviston_blocks = pd.read_csv(base_path + '/TX_Galveston_CONS_JP_blocks.csv')
tx_galviston_blocks['map'] = 'Galviston Cons/JP'
tx_galviston_blocks['state'] = 'TX'
tx_galviston_blocks['dist_type'] = 'Cons/JP'

tx_galviston_2= pd.read_csv(base_path + '/TX_Galveston_Comm_CT.csv')
tx_galviston_2['map'] = 'Galviston Comm Ct'
tx_galviston_2['state'] = 'TX'
tx_galviston_2['dist_type'] = 'Commissioners Court'
tx_galviston_2_blocks = pd.read_csv(base_path + '/TX_Galveston_Comm_CT_blocks.csv')
tx_galviston_2_blocks['map'] = 'Galviston Comm Ct'
tx_galviston_2_blocks['state'] = 'TX'
tx_galviston_2_blocks['dist_type'] = 'Commissioners Court'

tx_guadalupe= pd.read_csv(base_path + '/TX_Guadalupe_Groundwater_Dist.csv')
tx_guadalupe['map'] = 'Guadalupe Groundwater Dists'
tx_guadalupe['state'] = 'TX'
tx_guadalupe['dist_type'] = 'Groundwater'
tx_guadalupe_blocks = pd.read_csv(base_path + '/TX_Guadalupe_Groundwater_Dist_blocks.csv')
tx_guadalupe_blocks['map'] = 'Guadalupe Groundwater Dists'
tx_guadalupe_blocks['state'] = 'TX'
tx_guadalupe_blocks['dist_type'] = 'Groundwater'

tx_hale= pd.read_csv(base_path + '/TX_Hale_Comm_CT_CON_JP.csv')
tx_hale['map'] = 'Hale Comm Ct/Con/JP'
tx_hale['state'] = 'TX'
tx_hale['dist_type'] = 'Comm Ct/Con/JP'
tx_hale_blocks = pd.read_csv(base_path + '/TX_Hale_Comm_CT_CON_JP_blocks.csv')
tx_hale_blocks['map'] = 'Hale Comm Ct/Con/JP'
tx_hale_blocks['state'] = 'TX'
tx_hale_blocks['dist_type'] = 'Comm Ct/Con/JP'

tx_plainview= pd.read_csv(base_path + '/TX_Hale_Plainview_ISD.csv')
tx_plainview['map'] = 'Plainview ISD'
tx_plainview['state'] = 'TX'
tx_plainview['dist_type'] = 'School District'
tx_plainview_blocks = pd.read_csv(base_path + '/TX_Hale_Plainview_ISD_blocks.csv')
tx_plainview_blocks['map'] = 'Plainview ISD'
tx_plainview_blocks['state'] = 'TX'
tx_plainview_blocks['dist_type'] = 'School District'

tx_harris= pd.read_csv(base_path + '/TX_Harris_Comm_Court.csv')
tx_harris['map'] = 'Harris Comm Ct'
tx_harris['state'] = 'TX'
tx_harris['dist_type'] = 'Commissioners Court'
tx_harris_blocks = pd.read_csv(base_path + '/TX_Harris_Comm_Court_blocks.csv')
tx_harris_blocks['map'] = 'Harris Comm Ct'
tx_harris_blocks['state'] = 'TX'
tx_harris_blocks['dist_type'] = 'Commissioners Court'

tx_kyle= pd.read_csv(base_path + '/TX_Hays_Kyle.csv')
tx_kyle['map'] = 'Kyle City'
tx_kyle['state'] = 'TX'
tx_kyle['dist_type'] = 'City'
tx_kyle_blocks = pd.read_csv(base_path + '/TX_Hays_Kyle_blocks.csv')
tx_kyle_blocks['map'] = 'Kyle City'
tx_kyle_blocks['state'] = 'TX'
tx_kyle_blocks['dist_type'] = 'City'

tx_hockley= pd.read_csv(base_path + '/TX_Hockley_Comm_CT_CONS_JP.csv')
tx_hockley['map'] = 'Hockley Comm Ct/Cons/JP'
tx_hockley['state'] = 'TX'
tx_hockley['dist_type'] = 'Comm Ct/Cons/JP'
tx_hockley_blocks = pd.read_csv(base_path + '/TX_Hockley_Comm_CT_CONS_JP_blocks.csv')
tx_hockley_blocks['map'] = 'Hockley Comm Ct/Cons/JP'
tx_hockley_blocks['state'] = 'TX'
tx_hockley_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_howard= pd.read_csv(base_path + '/TX_Howard_Comm_CT_CONS_JP.csv')
tx_howard['map'] = 'Howard Comm Ct/Cons/JP'
tx_howard['state'] = 'TX'
tx_howard['dist_type'] = 'Comm Ct/Cons/JP'
tx_howard_blocks = pd.read_csv(base_path + '/TX_Howard_Comm_CT_CONS_JP_blocks.csv')
tx_howard_blocks['map'] = 'Howard Comm Ct/Cons/JP'
tx_howard_blocks['state'] = 'TX'
tx_howard_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_karnes= pd.read_csv(base_path + '/TX_Karnes_Comm_Court.csv')
tx_karnes['map'] = 'Karnes Comm Ct'
tx_karnes['state'] = 'TX'
tx_karnes['dist_type'] = 'Commissioners Court'
tx_karnes_blocks = pd.read_csv(base_path + '/TX_Karnes_Comm_Court_blocks.csv')
tx_karnes_blocks['map'] = 'Karnes Comm Ct'
tx_karnes_blocks['state'] = 'TX'
tx_karnes_blocks['dist_type'] = 'Commissioners Court'

tx_kleberg= pd.read_csv(base_path + '/TX_Karnes_Comm_Court.csv')
tx_kleberg['map'] = 'Kleberg Comm Ct'
tx_kleberg['state'] = 'TX'
tx_kleberg['dist_type'] = 'Commissioners Court'
tx_kleberg_blocks = pd.read_csv(base_path + '/TX_Karnes_Comm_Court_blocks.csv')
tx_kleberg_blocks['map'] = 'Kleberg Comm Ct'
tx_kleberg_blocks['state'] = 'TX'
tx_kleberg_blocks['dist_type'] = 'Commissioners Court'

tx_waco= pd.read_csv(base_path + '/TX_McClennan_Waco_ISD.csv')
tx_waco['map'] = 'Waco ISD'
tx_waco['state'] = 'TX'
tx_waco['dist_type'] = 'School District'
tx_waco_blocks = pd.read_csv(base_path + '/TX_McClennan_Waco_ISD_blocks.csv')
tx_waco_blocks['map'] = 'Waco ISD'
tx_waco_blocks['state'] = 'TX'
tx_waco_blocks['dist_type'] = 'School District'

tx_moore= pd.read_csv(base_path + '/TX_Moore_Comm_CT_CONS_JP.csv')
tx_moore['map'] = 'Moore Comm Ct/Cons/JP'
tx_moore['state'] = 'TX'
tx_moore['dist_type'] = 'Comm Ct/Cons/JP'
tx_moore_blocks = pd.read_csv(base_path + '/TX_Moore_Comm_CT_CONS_JP_blocks.csv')
tx_moore_blocks['map'] = 'Moore Comm Ct/Cons/JP'
tx_moore_blocks['state'] = 'TX'
tx_moore_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_lone_star= pd.read_csv(base_path + '/TX_Morris_Titus_Lone_Star_ISD.csv')
tx_lone_star['map'] = 'Daingerfield-Lone Star ISD'
tx_lone_star['state'] = 'TX'
tx_lone_star['dist_type'] = 'School District'
tx_lone_star_blocks = pd.read_csv(base_path + '/TX_Morris_Titus_Lone_Star_ISD_blocks.csv')
tx_lone_star_blocks['map'] = 'Daingerfield-Lone Star ISD'
tx_lone_star_blocks['state'] = 'TX'
tx_lone_star_blocks['dist_type'] = 'School District'

tx_sweetwater= pd.read_csv(base_path + '/TX_Nolan_Sweetwater.csv')
tx_sweetwater['map'] = 'Sweetwater'
tx_sweetwater['state'] = 'TX'
tx_sweetwater['dist_type'] = 'City'
tx_sweetwater_blocks = pd.read_csv(base_path + '/TX_Nolan_Sweetwater_blocks.csv')
tx_sweetwater_blocks['map'] = 'Sweetwater'
tx_sweetwater_blocks['state'] = 'TX'
tx_sweetwater_blocks['dist_type'] = 'City'

tx_ochiltree= pd.read_csv(base_path + '/TX_Ochiltree_Comm_Court.csv')
tx_ochiltree['map'] = 'Ochiltree Comm Ct'
tx_ochiltree['state'] = 'TX'
tx_ochiltree['dist_type'] = 'Commissioners Court'
tx_ochiltree_blocks = pd.read_csv(base_path + '/TX_Ochiltree_Comm_Court_blocks.csv')
tx_ochiltree_blocks['map'] = 'Ochiltree Comm Ct'
tx_ochiltree_blocks['state'] = 'TX'
tx_ochiltree_blocks['dist_type'] = 'Commissioners Court'

tx_reagan= pd.read_csv(base_path + '/TX_Reagan_Hospital_Dist.csv')
tx_reagan['map'] = 'Reagan Hospital Dist'
tx_reagan['state'] = 'TX'
tx_reagan['dist_type'] = 'Hospital'
tx_reagan_blocks = pd.read_csv(base_path + '/TX_Reagan_Hospital_Dist_blocks.csv')
tx_reagan_blocks['map'] = 'Reagan Hospital Dist'
tx_reagan_blocks['state'] = 'TX'
tx_reagan_blocks['dist_type'] = 'Hospital'

tx_sterling= pd.read_csv(base_path + '/TX_Sterling_Sterling_ISD.csv')
tx_sterling['map'] = 'Sterling ISD'
tx_sterling['state'] = 'TX'
tx_sterling['dist_type'] = 'School Districts'
tx_sterling_blocks = pd.read_csv(base_path + '/TX_Sterling_Sterling_ISD_blocks.csv')
tx_sterling_blocks['map'] = 'Sterling ISD'
tx_sterling_blocks['state'] = 'TX'
tx_sterling_blocks['dist_type'] = 'School District'

tx_sonora= pd.read_csv(base_path + '/TX_Sutton_Sonora_ISD.csv')
tx_sonora['map'] = 'Sonora IDS'
tx_sonora['state'] = 'TX'
tx_sonora['dist_type'] = 'School Districts'
tx_sonora_blocks = pd.read_csv(base_path + '/TX_Sutton_Sonora_ISD_blocks.csv')
tx_sonora_blocks['map'] = 'Sonora IDS'
tx_sonora_blocks['state'] = 'TX'
tx_sonora_blocks['dist_type'] = 'School Districts'

tx_tilia= pd.read_csv(base_path + '/TX_Swisher_Tulia.csv')
tx_tilia['map'] = 'Tulia City'
tx_tilia['state'] = 'TX'
tx_tilia['dist_type'] = 'City'
tx_tilia_blocks = pd.read_csv(base_path + '/TX_Swisher_Tulia_blocks.csv')
tx_tilia_blocks['map'] = 'Tulia City'
tx_tilia_blocks['state'] = 'TX'
tx_tilia_blocks['dist_type'] = 'City'

tx_terry= pd.read_csv(base_path + '/TX_Terry_Comm_CT_CONS_JP.csv')
tx_terry['map'] = 'Terry Comm Ct/Cons/JP'
tx_terry['state'] = 'TX'
tx_terry['dist_type'] = 'Comm Ct/Cons/JP'
tx_terry_blocks = pd.read_csv(base_path + '/TX_Terry_Comm_CT_CONS_JP_blocks.csv')
tx_terry_blocks['map'] = 'Terry Comm Ct/Cons/JP'
tx_terry_blocks['state'] = 'TX'
tx_terry_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_titus= pd.read_csv(base_path + '/TX_Titus_Comm_CT_CONS_JP.csv')
tx_titus['map'] = 'Titus Comm Ct/Cons/JP'
tx_titus['state'] = 'TX'
tx_titus['dist_type'] = 'Comm Ct/Cons/JP'
tx_titus_blocks = pd.read_csv(base_path + '/TX_Titus_Comm_CT_CONS_JP_blocks.csv')
tx_titus_blocks['map'] = 'Titus Comm Ct/Cons/JP'
tx_titus_blocks['state'] = 'TX'
tx_titus_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_austen= pd.read_csv(base_path + '/TX_Travis_Austin_ISD.csv')
tx_austen['map'] = 'Austen ISD'
tx_austen['state'] = 'TX'
tx_austen['dist_type'] = 'School Districts'
tx_austen_blocks = pd.read_csv(base_path + '/TX_Travis_Austin_ISD_blocks.csv')
tx_austen_blocks['map'] = 'Austen ISD'
tx_austen_blocks['state'] = 'TX'
tx_austen_blocks['dist_type'] = 'School District'

tx_upton= pd.read_csv(base_path + '/TX_Upton_Comm_CT_CONS_JP.csv')
tx_upton['map'] = 'Upton Comm Ct/Cons/JP'
tx_upton['state'] = 'TX'
tx_upton['dist_type'] = 'Comm Ct/Cons/JP'
tx_upton_blocks = pd.read_csv(base_path + '/TX_Upton_Comm_CT_CONS_JP_blocks.csv')
tx_upton_blocks['map'] = 'Upton Comm Ct/Cons/JP'
tx_upton_blocks['state'] = 'TX'
tx_upton_blocks['dist_type'] = 'Comm Ct/Cons/JP'

tx_victoria= pd.read_csv(base_path + '/TX_Victoria_Groundwater_Dist.csv')
tx_victoria['map'] = 'Victoria Groundwater Dist'
tx_victoria['state'] = 'TX'
tx_victoria['dist_type'] = 'Groundwater'
tx_victoria_blocks = pd.read_csv(base_path + '/TX_Victoria_Groundwater_Dist_blocks.csv')
tx_victoria_blocks['map'] = 'Victoria Groundwater Dist'
tx_victoria_blocks['state'] = 'TX'
tx_victoria_blocks['dist_type'] = 'Groundwater'

tx_wharton= pd.read_csv(base_path + '/TX_Wharton_Wharton.csv')
tx_wharton['map'] = 'Wharton City'
tx_wharton['state'] = 'TX'
tx_wharton['dist_type'] = 'City'
tx_wharton_blocks = pd.read_csv(base_path + '/TX_Wharton_Wharton_blocks.csv')
tx_wharton_blocks['map'] = 'Wharton City'
tx_wharton_blocks['state'] = 'TX'
tx_wharton_blocks['dist_type'] = 'City'




#combine jurisdictions into one big dataframe
jurisdictions = [tx_corp, tx_lytle, tx_karne_city, tx_bexar, tx_judson, tx_san_antonio, tx_san_antonio_2, tx_floresville, tx_alvin, 
                 tx_brewster, tx_caldwell, tx_hayes, tx_lockhart, tx_luling, tx_dimmitt, tx_mckinney, tx_concho, tx_ralls, tx_dawson, 
                 tx_spur, tx_ector, tx_houston, tx_gaines, tx_galviston, tx_galviston_2, tx_guadalupe, tx_hale, tx_plainview, tx_harris, 
                 tx_kyle, tx_hockley, tx_howard, tx_karnes, tx_kleberg, tx_waco, tx_moore, tx_lone_star, tx_sweetwater, tx_ochiltree, 
                 tx_reagan, tx_sterling, tx_sonora, tx_tilia, tx_terry, tx_titus, tx_austen, tx_upton, tx_victoria, tx_wharton]



all_data = pd.concat(jurisdictions)
all_data = all_data.loc[all_data['local_id'] > 0]

#combine blocks, too
blocks = [tx_corp_blocks, tx_lytle_blocks, tx_karne_city_blocks, tx_bexar_blocks, tx_judson_blocks, tx_san_antonio_blocks, 
          tx_san_antonio_2_blocks, tx_floresville_blocks, tx_alvin_blocks, tx_brewster_blocks, tx_caldwell_blocks, tx_hayes_blocks, 
          tx_lockhart_blocks, tx_luling_blocks, tx_dimmitt_blocks, tx_mckinney_blocks, tx_concho_blocks, tx_ralls_blocks, 
          tx_dawson_blocks, tx_spur_blocks, tx_ector_blocks, tx_houston_blocks, tx_gaines_blocks, tx_galviston_blocks, 
          tx_galviston_2_blocks, tx_guadalupe_blocks, tx_hale_blocks, tx_plainview_blocks, tx_harris_blocks, tx_kyle_blocks, 
          tx_hockley_blocks, tx_howard_blocks, tx_karnes_blocks, tx_kleberg_blocks, tx_waco_blocks, tx_moore_blocks, 
          tx_lone_star_blocks, tx_sweetwater_blocks, tx_ochiltree_blocks, tx_reagan_blocks, tx_sterling_blocks, 
          tx_sonora_blocks, tx_tilia_blocks, tx_terry_blocks, tx_titus_blocks, tx_austen_blocks, tx_upton_blocks, 
          tx_victoria_blocks, tx_wharton_blocks]


all_blocks = pd.concat(blocks)
all_blocks = all_blocks.loc[all_blocks['local_id'] > 0]

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
    types = all_data.dist_type.unique()
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 16})
    ax.yaxis.set_major_formatter(PercentFormatter(decimals = 1))
    plt.ylim([-5.25, 5.25])
    for i in types:
        # subset the data by district only in the ith political level
        df = all_data[all_data["dist_type"] == i]
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
total_df.to_csv(r'D:/Github/EIL-DP_Analysis/DOJ Jurisdictions/Analysis/DOJ_jurisdictions_TX.csv')


### final stats about districts by type

# demographics by district type
all_data_sort = all_data.groupby('dist_type').mean()

# number of blocks and populated blocks by district type
all_blocks_sort = all_blocks[['geoid', 'dist_type']].groupby('dist_type').count()

all_blocks_pop = all_blocks.loc[all_blocks['tot']>0]
all_blocks_pop_sort = all_blocks_pop[['geoid', 'dist_type']].groupby('dist_type').count()

all_blocks_join = all_blocks_sort.merge(all_blocks_pop_sort, on='dist_type')
all_blocks_join['pct_populated'] = (all_blocks_join['geoid_y'] / all_blocks_join['geoid_x']) * 100
