from dagster import asset


@asset(
    description="Retorna uma lista de inteiros.",
    compute_kind="dbt",
    group_name="educorp",
)
def my_asset(
) -> list[int]:
    data = [1, 2, 3]
    data = [x * 2 for x in data]
    return data
