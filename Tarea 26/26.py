from pathlib import Path
import subprocess, csv, os
from openpyxl import Workbook

script_path = Path(__file__).parent / "servicios.ps1"

try:
    result = subprocess.run(["powershell", "-File", str(script_path)], capture_output=True, text=True)

    if result.returncode == 0:
        print("Script de PowerShell ejecutado con éxito.")
        print("Salida del script:\n", result.stdout)
        if Path("Exported.csv").exists():
            print("Archivo CSV encontrado.")
        else:
            print("Archivo CSV no encontrado en el directorio actual.")
        csv_file = Path("Exported.csv")
        excel_file = Path("ServicesDoc.xlsx")

        with csv_file.open('r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  
            data = list(reader)
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Nombre", "DisplayName", "Status", "StartType"])
        for row in data:
            sheet.append(row)
        workbook.save(excel_file)
        print(f"Datos exportados a {excel_file}")
    else:
        print("Error en la ejecución del script de PowerShell.")
        print("Error:", result.stderr)
except Exception as e:
    print(f"Ocurrió un error: {e}")


