![Logo](./documentation/logo.png)

Python and C++ are the most common programming languages, when it comes to image processing and computer vision. Especially, Python has grown more and more in this area in recent years. With this project we want to show that image processing is not only limited to these progamming languages. For this reason, we present a performance comparision of Java and Python in the context of CPU based image processing, since GPU support is more or less limited to C++. The comparision is done using pure programming language specific implementations without any additional frameworks as well as comparisions based on state of the art frameworks. In addition to that we also compare the implementations using different interpreters. As foundation of the comparision we are using a simple kernel-based averaging filter on a greyscale image.

In addition to the state of the art frameworks we also compare the different implementations with our [Imaging](https://github.com/FHOOEAIST/imaging) project.

The idea of this project is based on the comparision of Pereira et. al in the context of energy efficiency across programming languages.
```
@inproceedings{pereira2017energy,
  title={Energy efficiency across programming languages: how do energy, time, and memory relate?},
  author={Pereira, Rui and Couto, Marco and Ribeiro, Francisco and Rua, Rui and Cunha, J{\'a}come and Fernandes, Jo{\~a}o Paulo and Saraiva, Jo{\~a}o},
  booktitle={Proceedings of the 10th ACM SIGPLAN International Conference on Software Language Engineering},
  pages={256--267},
  year={2017}
}
```

## Results

TODO - show results, and list/describe used frameworks



## Getting Started

To reproduce the results just use the provided .bat file and adapt the path to the folder that is mounted into the used Docker containers.

### Requirements

This comparision uses Java and Python in a Docker environment. For this reason [Docker](https://www.docker.com/) is required to execute the comparision on your own.

## FAQ

If you have any questions, please checkout our <insert FAQ link here if using maven site, otherwise write a small FAQ section here>.

## Contributing

**First make sure to read our [general contribution guidelines](https://fhooeaist.github.io/CONTRIBUTING.html).**
   
## Licence

Copyright (c) 2021 the original author or authors.
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

## Research

If you are going to use this project as part of a research paper, we would ask you to reference this project by citing
it. 

<TODO zenodo doi>
