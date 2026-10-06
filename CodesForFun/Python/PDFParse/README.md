# PDF image extractor

A script that goes through every PDF in a folder and saves each embedded
image as its own file, in a subfolder named after the PDF.

It is the companion to the [Excel data automation tool](../ExcelParse): that
one pulls images out of spreadsheets, this one pulls them out of PDFs.

| File | Contents |
| --- | --- |
| `main.py` | Opens each PDF with PyMuPDF, walks through its pages, and writes out every image as `image<page>_<number>` |
| `*.pdf` and the image folder | Sample input and the output it produced |

The folder to process is set near the bottom of `main.py`. Progress is logged
to `newfile.log`.

Built with Python, PyMuPDF and Pillow.
