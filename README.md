**Extract information from GO file**

This python script will extract information about the BP, MF, CC information for the input gene_ID

# Gene Information Extractor

This repository contains a Python script for extracting gene information from a given dataset. The script takes two CSV files as input: one containing gene information and another containing a list of gene IDs to query. It then outputs the corresponding gene annotations for each gene ID.

## Prerequisites

- Python 3

## Usage

```
python3 get_info.py info_BP.csv gene_ID.csv output.csv
```

- `info_BP.csv`: CSV file containing gene information with annotations.
- `gene_ID.csv`: CSV file containing a list of gene IDs to query.
- `output.csv`: Output file to store the gene annotations.


## Code Improvement

The code has been improved with the following changes:

- Modularized the code into functions for better readability and reusability.
- Used the `csv` module for reading and writing CSV files.
- Ensured proper file handling using the `with` statement.
- Added error handling for incorrect command-line arguments.
- Created separate functions for transforming the CSV information into a dictionary and processing the query list.
- Utilized the `setdefault` method to simplify dictionary initialization.

## License

This project is licensed under the [MIT License](LICENSE).


Feel free to modify the README file according to your needs and add any additional information about the project or usage instructions.
