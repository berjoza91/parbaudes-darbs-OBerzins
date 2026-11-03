$diski = Get-PSDrive -PSProvider FileSystem |
    Select-Object Name, Used, Free

$diski | Export-Csv -Path "diski.csv" -NoTypeInformation -Encoding utf8

# TODO: saglabā $diski failā diski.csv