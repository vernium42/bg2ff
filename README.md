# bq2ff
Save query from Bigquery to a flat-file - Great for pulling samples to work locally
## How to install bq2ff
### Create a virtual environment
```shell
python3 -m venv venv
```
### Install bq2ff
```shell
pip3 install google-cloud-bigquery
pip3 install git+https://github.com/vernium42/bq2ff.git
```

## Example
- Get a service account JSON file if you do not already have one that has access to Bigquery:

    https://cloud.google.com/docs/authentication/getting-started

- Run in a notebook or create a python file:
```python
from google.cloud import bigquery
from bq2ff import BQ2FF

client = bigquery.Client.from_service_account_json("bq_service_account.json")
bf = BQ2FF(client)
bf.export("""
SELECT *
FROM `bigquery-public-data.baseball.games_wide`
LIMIT 100
""", "baseball.csv", "csv", True)
```
##### TODO:
- Add comments to code.
