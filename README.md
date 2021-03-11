![Logo](./documentation/logo.png)

Python and C++ are the most common programming languages, when it comes to image processing and computer vision.
Especially, Python has grown more and more in this area in recent years. With this project we want to show that image
processing is not only limited to these programming languages. For this reason, we present a performance comparison of
Java and Python in the context of CPU based image processing, since GPU support is more or less limited to C++. The
comparison is done using pure programming language specific implementations without any additional frameworks as well as
comparisons based on state-of-the-art frameworks. In addition to that we also compare the implementations using
different interpreters. A foundation of the comparison we are using a simple kernel-based averaging filter on a
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

Our test setup is composed of different Python and Java execution. In the course of this we do not only compare Java and
Python, but also different concepts in each Python and Java, as well as different runtime environments in Java. This
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

In Python, we are compare a pure Python-based implementation, with state-of-the-art frameworks
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
| adopt-imaging-parallel | 74.716 | 74 | 2.214349566 | 73 | 92 |
| adopt-imaging-single | 266.906 | 267 | 1.512998348 | 264 | 275 |
| adopt-plain | 236.234 | 236 | 3.081759887 | 233 | 263 |
| amazoncorretto-imaging-parallel | 66.432 | 66 | 2.159485124 | 65 | 78 |
| amazoncorretto-imaging-single | 260.636 | 260 | 4.100427295 | 256 | 289 |
| amazoncorretto-plain | 231.815 | 231 | 3.956864289 | 229 | 262 |
| graaljdk-imaging-parallel | 76.063 | 76 | 2.526861888 | 74 | 95 |
| graaljdk-imaging-single | 226.756 | 226 | 2.608536755 | 224 | 261 |
| graaljdk-plain | 163.369 | 163 | 3.611763973 | 161 | 247 |
| openjdk-imaging-parallel | 73.966 | 73 | 2.55750738 | 72 | 99 |
| openjdk-imaging-single | 266.254 | 266 | 4.088457411 | 263 | 293 |
| openjdk-opencv | 0.3874037 | 0.38555 | 0.010192285 | 0.3669 | 0.4877 |
| openjdk-openimaj | 30.992 | 30 | 1.519189257 | 29 | 35 |
| openjdk-plain | 236.353 | 236 | 4.005545032 | 232 | 269 |
| zulu-imaging-parallel | 84.96 | 84 | 2.259734498 | 83 | 101 |
| zulu-imaging-single | 277.464 | 277 | 4.502966134 | 273 | 308 |
| zulu-plain | 248.496 | 248 | 4.407038008 | 244 | 282 |
| python-pure-simple | 14597.55727 | 14521.5646 | 228.2797177 | 14342.3267 | 15254.21 |
| python-with-itertools | 13166.17094 | 13155.9817 | 31.02182746 | 13118.6995 | 13239.8873 |
| python-pure-simple-with-numba | 236.7716764 | 236.4792 | 1.002887261 | 234.9782 | 243.4942 |
| python-pure-simple-with-numba-parallel | 40.4083385 | 40.15895 | 1.136760149 | 39.4646 | 49.9453 |
| python-itertools-with-numba | 3355.023436 | 3352.3944 | 11.10746727 | 3334.9832 | 3410.886 |
| python-with-numpy | 8622.696959 | 8613.3275 | 37.4140637 | 8557.2733 | 8795.8881 |
| python-with-numpy-with-numba | 83.0877721 | 83.0067 | 0.343173192 | 82.4468 | 85.8613 |
| python-with-numpy-with-numba-parallel | 3.684825 | 3.62215 | 0.442201182 | 3.487000002 | 11.2139 |
| python-with-numpy-and-scipy | 33.7167672 | 33.6834 | 0.257274667 | 33.0048 | 35.6594 |
| python-with-opencv | 4.6194036 | 4.61255 | 0.048011085 | 4.5519 | 4.817200001 |

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
