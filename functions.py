def filter_query(value, data):
    return filter(lambda x: value in x, data)

def map_query(value, data):
    return map(lambda x: x.split()[value], data)
