import csv

# Input and output file names
input_file = "sentences-copy.tsv"
output_file = "sentences-no-duplicates.tsv"

# Dictionary to store unique rows based on the first column
unique_rows = {}

# Read the input file and filter duplicates
with open(input_file, "r", encoding="utf-8") as infile:
    tsv_reader = csv.reader(infile, delimiter="\t")
    for row in tsv_reader:
        # Use the first column as the key to detect duplicates
        key = row[0]
        if key not in unique_rows:
            unique_rows[key] = row

# Write the unique rows to the output file
with open(output_file, "w", encoding="utf-8", newline="") as outfile:
    tsv_writer = csv.writer(outfile, delimiter="\t")
    for row in unique_rows.values():
        tsv_writer.writerow(row)