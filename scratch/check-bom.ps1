$folders = @('_sessions', '_uas', '_prototypes', '_projets', '_tutos', '.agents')
$files = Get-ChildItem -Path $folders -Recurse -Filter '*.md'
$bomFiles = @()

foreach ($file in $files) {
    $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        $bomFiles += $file.FullName
    }
}

if ($bomFiles.Count -eq 0) {
    Write-Host "SUCCESS: ALL $($files.Count) MARKDOWN FILES ARE STRICT UTF-8 WITHOUT BOM!"
} else {
    Write-Host "WARNING: $($bomFiles.Count) files have BOM:"
    foreach ($b in $bomFiles) {
        Write-Host " - $b"
    }
}
