import os
import yaml

config = None

def load_yaml(path):
    global config
    if config is None:
       with open(path, 'r',encoding='utf-8') as f:
          config = yaml.safe_load(f.read())
    return config


def get_base_url():
    base = load_yaml('./config/config.yml')
    base_url = base['test']['base_url']
    return base_url

def get_config():
    """获取当前环境的完整配置"""
    config = load_yaml('./config/config.yml')
    env = os.getenv('TEST_ENV', 'dev')
    return config.get(env, config['dev'])
