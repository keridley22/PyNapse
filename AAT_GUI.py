
import tkinter as tk
from tkinter import messagebox, filedialog
from image_aligner import ImageAligner
from segmenter import SynapsisSegmenter
from colocalization_analyzer import ColocalizationAnalyzer
from plaque_distance_analyzer import PlaqueDistanceAnalyzer

class AATGUI:
    def __init__(self, master):
        self.master = master
        master.title("AT")
        master.geometry('200x300')

        # Config Paths (These could be set through the interface)
        self.src_path = 'path/to/images'
        self.output_path = 'path/to/output'
        
        # Initialize here more attributes as needed for your modules
        
        self.label = tk.Label(master, text="--------------- Processing ---------------")
        self.label.pack(pady=10)

        # Buttons
        self.align_button = tk.Button(master, text="Align sequences", command=self.align)
        self.align_button.pack(pady=5)
        # The rest of your buttons here ...

    def align(self):
        # Example: Calling the ImageAligner class
        src_path = filedialog.askdirectory(title="Select Source Directory")
        if not src_path:  # If the user cancels the dialog, src_path will be empty
            return
        aligner = ImageAligner(src_path=self.src_path, output_path=self.output_path)
        aligner.perform_alignment()
        messagebox.showinfo("Action", "Alignment completed.")

    # Similar methods for segment, density, coloc, plaque ...