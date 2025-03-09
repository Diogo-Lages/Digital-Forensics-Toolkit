# Digital-Forensics-Toolkit

Toolkit for digital forensics. This tool helps extract, analyze, and manipulate metadata from various file types, detect suspicious patterns, and perform advanced file operations.

## Features
- **Metadata Extraction**: Extract detailed metadata from images, documents, audio, video, and other file types.
- **Batch Processing**: Process multiple files at once to save time.
- **Export Options**: Save metadata in JSON, CSV, XML, HTML, or plain text formats.
- **File Preview**: View binary previews and entropy analysis for files.
- **Suspicious Pattern Detection**: Identify potential threats like hidden scripts, passwords, or email addresses.
- **File Signature Spoofing**: Modify file headers for testing purposes.
- **PDF JavaScript Injection**: Inject custom JavaScript into PDFs (educational use only).
- **Metadata Removal**: Strip metadata from files while preserving their usability.
- **Comparison Tool**: Compare metadata between two files to identify differences and similarities.
- **Customizable Themes**: Switch between light and dark themes for better usability.

## Requirements
- Python 3.x
- Required Libraries: `tkinter`, `reportlab`, `python-magic`, `hashlib`, `Pillow`, `matplotlib`
- Operating System: Windows, macOS, or Linux

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Diogo-Lages/Digital-Forensics-Toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Digital-Forensics-Toolkit
   ```
3. Run the application:
   ```bash
   python digital_forensics_toolkit.py
   ```

## Usage
1. Launch the application by running `digital_forensics_toolkit.py`.
2. Use the intuitive GUI to upload files and select the desired operation:
   - Extract metadata
   - Compare files
   - Remove metadata
   - Spoof file signatures
   - Inject JavaScript into PDFs
3. Export results in your preferred format (JSON, CSV, XML, etc.).
4. Customize the theme (light/dark mode) via the settings menu.

## Code Structure
The project is organized into the following modules:
- **`AppConfig`**: Handles application configuration and user preferences.
- **`MetadataExtractor`**: Extracts and processes metadata from files.
- **`FileProcessor`**: Performs batch processing and file operations.
- **`PDFInjector`**: Injects JavaScript into PDFs for testing purposes.
- **`SignatureSpoof`**: Modifies file headers to test forensic tools.
- **`UIComponents`**: Implements the graphical user interface using `tkinter`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
