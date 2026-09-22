import flet as ft
import sqlite3 as neilson
from component.classe_campo_tarefas import Campo_tarefa

def main(pagina:ft.Page):
    pagina.window.width = 1200
    pagina.window.height = 1000
    pagina.title="Gerenciado de tarefas Godoy"
    pagina.horizontal_alignment = "center"
    pagina.bgcolor = "#767686"

    # Criando a tabela de tarefas no banco de dados SQLITE3
    conexao = neilson.connect('bd_tarefas.sqlite')   # Conectando ao banco de dados
    cursor = conexao.cursor() #Criando cursor
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
    cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT,
    status TEXT);
    ''')

    conexao.commit() #Salvando as alterações
    conexao.close() #Fechando a conexão

    titulo = ft.Text(value="Gerenciador de Tarefas do Godoy",
                     font_family= 'Arial',
                     color='#FFFFFF',
                     size=30,
                     weight=ft.FontWeight.BOLD)

    lista_campo_tarefas = []

    tarefa = ft.TextField(value="",
                          label="Tarefa",
                          color='#000000',
                          bgcolor='#FFFFFFF',
                          border_color='#000000',
                          border_radius= 20,)

    def excluir_campo(campo_tarefa):
        lista_campo_tarefas.remove(campo_tarefa)
    
    def adicionar_tarefa():
        lista_campo_tarefas.append(Campo_tarefa(valor=tarefa.value,
                                                funcao_excluir=excluir_campo))

    


        


        #Incluindo na tabela tarefas
        conexao = neilson.connect('bd_tarefas.sqlite')
        cursor = conexao.cursor()
        cursor.execute('''
                    INSERT INTO tarefas (tarefa, status)
                    VALUES (?,?);
                       ''',
                       [tarefa.value, 'PENDENTE'],)
        
        conexao.commit()
        conexao.close()
        tarefa.value = ''

    def atualizar (cod_tarefa,novo_status):
        conexao = neilson.connect('bd_tarefas.sqlite')
        cursor = conexao.cursor()
        cursor.execute ('''
            UPDATE FROM tarefas
            SET status = ?
            WHERE cod_tarefa = ?;
    ''',
    [novo_status, cod_tarefa])
        conexao.commit()
        conexao.close()
        
    botao_adicionar_tarefa = ft.FloatingActionButton(icon=ft.Icons.ADD,
                                                     width=30,
                                                     height=30,
                                       on_click=adicionar_tarefa)

    coluna_tarefas = ft.Column(controls=lista_campo_tarefas,
                               alignment='center'
                               )


    linha_tarefa_add = ft.Row(controls=[tarefa,botao_adicionar_tarefa],
                              alignment="center")


        
    pagina.controls = [titulo,
                       linha_tarefa_add,
                       coluna_tarefas,
                       ]

ft.run(main)
