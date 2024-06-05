import argparse
from vault.credentials import Vault
from jenkinshelper.jenkinscredentials import JenkinsAuth

# Parse command line arguments
parser = argparse.ArgumentParser(description='Process Jenkins credentials.')
parser.add_argument("--vault_url", required=True, help="Vault URL")
parser.add_argument("--root_token", required=True, help="Root token")
parser.add_argument("--jenkins_url", required=True, help="Jenkins URL")
parser.add_argument("--jenkins_username", required=True, help="Jenkins username")
parser.add_argument("--jenkins_password", required=True, help="Jenkins password")
parser.add_argument("--foldername", required=True, help="Foldername")
parser.add_argument("--credsId", required=True, help="Credentials ID")
args = parser.parse_args()

# Setup configurations from command line arguments
vault_config = {"vaultUrl": args.vault_url, "rootToken": args.root_token}
jenkins_config = {
    "jenkinsUrl": args.jenkins_url,
    "jenkinsUsername": args.jenkins_username,
    "jenkinsPassword": args.jenkins_password,
    "foldername": args.foldername,
    "credsId": args.credsId,
}

vault = Vault(vault_config)
print(vault)
role_id, secret_id = vault.getCredentials('kickstarter-stage')
jenkins = JenkinsAuth(jenkins_config)
jenkins.runner(jenkins_config['credsId'], jenkins_config['credsId'], role_id, secret_id, 'approle',
               jenkins_config['foldername'])