# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"14GB.00","system":"readv2"},{"code":"36796.0","system":"readv2"},{"code":"25534.0","system":"readv2"},{"code":"96779.0","system":"readv2"},{"code":"105290.0","system":"readv2"},{"code":"98433.0","system":"readv2"},{"code":"61121.0","system":"readv2"},{"code":"93455.0","system":"readv2"},{"code":"98760.0","system":"readv2"},{"code":"68122.0","system":"readv2"},{"code":"92887.0","system":"readv2"},{"code":"102017.0","system":"readv2"},{"code":"99817.0","system":"readv2"},{"code":"65163.0","system":"readv2"},{"code":"11603.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('osteoporosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["osteoporosis-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["osteoporosis-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["osteoporosis-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
