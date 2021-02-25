set basepath=C:\Users\P41743\Desktop\cbs\coffee-burns-snake

set openjdk=openjdk:11-jre-slim
set amazoncorretto=amazoncorretto:11-alpine
set zulu=azul/zulu-openjdk:11
set adopt=adoptopenjdk:11-jre-hotspot
set graaljdk=ghcr.io/graalvm/graalvm-ce:latest

set python3710=python:3.7.10-buster

set volumeimaging=%basepath%:/app/

set statementplaint=java -cp /app/ Pure
set statementimagingsingle=java -cp /app/:/app/core_single.jar Imaging
set statementimagingparallel=java -cp /app/:/app/core_parallel.jar Imaging
set statementopencv=java -cp /app/:/app/aistcv-4.3.0.jar OpenCVPerformanceTest

set statementpython=/bin/bash -c "apt update; apt install -y libgl1-mesa-glx; cd /app; pip install -r requirements.txt; python performance_test.py"

mkdir res


rem Java Plain

docker container run -v %volumeimaging% --rm %openjdk% %statementplaint% > res/openjdk-plain.txt
docker container run -v %volumeimaging% --rm %amazoncorretto% %statementplaint% > res/amazoncorretto-plain.txt
docker container run -v %volumeimaging% --rm %zulu% %statementplaint% > res/zulu-plain.txt
docker container run -v %volumeimaging% --rm %adopt% %statementplaint% > res/adopt-plain.txt
docker container run -v %volumeimaging% --rm %graaljdk% %statementplaint% > res/graaljdk-plain.txt

rem Java using Imaging (Single Core)

docker container run -v %volumeimaging% --rm %openjdk% %statementimagingsingle% > res/openjdk-imaging-single.txt
docker container run -v %volumeimaging% --rm %amazoncorretto% %statementimagingsingle% > res/amazoncorretto-imaging-single.txt
docker container run -v %volumeimaging% --rm %zulu% %statementimagingsingle% > res/zulu-imaging-single.txt
docker container run -v %volumeimaging% --rm %adopt% %statementimagingsingle% > res/adopt-imaging-single.txt
docker container run -v %volumeimaging% --rm %graaljdk% %statementimagingsingle% > res/graaljdk-imaging-single.txt

rem Java using Imaging (Multi Core)

docker container run -v %volumeimaging% --rm %openjdk% %statementimagingparallel% > res/openjdk-imaging-parallel.txt
docker container run -v %volumeimaging% --rm %amazoncorretto% %statementimagingparallel% > res/amazoncorretto-imaging-parallel.txt
docker container run -v %volumeimaging% --rm %zulu% %statementimagingparallel% > res/zulu-imaging-parallel.txt
docker container run -v %volumeimaging% --rm %adopt% %statementimagingparallel% > res/adopt-imaging-parallel.txt
docker container run -v %volumeimaging% --rm %graaljdk% %statementimagingparallel% > res/graaljdk-imaging-parallel.txt

rem Java using OpenCV

docker container run -v %volumeimaging% --rm %openjdk% %statementopencv% > res/openjdk-opencv-parallel.txt

rem Python

docker container run -v %volumeimaging% --rm %python3710% %statementpython% > res/python-3-7-10.txt