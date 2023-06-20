#!/bin/bash

if [ $# -ne 4 ]; then
  echo "wrong number of arguments"
  echo "run_backend <port> <project_path> <conda_path> <conda_env>"
  exit 1
fi

port=$1
project_path=$2
conda_path=$3
conda_env=$4

if ! netstat -tuln | grep ":$port " > /dev/null; then
    echo "starting backend server on port $port..."
    . $conda_path
    conda activate $conda_env
    cd $project_path
    if npm run dev > /dev/null & then
       echo "backend started successfully"
    fi
else
  echo "something is already listening to port $port"
fi

