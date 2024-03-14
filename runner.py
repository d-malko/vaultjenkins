from config.loader import getConfig
from vault.credentials import Vault

config=getConfig()

vault=Vault(config['vault'])
print(vault)
role_id,secret_id=vault.getCredentials('terraform')

