import subprocess
from config import *

HOST = 'egc-med-tesla'

# kill database server
p1 = subprocess.Popen(f"ssh -f {HOST} '{KILL_MONGO_PATH} {MONGO_PORT} {MONGO_DBPATH} {CONDA_PATH} {CONDA_ENV}'",
                      shell=True,
                      stderr=subprocess.PIPE,
                      stdout=subprocess.PIPE
                      )
stdout, stderr = p1.communicate()
print(stdout.decode('utf-8'))

# kill backend server
p2 = subprocess.Popen(f"ssh -f {HOST} '{KILL_BACKEND_PATH} {BACKEND_PORT}'",
                      shell=True,
                      stderr=subprocess.PIPE,
                      stdout=subprocess.PIPE
                      )
stdout, stderr = p2.communicate()
print(stdout.decode('utf-8'))

# kill frontend server

p3 = subprocess.Popen(f"ssh -f {HOST} '{KILL_FRONTEND_PATH} {FRONTEND_PORT}'",
                      shell=True,
                      stderr=subprocess.PIPE,
                      stdout=subprocess.PIPE
                      )
stdout, stderr = p3.communicate()
print(stdout.decode('utf-8'))
