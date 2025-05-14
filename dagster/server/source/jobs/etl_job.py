from dagster import job
from assets.my_asset import my_asset


@job
def etl_job():
    my_asset()
