import pytest
import json
import subprocess
import os

# Load the sample JSON structure
data = {
    "name": "interpreter",
    "size": 4096,
    "time_modified": 1699957865,
    "permissions": "-rw-r--r--",
    "contents": [
        {"name": ".gitignore", "size": 8911, "time_modified": 1699941437, "permissions": "drwxr-xr-x"},
        {"name": "LICENSE", "size": 1071, "time_modified": 1699941437, "permissions": "drwxr-xr-x"},
        {"name": "README.md", "size": 83, "time_modified": 1699941437, "permissions": "drwxr-xr-x"},
        {"name": "ast", "size": 4096, "time_modified": 1699957739, "permissions": "-rw-r--r--", "contents": [
            {"name": "go.mod", "size": 225, "time_modified": 1699957780, "permissions": "-rw-r--r--"},
            {"name": "ast.go", "size": 837, "time_modified": 1699957719, "permissions": "drwxr-xr-x"}
        ]},
        {"name": "go.mod", "size": 60, "time_modified": 1699950073, "permissions": "drwxr-xr-x"},
        {"name": "lexer", "size": 4096, "time_modified": 1699955487, "permissions": "drwxr-xr-x", "contents": [
            {"name": "lexer_test.go", "size": 1729, "time_modified": 1699955126, "permissions": "drwxr-xr-x"},
            {"name": "go.mod", "size": 227, "time_modified": 1699944819, "permissions": "-rw-r--r--"},
            {"name": "lexer.go", "size": 2886, "time_modified": 1699955487, "permissions": "drwxr-xr-x"}
        ]},
        {"name": "main.go", "size": 74, "time_modified": 1699950453, "permissions": "-rw-r--r--"},
        {"name": "parser", "size": 4096, "time_modified": 1700205662, "permissions": "drwxr-xr-x", "contents": [
            {"name": "parser_test.go", "size": 1342, "time_modified": 1700205662, "permissions": "drwxr-xr-x"},
            {"name": "parser.go", "size": 1622, "time_modified": 1700202950, "permissions": "-rw-r--r--"},
            {"name": "go.mod", "size": 533, "time_modified": 1699958000, "permissions": "drwxr-xr-x"}
        ]},
        {"name": "token", "size": 4096, "time_modified": 1699954070, "permissions": "-rw-r--r--", "contents": [
            {"name": "token.go", "size": 910, "time_modified": 1699954070, "permissions": "-rw-r--r--"},
            {"name": "go.mod", "size": 66, "time_modified": 1699944730, "permissions": "drwxr-xr-x"}
        ]}
    ]
}

# Path to the test JSON file
TEST_JSON_PATH = os.path.join(os.path.dirname(__file__), 'data.json')


@pytest.fixture(scope="module", autouse=True)
def setup_test_json():
    with open(TEST_JSON_PATH, 'w') as f:
        json.dump(data, f)
    yield
    os.remove(TEST_JSON_PATH)


def run_pyls_command(args):
    result = subprocess.run(
        ['python', '-m', 'pyls'] + args,
        capture_output=True,
        text=True
    )
    print(result)
    return result.stdout.strip(), result.stderr.strip()


def test_ls():
    stdout, _ = run_pyls_command([])
    assert stdout == "LICENSE README.md ast go.mod lexer main.go parser token"


def test_ls_A():
    stdout, _ = run_pyls_command(['-A'])
    assert stdout == ".gitignore LICENSE README.md ast go.mod lexer main.go parser token"


def test_ls_l():
    stdout, _ = run_pyls_command(['-l'])
    assert "LICENSE" in stdout
    assert "README.md" in stdout
    assert "ast" in stdout


def test_ls_l_r():
    stdout, _ = run_pyls_command(['-l', '-r'])
    expected_order = ["token", "parser", "main.go", "lexer", "go.mod", "ast", "README.md", "LICENSE"]
    output_files = [line.split()[-1] for line in stdout.splitlines()]
    assert output_files == expected_order


def test_ls_l_r_t():
    stdout, _ = run_pyls_command(['-l', '-r', '-t'])
    expected_order = ["parser", "ast", "lexer", "token", "main.go", "go.mod", "README.md", "LICENSE"]
    output_files = [line.split()[-1] for line in stdout.splitlines()]
    assert output_files == expected_order


def test_ls_l_r_t_filter_dir():
    stdout, _ = run_pyls_command(['-l', '-r', '-t', '--filter=dir'])
    expected_order = ["parser", "ast", "lexer", "token"]
    output_dirs = [line.split()[-1] for line in stdout.splitlines()]
    assert output_dirs == expected_order


def test_ls_l_r_t_filter_file():
    stdout, _ = run_pyls_command(['-l', '-r', '-t', '--filter=file'])
    expected_order = ["main.go", "go.mod", "README.md", "LICENSE"]
    output_files = [line.split()[-1] for line in stdout.splitlines()]
    assert output_files == expected_order


def test_ls_with_path():
    stdout, _ = run_pyls_command(['-l', 'parser'])

    assert "parser" in stdout
    assert "go.mod" in stdout


def test_ls_human_readable():
    stdout, _ = run_pyls_command(['-l', 'parse'])
    assert "4.0K" in stdout  # For parser.go


def test_ls_help():
    stdout, _ = run_pyls_command(['--help'])
    assert "usage:" in stdout
    assert "options:" in stdout
