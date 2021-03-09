package science.aist.imaging.service.openimaj.imageprocessing;

import org.openimaj.image.FImage;
import org.openimaj.image.processing.convolution.FourierConvolve;

public class OpenImajTest {
    public static int current = 0;

    public static void main(String[] args) {
        int warmups = 25;
        int runs = 100;
        int imageWidth = 1920;
        int imageHeight = 1080;
        int kernelSize = 5;

        FImage image = new FImage(imageWidth, imageHeight);
        for(int x = 0; x < imageWidth; x++){
            for (int y = 0; y < imageHeight; y++) {
                float cval = (float)current / 255.0f;
                image.setPixel(x, y, cval);
                current++;
                if (current > 255) current = 0;
            }
        }

        float[][] mask = new float[][]{
                new float[]{1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize))},
                new float[]{1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize))},
                new float[]{1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize))},
                new float[]{1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize))},
                new float[]{1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize)), 1.0f / ((float) (kernelSize * kernelSize))},
        };

        for (int i = 0; i < warmups; i++) {
            FourierConvolve.convolve(image, mask, false);
        }

        for (int i = 0; i < runs; i++) {
            long before = System.currentTimeMillis();
            FourierConvolve.convolve(image, mask, false);
            long after = System.currentTimeMillis();
            System.out.println("" + (after - before));
        }

    }
}