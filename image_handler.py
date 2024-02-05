
import tifffile

class ImageHandler:
    @staticmethod
    def read_stack_tiff(filename):
        """
        Reads a TIFF stack.
        """
        return tifffile.imread(filename)

    @staticmethod
    def save_tiff_stack(image_stack, output_filename):
        """
        Saves the image stack into a TIFF file.
        """
        tifffile.imsave(output_filename, image_stack.astype(image_stack.dtype))