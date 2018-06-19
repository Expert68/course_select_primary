import os
import pickle
from conf import settings

def save(obj):
    obj_path = os.path.join(settings.BASE_DB,obj.__class__.__name__.lower())
    if not os.path.isdir(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path,obj.name)
    with open(file_path,'wb') as f:
        pickle.dump(obj,f)


def select(name,type):
    obj_path = os.path.join(settings.BASE_DB, type)
    if not os.path.isdir(obj_path):
        os.mkdir(obj_path)
    file_path = os.path.join(obj_path,name)
    if os.path.isdir(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    else:
        return None
