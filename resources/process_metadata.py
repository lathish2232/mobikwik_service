
import pprint
import json
from atm_dict import atmdata

slno=1
record=[]
for rec in atmdata:
    rec.update({'atmId':slno})
    record.append(rec)
    slno+=1

with open("atm_json.json", "w") as outfile: 
    json.dump(record, outfile)
print('--------------------------------------')