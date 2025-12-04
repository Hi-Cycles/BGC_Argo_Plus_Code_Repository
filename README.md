# BGC Argo Plus code repository
The purpose of this repository is to make it easier for people to get up and running using data from the global array of biogeochemical Argo floats. 
These are basic examples of how to use float data from this database and will hopefully be updated over time. Additional contributions are welcome. 

## Getting started. To use the code contained in this repository, you will need to:
1) Download some amount of float data from BGCArgoPlus.info/download
2) Clone, fork, or download this repository
3) Have a working install of Python and a virtual environment with the packages listed in "bgcargoplus.yml". You can use this yml file to directly create a new environment using the command: XXXX, or use an existing environment that has the required packages. 

## Current list of scripts and their functionality:
**Complete:**

Name | Purpose
--- | ---
Float_file_exploration.ipynb | Loads a single float file, makes some basic plots to explore the data

**Wish list:**

Name | Purpose
--- | ---
Geo_Search.ipynb | Get floats in a specific region, explore the data, make mean seasonal cycles and profiles
Outlier_Detection.ipynb | Allows you to go through the same outlier detection steps that we do
