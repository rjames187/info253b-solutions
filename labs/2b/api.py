db = {}

def set_item(db, key, value):
    db[key] = value

def get_item(db, key):
    return db[key]

def remove_item(db, key):
    del db[key]