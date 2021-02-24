import java.util.stream.IntStream;

public class Test {
    public static void main(String[] args) {
        int warmup = 25;
        int runs = 100;

        int width = 1920;
        int height = 1080;
        int channels = 1;
        boolean normalize = true;

        int kernelSize = 5;
        double[][] averageKernel = new double[kernelSize][kernelSize];
        for (int x = 0; x < kernelSize; x++) {
            for (int y = 0; y < kernelSize; y++) {
                averageKernel[x][y] = 1.0 / ((double) (kernelSize * kernelSize));
            }
        }

        short[][][] image = new short[height][width][channels];

        short cnt = 0;
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                for (int c = 0; c < channels; c++) {
                    image[y][x][c] = cnt++;

                    if (cnt > 255) {
                        cnt = 0;
                    }
                }
            }
        }

        for (int r = 0; r < runs + warmup; r++) {
            long before = System.currentTimeMillis();
            short[][][] result = new short[height][width][channels];


            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    for (int c = 0; c < channels; c++) {
                        double sum = 0.0;
                        double maskSum = 0.0;
                        int yRadius = (kernelSize - 1) / 2;
                        for (int yOffset = -yRadius; yOffset <= yRadius; yOffset++) {
                            int xRadius = (kernelSize - 1) / 2;
                            for (int xOffset = -xRadius; xOffset <= xRadius; xOffset++) {
                                int nbX = x + xOffset;
                                int nbY = y + yOffset;
                                if ((nbX >= 0) && (nbX < width) && (nbY >= 0) && (nbY < height)) {
                                    sum += result[nbY][nbX][0] * averageKernel[yOffset + yRadius][xOffset + xRadius];
                                    maskSum += averageKernel[yOffset + yRadius][xOffset + xRadius];
                                } //range check
                            } // xOffset
                        } // yOffset
                        if (normalize) {
                            if (maskSum == 0) {
                                throw new IllegalStateException("KernelSum is 0 but normalizing is active");
                            }
                            sum *= 1.0 / maskSum;
                        } // normalize

                        result[y][x][c] = (short) sum;
                    }
                }
            }

            long after = System.currentTimeMillis();
            if(r > warmup - 1){
                System.out.println("#" + (r - warmup) + " Kernel Runtime: " + (after - before));
            }
        }
    }
}
