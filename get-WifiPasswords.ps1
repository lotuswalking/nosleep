# Save the following script to a file named Get-WiFiPasswords.ps1
$wifiProfiles = netsh wlan show profiles | Select-String "All User Profile" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }

$wifiPasswords = foreach ($profile in $wifiProfiles) {
    $profileInfo = netsh wlan show profile name="$profile" key=clear
    $keyContent = $profileInfo | Select-String "Key Content" | ForEach-Object { $_.ToString().Split(":")[1].Trim() }
    [PSCustomObject]@{
        WiFiName = $profile
        Password = $keyContent
    }
}

