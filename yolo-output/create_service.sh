#! /bin/sh
cd /Users/micheleenharris/Documents/bin/mlflow_stuff/mlflow-keras-example/yolo-output
az ml service create realtime -n $1 --model-file model -f score.py   -r python -p requirements.txt
