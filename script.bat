rem Copyright (c) 2021 the original author or authors.
rem DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
rem This Source Code Form is subject to the terms of the Mozilla Public
rem License, v. 2.0. If a copy of the MPL was not distributed with this
rem file, You can obtain one at https://mozilla.org/MPL/2.0/.

set basepath=%cd%

set openjdk=openjdk:11-jre-slim
set amazoncorretto=amazoncorretto:11-alpine
set zulu=azul/zulu-openjdk:11
set adopt=adoptopenjdk:11-jre-hotspot
set graaljdk=ghcr.io/graalvm/graalvm-ce:latest

set python3710=python:3.7.10-buster

set volumeimaging=%basepath%:/app/

set statementpure=java -cp /app/ Pure
set statementimagingsingle=java -cp /app/:/app/core_single.jar Imaging
set statementimagingparallel=java -cp /app/:/app/core_parallel.jar Imaging
set statementopencv=java -cp /app/:/app/aistcv-4.3.0.jar OpenCVPerformanceTest
set statementopenimaj=java -cp /app/:/app/openimaj-1.3.10.jar OpenImajTest

set statementpython=/bin/bash -c "apt update; apt install -y libgl1-mesa-glx; cd /app; pip install -r requirements.txt; python 

mkdir res

rem  Java Pure

docker container run --cpus=4 -v %volumeimaging% --rm %openjdk% %statementpure% > res/openjdk-pure.txt
docker container run --cpus=4 -v %volumeimaging% --rm %amazoncorretto% %statementpure% > res/amazoncorretto-pure.txt
docker container run --cpus=4 -v %volumeimaging% --rm %zulu% %statementpure% > res/zulu-pure.txt
docker container run --cpus=4 -v %volumeimaging% --rm %adopt% %statementpure% > res/adopt-pure.txt
docker container run --cpus=4 -v %volumeimaging% --rm %graaljdk% %statementpure% > res/graaljdk-pure.txt

rem Java using Imaging (Single Core)

docker container run --cpus=4 -v %volumeimaging% --rm %openjdk% %statementimagingsingle% > res/openjdk-imaging-single.txt
docker container run --cpus=4 -v %volumeimaging% --rm %amazoncorretto% %statementimagingsingle% > res/amazoncorretto-imaging-single.txt
docker container run --cpus=4 -v %volumeimaging% --rm %zulu% %statementimagingsingle% > res/zulu-imaging-single.txt
docker container run --cpus=4 -v %volumeimaging% --rm %adopt% %statementimagingsingle% > res/adopt-imaging-single.txt
docker container run --cpus=4 -v %volumeimaging% --rm %graaljdk% %statementimagingsingle% > res/graaljdk-imaging-single.txt

rem Java using Imaging (Multi Core)

docker container run --cpus=4 -v %volumeimaging% --rm %openjdk% %statementimagingparallel% > res/openjdk-imaging-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %amazoncorretto% %statementimagingparallel% > res/amazoncorretto-imaging-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %zulu% %statementimagingparallel% > res/zulu-imaging-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %adopt% %statementimagingparallel% > res/adopt-imaging-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %graaljdk% %statementimagingparallel% > res/graaljdk-imaging-parallel.txt

rem Java using OpenCV

docker container run --cpus=4 -v %volumeimaging% --rm %openjdk% %statementopencv% > res/openjdk-opencv.txt

rem Java using OpenIMAJ

docker container run --cpus=4 -v %volumeimaging% --rm %openjdk% %statementopenimaj% > res/openjdk-openimaj.txt

rem Python

docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_pure_simple_python.py"> res/python-pure.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_pure_simple_python_while.py"> res/python-pure-while.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_pure_simple_python_with_numba.py"> res/python-pure-numba.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_pure_simple_python_with_numba_parallel.py"> res/python-pure-numba-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_itertools.py"> res/python-itertools.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_itertools_with_numba.py"> res/python-itertools-numba.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_numpy.py"> res/python-numpy.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_numpy_and_scipy.py"> res/python-numpy,scipy.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_numpy_with_numba.py"> res/python-numpy-numba.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_numpy_with_numba_parallel.py"> res/python-numy-numba-parallel.txt
docker container run --cpus=4 -v %volumeimaging% --rm %python3710% %statementpython% run_with_opencv.py"> res/python-opencv.txt
