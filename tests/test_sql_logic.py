from sqlfluff.core import Linter

def test_sql_linting():
    # Configura o linter para o dialeto BigQuery
    linter = Linter(dialect="bigquery")
    
    # Caminho para o arquivo SQL
    sql_file_path = "scripts/cobranca_liquidacao_parc_acordo.sqlx"
    
    # Leia o código SQL do arquivo
    with open(sql_file_path, "r") as file:
        sql_code = file.read()

    # Execute o linting
    lint_result = linter.lint_string(sql_code)
    
    # Verifique se há erros
    assert not lint_result.get_violations(), f"Erros de linting encontrados: {lint_result.get_violations()}"
