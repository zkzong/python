import pandas as pd
import concurrent.futures


def read_csv(filename):
    df = pd.read_csv(filename)
    return df


filenames = ['file/example.csv', 'file/example.csv']

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(read_csv, filenames)
    for result in results:
        print(result)
