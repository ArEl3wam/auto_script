import subprocess


class BackendChecker:
    __instance = None
    NODE_PATH = "/home/ahmela3q/.conda/envs/awam_env/bin/node"
    SERVER_PATH = "/home/ahmela3q/testSuitesApps/testSuiteManager/dist/server.js"
    PORT = 8080
    HOST = None

    def __new__(cls, host: str):
        if BackendChecker.__instance is None:
            cls.__instance = super(BackendChecker, cls).__new__(cls)
            cls.HOST = host
        return cls.__instance

    def check_backend(self) -> bool:
        if self.check_server():
            print("Backend server is already available.")
            return True
        else:
            print("Backend server is not available.")
            print(f"Starting backend on {self.HOST} ...")
            if self.create_backend():
                print("Backend server created successfully")
                return True
            else:
                print("failed to create backend server")
                return False

    def check_server(self) -> bool:
        print(f"Checking server on {self.HOST} ...")
        proc = subprocess.Popen(
            f"ssh {self.HOST} 'netstat -tlnp | grep :{self.PORT}'",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        out, error = proc.communicate()
        output = out.decode("utf-8")
        return "node" in output

    def create_backend(self) -> bool:
        proc = subprocess.Popen(
            f"ssh {self.HOST} '{self.NODE_PATH} {self.SERVER_PATH}'",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        try:
            out, error = proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            out, error = proc.communicate()

        err_message = error.decode("utf-8")
        return "address already in use" in err_message or len(err_message) == 0
