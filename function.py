import json as js

file_name = 'file.json'

def read_file_json():
    with open(file_name, 'r') as file:
        data = js.load(file)
    
    return data

def write_file_json(data):
    with open(file_name, 'w') as file:
        js.dump(data,file, indent=4)

def generate_id(largest_id):
    largest_id = int(largest_id)
    largest_id+=1
    return largest_id

#file testing 


# data = {
#     '1': {
#         'name':'ahmed',
#         'age': 23
#     },
#     '2': {
#         'name':'zeo',
#         'age': 30
#     }
# }

# write_file_json(data=data)

# data = read_file_json()

# print(data['2'])
