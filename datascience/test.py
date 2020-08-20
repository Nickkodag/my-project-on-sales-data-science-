
import pandas as pd
import quandl
import math

df =quandl.get("BATS/EDGA_QFIN", transform="diff")
df.fillna(-22277.0, str(inplace="True")




Forecast_out=int(math.ceil(0.01*len(df)))
df["label"]=df[Forecast_cast].shift(-forecast_out)
print(df)
