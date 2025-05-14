from dagster import ScheduleDefinition
from jobs.etl_job import etl_job


etl_schedule = ScheduleDefinition(
    job=etl_job,
    cron_schedule="*/15 * * * *",  # Executa a cada 15 minutos
    description="Executa o ETL Meltano a cada 15 minutos.",
)
