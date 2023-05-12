from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import random
import numpy as np
import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "22rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "24rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

Header_component = dbc.Container(
    [
        html.H1("Trabajo Práctico N°3 - Simulación", style={'color': 'darkcyan'}),
        html.Hr()
    ])

Input_component = dbc.Container(children=[
    html.H2("Simulación de Montecarlo"),
    html.Hr(),
    html.H4("Ingrese cantidad de simulaciones a generar: "),
    dcc.Input(id="input-n", type="number", value=1000, inputMode='numeric', required=True, max=100001, disabled=False),
    html.Br(),
    html.Br(),
    html.Hr(),
    html.H4("Variables del Modelo: "),
    html.H5("Costo Revisión: "),
    dcc.Input(id="input-revision", type="number", value=900, inputMode='numeric', required=True, max=100001, disabled=True),
    html.Br(),
    html.Br(),
    html.H5("Costo Reparación Motor: "),
    dcc.Input(id="input-reparacion", type="number", value=2500, inputMode='numeric', required=True, max=100001, disabled=True),
    html.Br(),
    html.Br(),
    html.H5("Cantidad Dia Revisión: "),
    dcc.Input(id="input-diasrev", type="number", value=6, inputMode='numeric', required=True, min= 5, max=8, disabled=True),
    html.Br(),
    html.Br(),
    html.Div([
        dbc.Checklist(['Editar'], id='check', switch=True)
    ]),
    html.Br(),
    html.Hr(),
    html.H4("Vector de Estados (Tabla): "),
    html.H5("Mostrar desde: "),
    dcc.Input(id="input-desde", type="number", value=1, inputMode='numeric', required=True, max=100001, disabled=False),
    html.Br(),
    html.Br(),
])

Boton_generar_component = dbc.Row([
    dbc.Button("Generar Simulación", color="primary",
               id="btn-generar",
               className="mb-3")
        ])

Tabla_component = dcc.Loading(
    id="loading-output-table",
    children=dash_table.DataTable(
        id='output-table',
        columns=[
            {'name': 'N° DIA', 'id': 'col0', 'type': 'any'},
            {'name': 'Horas Motor', 'id': 'col1', 'type': 'any'},
            {'name': 'Horas Promedio', 'id': 'col2', 'type': 'any'},
            {'name': 'RND Averia C', 'id': 'col3', 'type': 'any'},
            {'name': 'Dia Averia C', 'id': 'col4', 'type': 'any'},
            {'name': 'Falla C', 'id': 'col5', 'type': 'any'},
            {'name': 'Cantidad Fallas C', 'id': 'col6', 'type': 'any'},
            {'name': 'Costo C', 'id': 'col7', 'type': 'any'},
            {'name': 'Costo C AC', 'id': 'col8', 'type': 'any'},
            {'name': 'Costo Diario C', 'id': 'col9', 'type': 'any'},
            {'name': 'RND Averia P', 'id': 'col10', 'type': 'any'},
            {'name': 'Dia Averia P', 'id': 'col11', 'type': 'any'},
            {'name': 'Dia Revision P', 'id': 'col12', 'type': 'any'},
            {'name': 'Falla P', 'id': 'col13', 'type': 'any'},
            {'name': 'Cantidad Fallas P', 'id': 'col14', 'type': 'any'},
            {'name': 'Revision P', 'id': 'col15', 'type': 'any'},
            {'name': 'Cantidad Revision P', 'id': 'col16', 'type': 'any'},
            {'name': 'Costo P', 'id': 'col17', 'type': 'any'},
            {'name': 'Costo P AC', 'id': 'col18', 'type': 'any'},
            {'name': 'Costo Diario P', 'id': 'col19', 'type': 'any'},

        ],
        page_size=501,
        virtualization=True,
        fixed_rows={'headers': True, 'data': 0},
        style_header={
            'backgroundColor': '#b0c4de',
            'color': 'black'
        },
        style_data={
            'backgroundColor': 'aliceblue',
            'color': 'black'
        },
        style_cell={'border': '1px solid grey'},
        style_table={'height': '500px', 'overflowY': 'auto'},
        style_cell_conditional=[
            {
                'if': {'column_id': 'col0'},
                'width': '100px'
            },
            {
                'if': {'column_id': 'col1'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'col2'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'col3'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'col4'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'col5'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col6'},
                'width': '150px'
            }
            , {
                'if': {'column_id': 'col7'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col8'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col9'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col10'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'col11'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col12'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col13'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col14'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col15'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col16'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col17'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col18'},
                'width': '150px'
            }, {
                'if': {'column_id': 'col19'},
                'width': '150px'
            },
        ]
    ),
    type="default"
)


Cuerpo_component = html.Div([
    Tabla_component
],
    id='div-tabla',
    style={"display": "none"}
    )

Resultados_component = dbc.Container(children=[
    dbc.Container(id='output-ultimo')
])

modal_error = dbc.Modal(
    [
        dbc.ModalHeader("Error"),
        dbc.ModalBody("Los datos ingresados son incorrectos. Por favor, verifique e intente nuevamente."),
    ],
    id="modal-error",
    centered=True,
    is_open=False,
)

sidebar = html.Div(
    [
        Input_component,
        html.Br(),
        Boton_generar_component
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([
    Header_component,
    Cuerpo_component,
    Resultados_component,
    modal_error
], id="page-content", style=CONTENT_STYLE)


app.layout = html.Div([sidebar, content])

@app.callback(
    Output("div-tabla", "style"),
    Input("btn-generar", "n_clicks"))
def mostrar_table(n_clicks):
    if n_clicks == 0 or n_clicks is None:
        return {"display": "none"}
    else:
        return {"display": "block"}

@app.callback(
    [Output("output-table", "data"),
     Output("output-ultimo", "children")],
    Input("btn-generar", "n_clicks"),
    [State("input-n", "value"),
     State("input-desde", "value"),
     State("input-revision", "value"),
     State("input-reparacion", "value"),
     State("input-diasrev", "value")])
def generar_arreglo_tabla(n_clicks, n, desde, costo_cor, costo_pre, diasrev):
    text = []
    data = []
    if n_clicks is None:
        return [], []
    elif n is None:
        return [], []
    elif desde is None:
        return [], []
    else:
        data = Crear_Montecarlo(n, costo_cor, costo_pre, diasrev)
        indice = int(desde) - 1
        if indice >= len(data):
            return [], []
        else:
            dat = [{'col0': data[i]['N° DIA'],
                    'col1': Formatear_Hora(data[i]['Horas Motor']),
                    'col2': Formatear_Hora(data[i]['Horas Promedio']),
                    'col3': Formatear_rnd(data[i]['RND Averia C']),
                    'col4': data[i]['Dia Averia C'],
                    'col5': Condicionales(data[i]['Falla C']),
                    'col6': data[i]['Cantidad Fallas C'],
                    'col7': data[i]['Costo C'],
                    'col8': data[i]['Costo C AC'],
                    'col9': data[i]['Costo Diario C'],
                    'col10': Formatear_rnd(data[i]['RND Averia P']),
                    'col11': data[i]['Dia Averia P'],
                    'col12': data[i]['Dia Revision P'],
                    'col13': Condicionales(data[i]['Falla P']),
                    'col14': data[i]['Cantidad Fallas P'],
                    'col15': Condicionales(data[i]['Revision P']),
                    'col16': data[i]['Cantidad Revision P'],
                    'col17': data[i]['Costo P'],
                    'col18': data[i]['Costo P AC'],
                    'col19': data[i]['Costo Diario P'],
                    } for i in range(n)]

            dato_final = dat[indice:indice + 500]

            if desde < (n - 500):
                ultima = {'col0': data[n - 1]['N° DIA'],
                          'col1': Formatear_Hora(data[n - 1]['Horas Motor']),
                          'col2': Formatear_Hora(data[n - 1]['Horas Promedio']),
                          'col3': Formatear_rnd(data[n - 1]['RND Averia C']),
                          'col4': data[n - 1]['Dia Averia C'],
                          'col5': Condicionales(data[n - 1]['Falla C']),
                          'col6': data[n - 1]['Cantidad Fallas C'],
                          'col7': data[n - 1]['Costo C'],
                          'col8': data[n - 1]['Costo C AC'],
                          'col9': data[n - 1]['Costo Diario C'],
                          'col10': Formatear_rnd(data[n - 1]['RND Averia P']),
                          'col11': data[n - 1]['Dia Averia P'],
                          'col12': data[n - 1]['Dia Revision P'],
                          'col13': Condicionales(data[n - 1]['Falla P']),
                          'col14': data[n - 1]['Cantidad Fallas P'],
                          'col15': Condicionales(data[n - 1]['Revision P']),
                          'col16': data[n - 1]['Cantidad Revision P'],
                          'col17': data[n - 1]['Costo P'],
                          'col18': data[n - 1]['Costo P AC'],
                          'col19': data[n - 1]['Costo Diario P']
                          }
                dato_final.append(ultima)

            costo_diario_correctivo = ultima["col9"]


            costo_diario_preventivo = ultima["col19"]
            print(costo_diario_correctivo,costo_diario_preventivo)
            if costo_diario_correctivo < costo_diario_preventivo:
                text = html.Div(children=[
                    html.Br(),
                    html.Br(),
                    html.H2("CONCLUSION: "),
                    html.Br(),
                    html.H3("Conviene optar por la OPCIÓN CORRECTIVA, ya que el costo es menor.")
                ])
            if costo_diario_correctivo > costo_diario_preventivo:
                text = html.Div(children=[
                    html.Br(),
                    html.Br(),
                    html.H2("CONCLUSION: "),
                    html.Br(),
                    html.H3("Conviene optar por la OPCIÓN PREVENTIVA, ya que el costo es menor.")
                ])
            if costo_diario_correctivo == costo_diario_preventivo:
                text = html.Div(children=[
                    html.Br(),
                    html.Br(),
                    html.H2("CONCLUSION: "),
                    html.Br(),
                    html.H3(
                        "El costo es el mismo para ambos, por lo que podemos optar por cualquiera de las 2 opciones. ")
                ])
        return dato_final, text


@app.callback(
    [Output("input-revision", "disabled"), Output("input-reparacion", "disabled"), Output("input-revision", "value"), Output("input-reparacion", "value"), Output("input-diasrev", "disabled"), Output("input-diasrev", "value")],
    [Input('check', 'value')],
    [State("input-revision", "value"), State("input-reparacion", "value"), State("input-diasrev", "value")]
)
def toggle_inputs(value, revision, reparacion, diasrev):
    if value:
        return False, False, revision, reparacion, False, diasrev
    else:
        return True, True, 900, 2500, True, 6


@app.callback(
    Output("modal-error", "is_open"),
    [Input("btn-generar", "n_clicks")],
    [State("input-n", "value"),
     State("input-revision", "value"),
     State("input-reparacion", "value"),
     State("input-desde", "value")]
)
def mostrar_modal_error(n_clicks, n, costo_revision, costo_reparacion, desde):
    if n_clicks is None:
        return False
    elif n is None or costo_revision is None or costo_reparacion is None or desde is None:
        return True
    elif n < 1 or costo_revision < 0 or costo_reparacion < 0 or desde < 1 or desde > n:
        return True
    else:
        return False


# MONTECARLO--------------------------------------------------------------------------------------------------------

def Dia_rnd(rnd_averia):
    dia_ave = None
    if rnd_averia < 0.25:
        dia_ave = 5
    elif rnd_averia < 0.70:
        dia_ave = 6
    elif rnd_averia < 0.90:
        dia_ave = 7
    elif rnd_averia <= 1:
        dia_ave = 8

    return (dia_ave)


# Para el dia actual se fija si hay que hacer el random de averia y devuelve el dia de averia, rnd averia y actualiza la bandera
def Generar_Valores_correctivo(bandera_falla, dia, dia_ave):
    if bandera_falla:
        rnd_averia = random.random()
        rnd_averia = round(rnd_averia, 2)
        dia_aux = Dia_rnd(rnd_averia)
        print("dia", type(dia), "dia_aux", type(dia_aux), "rnd_averia", rnd_averia)
        dia_ave = (dia + dia_aux - 1)
        bandera_falla = False
    else:
        rnd_averia = -1

    return rnd_averia, dia_ave, bandera_falla


#Una vez que se uso Generar_Valores se fija si el motor fallo y actualiza la bandera para que el proximo dia se haga el random
def Comprobar_bandera_correctivo(dia,dia_ave,costo_cor):

    if dia == dia_ave:
        costo_hoy = costo_cor
        bandera_falla = True
    else:
        costo_hoy = 0
        bandera_falla = False

    return (bandera_falla, costo_hoy)

def Hora_Dia():
    # Definir los parámetros

    media = 14 * 60  # Media en minutos
    desv_std = 90  # Desviación estándar en minutos
    valor = np.random.normal(loc=media, scale=desv_std)
    valor = round(valor, 2)

    return valor

def Formatear_Hora(valor):
    hora = int(valor/ 60)
    minuto = int(valor % 60)
    hora_exacta = f"{hora:02d}:{minuto:02d}"

    return hora_exacta


def Montecarlo_Correctivo(n,costo_cor):
    bandera_falla = True
    dia_ave = 0
    cant_fallas = -1
    costo = 0
    costoAC = 0
    costoDiario = 0
    horas_motor = 0
    horas_ac = 0
    horas_prom = 0
    dia_aux = 0
    array_correctivo = []

    for i in range(n):
        dia_aux = dia_aux + 1
        horas_motor = Hora_Dia()
        horas_ac = horas_ac + horas_motor
        horas_ac = round(horas_ac, 2)
        horas_prom = (horas_ac / dia_aux)
        horas_prom = round(horas_prom, 3)

        if bandera_falla:
            cant_fallas = cant_fallas + 1
        rnd_averia, dia_ave, bandera_falla = Generar_Valores_correctivo(bandera_falla, dia_aux, dia_ave)
        bandera_falla, costo = Comprobar_bandera_correctivo(dia_aux, dia_ave,costo_cor)
        costoAC = costoAC + costo
        costoDiario = (costoAC / dia_aux)
        costoDiario = round(costoDiario, 2)
        array_correctivo.append(
            (dia_aux, horas_motor, horas_prom, rnd_averia, dia_ave, bandera_falla, cant_fallas, costo, costoAC, costoDiario))

    return array_correctivo


# Para el dia actual se fija si hay que hacer el random de averia o revisar y devuelve el dia de averia, dia_revision, rnd averia y actualiza las banderas
def Generar_Valores_preventivo(bandera_falla, bandera_revision, dia, dia_ave, dia_revision,diasrev):
    if bandera_falla or bandera_revision:
        rnd_averia = random.random()
        rnd_averia = round(rnd_averia, 2)
        dia_ave = (dia + Dia_rnd(rnd_averia) - 1)
        dia_revision = ((dia + diasrev) - 1)
        bandera_revision = False
        bandera_falla = False
    else:
        rnd_averia = -1

    return rnd_averia, dia_ave, dia_revision, bandera_falla, bandera_revision


# Una vez que se uso Generar_Valores se fija si el motor fallo y actualiza la bandera para que el proximo dia se haga el random
def Comprobar_bandera_preventivo(dia, dia_ave, dia_revision,costo_cor,costo_pre):
    if dia == dia_ave:
        costo_hoy = costo_cor
        bandera_falla = True
        bandera_revision = False
    elif dia == dia_revision:
        costo_hoy = costo_pre
        bandera_revision = True
        bandera_falla = False
    else:
        costo_hoy = 0
        bandera_revision = False
        bandera_falla = False

    return (bandera_falla, bandera_revision, costo_hoy)


def Montecarlo_Preventivo(n,costo_cor,costo_pre,diasrev):
    bandera_falla = True
    bandera_revision = True
    dia_ave = 0
    cant_fallas = -1
    cant_revision = -1
    costo = 0
    costoAC = 0
    costoDiario = 0
    dia_aux = 0
    dia_revision = 0
    array_preventivo = []

    for i in range(n):
        dia_aux = dia_aux + 1
        if bandera_falla:
            cant_fallas = cant_fallas + 1
        if bandera_revision:
            cant_revision = cant_revision + 1

        rnd_averia, dia_ave, dia_revision, bandera_falla, bandera_revision = Generar_Valores_preventivo(bandera_falla,
                                                                                                        bandera_revision,
                                                                                                        dia_aux, dia_ave,
                                                                                                        dia_revision,diasrev)
        bandera_falla, bandera_revision, costo = Comprobar_bandera_preventivo(dia_aux, dia_ave, dia_revision,costo_cor,costo_pre)
        costoAC = costoAC + costo
        costoDiario = (costoAC / dia_aux)
        costoDiario = round(costoDiario, 2)

        array_preventivo.append((dia_aux, rnd_averia, dia_ave, dia_revision, bandera_falla, cant_fallas, bandera_revision,
                                 cant_revision, costo, costoAC, costoDiario))

    return array_preventivo

def Juntar_Arrays(array_correctivo,array_preventivo):
    array_final = []
    largo = len(array_correctivo)

    for i in range(largo):

        result = array_correctivo[i] + array_preventivo[i][1:]
        array_final.append(result)
    return array_final


def Crear_Montecarlo(n,costo_cor,costo_pre,diasrev):
    array1 = Montecarlo_Correctivo(n,costo_pre)
    array2 = Montecarlo_Preventivo(n,costo_pre,costo_cor,diasrev)
    array_final = Juntar_Arrays(array1, array2)
    df = pd.DataFrame(array_final, columns=['N° DIA', 'Horas Motor', 'Horas Promedio', 'RND Averia C', 'Dia Averia C', 'Falla C', 'Cantidad Fallas C', 'Costo C', 'Costo C AC', 'Costo Diario C', 'RND Averia P', 'Dia Averia P', 'Dia Revision P', 'Falla P', 'Cantidad Fallas P', 'Revision P', 'Cantidad Revision P', 'Costo P', 'Costo P AC', 'Costo Diario P'])
    data_dict = df.to_dict('records')
    return data_dict

def Condicionales(cond):
    if cond:
        cond = "Si"
    else:
        cond = "No"
    return cond

def Formatear_rnd(rnd):
    if rnd == -1:
        rnd = ""
    return rnd





if __name__ == "__main__":
    app.run_server(debug=True)