#!/bin/bash

if [ $# -ne 4 ]; then
  echo "wrong number of arguments"
  echo "run_backend <port> <project_path> <conda_path> <conda_env>"
  exit 1
fi

port=$1
build_folder=$2
conda_path=$3
conda_env=$4


if ! netstat -tuln | grep ":$port " > /dev/null; then
    echo "starting the static server..."
    . $conda_path
    conda activate $conda_env
    npx serve -s $build_folder -l $port > /dev/null &
    echo "started successfully!"

else
  echo "something is already listening to port $port"
fi

