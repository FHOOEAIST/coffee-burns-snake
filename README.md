![Logo](./documentation/logo.png)

Python and C++ are the most common programming languages, when it comes to image processing and computer vision.
Especially, Python has grown more and more in this area in recent years. With this project we want to show that image
processing is not only limited to these programming languages. For this reason, we present a performance comparison of
Java and Python in the context of CPU based image processing, since GPU support is more or less limited to C++. The
comparison is done using pure programming language specific implementations without any additional frameworks as well as
comparisons based on state-of-the-art frameworks. In addition to that we also compare the implementations using
different interpreters. As foundation of the comparison we are using a simple kernel-based averaging filter on a
greyscale image.

In addition to the state-of-the-art frameworks we also compare the different implementations with
our [Imaging](https://github.com/FHOOEAIST/imaging) project.

The idea of this project is based on the comparison of Pereira et. al in the context of energy efficiency across
programming languages.

```
@inproceedings{pereira2017energy,
  title={Energy efficiency across programming languages: how do energy, time, and memory relate?},
  author={Pereira, Rui and Couto, Marco and Ribeiro, Francisco and Rua, Rui and Cunha, J{\'a}come and Fernandes, Jo{\~a}o Paulo and Saraiva, Jo{\~a}o},
  booktitle={Proceedings of the 10th ACM SIGPLAN International Conference on Software Language Engineering},
  pages={256--267},
  year={2017}
}
```

## Setup

Our test setup is composed of different Python and Java executions. In the course of this we do not only compare Java
and Python, but also different concepts in each Python and Java, as well as different runtime environments in Java. This
section will describe the different concepts and will show the different executions that are executed.

### Java

The main comparison in Java is between a pure Java-based implementation (compare Pure.java) and the implementation of
the [Imaging-Framework](https://github.com/FHOOEAIST/imaging). The plain implementation is using simple for-loops to
iterate through the image, whereas the Imaging-Framework is using multiple abstraction layers, to get a high advanced
software architecture. Behind that
the [Java Streaming API](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html) is utilized to
iterate the images. This also allows us, to easily execute the process in parallel.

Moreover, we are comparing that to other concepts
like [OpenCV filter2D](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html) as well as
[OpenImaJ FourierConvolve](http://openimaj.org/apidocs/org/openimaj/image/processing/convolution/FourierConvolve.html).
Please note, that these implementations rely on a different concept on how to apply the convolution filter.

### Python

In Python, we compare a pure Python-based implementation, with state-of-the-art frameworks
like [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html). In addition to that we
compare how the base array type performs in comparison with
the [numpy array](https://numpy.org/doc/stable/reference/generated/numpy.array.html). Moreover, we added the framework
[numba](https://numba.pydata.org/) to evaluate the performance utilizing JIT compilation. Finally, we are adding the
OpenCV filter2D in Python, to see how it performs there.

All of this now results in the following test-setup:

| Execution Name | Language | Framework | Parallel |
|-|-|-|-|
| adopt-imaging-parallel | Java 11 (AdoptOpenJDK) | Imaging | X |
| adopt-imaging-single | Java 11 (AdoptOpenJDK) | Imaging |  |
| adopt-plain | Java 11 (AdoptOpenJDK) | Plain Java |  |
| amazoncorretto-imaging-parallel | Java 11 (Amazon Corretto) | Imaging | X |
| amazoncorretto-imaging-single | Java 11 (Amazon Corretto) | Imaging |  |
| amazoncorretto-plain | Java 11 (Amazon Corretto) | Plain Java |  |
| graaljdk-imaging-parallel | Java 11 (GraalVM) | Imaging | X |
| graaljdk-imaging-single | Java 11 (GraalVM) | Imaging |  |
| graaljdk-plain | Java 11 (GraalVM) | Plain Java |  |
| openjdk-imaging-parallel | Java 11 (OpenJDK) | Imaging | X |
| openjdk-imaging-single | Java 11 (OpenJDK) | Imaging |  |
| openjdk-opencv | Java 11 (OpenJDK) | OpenCV (filter2d) |  |
| openjdk-openimaj | Java 11 (OpenJDK) | OpenImaJ (FourierConvolve) |  |
| openjdk-plain | Java 11 (OpenJDK) | Plain Java |  |
| zulu-imaging-parallel | Java 11 (Zulu OpenJDK) | Imaging | X |
| zulu-imaging-single | Java 11 (Zulu OpenJDK) | Imaging |  |
| zulu-plain | Java 11 (Zulu OpenJDK) | Plain Java |  |
| python-pure-simple | Python 3.7.10 | Plain Python |  |
| python-with-itertools | Python 3.7.10 | Itertools |  |
| python-pure-simple-with-numba | Python 3.7.10 | Numba |  |
| python-pure-simple-with-numba-parallel | Python 3.7.10 | Numba | X |
| python-itertools-with-numba | Python 3.7.10 | Itertools + Numba |  |
| python-with-numpy | Python 3.7.10 | Numpy |  |
| python-with-numpy-with-numba | Python 3.7.10 | Numpy + Numba |  |
| python-with-numpy-with-numba-parallel | Python 3.7.10 | Numpy + Numba | X |
| python-with-numpy-and-scipy | Python 3.7.10 | Numpy + Scipy (convolve) |  |
| python-with-opencv | Python 3.7.10 | OpenCV (filter2d) |  |

## Results

| Execution Name | Avg | Median | Stdev | Min | Max |
|---|--:|--:|--:|--:|--:|
| adopt-imaging-parallel | 74.72 | 74.00 | 2.21 | 73.00 | 92.00 |
| adopt-imaging-single | 266.91 | 267.00 | 1.51 | 264.00 | 275.00 |
| adopt-plain | 236.23 | 236.00 | 3.08 | 233.00 | 263.00 |
| amazoncorretto-imaging-parallel | 66.43 | 66.00 | 2.16 | 65.00 | 78.00 |
| amazoncorretto-imaging-single | 260.64 | 260.00 | 4.10 | 256.00 | 289.00 |
| amazoncorretto-plain | 231.82 | 231.00 | 3.96 | 229.00 | 262.00 |
| graaljdk-imaging-parallel | 76.06 | 76.00 | 2.53 | 74.00 | 95.00 |
| graaljdk-imaging-single | 226.76 | 226.00 | 2.61 | 224.00 | 261.00 |
| graaljdk-plain | 163.37 | 163.00 | 3.61 | 161.00 | 247.00 |
| openjdk-imaging-parallel | 73.97 | 73.00 | 2.56 | 72.00 | 99.00 |
| openjdk-imaging-single | 266.25 | 266.00 | 4.09 | 263.00 | 293.00 |
| openjdk-opencv | 0.39 | 0.39 | 0.01 | 0.37 | 0.49 |
| openjdk-openimaj | 30.99 | 30.00 | 1.52 | 29.00 | 35.00 |
| openjdk-plain | 236.35 | 236.00 | 4.01 | 232.00 | 269.00 |
| zulu-imaging-parallel | 84.96 | 84.00 | 2.26 | 83.00 | 101.00 |
| zulu-imaging-single | 277.46 | 277.00 | 4.50 | 273.00 | 308.00 |
| zulu-plain | 248.50 | 248.00 | 4.41 | 244.00 | 282.00 |
| python-pure-simple | 14597.56 | 14521.56 | 228.28 | 14342.33 | 15254.21 |
| python-with-itertools | 13166.17 | 13155.98 | 31.02 | 13118.70 | 13239.89 |
| python-pure-simple-with-numba | 236.77 | 236.48 | 1.00 | 234.98 | 243.49 |
| python-pure-simple-with-numba-parallel | 40.41 | 40.16 | 1.14 | 39.46 | 49.95 |
| python-itertools-with-numba | 3355.02 | 3352.39 | 11.11 | 3334.98 | 3410.89 |
| python-with-numpy | 8622.70 | 8613.33 | 37.41 | 8557.27 | 8795.89 |
| python-with-numpy-with-numba | 83.09 | 83.01 | 0.34 | 82.45 | 85.86 |
| python-with-numpy-with-numba-parallel | 3.68 | 3.62 | 0.44 | 3.49 | 11.21 |
| python-with-numpy-and-scipy | 33.72 | 33.68 | 0.26 | 33.00 | 35.66 |
| python-with-opencv | 4.62 | 4.61 | 0.05 | 4.55 | 4.82 |

## Getting Started

To reproduce the results just use the provided .bat file and adapt the path to the folder that is mounted into the used
Docker containers.

### Requirements

This comparison uses Java and Python in a Docker environment. For this reason [Docker](https://www.docker.com/) is
required to execute the comparison on your own.

## Contributing

**First make sure to read our [general contribution guidelines](https://fhooeaist.github.io/CONTRIBUTING.html).**

## Licence

Copyright (c) 2021 the original author or authors. DO NOT ALTER OR REMOVE COPYRIGHT NOTICES.

This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not
distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

## Research

If you are going to use this project as part of a research paper, we would ask you to reference this project by citing
it.

<TODO zenodo doi>
