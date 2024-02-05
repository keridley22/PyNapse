from image_aligner import ImageAligner
from segmenter import SynapseSegmenter
from density_analyzer import DensityAnalyzer
from colocalization_analyzer import ColocalizationAnalyzer 
from plaque_distance_analyzer import PlaqueDistanceAnalyzer # Import the SynapseSegmenter class

from AAT_GUI import AATGUI

import tkinter as tk


def main():
    # Create the main window
    root = tk.Tk()
    
    # Initialize the GUI Application, passing the root window
    app = AATGUI(root)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()

'''def main():
    # Alignment steps
    src_path = 'path/to/images'
    channels = ['channel1', 'channel2', 'reference_channel']
    reference_channel_name = 'reference_channel'
    output_path = 'path/to/output'

    aligner = ImageAligner(src_path, channels, reference_channel_name, output_path)
    aligner.perform_alignment()
    
    print("Alignment process has been completed.")

    # Segmentation steps after alignment
    # Assume the aligned images are saved in a subdirectory within 'path/to/output', adjust if different
    aligned_images_path = 'path/to/output/Aligned'
    window_size = 51  # Example window size for local thresholding
    corr_factor = 10  # Example correction factor
    method = "mean"  # or "median", depending on your specific need
    min_size = 50  # Minimum object size for segmentation
    max_size = 500  # Maximum object size for segmentation

    segmenter = SynapseSegmenter(
        src_path=aligned_images_path,  # Use the directory where aligned images are saved
        window_size=window_size,
        corr_factor=corr_factor,
        method=method,
        min_size=min_size,
        max_size=max_size
    )

    segmenter.segment_images()
    
    print("Segmentation process has been completed.")

    src_path = 'path/to/images'
    channels = ['channel1', 'channel2', 'reference_channel']
    neuropil_channel = 'reference_channel'
    xy_res = 0.102  # Lateral resolution in micron/pixel
    z_res = 0.07  # Axial resolution in micron/pixel

    analyzer = DensityAnalyzer(src_path, channels, neuropil_channel, xy_res, z_res)
    analyzer.analyze_density()
    analyzer.save_results()
    
    print("Density analysis completed and results saved.")

    src_path = 'path/to/images'
    channels = ['channel1', 'channel2', 'reference_channel']
    xy_res = 0.102  # Microns per pixel resolution in X-Y
    z_res = 0.07  # Microns per pixel resolution in Z
    max_distance = 0.5  # Maximum distance for distance-based colocalization
    min_overlap = 10  # Minimum percent overlap for overlap-based colocalization
    
    analyzer = ColocalizationAnalyzer(src_path, channels, xy_res, z_res, max_distance, min_overlap)
    analyzer.analyze()

    src_path = 'path/to/images'
    channels = ['OC', 'SYPH', 'PSD', 'TAU']
    abeta_name = 'OC'
    xy_res = 0.102  # Lateral resolution in micron/pixel
    z_res = 0.07  # Axial resolution in micron/pixel
    max_um = 50
    step_um = 10
    neuropil_channel = 'SYPH'

    analyzer = PlaqueDistanceAnalyzer(src_path, channels, abeta_name, xy_res, z_res, max_um, step_um, neuropil_channel)
    analyzer.analyze()

if __name__ == "__main__":
    main()'''
