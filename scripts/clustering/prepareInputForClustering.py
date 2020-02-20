import pandas as pd
import sys

dataFrame = pd.read_csv(sys.argv[1])

#removemos los elementos no necesarios para formar la matriz final
dataFrame = dataFrame.drop('Code', axis=1)
dataFrame = dataFrame.drop('Description', axis=1)

dataFrame.to_csv(sys.argv[2], index=False)
