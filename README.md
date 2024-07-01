## OCR sample program with m3, macOS 14.5, Python 3.10.14

### CLI (`img_to_text.py` on terminal)

1. Set image files in `source` directory.
2. Run `python3 img_to_text.py`
3. Conversion result is in the `result` directory.)

#### GUI (Web) (`http://[hostname]:5001/`)

1. Run `python3 front_web.py`
1. Run browser and input `http://[hostname]:5001/` to address bar.
1. Upload image file to web, and start conversion.
1. Conversion result is on the Web.

### Installation instructions:
#### for macOS:
  1. Install homebrew (https://brew.sh/ja/)
  1. brew install python@3.10
  1. pip3 install pillow 
  1. pip3 install opencv-python
  1. pip3 install pyocr

#### for Windows:
  1. pip3 install pillow 
  1. pip3 install opencv-python
  1. pip3 install pyocr
  1. Install tesseract (https://github.com/UB-Mannheim/tesseract/wiki)
