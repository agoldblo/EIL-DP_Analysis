# EIL DAS Demonstration Product Analysis
***
The Electoral Innovation Lab at Princeton analyzed the epsilon = 12.2 Census DAS demonstration dataset to look at how these changes might effect redistricting.
***
## Files
DAS_get_data.py: Python script that ingests the raw Census DP demonstration data, parses it into separate data frames for each state, groups by populated Census block, and writes those dataframes to file in csv format.
DAS_aggregate_blocks.py: Python script that ingests the each state's dataframe of block level DP demonstration data, merges it with a 2010 block level shapefile with demographic data, and outputs the data as a csv and shapefile.

### Data
AL_blocks_join_DP12_2.csv: Table of block level census data with both the DP and 2010 versions of each variable. Result of DAS_aggregate_blocks.py.

### Analysis:
#### Code
Census Relative Distance for MVAP.py: Python script that consumes the input data, calculates the Census Bureau's Relative Distance measure for each district and for each demographic group of interest, and plots them. The Census Bureau's Relative Distance measure is defined as the difference of the minority voting age population in the 2010 Census data with and without differential privacy applied as a fraction of the total VAP in the 2010 Census.
#### Figures
American Indian VAP Relative Distance.png: Plots the Census Bureau's Relative Distance measure for American Indian voting age populations over a variety of district sizes.

Asian VAP Relative Distance.png: Plots the Census Bureau's Relative Distance measure for Asian voting age populations over a variety of district sizes.

Black VAP Relative Distance.png: Plots the Census Bureau's Relative Distance measure for Black voting age populations over a variety of district sizes.

Hispanic VAP Relative Distance.png: Plots the Census Bureau's Relative Distance measure for Hispanic voting age populations over a variety of district sizes.

#### Input Data
Epsilon12.2Data.xlsx: Input data file with columns representing the political level (Congressional, State House, ...) and Census demographic data both in the 2010 Census and the 2010 Census with differential privacy applied. Each row represents a single district.

## License
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

This work is licensed under a
[Creative Commons Universal License][https://github.com/github/gitignore/blob/master/LICENSE].
