# ============================================================
#  editpro_lushows - Control de calidad de la propia skill
#
#  Comprueba que:
#   1. Existan los 200 modulos
#   2. Las referencias cruzadas entre modulos apunten a archivos reales
#   3. Ningun archivo tenga BOM (rompe herramientas aguas abajo)
#   4. Todos cierren con "## Errores comunes" y "## Checklist"
#   5. El indice del SKILL.md coincida con los archivos reales
#
#  Uso: powershell -ExecutionPolicy Bypass -File verificar-skill.ps1
# ============================================================

$raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
$refs = Join-Path $raiz "references"
$f = Get-ChildItem $refs -Filter *.md | Sort-Object Name
$nums = $f | ForEach-Object { ($_.Name -split '-')[0] }

Write-Output "=== 1. INVENTARIO ==="
Write-Output "modulos: $($f.Count)/200"
$esperados = @(); 0..19 | ForEach-Object { $b=$_; 0..9 | ForEach-Object { $esperados += ("{0}{1}" -f $b,$_) } }
$faltan = $esperados | Where-Object { $_ -notin $nums }
if ($faltan) { Write-Output "FALTAN: $($faltan -join ', ')" } else { Write-Output "completo" }

Write-Output "`n=== 2. REFERENCIAS CRUZADAS ROTAS ==="
$rotas = 0
foreach ($m in $f) {
    # -Encoding UTF8 obligatorio: PowerShell 5.1 lee como ANSI si el archivo no tiene BOM,
    # y eso convierte las enes en "Ã±", produciendo falsas alarmas al comparar nombres.
    $txt = Get-Content $m.FullName -Raw -Encoding UTF8
    # Busca referencias tipo `109` o `64-nombre.md`.
    # OJO: hay que filtrar por rango. Sin esto daba falsas alarmas con numeros que
    # NO son modulos: `520` (pixeles de margen), `768` (resolucion), `001` (parte de
    # un nombre de modelo). Un modulo valido va de 00 a 199.
    # Nada de rangos de caracteres acentuados en la expresion: al guardar el archivo
    # la codificacion los deforma y el rango queda invalido. Se acepta cualquier cosa
    # que no sea comilla invertida, que es mas simple y no se rompe nunca.
    $citas = [regex]::Matches($txt, '`(\d{2,3})(?:-[^`]+\.md)?`') |
             ForEach-Object { $_.Groups[1].Value } |
             Where-Object { $v = [int]$_; $v -ge 0 -and $v -le 199 -and -not ($_.Length -eq 3 -and $_[0] -eq '0') } |
             Sort-Object -Unique
    foreach ($c in $citas) {
        if ($c -notin $nums) {
            Write-Output "  $($m.Name) -> cita '$c' que no existe"
            $rotas++
        }
    }
}
if ($rotas -eq 0) { Write-Output "  ninguna rota" } else { Write-Output "  TOTAL ROTAS: $rotas" }

Write-Output "`n=== 3. ARCHIVOS CON BOM ==="
$conBom = 0
foreach ($m in $f) {
    $b = [byte[]](Get-Content $m.FullName -Encoding Byte -TotalCount 3 -ErrorAction SilentlyContinue)
    if ($b.Count -eq 3 -and $b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF) {
        Write-Output "  $($m.Name)"; $conBom++
    }
}
if ($conBom -eq 0) { Write-Output "  ninguno" }

Write-Output "`n=== 4. ESTRUCTURA (cierre esperado) ==="
$sinCierre = @()
foreach ($m in $f) {
    # -Encoding UTF8 obligatorio: PowerShell 5.1 lee como ANSI si el archivo no tiene BOM,
    # y eso convierte las enes en "Ã±", produciendo falsas alarmas al comparar nombres.
    $txt = Get-Content $m.FullName -Raw -Encoding UTF8
    if ($txt -notmatch '## Errores comunes' -or $txt -notmatch '## Checklist') { $sinCierre += $m.Name }
}
if ($sinCierre.Count -eq 0) { Write-Output "  todos cierran bien" }
else { Write-Output "  sin cierre completo ($($sinCierre.Count)):"; $sinCierre | ForEach-Object { Write-Output "    $_" } }

Write-Output "`n=== 5. INDICE DEL SKILL.md vs ARCHIVOS REALES ==="
$skill = Get-Content (Join-Path $raiz "SKILL.md") -Raw -Encoding UTF8
$indexados = [regex]::Matches($skill, '`(\d{2,3}-[^`]+\.md)`') | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique
$reales = $f.Name
$indexadosQueNoExisten = $indexados | Where-Object { $_ -notin $reales }
$realesNoIndexados     = $reales | Where-Object { $_ -notin $indexados }
if ($indexadosQueNoExisten) {
    Write-Output "  indexados pero NO existen ($($indexadosQueNoExisten.Count)):"
    $indexadosQueNoExisten | ForEach-Object { Write-Output "    $_" }
} else { Write-Output "  todo lo indexado existe" }
if ($realesNoIndexados) {
    Write-Output "  existen pero NO indexados ($($realesNoIndexados.Count)):"
    $realesNoIndexados | ForEach-Object { Write-Output "    $_" }
}

Write-Output "`n=== RESUMEN ==="
$lineas = ($f | ForEach-Object { (Get-Content $_.FullName | Measure-Object -Line).Lines } | Measure-Object -Sum).Sum
Write-Output "$($f.Count) modulos | $lineas lineas | $([math]::Round(($f | Measure-Object Length -Sum).Sum/1KB)) KB"
