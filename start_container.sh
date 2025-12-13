#!/bin/bash

docker run -it -p 8888:8888 =v .:/home/jovyan/files quay.io/jupyter/pyspark-notebook:latest