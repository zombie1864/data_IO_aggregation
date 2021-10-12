import os 
import pytest 
from click.testing import CliRunner
from module_two.fetch_one import main
import pathlib
parent_path = os.path.dirname(os.getcwd())  


def test_main_facility_id():
    runner = CliRunner()
    with runner.isolated_filesystem():
        file_path = pathlib.Path(parent_path) / 'module_two' / 'project_data' / 'facility_0.json'
        facility_id = '0'
        result = runner.invoke(main, [facility_id])
        assert result.exit_code == 0
        assert file_path.exists() is True 
        os.remove(file_path)
     

def test_(fetch_one_output):
    runner = CliRunner()
    result = runner.invoke(main,['0'])
    file_path = pathlib.Path(parent_path) / 'module_two' / 'project_data' / 'facility_0.json'
    assert result.output == fetch_one_output
    os.remove(file_path)