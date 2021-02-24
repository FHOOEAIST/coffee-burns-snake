#!/bin/bash

basepath=${pwd}
openjdk=openjdk:11-jre-slim
amazoncorretto=amazoncorretto:11-alpine
zulu=azul/zulu-openjdk:11
adopt=adoptopenjdk:11-jre-hotspot
graaljdk=ghcr.io/graalvm/graalvm-ce:latest
volumeplain=${basepath}/Test.class:/app/Test.class
volumeimaging=${basepath}:/app/
statementplaint='java -cp /app/ Test'
statementimagingsingle='java -cp /app/:/app/core_single.jar PerformanceTest'
statementimagingparallel='java -cp /app/:/app/core_parallel.jar PerformanceTest'

mkdir res

docker run -v  ${volumeplain} --rm ${openjdk} ${statementplaint} > res/openjdk-plain.txt
docker run -v  ${volumeplain} --rm ${amazoncorretto} ${statementplaint} > res/amazoncorretto-plain.txt
docker run -v  ${volumeplain} --rm ${zulu} ${statementplaint} > res/zulu-plain.txt
docker run -v  ${volumeplain} --rm ${adopt} ${statementplaint} > res/adopt-plain.txt
docker run -v  ${volumeplain} --rm ${graaljdk} ${statementplaint} > res/graaljdk-plain.txt

docker run -v  ${volumeimaging} --rm ${openjdk} ${statementimagingsingle} > res/openjdk-imaging-single.txt
docker run -v  ${volumeimaging} --rm ${amazoncorretto} ${statementimagingsingle} > res/amazoncorretto-imaging-single.txt
docker run -v  ${volumeimaging} --rm ${zulu} ${statementimagingsingle} > res/zulu-imaging-single.txt
docker run -v  ${volumeimaging} --rm ${adopt} ${statementimagingsingle} > res/adopt-imaging-single.txt
docker run -v  ${volumeimaging} --rm ${graaljdk} ${statementimagingsingle} > res/graaljdk-imaging-single.txt

docker run -v  ${volumeimaging} --rm ${openjdk} ${statementimagingparallel} > res/openjdk-imaging-parallel.txt
docker run -v  ${volumeimaging} --rm ${amazoncorretto} ${statementimagingparallel} > res/amazoncorretto-imaging-parallel.txt
docker run -v  ${volumeimaging} --rm ${zulu} ${statementimagingparallel} > res/zulu-imaging-parallel.txt
docker run -v  ${volumeimaging} --rm ${adopt} ${statementimagingparallel} > res/adopt-imaging-parallel.txt
docker run -v  ${volumeimaging} --rm ${graaljdk} ${statementimagingparallel} > res/graaljdk-imaging-parallel.txt
