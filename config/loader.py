import yaml

def getConfig():
    with open('.development.yml','r') as file:
        config=yaml.safe_load(file)
    return config
