designFile = "C:/Users/Diego/Google Drive/UTN/6to año/Proyecto Final/Proyecto/Desarrollo/FASE 4 - DISEÑO EN DETALLE/PDNAnalyzer_Output/praxis_top_level_pcbdoc_v3_fuente/odb.tgz"

powerNets = ["+12V_JACK", "+12V", "+12V_FUSE"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("CON1", "pdna_pin_1_1"), ("CON1", "pdna_pin_1_2") ],
"ground_pins": [ ("CON1", "3"), ("CON1", "2") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("CON2", "3") ],
"ground_pins": [ ("CON2", "6") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("CON3", "3") ],
"ground_pins": [ ("CON3", "6") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("CON4", "3") ],
"ground_pins": [ ("CON4", "6") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("CON5", "3") ],
"ground_pins": [ ("CON5", "6") ],
"current": 0.2,
"Rpin": 0.5,
}
]


voltage_regulators = [
{
"id": "5",
"type": "linear",

"in": [ ("D4", "1") ],
"out": [ ("D4", "2") ],
"ref": [],

"v2": -0.4,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "6",
"type": "linear",

"in": [ ("F1", "1") ],
"out": [ ("F1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4, 'Thickness': 8.636E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4, 'Thickness': 8.636E-05},
        {'name': 'INT1__GND_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.6, 'Thickness': 0.0007874},
        {'name': 'INT2__PWR_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-4', 'DielectricConstant': 4, 'Thickness': 8.636E-05},
        {'name': 'SUBSTRATE-5', 'DielectricConstant': 4, 'Thickness': 8.636E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2.54E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
