import os
import json
import exifread
import hashlib  # For checksum calculation
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from PIL import Image, ImageTk



class MetaDataFinderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MetaDataFinder - Professional Tool")
        self.root.geometry("1000x800")
        self.root.minsize(1000, 800)

        # Initialize variables
        self.image_path = None
        self.metadata = {}
        self.theme = "dark"  # Fixed to dark theme

        # Set initial theme
        self.set_theme()

        # Create UI Elements
        self.create_ui()

    def set_theme(self):
        if self.theme == "dark":
            self.bg_color = "#333333"
            self.fg_color = "#FFFFFF"
            self.button_bg = "#555555"
            self.button_fg = "#FFFFFF"
            self.text_area_bg = "#444444"
            self.text_area_fg = "#FFFFFF"
        self.root.configure(bg=self.bg_color)

    def create_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root,
            text="MetaDataFinder",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            padx=10,
            pady=10
        )
        title_label.pack(fill="x")

        # Description Label
        desc_label = tk.Label(
            self.root,
            text="A Comprehensive Image Metadata Finder & Manager Tool",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color
        )
        desc_label.pack(pady=10)

        # File Upload Button
        upload_button = tk.Button(
            self.root,
            text="Upload Image",
            command=self.upload_image,
            font=("Arial", 12),
            bg=self.button_bg,
            fg=self.button_fg,
            padx=10,
            pady=5
        )
        upload_button.pack(pady=10)

        # Image Preview Frame
        self.image_preview_frame = tk.Frame(self.root, bg=self.bg_color)
        self.image_preview_frame.pack(pady=10)
        self.image_label = tk.Label(self.image_preview_frame, bg=self.bg_color)
        self.image_label.pack()

        # Metadata Display Area
        self.metadata_display = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=("Arial", 10),
            bg=self.text_area_bg,
            fg=self.text_area_fg,
            insertbackground=self.fg_color
        )
        self.metadata_display.pack(pady=10)
        self.metadata_display.config(state="disabled")

        # Action Buttons Frame
        buttons_frame = tk.Frame(self.root, bg=self.bg_color)
        buttons_frame.pack(pady=10)

        # Check Metadata Button
        check_button = tk.Button(
            buttons_frame,
            text="Check Metadata",
            command=self.check_metadata,
            font=("Arial", 12),
            bg=self.button_bg,
            fg=self.button_fg,
            padx=10,
            pady=5
        )
        check_button.grid(row=0, column=0, padx=10)

        # Remove Metadata Button
        remove_button = tk.Button(
            buttons_frame,
            text="Remove Metadata",
            command=self.remove_metadata,
            font=("Arial", 12),
            bg=self.button_bg,
            fg=self.button_fg,
            padx=10,
            pady=5
        )
        remove_button.grid(row=0, column=1, padx=10)

        # Save Metadata Button
        save_button = tk.Button(
            buttons_frame,
            text="Save Metadata",
            command=self.save_metadata,
            font=("Arial", 12),
            bg=self.button_bg,
            fg=self.button_fg,
            padx=10,
            pady=5
        )
        save_button.grid(row=0, column=2, padx=10)

        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="indeterminate")
        self.progress.pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        if self.image_path:
            self.display_image()
        else:
            messagebox.showwarning("Warning", "No image selected.")

    def display_image(self):
        try:
            img = Image.open(self.image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)  # Use Resampling.LANCZOS for resizing
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def check_metadata(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return

        try:
            self.progress.start()
            self.metadata = self.format_metadata(self.image_path)
            self.display_metadata()
            self.progress.stop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read metadata: {str(e)}")
            self.progress.stop()

    def format_metadata(self, image_path):
        metadata = {}

        # EXIF Data
        try:
            with open(image_path, 'rb') as image_file:
                tags = exifread.process_file(image_file)
                metadata['Date and Time'] = tags.get('EXIF DateTimeOriginal', 'Not Available')
                metadata['Camera Model'] = tags.get('Image Model', 'Not Available')
                metadata['Device Name'] = tags.get('Image Make', 'Not Available')
                metadata['Software'] = tags.get('Image Software', 'Not Available')
                metadata['GPS Coordinates'] = self.get_gps_coordinates(tags)
        except Exception:
            metadata['EXIF Data'] = "No EXIF data found"

        # Additional Metadata Fields
        metadata['Checksum'] = self.calculate_checksum(image_path)
        metadata['File Name'] = os.path.basename(image_path)
        metadata['File Size'] = os.path.getsize(image_path)
        metadata['File Type'] = Image.open(image_path).format
        metadata['File Type Extension'] = os.path.splitext(image_path)[1].lower()
        metadata['MIME Type'] = Image.MIME[Image.open(image_path).format]

        img = Image.open(image_path)
        metadata['Image Width'] = img.width
        metadata['Image Height'] = img.height
        metadata['Bit Depth'] = getattr(img.info, 'bit', 'Not Available')  # Handle missing 'bit' attribute
        metadata['Color Type'] = img.mode
        metadata['RGB'] = "Yes" if img.mode == "RGB" else "No"
        metadata['Compression'] = img.info.get("compression", "Not Available")
        metadata['Filter'] = img.info.get("filter", "Not Available")
        metadata['Interlace'] = "Noninterlaced" if img.info.get("interlace") == 0 else "Interlaced"
        metadata['Image Size'] = f"{img.width}x{img.height}"
        metadata['Megapixels'] = round((img.width * img.height) / 1e6, 2)
        metadata['Category'] = "Image"

        return metadata

    def calculate_checksum(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def get_gps_coordinates(self, exif_data):
        if 'GPS GPSLatitude' in exif_data and 'GPS GPSLongitude' in exif_data:
            lat = self.convert_to_degrees(exif_data['GPS GPSLatitude'].values)
            lon = self.convert_to_degrees(exif_data['GPS GPSLongitude'].values)
            if exif_data['GPS GPSLatitudeRef'].values[0] != 'N':
                lat = -lat
            if exif_data['GPS GPSLongitudeRef'].values[0] != 'E':
                lon = -lon
            return lat, lon
        return None

    def convert_to_degrees(self, value):
        d = float(value[0].num) / float(value[0].den)
        m = float(value[1].num) / float(value[1].den)
        s = float(value[2].num) / float(value[2].den)
        return d + (m / 60.0) + (s / 3600.0)

    def display_metadata(self):
        self.metadata_display.config(state="normal")
        self.metadata_display.delete(1.0, tk.END)

        for key, value in self.metadata.items():
            if key == 'GPS Coordinates' and value:
                lat, lon = value
                self.metadata_display.insert(tk.END, f"{key}: https://www.google.com/maps?q={lat},{lon}\n")
            else:
                self.metadata_display.insert(tk.END, f"{key}: {value}\n")

        self.metadata_display.config(state="disabled")

    def remove_metadata(self):
        if not self.image_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return

        try:
            self.progress.start()
            image = Image.open(self.image_path)
            data = list(image.getdata())
            image_without_exif = Image.new(image.mode, image.size)
            image_without_exif.putdata(data)
            new_image_path = os.path.splitext(self.image_path)[0] + "_no_metadata" + os.path.splitext(self.image_path)[1]
            image_without_exif.save(new_image_path)
            messagebox.showinfo("Success", f"Metadata removed successfully. New image saved as {new_image_path}")
            self.progress.stop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove metadata: {str(e)}")
            self.progress.stop()

    def save_metadata(self):
        if not self.metadata:
            messagebox.showwarning("Warning", "No metadata available to save.")
            return

        file_types = [("Text File", "*.txt"), ("JSON File", "*.json")]
        file_path = filedialog.asksaveasfilename(title="Save Metadata", filetypes=file_types, defaultextension=".txt")

        if file_path:
            try:
                if file_path.endswith(".json"):
                    with open(file_path, 'w') as file:
                        json.dump(self.metadata, file, indent=4)
                else:
                    with open(file_path, 'w') as file:
                        for key, value in self.metadata.items():
                            if key == 'GPS Coordinates' and value:
                                lat, lon = value
                                file.write(f"{key}: https://www.google.com/maps?q={lat},{lon}\n")
                            else:
                                file.write(f"{key}: {value}\n")
                messagebox.showinfo("Success", f"Metadata saved as {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save metadata: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MetaDataFinderGUI(root)
    root.mainloop()