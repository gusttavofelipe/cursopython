import subprocess
#executa programas e processos externos

proc = subprocess.run(['ls'], capture_output=True, text=True)

saida = proc.stdout

for i in saida:
    saida = saida.replace('class', 'AULA')
    print(saida)