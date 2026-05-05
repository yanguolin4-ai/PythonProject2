import yaml

def read_yml(yml_path):
    with open (yml_path,'r',encoding='utf-8') as f:
        value=yaml.load(f,Loader=yaml.FullLoader)
        return value
