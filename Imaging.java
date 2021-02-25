import science.aist.imaging.api.domain.wrapper.ChannelType;
import science.aist.imaging.api.domain.wrapper.ImageWrapper;
import science.aist.imaging.api.domain.wrapper.implementation.ImageFactoryFactory;
import science.aist.imaging.service.core.imageprocessing.filter.ConvolveFunction;

public class Imaging {

    public static int current = 0;

    public static void main(String[] args) {
        int warmups = 25;
        int runs = 100;
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
