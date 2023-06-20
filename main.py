import subprocess
from config import *



# start database server
subprocess.Popen(
    f"ssh -f {HOST} '{RUN_MONGO_PATH} {MONGO_PORT} {MONGO_DBPATH} {CONDA_PATH} {CONDA_ENV}'",
    shell=True
)

# start backend server
subprocess.Popen(
    f"ssh -f {HOST} '{RUN_BACKEND_PATH} {BACKEND_PORT} {BACKEND_PROJECT_PATH} {CONDA_PATH} {CONDA_ENV}' ",
    shell=True
)

# start frontend server
p = subprocess.Popen(
    f"ssh -f {HOST} '{RUN_FRONTEND_PATH} {FRONTEND_PORT} {FRONTEND_PROJECT_BUILD_PATH} {CONDA_PATH} {CONDA_ENV}' ",
    shell=True,
    stdout=subprocess.PIPE
)

stdout, _ = p.communicate()
print(stdout.decode('utf-8'))


