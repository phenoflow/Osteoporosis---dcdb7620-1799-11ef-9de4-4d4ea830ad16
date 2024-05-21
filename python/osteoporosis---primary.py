# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"N330D00","system":"readv2"},{"code":"N330400","system":"readv2"},{"code":"N330.00","system":"readv2"},{"code":"N330100","system":"readv2"},{"code":"N330A00","system":"readv2"},{"code":"N330C00","system":"readv2"},{"code":"N330z00","system":"readv2"},{"code":"45736.0","system":"readv2"},{"code":"57301.0","system":"readv2"},{"code":"40428.0","system":"readv2"},{"code":"33526.0","system":"readv2"},{"code":"16857.0","system":"readv2"},{"code":"42354.0","system":"readv2"},{"code":"62702.0","system":"readv2"},{"code":"39334.0","system":"readv2"},{"code":"48772.0","system":"readv2"},{"code":"31580.0","system":"readv2"},{"code":"96342.0","system":"readv2"},{"code":"39217.0","system":"readv2"},{"code":"27597.0","system":"readv2"},{"code":"68019.0","system":"readv2"},{"code":"102730.0","system":"readv2"},{"code":"93981.0","system":"readv2"},{"code":"4013.0","system":"readv2"},{"code":"93497.0","system":"readv2"},{"code":"5841.0","system":"readv2"},{"code":"277.0","system":"readv2"},{"code":"16307.0","system":"readv2"},{"code":"3346.0","system":"readv2"},{"code":"34798.0","system":"readv2"},{"code":"41755.0","system":"readv2"},{"code":"38395.0","system":"readv2"},{"code":"19048.0","system":"readv2"},{"code":"9700.0","system":"readv2"},{"code":"11503.0","system":"readv2"},{"code":"12673.0","system":"readv2"},{"code":"25650.0","system":"readv2"},{"code":"36432.0","system":"readv2"},{"code":"93705.0","system":"readv2"},{"code":"24093.0","system":"readv2"},{"code":"18825.0","system":"readv2"},{"code":"93655.0","system":"readv2"},{"code":"70349.0","system":"readv2"},{"code":"17377.0","system":"readv2"},{"code":"46894.0","system":"readv2"},{"code":"14967.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('osteoporosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["osteoporosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["osteoporosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["osteoporosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
