# usage: python3 get_info.py info_BP.csv gene_ID.csv output.csv
import sys
import csv

info_source=sys.argv[1]  # info_BP.csv
query_list= sys.argv[2]  # gene_ID.csv
out_file_name =  sys.argv[3]  # output.csv

#print(info_source,query_list)

# Transforming the given csv information into dictionary
info_dict={}

with open(info_source, 'r') as source:
    next(source)
    source_reader = csv.reader(source)
    for info_row in source_reader:
        info_gene_ids=info_row[1].split()  # Defense response, [AT1G12220 AT1G14780 AT1G48500 AT1G66100]
        #print (info_row[0],info_gene_ids[0])
        for gene in info_gene_ids:
            if gene in info_dict:
                info_dict[gene].append(info_row[0])
            else:
                info_dict[gene]=[info_row[0]]
        
#print(info_dict)

out_file = open(out_file_name, 'w')
out_file_err = open(out_file_name+"_no_info.csv", 'w')

# Appending the information from dictionary to input gene_ID

with open(query_list,'r') as query:
    next(query)
    query_reader=csv.reader(query)
    for query_row in query_reader:
        if query_row[0] in info_dict:
            unique_annotation = list(set(info_dict[query_row[0]]))
            out_file.write(query_row[0]+","+",".join(map(str, unique_annotation))+"\n")
        else:
            out_file_err.write(query_row[0]+"\n")
