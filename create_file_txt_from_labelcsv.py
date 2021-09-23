import pandas as pd

def file_create(dataframe_path, output_filename):
    data = pd.read_csv(dataframe_path)
    files = list(data["filename"])
    files = [f.split(".jpg")[0] for f in files]
    with open(output_filename, 'w') as f:
        for item in files:
            f.write("%s\n" % item)
    print("Done...")

file_create("val.csv", "val.txt")
