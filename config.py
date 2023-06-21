HOST = 'egc-med-tesla'  # the host where the server will run

# conda configurations
CONDA_PATH = "/project/med/Wired/Install/anaconda3/etc/profile.d/conda.sh"
CONDA_ENV = "awam_env"

# mongo configurations
RUN_MONGO_PATH = "/home/ahmela3q/testSuitesApps/auto_script/run_mongo.sh"  # change later
KILL_MONGO_PATH = "/home/ahmela3q/testSuitesApps/auto_script/kill_mongo.sh"  # change later
MONGO_PORT = 27777
MONGO_DBPATH = "/home/ahmela3q/mongo_cdb"

# backend configurations
RUN_BACKEND_PATH = "/home/ahmela3q/testSuitesApps/auto_script/run_backend.sh"
KILL_BACKEND_PATH = "/home/ahmela3q/testSuitesApps/auto_script/kill_backend.sh"  # change later
BACKEND_PORT = 8080
BACKEND_PROJECT_PATH = "/home/ahmela3q/testSuitesApps/testSuiteManager"

# frontend configurations
RUN_FRONTEND_PATH = "/home/ahmela3q/testSuitesApps/auto_script/run_front.sh"
KILL_FRONTEND_PATH = "/home/ahmela3q/testSuitesApps/auto_script/kill_front.sh"  # change later
FRONTEND_PORT = 3333
FRONTEND_PROJECT_BUILD_PATH = "/home/ahmela3q/testSuitesApps/Siemens-MED-SW-Logger-System-FE/build"
