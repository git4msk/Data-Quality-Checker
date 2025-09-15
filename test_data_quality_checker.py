import pytest
from data_quality_tool.data_quality_checker import check_data_quality

# Create a simple dummy CSV file for testing
@pytest.fixture
def dummy_csv_file(tmp_path):
    """Creates a temporary CSV file with known data for testing."""
    content = "col1,col2,col3\n1,2,3\n4,,6\n7,8,9\n1,2,3"
    file_path = tmp_path / "test_data.csv"
    with open(file_path, "w") as f:
        f.write(content)
    return file_path

def test_missing_values(capsys, dummy_csv_file):
    """Test that the tool correctly identifies missing values."""
    check_data_quality(dummy_csv_file)
    captured = capsys.readouterr()
    assert "Missing Values per Column:" in captured.out
    assert "col2" in captured.out

def test_duplicate_rows(capsys, dummy_csv_file):
    """Test that the tool correctly identifies duplicate rows."""
    check_data_quality(dummy_csv_file)
    captured = capsys.readouterr()
    assert "Duplicate Rows:" in captured.out
    assert "Found 1 duplicate rows." in captured.out