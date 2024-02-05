import os
import numpy as np
import tifffile
from skimage.filters import threshold_local, median
from skimage.morphology import remove_small_objects, binary_opening
from skimage.io import imsave
from skimage.color import gray2rgb
from skimage.util import img_as_ubyte

class SynapseSegmenter:
    def __init__(self, src_path, window_size, corr_factor, method, min_size, max_size):
        self.src_path = src_path
        self.window_size = window_size
        self.corr_factor = corr_factor
        self.method = method
        self.min_size = min_size
        self.max_size = max_size
        self.segmented_path = os.path.join(src_path, 'Segmented')
        if not os.path.exists(self.segmented_path):
            os.makedirs(self.segmented_path)
    
    def _save_parameters(self):
        params_file = os.path.join(self.segmented_path, 'parameters.txt')
        with open(params_file, 'w') as f:
            f.write(f"SrcPath: {self.src_path}\n")
            f.write(f"Window size: {self.window_size}\n")
            f.write(f"Correction factor: {self.corr_factor}\n")
            f.write(f"Method: {self.method}\n")
            f.write(f"Object min size: {self.min_size}\n")
            f.write(f"Object MAX size: {self.max_size}\n")

    def segment_images(self):
        self._save_parameters()
        for filename in os.listdir(self.src_path):
            if not filename.endswith('.tif'): continue
            img_path = os.path.join(self.src_path, filename)
            img = tifffile.imread(img_path)
            segmented_img = self._segment_image(img)
            self._save_segmented_image(segmented_img, filename)

    def _segment_image(self, img):
        if self.method == "mean":
            thresh_img = self._apply_mean_thresh(img)
        elif self.method == "median":
            thresh_img = self._apply_median_thresh(img)
        else:
            raise ValueError(f"Unsupported method: {self.method}")
        
        # Remove small objects and save segmented images
        cleaned_img = remove_small_objects(thresh_img, self.min_size)
        return cleaned_img

    def _apply_mean_thresh(self, img):
        local_thresh = threshold_local(img, self.window_size, "mean")
        binary_img = img > (local_thresh - self.corr_factor)
        return binary_img
    
    def _apply_median_thresh(self, img):
        median_img = median(img, selem=np.ones((self.window_size, self.window_size)))
        s_img = median_img - img - self.corr_factor
        binary_img = s_img > 0
        return binary_img
    
    def _save_segmented_image(self, img, original_filename):
        output_filename = f"{original_filename[:-4]}_segmented.tif"
        output_path = os.path.join(self.segmented_path, output_filename)
        imsave(output_path, img_as_ubyte(img))