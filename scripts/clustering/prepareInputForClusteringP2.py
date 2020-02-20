import pandas as pd
import sys

dataFrame = pd.read_csv(sys.argv[1])

for key in dataFrame.keys():
    for i in range(len(dataFrame[key])):
        value = dataFrame[key][i]
        value = float(value)
        value = round(value, 3)
        dataFrame[key][i] = value

dataFrame.to_csv(sys.argv[1], index=False)
