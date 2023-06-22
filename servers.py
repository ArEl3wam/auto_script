from start import start_servers
from stop import stop_servers
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("to start the servers: python servers.py start")
        print("to stop the servers: python servers.py stop")
        sys.exit(1)

    if sys.argv[1] == "start":
        start_servers()
    elif sys.argv[1] == "stop":
        stop_servers()
