import subprocess


class DatabaseChecker:
    __instance = None
    MONGOD_PATH: str = "/home/ahmela3q/.conda/envs/awam_env/bin/mongod"
    MONGO_DATA_PATH: str = "/home/ahmela3q/mongo_cdb"
    HOST: str = 'egc-med-edison'
    PORT: int = 27651

    def __new__(cls, host: str):
        if DatabaseChecker.__instance is None:
            cls.__instance = super(DatabaseChecker, cls).__new__(cls)
            cls.HOST = host
        return cls.__instance

    def check_db(self) -> bool:
        if self.__check_mongo():
            print("MongoDB server is already available.")
            return True
        else:
            print("MongoDB server is not available.")
            print(f"Starting mongodb on {self.HOST} ...")
            if self.__create_db():
                print("mongo db server created successfully")
                return True
            else:
                print("failed to create mongo db server")
                return False

    def __create_db(self) -> bool:
        proc = subprocess.Popen(
            f"ssh {self.HOST} '{self.MONGOD_PATH} --dbpath {self.MONGO_DATA_PATH}'",
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
        return len(err_message) == 0

    def __check_mongo(self):
        proc = subprocess.Popen(
            f"ssh {self.HOST}  'netstat -tlnp | grep :{self.PORT}'",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )
        out, error = proc.communicate()
        output = out.decode("utf-8")
        return "mongod" in output
