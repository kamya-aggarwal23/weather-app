import json

# with open("states.json",'r') as f:
#     data=json.load(f)#here load()was used as we were using file handling
# for state in data['states']:
#     print(state)
#     print(state['name'],state[ 'abbreviation'])  

# delting from poython and making new json file 
with open("states.json",'r') as f:
    data=json.load(f)#here load()was used as we were using file handling
for state in data['states']:
    del state['area_codes']

with open("new_string",'w') as f:
    json.dump(data,f,indent=2)#dump()was used as we are writing to a file , first we write what we are dumping and then where we are dumping to 