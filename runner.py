from config.loader import getConfig
from vault.credentials import Vault
from jenkinshelper.jenkinscredentials import JenkinsAuth

config=getConfig()

vault=Vault(config['vault'])
print(vault)
role_id,secret_id=vault.getCredentials('terraform-2')
jenkins=JenkinsAuth(config['jenkins'])
jenkins.runner(config['jenkins']['credsId'],config['jenkins']['credsId'],role_id,secret_id,'approle',config['jenkins']['foldername'])

