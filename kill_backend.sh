#!/bin/bash
if [ $# -ne 1 ]; then
  echo "wrong number of arguments"
  echo "kill_backend <port>"
  exit 1
fi

port=$1


if ! curl -X POST http://localhost:$port/shutdown > /dev/null; then
    echo "there is no backend server on port $port..."

else
  echo "backend server on port $port killed successfully"
fi