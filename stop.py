import subprocess
from config import *


def stop_servers():
    # kill database server
    p1 = subprocess.Popen(f"ssh -f {HOST} '{KILL_MONGO_PATH} {MONGO_PORT} {MONGO_DBPATH} {CONDA_PATH} {CONDA_ENV}'",
                          shell=True,
                          stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE
                          )

    # kill backend server
    p2 = subprocess.Popen(f"ssh -f {HOST} '{KILL_BACKEND_PATH} {BACKEND_PORT}'",
                          shell=True,
                          stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE
                          )

    # kill frontend server

    p3 = subprocess.Popen(f"ssh -f {HOST} '{KILL_FRONTEND_PATH} {FRONTEND_PORT}'",
                          shell=True,
                          stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE
                          )

    for p in [p1, p2, p3]:
        stdout, stderr = p.communicate()
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())
