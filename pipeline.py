import sys
import pandas as pd




print('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_messenger": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output_{month}.parquet")


print(f'hello pipeline, month={month}')

# docker run -it --rm \
#   -e POSTGRES_USER="root" \
#   -e POSTGRES_PASSWORD="root" \
#   -e POSTGRES_DB="taxi_zone" \
#   -v taxi_zone_postgres_data:/var/lib/postgresql \
#   -p 5432:5432 \
#   postgres:18