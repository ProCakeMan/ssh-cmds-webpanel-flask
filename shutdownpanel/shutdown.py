from flask import Flask, render_template, request
import paramiko
import json

app = Flask(__name__)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Function template for running ssh commands on host
def sshExec(host, cmd):
    user = "" # Enter your desired username here
    password = "" # Enter your desired password here
    ssh.connect(host, 22, user, password) # host, port, user, pass
    ssh.exec_command(cmd)
    ssh.close()

# Redirect from root url to dashboard.html, and imports hosts.json
@app.route("/")
def test():
    with open('hosts.json') as clients:
        data = clients.read()

    return render_template("dashboard.html", jsonData=json.dumps(data))

# Loads add client page
@app.route("/addclientpage/", methods=['GET', 'POST'])
def addClientPage():
    return render_template("addclient.html")

# Grabs ip and name from input fields and converts them to a dict which is then stored in a json file
@app.route("/addclient/", methods=['GET', 'POST'])
def addClient():
    ip = request.form.get('ip')
    name = request.form.get('name')
    with open('hosts.json') as clients:
        data = json.load(clients)
        data[ip] = name
    with open('hosts.json', 'w') as clients:
        json.dump(data, clients)
    return render_template("addclient.html") 

# Requests client and command that is to be executed on ssh connection
@app.route("/dashboard/", methods=['GET', 'POST'])
def dashboard():
    client = request.form.get('clients')
    command = request.form.get('cmds')

    sshExec(client, command)
    with open('hosts.json') as clients:
        data = clients.read()

    return render_template("dashboard.html", jsonData=json.dumps(data))


# Runs on local ip
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")