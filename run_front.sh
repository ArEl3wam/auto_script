#!/bin/bash

port=5555  # the port the server will serve the file from
conda_path=/project/med/Wired/Install/anaconda3/etc/profile.d/conda.sh # conda.sh path
conda_env=awam_env  # the name of conda env which has npx
build_folder=/home/ahmela3q/testSuitesApps/Siemens-MED-SW-Logger-System-FE/build  #the path to the build folder of the project


if ! netstat -tuln | grep ":$port " > /dev/null; then
    echo "starting the frontend server..."
    . $conda_path
    conda activate $conda_env
    npx serve -s $build_folder -l $port > /dev/null &
    echo "started successfully!"

else
  echo "something is already listening to port $port"
fi

