import nmap
ns = nmap.PortScanner()

print(ns.nmap_version())

ns.scan('192.168.0.1' , '1-1024' , '-v')

print(ns.scaninfo())

print(ns.csv())