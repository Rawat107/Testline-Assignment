# Image Analysis and Segmentation Program

## Goal

The goal of this project is to build a program that separates text and visual elements from an image. It uses the Google Cloud Vision API for text extraction and OpenCV for segmenting visual elements. The extracted text and visual elements are then compiled into an HTML file.

## Technologies Used

- **Google Cloud Vision API**: For Optical Character Recognition (OCR) to extract text content from images.
- **OpenCV**: For image processing and segmenting visual elements.
- **Python**: The programming language used for implementing the solution.

## Usage

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install the Requirements

```sh
pip install -r requirements.txt
```

### 4. Set Up Google Cloud Vision API

1. **Enable the API**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing project.
   - Navigate to the "API & Services" dashboard.
   - Enable the "Vision API".

2. **Set Up Authentication**:
   - Create a service account key:
     - Go to "IAM & Admin" > "Service Accounts".
     - Create a new service account.
     - Grant it the "Project" > "Editor" role.
     - Create a key for the service account and download the JSON file.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your JSON key file:
     ```sh
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service_account_key.json"
     ```

### 5. Run the Program

```sh
python Testline Assignment.py
```

The program will prompt you to enter the image path. Enter the path to your image file, and the program will process the image to extract text and visual elements, then generate an HTML file with the results.

### 6. Output

- The program will create a directory for visual elements extracted from the image.
- An HTML file (`output.html`) will be generated with the visual elements and extracted text organized.

---
