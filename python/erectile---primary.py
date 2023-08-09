# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"1D1B.00","system":"readv2"},{"code":"E227311","system":"readv2"},{"code":"102274.0","system":"med"},{"code":"103966.0","system":"med"},{"code":"106360.0","system":"med"},{"code":"12066.0","system":"med"},{"code":"12790.0","system":"med"},{"code":"12867.0","system":"med"},{"code":"17639.0","system":"med"},{"code":"17894.0","system":"med"},{"code":"3838.0","system":"med"},{"code":"710.0","system":"med"},{"code":"94343.0","system":"med"},{"code":"94821.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('erectile-dysfunction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["erectile---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["erectile---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["erectile---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
