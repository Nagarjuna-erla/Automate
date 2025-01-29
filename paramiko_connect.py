import paramiko
x=paramiko.SSHClient()
x.set_missing_host_key_policy(paramiko.AutoAddPolicy())
x.connect(username="root",hostname="192.168.171.174",password="0043")
a,b,c=x.exec_command("ls -l")
print(b.read())
