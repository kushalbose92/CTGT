import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent
zip_path = script_dir / "molecules_zinc_full.zip"
data_dir = script_dir / "data"

print("Downloading molecules_zinc_full.zip...")
subprocess.run(
    [
        "curl",
        "--fail",
        "--location",
        "https://www.dropbox.com/s/grhitgnuuixoxwl/molecules_zinc_full.zip?dl=1",
        "--output",
        str(zip_path),
    ],
    check=True,
)
subprocess.run(
    ["unzip", "-o", str(zip_path), "-d", str(data_dir)],
    check=True,
)