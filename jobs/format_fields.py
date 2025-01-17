from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp
import argparse
import sys

DATE_COLUMN_IDENTIFIER = "date"
RAW_DATE_FORMAT = "dd/mm/yyyy"


def main(source, destination):
    df = read_parquet(source)
    df = format_date_fields(df)
    write_parquet(df, destination)


def format_date_fields(df):
    date_columns = [
        column for column in df.columns if DATE_COLUMN_IDENTIFIER in column]

    for date_column in date_columns:
        df = df.withColumn(date_column, to_timestamp(
            date_column, RAW_DATE_FORMAT))

    return df


def read_parquet(source):
    spark = SparkSession.builder \
        .appName("sfc_data_engineering_csv_to_parquet") \
        .getOrCreate()

    df = spark.read.parquet(source)

    return df


def write_parquet(df, destination):
    df.write.parquet(destination)


def collect_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", help="A parquet file used as source input", required=True)
    parser.add_argument(
        "--destination", help="A destination directory for outputting parquet files", required=True)

    args, unknown = parser.parse_known_args()

    return args.source, args.destination


if __name__ == '__main__':
    print("Spark job 'format_fields' starting...")
    print(f"Job parameters: {sys.argv}")

    source, destination = collect_arguments()
    main(source, destination)

    print("Spark job 'format_fields' done")
