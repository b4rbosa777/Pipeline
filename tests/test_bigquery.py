from google.cloud import bigquery

client = bigquery.Client()

def test_table_existence():
    dataset_id = "integracaohomologado.corp_gestao_processamento"
    table_id = "cobranca_liquidacao_parc_acordo"
    table_ref = f"{dataset_id}.{table_id}"
    
    try:
        table = client.get_table(table_ref)
        assert table is not None, f"Table {table_id} does not exist in dataset {dataset_id}."
    except Exception as e:
        assert False, f"Error checking table existence: {e}"

def test_query_execution():
    query = """
    SELECT COUNT(*) AS row_count
    FROM `integracaohomologado.corp_gestao_processamento.cobranca_liquidacao_parc_acordo`
    """
    result = client.query(query).result()
    row = list(result)[0]
    assert row.row_count > 0, "Table contains no rows."
