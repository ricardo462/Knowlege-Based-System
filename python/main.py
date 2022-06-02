import json
from model.Clause import Clause

PARAMETERS_PAHT = 'python/parameters.json'


with open(PARAMETERS_PAHT) as json_file:
    data = json.load(json_file)

