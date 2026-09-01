import flet as ft


class Campo_tarefa(ft.Row):
    def __init__(self, valor, funcao_excluir):
        super().__init__()

        self.funcao_excluir = funcao_excluir 

        self.tarefa = ft.TextField(value=valor,
                                  label="Tarefa",
                                  filled=True,
                                  color='#000000',
                                  bgcolor='#FFFFFFF',
                                  border_color='#000000',
                                  border_radius= 20,
                                  )

        self.verificacao = ft.Text(value='Pendente',
                                   weight=ft.FontWeight.BOLD,
                                   color = 'white')

 

        def mudar_texto ():
            if self.verificacao.value == 'Pendente':
                self.verificacao.value = 'Concluído'
            elif self.verificacao.value =='Concluído':
                self.verificacao.value = 'Pendente'

        def alterar_cor ():
            pass


        self.caixa_verificacao = ft.Checkbox(on_change=mudar_texto)

        self.botao_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                     width=30,
                                                     height=30,
                                                     on_click = lambda:self.funcao_excluir(self)
                                                    )

        self.botao_editar = ft.FloatingActionButton(icon=ft.Icons.EDIT,
                                                    height=30,
                                                    width=30
                                                    )

        self.coluna_tarefa = ft.Column(controls = [self.verificacao,self.tarefa])

        self.coluna_botoes = ft.Column(controls=[self.botao_excluir,self.botao_editar])

        self.controls = ft.Row(controls=[self.caixa_verificacao,self.coluna_tarefa,self.coluna_botoes],
                               alignment='center')

        self.alignment = ft.MainAxisAlignment.CENTER
