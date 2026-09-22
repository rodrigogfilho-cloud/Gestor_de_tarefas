from database.conexao import conectar_bd


def inserir_tarefa(texto_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
                                INSERT INTO tarefas (tarefa,status)
                                VALUES (?,?);
                                """,
                                [texto_tarefa, "PENDENTE"])
    conexao.commit()
    cod_tarefa = cursor.lastrowid
    conexao.close()
    return cod_tarefa


def recuperar_tarefas():
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM tarefas;")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas


def excluir_tarefa(codigo_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""DELETE FROM tarefas
                       WHERE cod_tarefa = ?;""",
                        [codigo_tarefa])
    conexao.commit()
    conexao.close()

def atualizar_status(codigo_tarefa, novo_status):
    conexao, cursor  = conectar_bd()
    cursor.execute("""
                    UPDATE tarefas
                    set status = ?
                    WHERE cod_tarefa = ?;
                   """,
                   [novo_status, codigo_tarefa])
    conexao.commit()
    conexao.close()

def atualizar_tarefa(codigo_tarefa, nova_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    UPDATE tarefas
                    set tarefa = ?
                    WHERE cod_tarefa = ?;                       
                  """,
                  [nova_tarefa,codigo_tarefa])
    conexao.commit()
    conexao.close()