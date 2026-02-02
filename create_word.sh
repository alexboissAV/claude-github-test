#!/bin/bash
# Create a Word document using Python standard library

cat > /tmp/make_docx.py << 'PYTHON_SCRIPT'
import zipfile

document_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:body>
        <w:p>
            <w:pPr>
                <w:jc w:val="center"/>
            </w:pPr>
            <w:r>
                <w:rPr>
                    <w:b/>
                    <w:sz w:val="48"/>
                </w:rPr>
                <w:t>Test Title</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:r>
                <w:t>This is a test Word document created by Claude.</w:t>
            </w:r>
        </w:p>
        <w:p>
            <w:r>
                <w:t>Document generated on: 2026-02-02</w:t>
            </w:r>
        </w:p>
    </w:body>
</w:document>'''

content_types_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

rels_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

with zipfile.ZipFile('test_document.docx', 'w', zipfile.ZIP_DEFLATED) as docx:
    docx.writestr('[Content_Types].xml', content_types_xml)
    docx.writestr('_rels/.rels', rels_xml)
    docx.writestr('word/document.xml', document_xml)

print('Document created successfully')
PYTHON_SCRIPT

python3 /tmp/make_docx.py
