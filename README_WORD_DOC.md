# Word Document Generator

This repository contains a Python script to generate a Word document (.docx) with a test title.

## Usage

Run the script to generate the Word document:

```bash
python3 generate_word_doc.py
```

This will create a file named `test_document.docx` in the current directory with "Test Title" as the heading.

## Requirements

- Python 3.x (no additional libraries required - uses only standard library)

## What it does

The script creates a properly formatted Microsoft Word document (.docx file) using the Office Open XML format. The document contains a title heading styled appropriately.

## Files

- `generate_word_doc.py` - Main script to generate the Word document
- `create_doc.py` - Alternative script using python-docx library (requires installation)
