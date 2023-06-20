#!/bin/bash

port=8080
conda_path=/project/med/Wired/Install/anaconda3/etc/profile.d/conda.sh # conda.sh path
conda_env=awam_env
project_path=/home/ahmela3q/testSuitesApps/testSuiteManager

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