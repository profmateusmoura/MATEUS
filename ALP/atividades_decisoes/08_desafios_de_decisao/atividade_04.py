"""
ATIVIDADE 04 — Diagnóstico de rede simplificado

Leia:
- status_cabo: CONECTADO ou DESCONECTADO
- possui_ip: SIM ou NAO
- ping_gateway: SIM ou NAO

Mostre um diagnóstico simplificado:
- cabo desconectado -> verificar cabo;
- cabo conectado, sem IP -> verificar DHCP/configuração;
- possui IP, sem ping no gateway -> verificar gateway/rede local;
- tudo positivo -> conectividade local aparentemente normal.

Escolha a combinação de estruturas mais clara.
"""

status_cabo = input("Informe status do cabo: CONECTADO ou DESCONECTADO ")
possui_ip = input("Informe se possui IP: SIM ou NAO ")
ping_gateway = input("Informe se o ping alcança o Gateway: SIM ou NAO ")

if status_cabo == "DESCONECTADO":
    print("verificar cabo")
elif possui_ip == "NAO":
    print("verificar DHCP/configuração")
elif ping_gateway == "NAO":
    print("verificar gateway/rede local")
else:
    print("conectividade local aparentemente normal")