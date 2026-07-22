from pathlib import Path

data_folder = Path("test_data")
file_path = data_folder/"users.csv"
print(file_path)
print(file_path.exists())

screenshots_folder = Path("screenshots")
screenshots_folder.mkdir(exist_ok=True)
reports_folder = Path("reports/2026")
reports_folder.mkdir(parents=True,exist_ok=True)



