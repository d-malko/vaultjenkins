import hvac

class Vault:
    def __init__(self,config):
        self.vaultUrl=config['vaultUrl']
        self.rootToken=config['rootToken']
        self.client=hvac.Client(url=self.vaultUrl, token=self.rootToken)

    def getCredentials(self,rolename,mountPoint='approle'):
        response = self.client.auth.approle.generate_secret_id(
            role_name=rolename,
            mount_point=mountPoint
        )
        role_id = self.client.auth.approle.read_role_id(rolename)['data']['role_id']
        secret_id = response['data']['secret_id']
        return role_id,secret_id
    
    def __str__(self):
        return f"Vault connected for {self.vaultUrl}"