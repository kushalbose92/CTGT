
import subprocess
from pathlib import Path


script_dir = Path(__file__).resolve().parent
data_dir = script_dir / "data" / "SBMs"
data_dir.mkdir(parents=True, exist_ok=True)
zip_path = data_dir / "SBM_PATTERN.zip"

if not zip_path.is_file() or zip_path.stat().st_size != 0:
    print("Downloading SBM_PATTERN.zip...")
    partial_path = zip_path.with_suffix(".zip.part")
    subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            "--retry",
            "3",
            "https://www.dropbox.com/s/qvu0r11tjyt6jyb/SBM_PATTERN.zip?dl=1",
            "--output",
            str(partial_path),
        ],
        check=True,
    )
    partial_path.replace(zip_path)
else:
    print(f"File already downloaded: {zip_path}")

subprocess.run(["unzip", "-o", str(zip_path), "-d", str(data_dir)], check=True)