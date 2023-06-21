#!/bin/bash

if [ $# -ne 4 ]; then
  echo "wrong number of arguments"
  echo "kill_mongo <port> <dbpath> <conda_path> <conda_env>"
  exit 1
fi
port=$1
dbpath=$2
conda_path=$3
conda_env=$4

if netstat -tlnp | grep ":$port.*mongod " > /dev/null ; then
    echo "killing mongodb on port $port..."
    . $conda_path
    conda activate $conda_env
    if mongod --shutdown --dbpath $dbpath --port $port > /dev/null & then
       echo "mongodb killed successfully"
    fi
else
  echo "there is no mongo server on port $port"
fi