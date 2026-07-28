# One-click: Start Streamlit + Cloudflare tunnel
$venv = "D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\.venv\Scripts\python.exe"
$dash = "D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard\dashboard.py"
$cd = "D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard"

# Kill old
Get-Process streamlit -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep 1

# Start Streamlit in background, hide warnings
Write-Host "[1/2] Starting Streamlit..." -ForegroundColor Yellow
$log = Join-Path $cd "streamlit_out.txt"
Start-Process -NoNewWindow powershell "-NoProfile -Command `"cd '$cd'; & '$venv' -m streamlit run '$dash' 2>&1 | Out-File '$log'`""

# Wait for it
Write-Host "Waiting..." -ForegroundColor Gray
$port = 8501
for ($i = 0; $i -lt 40; $i++) {
    Start-Sleep 1
    try { $r = Invoke-WebRequest -Uri "http://localhost:$port" -UseBasicParsing -TimeoutSec 1 -ErrorAction Stop; if ($r.StatusCode -eq 200) { break } } catch {}
    if ($i -eq 15) { $port = 8502; try { $r = Invoke-WebRequest -Uri "http://localhost:$port" -UseBasicParsing -TimeoutSec 1 -ErrorAction Stop; if ($r.StatusCode -eq 200) { break } } catch {} }
}

Write-Host "  Streamlit running on http://localhost:$port" -ForegroundColor Green

# Start Cloudflare tunnel
Write-Host "[2/2] Starting Cloudflare tunnel..." -ForegroundColor Yellow
$tlog = Join-Path $cd "tunnel_out.txt"
Start-Process -NoNewWindow powershell "-NoProfile -Command `"cloudflared tunnel --url http://localhost:$port 2>&1 | Out-File '$tlog'`""

Start-Sleep 10
$url = ""
if (Test-Path $tlog) {
    $c = Get-Content $tlog -Raw
    $m = [regex]::Match($c, 'https://[a-z-]+\.trycloudflare\.com')
    if ($m.Success) { $url = $m.Value }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  LOCAL: http://localhost:$port" -ForegroundColor Green
if ($url) { Write-Host "  SHARE: $url" -ForegroundColor Green } else { Write-Host "  SHARE: check tunnel_out.txt" -ForegroundColor Yellow }
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Close this window to stop." -ForegroundColor Gray

Read-Host "Press Enter to exit"
