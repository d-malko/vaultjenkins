import jenkins

# https://opendev.org/jjb/python-jenkins/src/branch/master/jenkins/__init__.py

class JenkinsAuth:
    def __init__(self,config):
        self.jenkinsUrl=config['jenkinsUrl']
        self.jenkinsUser=config['jenkinsUsername']
        self.jenkinsPassword=config['jenkinsPassword']
        self.jenkinsFolder=config['foldername']
        self.jenkinscredsId=config['credsId']
        self.jenkinsServer=jenkins.Jenkins(self.jenkinsUrl, username=self.jenkinsUser, password=self.jenkinsPassword)    
    
    def credExists(self):
        print(self.jenkinsServer.credential_exists(self, self.jenkinscredsId, self.jenkinsFolder))
        return True

    def createRoleCredentials(self,credId,credDesc,roleId,secretId,path,folder_name):  
        newConfig=f'''
            <com.datapipe.jenkins.vault.credentials.VaultAppRoleCredential plugin="hashicorp-vault-plugin@364.vf5d54b_3dc313">
              <id>{credId}</id>
              <description>{credDesc}</description>
              <usePolicies>false</usePolicies>
              <tokenExpiry/>
              <tokenCache/>
              <secretId>
                  {secretId}
              </secretId>
              <roleId>{roleId}</roleId>
              <path>{path}</path>
            </com.datapipe.jenkins.vault.credentials.VaultAppRoleCredential>
          '''
        # try:
        result=self.jenkinsServer.create_credential(folder_name,newConfig)
        return credId
        # except:
        #     print("There is some error while creating a app role credentials")

    def updateJenkinsCredApp(self,credId,credDesc,roleId,secretId,path,folder_name):
        reConfig=f'''
            <com.datapipe.jenkins.vault.credentials.VaultAppRoleCredential plugin="hashicorp-vault-plugin@364.vf5d54b_3dc313">
              <id>{credId}</id>
              <description>{credDesc}</description>
              <usePolicies>false</usePolicies>
              <tokenExpiry/>
              <tokenCache/>
              <secretId>
                  {secretId}
              </secretId>
              <roleId>{roleId}</roleId>
              <path>{path}</path>
            </com.datapipe.jenkins.vault.credentials.VaultAppRoleCredential>
          '''
        self.jenkinsServer.reconfig_credential(folder_name,reConfig)
        print(self.jenkinsServer.get_credential_config(roleId,folder_name))
      
    def runner(self,credId,credDesc,roleId,secretId,path,folder_name):
        if self.credExists():
            self.updateJenkinsCredApp(credId,credDesc,roleId,secretId,path,folder_name)
            print("Updated")
        else:
            self.createRoleCredentials(credId,credDesc,roleId,secretId,path,folder_name)
            print("Created")
    def __str__(self):
        user = self.jenkinsServer.get_whoami()
        version = self.jenkinsServer.get_version()
        return 'Hello %s from Jenkins %s' % (user['fullName'], version)