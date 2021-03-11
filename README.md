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
our Imaging project [^1].

The idea of this project is based on the comparison of Pereira et. al [^2] in the context of energy efficiency across
programming languages.

## Setup

Our test setup is composed of different Python and Java execution. In the course of this we do not only compare Java and
Python, but also different concepts in each Python and Java, as well as different runtime environments in Java. This
section will describe the different concepts and will show the different executions that are executed.

### Java

The main comparison in Java is between a pure Java-based implementation (compare Pure.java) and the implementation of
the Imaging-Framework [^1] . The plain implementation is using simple for-loops to
iterate through the image, whereas the Imaging-Framework is using multiple abstraction layers, to get a high advanced
software architecture. Behind that
the [Java Streaming API](https://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html) is utilized to
iterate the images. This also allows us, to easily execute the process in parallel.

Moreover, we are comparing different ... continue.

## Results

TODO - show results, and list/describe used frameworks

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

TODO zenodo doi

## References

[^1]: https://github.com/FHOOEAIST/imaging
[^2]: Pereira, Rui, et al. "Energy efficiency across programming languages: how do energy, time, and memory relate?."
Proceedings of the 10th ACM SIGPLAN International Conference on Software Language Engineering. 2017.
