# Metadata Finder

A Python-based GUI tool to extract, view, and remove metadata from images. Supports common image formats and provides detailed information such as EXIF data, GPS coordinates, file size, checksum, and more.

---

## Installation

1. **Clone the Repository:**
   Download or clone the repository containing the `metadata_finder.py` script.

2. **Install Required Libraries:**
   Ensure you have Python 3.x installed on your system. Then, install the required libraries using pip:
   ```bash
   pip install pillow exifread
   ```

   - **Pillow**: For image processing.
   - **ExifRead**: For reading EXIF metadata.

3. **Run the Program:**
   Execute the script using Python:
   ```bash
   python metadata_finder.py
   ```

---

## Usage

1. **Upload an Image:**
   - Click the "Upload Image" button to select an image file (supported formats: JPG, JPEG, PNG, GIF, BMP).

2. **Check Metadata:**
   - Click the "Check Metadata" button to extract and display the metadata of the uploaded image.

3. **Remove Metadata:**
   - Click the "Remove Metadata" button to strip all metadata from the image and save it as a new file.

4. **Save Metadata:**
   - Click the "Save Metadata" button to save the extracted metadata in either `.txt` or `.json` format.

---

## Features

- Extract detailed metadata such as EXIF data, GPS coordinates, file size, checksum, and more.
- Remove metadata from images and save them as new files.
- Save extracted metadata in `.txt` or `.json` format.
- User-friendly GUI with a dark theme.
- Real-time progress indicator for metadata extraction and removal processes.

---

## Example Output

### Metadata Display:
```
Date and Time: 2023:01:01 12:00:00
Camera Model: Canon EOS R5
GPS Coordinates: https://www.google.com/maps?q=40.7128,-74.0060
Checksum: d41d8cd98f00b204e9800998ecf8427e
File Name: example.jpg
File Size: 123456 bytes
File Type: JPEG
Image Width: 1920
Image Height: 1080
Bit Depth: 8
Color Type: RGB
Compression: Not Available
Interlace: Noninterlaced
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
