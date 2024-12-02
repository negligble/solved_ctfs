#!/bin/bash

docker build --tag=dreamdiary1 .
docker run -it -p 1337:1337 --rm --name=dreamdiary1 dreamdiary1