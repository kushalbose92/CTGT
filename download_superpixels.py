import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent
zip_path = script_dir / "superpixels.zip"
data_dir = script_dir / "data"

print("Downloading superpixels.zip...")
subprocess.run(
    [
        "curl",
        "--fail",
        "--location",
        "https://www.dropbox.com/s/y2qwa77a0fxem47/superpixels.zip?dl=1",
        "--output",
        str(zip_path),
    ],
    check=True,
)
subprocess.run(
    ["unzip", "-o", str(zip_path), "-d", str(data_dir)],
    check=True,
)

