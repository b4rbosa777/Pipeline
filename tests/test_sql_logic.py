from sqlfluff import Linter

def test_sql_linting():
    linter = Linter(dialect="bigquery")
    with open("scripts/cobranca_liquidacao_parc_acordo.sqlx", "r") as file:
        sql_code = file.read()

    lint_result = linter.lint_string(sql_code)
    assert lint_result.violations == [], f"SQL linting errors: {lint_result.violations}"
