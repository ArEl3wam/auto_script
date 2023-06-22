from os import path

HOST = 'egc-med-tesla'  # the host where the server will run
RUN_DIR = path.join(path.dirname(path.abspath(__file__)), "bash_scripts")

# conda configurations
CONDA_PATH = "/project/med/Wired/Install/anaconda3/etc/profile.d/conda.sh"
CONDA_ENV = "trenv"

# mongo configurations
RUN_MONGO_PATH = path.join(RUN_DIR, "run_mongo.sh")
KILL_MONGO_PATH = path.join(RUN_DIR, "kill_mongo.sh")
MONGO_PORT = 27651
MONGO_DBPATH = "/home/ahmsal8h/data2"

# backend configurations
RUN_BACKEND_PATH = path.join(RUN_DIR, "run_backend.sh")
KILL_BACKEND_PATH = path.join(RUN_DIR, "kill_backend.sh")
BACKEND_PORT = 8080
BACKEND_PROJECT_PATH = "/home/ahmsal8h/main/testSuitesApps/testSuiteManager"

# frontend configurations
RUN_FRONTEND_PATH = path.join(RUN_DIR, "run_front.sh")
KILL_FRONTEND_PATH = path.join("kill_front.sh")
FRONTEND_PORT = 3001
FRONTEND_PROJECT_BUILD_PATH = "/home/ahmsal8h/main/testSuitesApps/Siemens-MED-SW-Logger-System-FE/build"
