from typer.testing import CliRunner
from cashflow_13week.cli import app

runner = CliRunner()

def test_hello():
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "installed and ready" in result.stdout.lower()
