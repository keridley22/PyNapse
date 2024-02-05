
import os
import numpy as np
import tifffile
import pandas as pd
from skimage.measure import label, regionprops
from skimage.morphology import dilation, erosion, disk

class DensityAnalyzer:
    def __init__(self, src_path, channels, neuropil_channel, xy_res, z_res):
        self.src_path = src_path
        self.channels = channels
        self.neuropil_channel = neuropil_channel
        self.xy_res = xy_res
        self.z_res = z_res
        self.neuropil_mask = None
        self.results = []

        # Results directories
        self.results_dir = os.path.join(src_path, 'Density_Results')
        self.neuropil_mask_dir = os.path.join(self.results_dir, 'Neuropilmask')
        os.makedirs(self.results_dir, exist_ok=True)
        os.makedirs(self.neuropil_mask_dir, exist_ok=True)

    def load_channel_images(self, channel_name):
        """
        Load TIFF stack for a given channel name.
        """
        filename = os.path.join(self.src_path, f'{channel_name}.tif')
        image_stack = tifffile.imread(filename)
        return image_stack.astype(bool)

    def create_neuropil_mask(self):
        """
        Create a neuropil mask based on the specified channel.
        """
        image_stack = self.load_channel_images(self.neuropil_channel)
        z_proj = np.max(image_stack, axis=0)
        z_proj_dil = dilation(z_proj, disk(19))
        neuropil_mask = erosion(z_proj_dil, disk(10)) 
        # Save the neuropil mask to a file
        output_filename = os.path.join(self.neuropil_mask_dir, f'{self.neuropil_channel}_neuropilMask.tif')
        tifffile.imsave(output_filename, neuropil_mask.astype(np.uint8) * 255)
        self.neuropil_mask = neuropil_mask

    def analyze_density(self):
        """
        Analyze density for each channel and save the results.
        """
        self.create_neuropil_mask()
        neuropil_area = np.count_nonzero(self.neuropil_mask)

        for channel in self.channels:
            image_stack = self.load_channel_images(channel)
            obj_count = np.sum([np.any(slice_img) for slice_img in image_stack])
            total_area_vx = image_stack.size
            density = (obj_count / neuropil_area) / (self.xy_res * self.xy_res * self.z_res) * 1e9

            self.results.append({
                "Sequence_name": channel,
                "Objects": obj_count,
                "Total_area_vx": total_area_vx,
                "Neuropil_area_vx": neuropil_area,
                "Density_in_neuropil_mm3": density,
            })

    def save_results(self):
        """
        Saves the analysis results to an Excel file.
        """
        df = pd.DataFrame(self.results)
        output_file = os.path.join(self.results_dir, 'Densities.xlsx')
        df.to_excel(output_file, index=False)