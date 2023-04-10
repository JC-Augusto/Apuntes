staff = {
    'Juan': {'cargo': 'marketing','desempeño': 71},
    'Sofia': {'cargo': 'marketing','desempeño': 65},
    'Andres': {'cargo': 'marketing','desempeño': 49},
    'Romina': {'cargo': 'marketing','desempeño': 53}
}
"""
print(staff)
print("llaves")
print(staff.keys())
print("items")
print(staff.items())
print("valores")
print(staff.values())
#del(staff['Andres'])
#print(staff)


for trabajador in staff:
    print(trabajador)

for trabajador in staff:
    print(staff[trabajador])

for trabajador in staff:
    print(staff[trabajador]["desempeño"])
    """

def des(dic):
    despedidos = []
    for trabajador in dic:
        if dic[trabajador]["desempeño"] < 50:
            print('Se recomienda despedir al trabajador ', trabajador)
            despedidos.append(trabajador)
    for desp in despedidos:
        del(dic[desp])
    return dic

new_staff = des(staff)
print('Trabajadores de alto desempeño:')
for trabajador in new_staff:
    print(trabajador)