#!/bin/bash


port=27017
conda_path=/project/med/Wired/Install/anaconda3/etc/profile.d/conda.sh # conda.sh path
conda_env=awam_env
dbpath=/home/ahmela3q/mongo_cdb

if ! netstat -tuln | grep ":$port " > /dev/null; then
    echo "starting mongodb on port $port..."
    . $conda_path
    conda activate $conda_env
    if mongod --dbpath $dbpath --port $port > /dev/null & then
       echo "mongodb started successfully"
    fi
else
  echo "something is already listening to port $port"
fi