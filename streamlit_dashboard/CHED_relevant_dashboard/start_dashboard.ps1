# One-click: start Streamlit + a Cloudflare tunnel, and don't print the URL
# until it actually serves traffic.
#
# TWO MODES
#   Quick tunnel (default)  - no account needed, RANDOM url, changes every run.
#   Named tunnel            - stable url that never changes. Set $TunnelName and
#                             $TunnelHostname below. Requires a Cloudflare account
#                             with a domain, and a one-time setup:
#                                 cloudflared tunnel login
#                                 cloudflared tunnel create nmat-ched
#                                 cloudflared tunnel route dns nmat-ched ched.yourdomain.com
#                             Then set:  $TunnelName = "nmat-ched"
#                                        $TunnelHostname = "ched.yourdomain.com"

$TunnelName     = ""    # e.g. "nmat-ched"        leave empty for a quick tunnel
$TunnelHostname = ""    # e.g. "ched.yourdomain.com"

$venv = "D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\.venv\Scripts\python.exe"
$cd   = "D:\User\Desktop\Acads\NMAT Analysis\NMAT_Analysis\streamlit_dashboard\CHED_relevant_dashboard"
$dash = Join-Path $cd "dashboard.py"

Get-Process streamlit, cloudflared -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep 1

# ---- 1. Streamlit -----------------------------------------------------------
Write-Host "[1/2] Starting Streamlit..." -ForegroundColor Yellow
$log = Join-Path $cd "streamlit_out.txt"
Start-Process -NoNewWindow powershell "-NoProfile -Command `"cd '$cd'; & '$venv' -m streamlit run '$dash' 2>&1 | Out-File -Encoding utf8 '$log'`""

$port = 0
foreach ($p in 8501, 8502) {
    for ($i = 0; $i -lt 30; $i++) {
        try {
            if ((Invoke-WebRequest "http://localhost:$p/_stcore/health" -UseBasicParsing -TimeoutSec 1).Content.Trim() -eq "ok") { $port = $p; break }
        } catch { Start-Sleep 1 }
    }
    if ($port) { break }
}
if (-not $port) { Write-Host "  Streamlit did not come up - see $log" -ForegroundColor Red; Read-Host "Enter to exit"; exit 1 }
Write-Host "  Streamlit healthy on http://localhost:$port" -ForegroundColor Green

# ---- 2. Tunnel --------------------------------------------------------------
Write-Host "[2/2] Starting Cloudflare tunnel..." -ForegroundColor Yellow
$tlog = Join-Path $cd "tunnel_out.txt"

if ($TunnelName -and $TunnelHostname) {
    $args = "tunnel --url http://localhost:$port run $TunnelName"
    $url  = "https://$TunnelHostname"
} else {
    $args = "tunnel --url http://localhost:$port"
    $url  = ""
}
Start-Process -NoNewWindow powershell "-NoProfile -Command `"cloudflared $args 2>&1 | Out-File -Encoding utf8 '$tlog'`""

# A quick tunnel prints its hostname into the log a few seconds after start.
if (-not $url) {
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep 1
        if (Test-Path $tlog) {
            $m = [regex]::Match((Get-Content $tlog -Raw), 'https://[a-z0-9-]+\.trycloudflare\.com')
            if ($m.Success) { $url = $m.Value; break }
        }
    }
}
if (-not $url) { Write-Host "  Could not read a tunnel URL - see $tlog" -ForegroundColor Red; Read-Host "Enter to exit"; exit 1 }

# THE FIX: the old script slept 10s and printed the URL immediately. Cloudflare
# needs longer than that to make a fresh hostname routable, so the first click
# reliably failed. Poll until it really answers before showing it.
Write-Host "  Waiting for $url to become reachable..." -ForegroundColor Gray
$ready = $false
for ($i = 0; $i -lt 60; $i++) {
    try {
        if ((Invoke-WebRequest "$url/_stcore/health" -UseBasicParsing -TimeoutSec 3).Content.Trim() -eq "ok") { $ready = $true; break }
    } catch { Start-Sleep 2 }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  LOCAL: http://localhost:$port" -ForegroundColor Green
if ($ready) {
    Write-Host "  SHARE: $url" -ForegroundColor Green
    Write-Host "  (verified reachable - safe to send)" -ForegroundColor Gray
} else {
    Write-Host "  SHARE: $url" -ForegroundColor Yellow
    Write-Host "  (NOT yet answering after 2 min - give it a moment, then retry)" -ForegroundColor Yellow
}
if (-not $TunnelName) { Write-Host "  Note: quick tunnel - this URL changes every run." -ForegroundColor DarkGray }
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Close this window to stop." -ForegroundColor Gray
Read-Host "Press Enter to exit"
