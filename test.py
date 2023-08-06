import pandas as pd


data = "./data-raw/SGD_features.tab"
column_names = ["SGDID", "FEATURE_TYPE", "FEATURE_QUALIFIER", "FEATURE_NAME",
                "STANDARD_GENE_NAME", "ALIAS", "PARENT_FEATURE_NAME",
                "SECONDARY_SGDID", "CHROMOSOME", "START_COORDINATE",
                "STOP_COORDINATE", "STRAND", "GENETIC_POSITION",
                "COORDINATE_VERSION", "SEQUENCE_VERSION", "DESCRIPTION"]


def run():
    df = pd.read_csv(data, sep="\t")
    df.columns = column_names
    with open("./data/SGD_features.csv", "wb") as csv_file:
        df.to_csv(csv_file, index=False)


if __name__ == '__main__':
    run()
