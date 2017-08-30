"""
This module contain the global parameter for the LSTM model
Created on 28/08/17
by fccoelho
license: GPL V3 or Later
"""
#======Global importing data parameters=======
state = 'RJ'

# Data_types: list of types of data to get into combined_data function
# Possible types: 'alerta', 'weather', 'tweet'
data_types = ['alerta', 'weather']

#=======Clustering parameters========
# Variables to include in the correlation distance
cluster_vars = [
    "casos"
]
color_treshold = 0.6 # threshold for coloring the dendrogram
tmp_path = '/tmp' #path to temporary files for clustering aux data


#=======LSTM parameters==============

# Predictors must change to fit data_types list
predictors = [
    'casos',
    'p_rt1',
    'p_inc100k',
    'temp_min',
    'temp_max',
    'umid_min',
    'pressao_min'
]

HIDDEN = 4
LOOK_BACK = 4
BATCH_SIZE = 1
prediction_window = 3  # weeks
# city = 3304557 # Rio de Janeiro
# city = 3303500 # Nova Iguaçu
city = 3301009 # Campos dos Goytacazes
# city = 3205309 # Vitoria
# city = 3205200 # Vila Velha, ES
epochs = 100
