#!/bin/bash
if [ $# -ne 1 ]; then
  echo "wrong number of arguments"
  echo "kill_frontend <port>"
  exit 1
fi

port=$1



process_pid=$(netstat -nlp | grep ":$port " | awk '{print $7}' | awk -F"/" '{print $1}')
if [ -z "$process_pid" ]; then
    echo "there is no front server on port $port..."
    exit 1
fi
echo "killing front server process $process_pid on port $port..."
kill -9 $process_pid
echo "front server on port $port killed successfully"
