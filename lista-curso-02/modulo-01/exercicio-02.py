# 2. Uso do Módulo platform
# Crie um programa que exiba informações sobre o sistema operacional usando o módulo
# platform. O programa deve imprimir:
# • Nome do sistema operacional
# • Versão do sistema
# • Arquitetura do processador

import platform

print(f"Nome do sistema operacional: {platform.system()}")

print(f"Versão do sistema: {platform.version()}")

print(f"Arquitetura do processador: {platform.architecture()}")
