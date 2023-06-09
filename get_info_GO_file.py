# usage: python3 get_info.py info_BP.csv gene_ID.csv output.csv       
import sys
import csv

# Transforming the given csv information into dictionary
def transform_csv_to_dict(info_source):
    info_dict = {}
    with open(info_source, 'r') as source:
        next(source)
        source_reader = csv.reader(source)
        for info_row in source_reader:
            info_gene_ids = info_row[1].split()
            for gene in info_gene_ids:
                info_dict.setdefault(gene, []).append(info_row[0])
    return info_dict

# Appending the information from dictionary to input gene_ID

def process_query(info_dict, query_list, out_file_name):
    with open(query_list, 'r') as query, open(out_file_name, 'w') as out_file, open(out_file_name+"_no_info.csv", 'w') as out_file_err:
        next(query)
        query_reader = csv.reader(query)
        for query_row in query_reader:
            gene_id = query_row[0]
            if gene_id in info_dict:
                unique_annotation = set(info_dict[gene_id])
                out_file.write(gene_id + "," + ",".join(unique_annotation) + "\n")
            else:
                out_file_err.write(gene_id + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 get_info.py info_BP.csv gene_ID.csv output.csv")
        sys.exit(1)

    info_source=sys.argv[1]  # info_BP.csv
    query_list= sys.argv[2]  # gene_ID.csv
    out_file_name =  sys.argv[3]  # output.csv

    info_dict = transform_csv_to_dict(info_source)
    process_query(info_dict, query_list, out_file_name)
