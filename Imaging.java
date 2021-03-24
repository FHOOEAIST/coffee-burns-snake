/*
 * Copyright (c) 2021 the original author or authors.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

import science.aist.imaging.api.domain.wrapper.ChannelType;
import science.aist.imaging.api.domain.wrapper.ImageWrapper;
import science.aist.imaging.api.domain.wrapper.implementation.ImageFactoryFactory;
import science.aist.imaging.service.core.imageprocessing.filter.ConvolveFunction;

public class Imaging {

    public static int current = 0;

    public static void main(String[] args) {
        int warmups = 100;
        int runs = 1000;
        int imageWidth = 1920;
        int imageHeight = 1080;

        ImageWrapper<short[][][]> image = ImageFactoryFactory.getImageFactory(short[][][].class).getImage(imageHeight, imageWidth, ChannelType.GREYSCALE);
        image.applyFunction((image1, x, y, c) -> {
            image1.setValue(x,y, c, current);
            current++;
            if (current > 255) current = 0;
        });
        ConvolveFunction<short[][][], short[][][]> cf = new ConvolveFunction<>(ImageFactoryFactory.getImageFactory(short[][][].class));
        int kernelSize = 5;
        double[][] averageKernel = new double[kernelSize][kernelSize];
        for (int x = 0; x < kernelSize; x++) {
            for (int y = 0; y < kernelSize; y++) {
                averageKernel[x][y] = 1.0 / ((double) (kernelSize * kernelSize));
            }
        }

        for (int i = 0; i < warmups; i++) {
            cf.apply(image, averageKernel);
        }

        for (int i = 0; i < runs; i++) {
            long before = System.currentTimeMillis();
            cf.apply(image, averageKernel);
            long after = System.currentTimeMillis();
            System.out.println("" + (after - before));
        }


    }
}
