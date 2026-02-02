#!/bin/bash
# Creates a minimal Word document using bash and base64
# A .docx file is actually a ZIP archive containing XML files

# Create temporary directory structure
TMPDIR=$(mktemp -d)
cd "$TMPDIR"

# Create directory structure
mkdir -p _rels word

# Create [Content_Types].xml
cat > '[Content_Types].xml' << 'EOF'
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
    <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
    <Default Extension="xml" ContentType="application/xml"/>
    <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
EOF

# Create _rels/.rels
cat > '_rels/.rels' << 'EOF'
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
    <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
EOF

# Create word/document.xml
cat > 'word/document.xml' << 'EOF'
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
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
                <w:t>Test Title</w:t>
            </w:r>
        </w:p>
    </w:body>
</w:document>
EOF

# Create the ZIP archive (docx file)
zip -q -r "$OLDPWD/test_document.docx" .

# Cleanup
cd "$OLDPWD"
rm -rf "$TMPDIR"

echo "Successfully created test_document.docx with 'Test Title'"
