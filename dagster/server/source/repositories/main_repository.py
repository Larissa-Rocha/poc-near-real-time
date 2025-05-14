from dagster import Definitions, load_assets_from_package_module

import assets
from jobs.etl_job import etl_job
from schedules.etl_schedule import etl_schedule


all_assets = load_assets_from_package_module(assets)

defs = Definitions(
    jobs=[etl_job],
    schedules=[etl_schedule],
    assets=all_assets,
)
