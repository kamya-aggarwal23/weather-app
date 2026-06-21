''' JavaScript Object Notation '''

import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": [
                "johnsmith@bogusemail.com",
                "john.smith@work-place.com"
            ],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
# jason to python obeject
# data=json.loads(people_string)#loads nput json strign and conevrt to python obj
# for person in data['people']:
#     print(person)

# deleteing a key 
# data=json.loads(people_string)
# for person in data['people']:
#     del person['phone']

#python obj to json string
# data=json.loads(people_string)
# for person in data['people']:
#     del person['phone']
# new_string=json.dumps(data,indent=2,sort_key=True)#dumps input python obj and cnvert to json string,indent help for clear output,sort_keys sort the keys 
# print(new_string)

