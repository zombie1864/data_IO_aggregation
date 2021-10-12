import os 
import pytest 
import pathlib
from click.testing import CliRunner
from module_two.fetch_many import main
parent_path = os.path.dirname(os.getcwd())  

def test_main_keyword():
    runner = CliRunner()
    file_path = pathlib.Path(parent_path) / 'module_two' / 'project_data' / 'result.json'
    keyword = 'sqft_gte=99000'
    result = runner.invoke(main, ['-kw',keyword])
    assert result.exit_code == 0 
    assert file_path.exists() is True 
    os.remove(file_path)


def test_(fetch_many_output):
    runner = CliRunner()
    keyword = 'sqft_gte=99000'
    result = runner.invoke(main, ['-kw',keyword])
    assert result.output == fetch_many_output
    file_path = pathlib.Path(parent_path) / 'module_two' / 'project_data' / 'result.json'
    os.remove(file_path)