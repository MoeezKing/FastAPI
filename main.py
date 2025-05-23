from fastapi import FastAPI
from function import *
from json_obj import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- allows all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def startup():
    return {'Welcome': 'dear'}

@app.get('/get_all')
def get_all():
    data = read_file_json()
    return data

@app.get('/get/{id}')
def get_all(id):
    data = read_file_json()
    if id in data.keys():
        return data[id]
    else:
        return {'Status': f'No data avalianle for id {id}'}

@app.put('/update/{id}')
def update(id, name, age):
    data = read_file_json()
    if id in data.keys():
        data[id] = json_obj(name,age)
        write_file_json(data)
        return {'status': f'Data is successfully updated for id {id}'}
    else:
        return {'status': f'No data avalible for id {id}'}

@app.delete('/delete/{id}')
def delete(id):
    data = read_file_json()
    if id in data.keys():
        data.pop(str(id))
        write_file_json(data)
        return {'status': f'Data is successfully deleted for id {id}'}
    else:
        return {'status': f'No data avalible for id {id}'}
    

@app.post('/upload')
def upload(name,age):
    data = read_file_json()
    if len(data) >0:
        id = generate_id(max([x for x in data.keys()]))
    else:
        id = 1
    obj = json_obj(name,age)
    data = read_file_json()
    data[id] = obj
    write_file_json(data)
    return {'status': f'Data uploaded with id {id}'}
