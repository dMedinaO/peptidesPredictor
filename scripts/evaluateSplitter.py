'''
script que procesa un csv, agrupa por grupo y obtiene las propiedades de dicho grupo, ademas de ello
evalua cuantas de las propiedades distribuyen normal y cuantas no.

Genera como resultado un csv con el resumen de la informacion
'''

import pandas as pd
import sys

summary_groups = pd.read_csv(sys.argv[1])
properties_list = pd.read_csv(sys.argv[2])

list_distribution = []
list_p_values = []
for property in summary_groups['property']:

    for i in range(len(properties_list)):
        if properties_list['key-property'][i] == property:
            list_distribution.append(properties_list['normal-distribution'][i])
            list_p_values.append(properties_list['p-value'][i])
            break

summary_groups['status_distribution'] = list_distribution
summary_groups['p_value'] = list_p_values
summary_groups.to_csv(sys.argv[3], index=False)
