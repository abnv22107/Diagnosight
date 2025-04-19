# Diagnosight : A Medical Image Analysis Report Generator 🩺

## Overview
The **Diagnosight** is a web application built with **Streamlit** that uses advanced **AI-based image analysis** to generate diagnostic reports for medical images such as X-rays, MRIs, and CT scans. The application leverages the **Gemini AI model** to analyze medical images and produce detailed reports, including observations, potential findings, and clinical recommendations.

## Features
- Upload and analyze **medical images** (supports PNG, JPG, JPEG formats).
- **Generate diagnostic reports** based on image content (X-ray, MRI, CT scan).
- Detailed analysis including observations, findings, and recommendations.
- **Downloadable report** in **text format** for easy access.
- Built with **Streamlit** for interactive web-based interface.

## Technologies
- **Streamlit**: For building the web interface.
- **Google Gemini AI**: For generating diagnostic reports from images.
- **Python**: The core programming language for backend logic.
- **Pillow (PIL)**: For image handling and conversions.
- **io**: To handle byte data conversion for images.

## Prerequisites
- Python 3.7 or higher.
- **API key** from **Google Cloud** for accessing the **Gemini AI** model.

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/medical-image-report-generator.git
cd medical-image-report-generator
```

### Step 2: Install Dependencies
Ensure you have **Python 3.7+** installed. Then install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 3: API Key Configuration
1. Get your **Google Cloud API key** from the [Google Cloud Console](https://console.cloud.google.com/).
2. Save the API key as `api_key.py` in the root directory. The file should look like this:
   ```python
   api_key = 'YOUR_API_KEY'
   ```

### Step 4: Run the Application
Run the Streamlit app locally:

```bash
streamlit run app.py
```

Open the app in your browser at `http://localhost:8501`.

## Usage
1. Upload a medical image (X-ray, MRI, CT scan, etc.) using the **Upload Medical Image** button.
2. Click **Generate Report** to analyze the image and generate a detailed diagnostic report.
3. After processing, the report will be displayed on the page. You can download the report as a `.txt` file.

## Example Usage
- Upload an image of an X-ray, MRI, or CT scan.
- Click the "Generate Report" button to analyze the image.
- The app will generate a text report with potential findings and clinical recommendations.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contributing
We welcome contributions! If you'd like to improve or extend the project, feel free to fork the repo and create a pull request. You can also report bugs or suggest features via the Issues section.
