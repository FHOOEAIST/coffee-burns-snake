/*
 * Copyright (c) 2021 the original author or authors.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

import aist.science.aistcv.AistCVLoader;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.imgproc.Imgproc;

public class OpenCVPerformanceTest {
    public static int current = 0;

    public static void main(String[] args) {
        AistCVLoader.loadShared();
        int warmups = 100;
        int runs = 1000;
        int imageWidth = 1920;
        int imageHeight = 1080;

        Mat mat = Mat.zeros(imageHeight, imageWidth, CvType.CV_8U);
        for (int x = 0; x < imageWidth; x++) {
            for (int y = 0; y < imageHeight; y++) {
                mat.put(x,y,current);
                current++;
                if (current > 255) current = 0;
            }
        }
        Mat mat2 = Mat.zeros(mat.rows(), mat.cols(), mat.type());
        int kernelsize = 5;
        Mat kernel = Mat.zeros(kernelsize,kernelsize, mat.type());
        for (int x = 0; x < kernelsize; x++) {
            for (int y = 0; y < kernelsize; y++) {
                kernel.put(x,y,1.0 / (kernelsize * kernelsize));
            }
        }

        for (int i = 0; i < warmups; i++) {
            Imgproc.filter2D(mat, mat2, -1, kernel);
        }

        for (int i = 0; i < runs; i++) {
            long before = System.nanoTime();
            Imgproc.filter2D(mat, mat2, -1, kernel);
            long after = System.nanoTime();
            System.out.println(""+((after - before)/1000000.0));
        }
    }
}
