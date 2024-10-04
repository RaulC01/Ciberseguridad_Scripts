param(
    [string]$ReportPath = "Exported.csv"
)
Get-Service | Select-Object name, displayname, status, starttype | Export-Csv -Path $ReportPath -NoTypeInformation
