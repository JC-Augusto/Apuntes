import os


def generarGrafico(): 
    graficoInicio = """
    digraph L{node[shape = box  fillcolor =  "#FFEDBB" style = filled ]subgraph cluster_p{
    label = "TERRENO A RECORRER"
    bgcolor = "#398D9C"
    """


    grafico = """
    hola -> como estas  
    """


    graficoCierre = "}}"
    miArchivo = open('graphviz.dot','w')
    miArchivo.write(graficoInicio+grafico+graficoCierre)
    miArchivo.close    

generarGrafico("hola")

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
os.system('dot -Tpng graphviz.dot -o grafico.png')
os.startfile('grafico.png')

