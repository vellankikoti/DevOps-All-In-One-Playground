import paramiko

def check_disk_usage(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    stdin, stdout, stderr = client.exec_command('df -h')
    print(stdout.read().decode())
    client.close()

check_disk_usage('remote_host', 'username', 'password')
