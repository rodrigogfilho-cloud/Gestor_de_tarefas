import flet as ft
from model import model_tarefa


class Campo_tarefa(ft.Row):
    def __init__(self, texto_tarefa, funcao_excluir,cod_tarefa):
        super().__init__()

        self.cod_tarefa = cod_tarefa

        self.funcao_excluir = funcao_excluir

        self.caixa_tarefa_fazer = ft.TextField(value=texto_tarefa,
                                               border_color="#000000",
                                               read_only = True)
    
        self.caixa_estado = ft.Text(value="Pendente")
        
        
        
        self.caixa_verificacao = ft.Checkbox(value=0,
                                             on_change=self.mudar_texto)

        self.caixa_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                     mini=True,
                                                     on_click=lambda: self.funcao_excluir(self),
                                                     bgcolor="#FFFFFF"
                                                     
                                                     )

        self.caixa_editar = ft.FloatingActionButton(icon=ft.Icons.EDIT,
                                                    mini=True,
                                                    bgcolor="#FFFFFF",
                                                    on_click = self.alterar_tarefa 
                                                    )

        self.coluna_botoes = ft.Column(controls=[self.caixa_excluir,self.caixa_editar])

        self.coluna_tarefas = ft.Column(controls=[self.caixa_estado,self.caixa_tarefa_fazer])

        self.linha_tudo = ft.Row(controls=[self.caixa_verificacao,self.coluna_tarefas,self.coluna_botoes])

        self.container_tudo = ft.Container(content=self.linha_tudo,
                                           border_radius=20,
                                           bgcolor="#6C73C6")

        self.controls = [self.container_tudo]

    def mudar_texto(self):
                if self.caixa_verificacao.value == True:
                    self.caixa_estado.value = "Concluído"
                    self.container_tudo.bgcolor = "#D9FF1A"
                    model_tarefa.atualizar_status(self.cod_tarefa,"Concluído")
                else:
                    self.caixa_estado.value = "Pendente"
                    self.container_tudo.bgcolor = "#6C73C6"
                    model_tarefa.atualizar_status(self.cod_tarefa,"Pendente")
    def alterar_tarefa(self):
          model_tarefa.atualizar_tarefa(self.cod_tarefa,self.caixa_tarefa_fazer.value)

        
