# Excel Data Automation Tool

Two Python scripts that automate quality checks on Excel workbooks of image
alt-text, one workbook per book chapter. Each row describes one figure:
chapter, page number, caption, thumbnail, a short alt text and a long alt text.

Checking these by hand means opening every workbook and reading every row.
The scripts do it in one run and mark the problems in the workbook itself.

## What it does

**`mainXL.py`: quality checker**

- Flags rows with a missing chapter name or page number
- Flags short alt text that is empty or longer than 200 characters
- Flags alt text that contains the word "ChatGPT" (pasted-in AI output)
- Writes each flag into a spare column and fills the cell red, so the
  problem rows are visible when the workbook is opened
- Replaces the Category column with a live Excel formula that classifies
  each figure as Simple, Moderate or Complex from its long alt-text length
- Ignores trailing blank rows when working out where the data ends
- Writes a summary workbook with the Simple / Moderate / Complex count
  for every chapter

**`main.py`: template builder and image extractor**

- Adds borders, centring and text wrapping to every cell
- Turns the two length columns into live `=LEN()` formulas
- Clears the remaining data columns to leave a blank template
- Saves every embedded thumbnail image as a PNG

`main.py` overwrites the workbooks it processes, so run it on a copy.

## Running it

```bash
pip install -r requirements.txt

# check every .xlsx in a folder and write the summary next to it
python mainXL.py path/to/folder

# format the workbooks in a folder and extract their images
python main.py path/to/folder
```

With no argument, `mainXL.py` uses the `9780323901086/` sample folder and
`main.py` uses this folder. Progress is logged to `newfile.log`.

## Expected columns

`Chapter Name/Number`, `Page Number`, `Category`, `Short Alt Text`,
`Long Alt Text`. Other columns are left alone by the checker.

## Built with

Python, openpyxl, openpyxl-image-loader
