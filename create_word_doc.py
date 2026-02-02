#!/usr/bin/env python3
"""
Simple script to create a Word document with a test title.
Uses only Python standard library - no external dependencies required.
"""

import zipfile
from io import BytesIO

def create_word_document(filename='test_document.docx', title='Test Title'):
    """Create a Word document with a title using Office Open XML format."""

    # Office Open XML structure for a minimal Word document
    # [Content_Types].xml - defines content types
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

    # _rels/.rels - package relationships
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

    # word/document.xml - the actual document content
    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <w:p>
            <w:pPr>
                <w:pStyle w:val="Heading1"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:b/>
                    <w:sz w:val="32"/>
                </w:rPr>
                <w:t>{title}</w:t>
            </w:r>
        </w:p>
    </w:body>
</w:document>'''

    # Create the .docx file (which is actually a ZIP archive)
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        # Add [Content_Types].xml
        docx.writestr('[Content_Types].xml', content_types)

        # Add _rels/.rels
        docx.writestr('_rels/.rels', rels)

        # Add word/document.xml
        docx.writestr('word/document.xml', document)

    print(f"Successfully created {filename} with title: '{title}'")

if __name__ == '__main__':
    create_word_document()
