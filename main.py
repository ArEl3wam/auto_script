from backend_checker import BackendChecker
from database_checker import DatabaseChecker
import subprocess

//27651
HOST = 'egc-med-tesla'

subprocess.Popen(f"ssh -f {HOST} '/home/ahmela3q/testSuitesApps/auto_script/run_mongo.sh'", shell=True)
subprocess.Popen(f"ssh -f {HOST} '/home/ahmela3q/testSuitesApps/auto_script/run_backend.sh' ", shell=True)


p = subprocess.Popen(
    f"ssh -f {HOST} '/home/ahmela3q/testSuitesApps/auto_script/run_front.sh' ",
    shell=True,
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE
)

stdout, stderr = p.communicate()
print(stdout.decode('utf-8'))
