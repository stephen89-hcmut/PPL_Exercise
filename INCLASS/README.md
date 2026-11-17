# INCLASS Exercises

INCLASS gom cac bai Functional Programming va AST/Expression tu attachment.

## Setup

Windows PowerShell:

```powershell
py -m venv .venv
python3 -m pip install -r requirements.txt
python3 INCLASS/setup.py
```

Linux/macOS:

```bash
python3 -m pip install -r requirements.txt
python3 INCLASS/setup.py
```

## Chay dap an tham khao

```bash
python3 INCLASS/run_all.py --answer
```

Trên Windows PowerShell, thay executable bằng
`python3` và dùng dấu `/` cho đường dẫn:

```powershell
python3 INCLASS/run_all.py --answer
```

## Chay skeleton sinh vien

```bash
python3 INCLASS/run_all.py
```

```powershell
python3 INCLASS/run_all.py
```

Moi `description.md` cua bai deu co muc `## Run` voi day du lenh Windows
PowerShell va Linux/macOS, gom buoc generate parser va lenh chay rieng bai do.

Mỗi exercise co `description.md`, `solution.py`, `answer.py` va `main.py`. Report co cot `Test`, `Expected`, `Got`, `Status` va `Reason` khi fail.
