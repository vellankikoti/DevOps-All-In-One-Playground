import paramiko

def ssh_connect(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command('uptime')
    print(stdout.read().decode())
    client.close()

ssh_connect('remote_host', 'username', 'password')
