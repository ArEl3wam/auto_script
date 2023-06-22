import subprocess
from config import *


def start_servers():
    # start database server
    p1 = subprocess.Popen(
        f"ssh -f {HOST} '{RUN_MONGO_PATH} {MONGO_PORT} {MONGO_DBPATH} {CONDA_PATH} {CONDA_ENV}'",
        shell=True
    )

    # start backend server
    p2 = subprocess.Popen(
        f"ssh -f {HOST} '{RUN_BACKEND_PATH} {BACKEND_PORT} {BACKEND_PROJECT_PATH} {CONDA_PATH} {CONDA_ENV}' ",
        shell=True
    )

    # start frontend server
    p3 = subprocess.Popen(
        f"ssh -f {HOST} '{RUN_FRONTEND_PATH} {FRONTEND_PORT} {FRONTEND_PROJECT_BUILD_PATH} {CONDA_PATH} {CONDA_ENV}' ",
        shell=True,
        stdout=subprocess.PIPE
    )

    for p in [p1, p2, p3]:
        stdout, stderr = p.communicate()
        if stdout:
            print(stdout.decode())
        if stderr:
            print(stderr.decode())