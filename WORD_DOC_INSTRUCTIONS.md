# Word Document Generation Instructions

This directory contains scripts to generate a Word document with a "Test Title" heading.

## Quick Start

Run either of these commands:

```bash
python3 generate_doc.py
```

OR

```bash
python3 create_docx.py
```

Both will create `test_document.docx` in the current directory.

## What Each Script Does

### generate_doc.py (Recommended)
Uses the python-docx library (already installed in the workflow) to create a clean, properly formatted Word document.

```python
from docx import Document
doc = Document()
doc.add_heading('Test Title', level=0)
doc.save('test_document.docx')
```

### create_docx.py
Creates a Word document using only Python's standard library (zipfile). This manually constructs the Office Open XML format.

## Requirements

- Python 3.x
- For `generate_doc.py`: python-docx library (`pip install python-docx`)
- For `create_docx.py`: No external dependencies (uses only zipfile from standard library)

## Output

Both scripts create: **test_document.docx**

The document contains a single title heading: "Test Title"
