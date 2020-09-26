import os.path

url = "http://automationpractice.com/index.php"
project_root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
logs_path = project_root + '/logs'

# os.getcwd() =  Current working directory ;  os.pardir = Parent Directory of the current Directory , os.path.join =  read it
