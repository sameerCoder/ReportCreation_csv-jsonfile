#csv+json file report generation.
import pandas as pd
from pandas_profiling import ProfileReport
bank1=pd.read_csv("bank1.csv")
print(bank1.columns)
bank2=pd.read_json("bank2json.json",orient="values")
print(bank2.columns)
finaldf=pd.concat([bank1,bank2])
print(finaldf.info())
profile=ProfileReport(finaldf)
profile.to_file(output_file="finalreportfilecsvjson.html")
