from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(desc, dataI, dataT, resp, tipo, obs):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_controle
                (descri, dataI, dataT, respo, tipo, obs)
                VALUES
                ('{desc}','{dataI}','{dataT}','{resp}','{tipo}','{obs}')
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()