from dagster import (
    asset,
    MonthlyPartitionsDefinition,
    Output,
    AssetObservation,
    MetadataValue,
)

# Configurar particionamento mensal
partitions_def = MonthlyPartitionsDefinition(start_date="2023-01-01")


@asset(partitions_def=partitions_def)
def fetch_monthly_data(context):
    # Obter a chave da partição atual
    partition_key = context.asset_partition_key_for_output()
    context.log.info(f"Processando partição mensal: {partition_key}")

    # Calcular o intervalo de datas da partição
    # Data inicial do mês
    start_date = partition_key
    # Data inicial do próximo mês
    end_date = partitions_def.get_next_partition_key(start_date)

    context.log.info(
        f"Buscando dados de {start_date} até {end_date} (não inclusivo)",
    )

    # Simular busca de dados para o mês
    new_data = [
        {"id": i, "value": f"data-{i}", "date": start_date} for i in range(1, 6)
    ]

    row_count = len(new_data)

    # Adicionar eventos personalizados para observabilidade
    context.log_asset_observation(
        AssetObservation(
            asset_key="fetch_monthly_data",
            metadata={
                "partition_key": partition_key,
                "row_count": row_count,
                "start_date": MetadataValue.text(start_date),
                "end_date": MetadataValue.text(end_date),
            },
            description=f"Dados observados para a partição {partition_key}",
        )
    )

    # Materializar o asset com metadados
    return Output(
        value=new_data,
        metadata={
            "row_count": len(new_data),
            "partition_start_date": start_date,
            "partition_end_date": end_date,
        },
    )
