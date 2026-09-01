import flet as ft


class Campo_tarefa(ft.Row):
    def __init__(self, valor):
        super().__init__()

        self.tarefa = ft.TextField(value=valor,
                                  label="Tarefa",
                                  filled=True,
                                  color='#000000',
                                  bgcolor='#FFFFFFF',
                                  border_color='#000000',
                                  border_radius= 20,
                                  )

        self.caixa_estado = ft.Text(value='Pendente')

        def mudar_estado ():
            if self.caixa_estado == 'Pendente':
                self.caixa_estado = 'Conclúido'
            elif self.caixa_estado == 'Concluído':
                self.caixa_estado = 'Pendente'

        self.caixa_verificacao = ft.Checkbox(value=0,
                                             on_change=mudar_estado)

        self.botao_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                     width=30,
                                                     height=30
                                                    )

        self.botao_editar = ft.FloatingActionButton(icon=ft.Icons.EDIT,
                                                    height=30,
                                                    width=30
                                                    )

        self.coluna_botoes = ft.Column(controls=[self.botao_excluir,self.botao_editar])

        self.controls = ft.Row(controls=[self.caixa_verificacao,self.tarefa,self.coluna_botoes],
                               alignment='center')

        self.alignment = ft.MainAxisAlignment.CENTER
