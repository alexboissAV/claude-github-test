#!/usr/bin/env python3
"""
Generate a Word document with a test title.

This script creates a proper .docx file (Office Open XML format) without
requiring the python-docx library. It manually creates the XML structure
and packages it as a ZIP file with .docx extension.
"""

import zipfile
import os
from datetime import datetime

def create_word_document(filename='test_document.docx', title='Test Title'):
    """Create a Word document with the specified title."""

    # Define the XML content for various parts of the document

    # [Content_Types].xml - defines the content types
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
    <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
    <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

    # _rels/.rels - defines relationships
    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
    <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
    <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

    # word/document.xml - main document content with title
    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <w:p>
            <w:pPr>
                <w:pStyle w:val="Title"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:b/>
                    <w:sz w:val="56"/>
                </w:rPr>
                <w:t>{title}</w:t>
            </w:r>
        </w:p>
    </w:body>
</w:document>'''

    # docProps/core.xml - document properties
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    core = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <dc:title>{title}</dc:title>
    <dc:creator>Claude</dc:creator>
    <cp:lastModifiedBy>Claude</cp:lastModifiedBy>
    <dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
    <dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''

    # docProps/app.xml - application properties
    app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
    <Application>Claude Code</Application>
    <DocSecurity>0</DocSecurity>
    <ScaleCrop>false</ScaleCrop>
    <Company></Company>
    <LinksUpToDate>false</LinksUpToDate>
    <SharedDoc>false</SharedDoc>
    <HyperlinksChanged>false</HyperlinksChanged>
    <AppVersion>1.0</AppVersion>
</Properties>'''

    # Create the .docx file (which is a ZIP archive)
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as docx:
        # Write all the XML files
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', rels)
        docx.writestr('word/document.xml', document)
        docx.writestr('docProps/core.xml', core)
        docx.writestr('docProps/app.xml', app)

    print(f"✓ Word document '{filename}' created successfully!")
    print(f"  Title: {title}")
    print(f"  Size: {os.path.getsize(filename)} bytes")

if __name__ == '__main__':
    create_word_document()
