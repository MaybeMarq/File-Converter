# Welcome
Tired of using sketchy, poorly working websites to convert your files? File Convertor is a simple command-line python script used to convert almost any image file into a JPEG or a .docx document into a .pdf document.

**Note: Currently being rewritten in Rust to provide better cross-platform support as well as to streamline installation and utilization.**

![Screenshot of landing page for GUI (taken on Fedora - Gnome 44)](https://github.com/MaybeMarq/File-Converter/assets/62733985/9eebf3ed-a9d3-4e4e-98ca-0983e7de9d07)

## Dependencies
This project uses the following libraries:
- PIL - Image manipulation library
- tkinter - Python's GUI toolkit
- docx2pdf - Allows for the conversion from .docx to .pdf
- pillow-heif - Additional library for manipulating .heif images (default file type for images taken on an iPhone)

For required library installation instructions, refer to the documentation file.

## Features
- Can convert most images into a JPEG image
- Can convert a Word document (.docx) into a PDF

## User Privacy
This script makes use of Microsoft Office and LibreOffice for some functionality. Please look at their privacy policies for more information on how they use user data. No data regarding content of files, type of files, or current user is stored or shared with the maintainer of this script. 

## Supported Operating Systems
- Windows
- Linux

Note: may work on Mac OS however it is not officially supported.

## Prerequisites
- Must have a system that has either Microsoft Office or LibreOffice for .docx to .pdf conversion
- Must have a relatively current installation of Python (>3.0)

## Installation
Refer to the documentation file which goes into detail of installing python, the required dependencies, and this script.
