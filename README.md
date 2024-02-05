# PyNapse




# Image Analysis Suite for Array Tomography

This suite provides advanced image analysis capabilities for array tomography datasets, including alignment, segmentation, colocalization, density estimation, and plaque distance analysis. Our intuitive graphical user interface (GUI) facilitates seamless processing of image stacks for detailed biological research and analysis.

## Getting Started

### Prerequisites

- Python 3.6+ installed on your system.
- Required Python Libraries: `numpy`, `pandas`, `scikit-image`, `tifffile`, `openpyxl`.
- Install the required libraries using:
    ```bash
    pip install numpy pandas scikit-image tifffile openpyxl
    ```

### Installation

- Clone the repository or download the source code to your desired directory.
    ```
    git clone <repository-url>
    ```
- Navigate to the project directory:
    ```
    cd image-analysis-suite
    ```

### Running the Suite

1. **Launching the GUI**:
   
   Execute `main.py` to start the application:
   ```bash
   python main.py
   ```
2. **Using the GUI**:

   Upon launch, you'll be presented with a straightforward interface, enabling you to select and process your image data through the following functionalities.

### Workflows

#### 1. **Pre-Processing**

- **Image Preparation**: Have your images saved as stacks of consecutive images, with each channel separated and aptly named. The naming convention is crucial for automated processing (e.g., `Case1_syph.tif`, `Case1_abeta.tif`).

- **Data Organization**: Store different cases or sections with the same channel combination in a single folder for batch processing.

#### 2. **Image Alignment**

- Select *"Align sequences"* to align image stacks.
  
- Select the folder containing images and specify the reference channel. The alignment process may take time depending on the image sizes.

#### 3. **Segmentation**

- Choose *"Segmentation"* for segmenting objects within your images.
  
- Select a folder and adjust parameters such as window size and correction factor for automatic local thresholding.

#### 4. **Density Analysis**

- Click on *"Density"* to calculate the number of 3D objects present in a stack. Ensure images are pre-segmented.
  
- This feature includes calculations of densities and saves results in a dedicated folder.

#### 5. **Colocalization Analysis**

- Opt for *"Colocalization"* to evaluate the percent of object colocalization within your samples based on distance or overlap.

- Follow the prompts to select images, set analysis parameters, and choose between saving images of colocalization.

#### 6. **Plaque Distance Analysis**

- Select *"Plaque distance"* to measure the distance of objects from amyloid plaques.
  
- Specify relevant channels, plaque identifiers, and configure analysis preferences including bin sizes for results categorization.

### Customization and Advanced Usage

- While the GUI provides immediate access to tool functionalities, advanced users can tweak parameters directly within the code (`image_aligner.py`, `segmenter.py`, etc.) for more granular control.
  
- For detailed parameter adjustments that are not available via the GUI, see comments and documentation within each module or script.

## Contributing

We welcome contributions to enhance the Image Analysis Suite's capabilities or address any issues. Please review `CONTRIBUTING.md` for guidelines on contributions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Note:** The `<repository-url>` needs to be replaced with the actual URL of your Git repository. Adjust the readme documentation as necessary to align with your specific setup or additional features you might implement.
