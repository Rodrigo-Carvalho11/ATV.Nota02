from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(cod,desc, dataI, dataT, resp, tipo, obs):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_inventarios
            SET descri='{desc}', dataI='{dataI}',dataT='{dataT}'
            respo='{resp}', tipo='{tipo}, obs='{obs}' WHERE cod='{cod}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()