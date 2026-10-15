# INCLASS Exercises

INCLASS gom cac bai Functional Programming va AST/Expression tu attachment.

## Setup

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe INCLASS\setup.py
```

Linux/macOS:

```bash
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python INCLASS/setup.py
```

## Chay dap an tham khao

```bash
.venv/bin/python INCLASS/run_all.py --answer
```

Trên Windows PowerShell, thay executable bằng
`.\.venv\Scripts\python.exe` và dùng dấu `\` cho đường dẫn:

```powershell
.\.venv\Scripts\python.exe INCLASS\run_all.py --answer
```

## Chay skeleton sinh vien

```bash
.venv/bin/python INCLASS/run_all.py
```

```powershell
.\.venv\Scripts\python.exe INCLASS\run_all.py
```

Moi `description.md` cua bai deu co muc `## Run` voi day du lenh Windows
PowerShell va Linux/macOS, gom buoc generate parser va lenh chay rieng bai do.

Mỗi exercise co `description.md`, `solution.py`, `answer.py` va `main.py`. Report co cot `Test`, `Expected`, `Got`, `Status` va `Reason` khi fail.
