# Python Async Programming Interview Test (unittest workflow)

This repository contains a short Python async programming test used in interviews. The project has been reorganized so each question is implemented in its own module and validated using `unittest` test cases.

Keep changes minimal and implement answers inside the files under `src/questions/`.

## Project layout

- `src/questions/` — contains one file per question (for example `q_1.py`, `q_2.py`, ...). Implement the required functions/classes in these files.
- `testing/` — unit tests written with the standard `unittest` framework. Each file is named `test_qN.py` and targets the corresponding `src/questions/q_N.py` implementation.
- `requirements.txt` — external dev/runtime dependencies (if any).

## Quick start (PowerShell)

1. Create and activate a virtual environment (optional):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

1. Install dependencies if needed:

```powershell
pip install -r requirements.txt
```

1. Run all tests:

```powershell
python -m unittest discover -s testing -p "test_*.py"
```

1. Run a single test file (example: question 1):

```powershell
python -m unittest testing.test_q1
```

If a test fails, open the corresponding `src/questions/q_N.py` file, update the implementation, and re-run the tests.

## What we expect you to change

- Implement the functions/classes inside the files in `src/questions/` that the tests import.
- Do not modify the tests in `testing/` unless asked.
- Keep your changes focused and well-scoped; prefer small, readable commits.

## Notes

- The tests use the built-in `unittest` module — no test runner required.
- If you need to run tests with a specific Python executable in PowerShell, use the full path or the environment's Python (for example, `.\.venv\Scripts\python.exe -m unittest ...`).

Good luck — implement one question at a time and run the tests frequently.

Don't forget to think out loud and commit often!
