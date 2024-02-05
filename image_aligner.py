import numpy as np
from skimage.registration import phase_cross_correlation
from scipy.ndimage import affine_transform
from skimage.transform import resize
from image_handler import ImageHandler

class ImageAligner:
    def __init__(self, src_path, channels, reference_channel_name, output_path=None, downsampling_factor=6):
        self.src_path = src_path
        self.channels = channels
        self.reference_channel_name = reference_channel_name
        self.output_path = output_path if output_path else src_path
        self.downsampling_factor = downsampling_factor
        self.reference_image_stack = None
        self.moving_images = []

    def load_images(self):
        """
        Reads the stack for each channel and separates the reference from the moving images.
        """
        for channel in self.channels:
            filename = f"{self.src_path}/{channel}.tif"
            img_stack = ImageHandler.read_stack_tiff(filename)

            if channel == self.reference_channel_name:
                self.reference_image_stack = img_stack
            else:
                self.moving_images.append((channel, img_stack))

    @staticmethod
    def align_images(reference_image, moving_image, downsampling_factor):
        """
        Aligns moving_image to reference_image.
        """
        # Downsample images for initial phase correlation
        downscaled_ref = resize(reference_image, (reference_image.shape[0] // downsampling_factor, reference_image.shape[1] // downsampling_factor), anti_aliasing=True)
        downscaled_mov = resize(moving_image, (moving_image.shape[0] // downsampling_factor, moving_image.shape[1] // downsampling_factor), anti_aliasing=True)

        # Phase cross-correlation to find the translations
        shift, error, diffphase = phase_cross_correlation(downscaled_ref, downscaled_mov)

        # Scale shift back to original image size
        shift = shift * downsampling_factor

        # Create affine transform with the estimated shift
        af = np.array([[1, 0, shift[1]],
                       [0, 1, shift[0]],
                       [0, 0, 1]])

        # Apply transformation
        aligned_image = affine_transform(moving_image, af, order=1, output_shape=moving_image.shape, cval=np.min(moving_image))
        return aligned_image

    def perform_alignment(self):
        """
        Performs alignment for all moving images to reference.
        """
        self.load_images()
        
        for name, stack in self.moving_images:
            aligned_stack = np.zeros_like(stack)
            for i in range(stack.shape[0]):
                aligned_stack[i] = self.align_images(self.reference_image_stack[i], stack[i], self.downsampling_factor)
            ImageHandler.save_tiff_stack(aligned_stack, f"{self.output_path}/Aligned/{name}_aligned.tif")
        print("Alignment done.")