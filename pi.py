#ANTES DE TUDO EXECUTAR O COMANDO "python -m pip install oracledb" no CMD

import getpass
import oracledb

try:
    conexao = oracledb.connect(
    user = "BD150224315",
    password = 'Fsqad8',
    dsn="BD-ACD/xe")
except Exception as erro:
    print('Erro de conexão', erro)
else:
    print("Conectado", conexao.version)

cursor = conexao.cursor()

cursor.execute("select * from estoque")
resultado = cursor.fetchall()
print(resultado)
cursor.close()
conexao.close()