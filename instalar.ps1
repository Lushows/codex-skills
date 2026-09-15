# Instala las skills de Lushows en este equipo.
# Uso:  powershell -ExecutionPolicy Bypass -File .\instalar.ps1

$origen = Join-Path $PSScriptRoot "skills"

if (-not (Test-Path $origen)) {
    Write-Host "ERROR: no encuentro la carpeta 'skills' junto a este script." -ForegroundColor Red
    Write-Host "Descomprime el repo completo y vuelve a ejecutar." -ForegroundColor Red
    exit 1
}

$skills = Get-ChildItem $origen -Directory
Write-Host ""
Write-Host "Skills encontradas: $($skills.Count)" -ForegroundColor Cyan
Write-Host ""
Write-Host "  1) Codex      -> ~\.codex\skills"
Write-Host "  2) Claude Code-> ~\.claude\skills"
Write-Host "  3) Los dos"
Write-Host ""
$opcion = Read-Host "Donde las instalo? (1/2/3)"

$destinos = @()
switch ($opcion) {
    "1" { $destinos += Join-Path $HOME ".codex\skills" }
    "2" { $destinos += Join-Path $HOME ".claude\skills" }
    "3" { $destinos += Join-Path $HOME ".codex\skills"; $destinos += Join-Path $HOME ".claude\skills" }
    default { Write-Host "Opcion no valida. Cancelado." -ForegroundColor Yellow; exit 1 }
}

foreach ($destino in $destinos) {
    New-Item -ItemType Directory -Force -Path $destino | Out-Null
    Write-Host ""
    Write-Host "Instalando en $destino" -ForegroundColor Cyan

    foreach ($skill in $skills) {
        $target = Join-Path $destino $skill.Name
        $existia = Test-Path $target
        if ($existia) { Remove-Item $target -Recurse -Force }
        Copy-Item $skill.FullName -Destination $target -Recurse
        if ($existia) {
            Write-Host "  reemplazada  $($skill.Name)" -ForegroundColor Yellow
        } else {
            Write-Host "  instalada    $($skill.Name)" -ForegroundColor Green
        }
    }
}

Write-Host ""
Write-Host "Listo. Cierra y vuelve a abrir Codex (o Claude Code)." -ForegroundColor Green
Write-Host ""
