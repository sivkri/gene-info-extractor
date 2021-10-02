**Extract information from GO file**

This python script will extract information about the BP, MF, CC information for the input gene_ID

Requirement: Linux and python3. Both gene_ID and GO information must be in csv format

**usage**

python3 get_info_GO_file.py go_information.csv gene_ID.csv result.csv

_Step1_: Convert the given go_information file into a dictionary format

_Step2_: vlookup the information for the given gene_ID from the dictionary and provide both mapped and unmapped information
