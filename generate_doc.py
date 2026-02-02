from docx import Document

# Create a new Document
doc = Document()

# Add a title
doc.add_heading('Test Title', level=0)

# Save the document
doc.save('test_document.docx')

print('Word document created: test_document.docx')
