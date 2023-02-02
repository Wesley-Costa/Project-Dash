# from dash import Dash, html, dcc, Input, Output
# import plotly.express as px
# import pandas as pd
# from datetime import date, timedelta, datetime
# import coleta_dados
# import dash
# import dash_bootstrap_components as dbc
# import numpy as np

# # Criação do gráfico
# fig = px.line(df_aux_percentage, x=df_aux_percentage.index, y=df_aux_percentage.columns, labels={
#     "value": "Índice de conteúdo político (%)",
#     "index": "Dias",
#     "Nome": "Contas"
# },
#     title="Porcentagem de conteúdo político")

# # Lista com as opções para os tipos de seleção na tela
# opcoes = list(df_aux_percentage.columns.unique())
# opcoes.append("Todas as contas")
# button_howto = dbc.Button(
#     "Learn more",
#     id="howto-open",
#     outline=True,
#     color="info",
#     # Turn off lowercase transformation for class .button in stylesheet
#     style={"textTransform": "none"},
# )

# button_github = dbc.Button(
#     "View Code on github",
#     outline=True,
#     color="primary",
#     href="https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-image-segmentation",
#     id="gh-link",
#     style={"text-transform": "none"},
# )
# header = dbc.Navbar(
#     dbc.Container(
#         [
#             dbc.Row(
#                 [
#                     dbc.Col(
#                         html.Img(
#                             id="logo",
#                             src=app.get_asset_url("bar-chart.png"),
#                             height="30px",
#                         ),
#                         md="auto",
#                     ),
#                     dbc.Col(
#                         [
#                             html.Div(
#                                 [
#                                     html.H3("Comunicação política no Twitter"),
#                                     html.P(
#                                         "Porcentagem de conteúdo politico e Quantidade de posts ao longo das semanas"),
#                                 ],
#                                 id="app-title",
#                             )
#                         ],
#                         md=True,
#                         align="center",
#                     ),
#                 ],
#                 align="center",
#             ),
#         ],
#         fluid=True,
#     ),
#     dark=True,
#     color="dark",
#     sticky="top",
# )
# # Estrutura da tela
# controlsCheckPerc = dbc.Card(
#     [
#         html.Div(
#             [
#                 dcc.Checklist(opcoes, value=[opcoes[-1]], id='check_contas')
#             ],
#             className="body"
#         )
#     ],
#     body=True,
# )

# controlsCheckQtd = dbc.Card(
#     [
#         html.Div(
#             [
#                 dcc.Checklist(
#                     opcoes, value=[opcoes[-1]], id='check_qtd_contas')
#             ],
#             className="body",
#         )
#     ],
#     body=True,
# )

# controlsList = dbc.Card(
#     [
#         html.Div(
#             [
#                 dcc.Dropdown(opcoes, value='Todas as contas',
#                              id='list_contas'),
#             ],
#             className="body",
#         )
#     ],
#     body=True,
# )
# md_val = 10
# md_val_col = 2
# app.layout = dbc.Container(
#     [
#         header,
#         html.Div(
#             className="container-body",
#             children=[
#                 html.Br(),
#                 # html.Div(
#                 #     "Porcentagem semanal de conteúdo político nos posts", className="subContainer"),
#                 dbc.Row(
#                     [
#                         dbc.Col(controlsCheckPerc, md=md_val_col),
#                         dbc.Col(dcc.Graph(id='grafico_porcentagem_conta',
#                                           figure=fig), md=md_val),
#                     ],
#                     align="center",
#                 ),
#                 html.Hr(),
#                 # html.H5("Quantidade de posts semanais",
#                 #         className="subContainer"),
#                 dbc.Row(
#                     [
#                         dbc.Col(controlsCheckQtd, md=md_val_col),
#                         dbc.Col(dcc.Graph(id='grafico_qtd_conta',
#                                           figure=fig), md=md_val),
#                     ],
#                     align="center",
#                 ),
#                 html.Hr(),
#                 # html.H5("Porcentagem semanal de conteúdo político nos posts",
#                 #         className="subContainer"),
#                 dbc.Row(
#                     [
#                         dbc.Col(controlsList, md=md_val_col),
#                         dbc.Col(
#                             dcc.Graph(id='grafico_porcentagem_conta2'), md=md_val),
#                     ],
#                     align="center",
#                 ), ],
#         ),
#     ],
#     fluid=True,
#     className="containerBody"
# )

# # Gráfico de Porcentagem

# font_size = 30


# def grafico_percent(dados):
#     fig = px.line(dados, x=dados.index, y=dados.columns, labels={
#         "value": "Índice de conteúdo político (%)",
#         "index": "Semanas",
#         "Nome": "Contas"
#     })
#     fig.update_layout(
#         title="<b>Porcentagem semanal de conteúdo político nos posts</b>")
#     fig.update_layout(title_font_size=font_size)
#     return fig

# # Gráfico de Quantidade


# def grafico_qtd(dados):
#     fig = px.line(dados, x=dados.index, y=dados.columns, labels={
#         "value": "Quantidade de conteúdo postado na semana",
#         "index": "Semanas",
#         "Nome": "Contas"
#     })
#     fig.update_layout(title="<b>Quantidade de posts semanais</b>")
#     fig.update_layout(title_font_size=font_size)

#     return fig

# # Callback para o gráfico de porcentagem


# @ app.callback(
#     Output('grafico_porcentagem_conta2', 'figure'),
#     Input('list_contas', 'value')
# )
# def update_output(value):
#     if value == "Todas as contas":
#         fig = grafico_percent(df_aux_percentage)

#         fig.update_xaxes(
#             tickformatstops=[
#                 dict(dtickrange=[df_aux_percentage.columns[0], df_aux_percentage.columns[-1]], value="%w")]
#         )
#     else:
#         tabela_filtrada = df_aux_percentage.loc[:,
#                                                 df_aux_percentage.columns == value]
#         fig = grafico_percent(tabela_filtrada)
#     return fig


# @ app.callback(
#     Output('grafico_porcentagem_conta', 'figure'),
#     Input('check_contas', 'value')
# )
# def update_output(value):
#     if len(value) == 1 and value[0] == opcoes[-1]:
#         fig = grafico_percent(df_aux_percentage)
#     elif len(value) >= 1:
#         tabela_filtrada = pd.DataFrame()
#         df_aux = pd.DataFrame()
#         for name in value:
#             if name != opcoes[-1]:
#                 df_aux = df_aux_percentage.loc[:,
#                                                df_aux_percentage.columns == name]
#                 tabela_filtrada = pd.concat([tabela_filtrada, df_aux])
#         fig = grafico_percent(tabela_filtrada)
#     elif len(value) == 0:
#         fig = px.line()
#     return fig

# # Callback para o gráfico de quantidade


# @ app.callback(
#     Output('grafico_qtd_conta', 'figure'),
#     Input('check_qtd_contas', 'value')
# )
# def update_output(value):
#     if len(value) == 1 and value[0] == opcoes[-1]:
#         fig = grafico_qtd(df_aux_amount)
#     elif len(value) >= 1:
#         tabela_filtrada = pd.DataFrame()
#         df_aux = pd.DataFrame()
#         for name in value:
#             if name != opcoes[-1]:
#                 df_aux = df_aux_amount.loc[:, df_aux_amount.columns == name]
#                 tabela_filtrada = pd.concat([tabela_filtrada, df_aux])
#         fig = grafico_qtd(tabela_filtrada)
#     elif len(value) == 0:
#         fig = px.line()
#     return fig
