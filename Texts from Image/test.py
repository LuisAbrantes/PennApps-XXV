from ocrmac import ocrmac
annotations = ocrmac.OCR('test.png').recognize()
print(annotations)