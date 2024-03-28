#Py script for comparing between a list of IP's to a log in csv.

import csv
def compare_ips():
    txt_file = "C:/Users/razr/Downloads/test.txt"  # Replace with your text file path
    csv_file = "C:/Users/razr/Downloads/acc1.csv"  # Replace with your CSV file path

    txt_ips = set()
    with open(txt_file, "r") as file:
        txt_ips.update(line.strip() for line in file)

    csv_ips = set()
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                if cell.strip():
                    csv_ips.add(cell.strip())
           

    # Find matches and differences
    matches = txt_ips.intersection(csv_ips)
    differences = txt_ips.difference(csv_ips)

    print("Matching IPs in the Access logs:")
    for ip in matches:
        print(ip)

    print("\nIPs in TXT file but not in CSV:")
    for ip in differences:
        print(ip)

if __name__ == "__main__":
    compare_ips()
