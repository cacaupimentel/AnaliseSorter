# -*- coding: utf-8 -*-
import tracemalloc
import random 
import time
from random import randint

# pip install tracemalloc


# Algoritmos Bubble, Quick e Merge Sort
# Fonte
# https://github.com/programacaodinamica/algorithms/blob/master/sorting/sorting.py


# Variaveis
lista_caso_ordenado = []
lista_medio_caso = []
lista_caso_decresc = []
lista_rnd_caso1 = []
lista_rnd_caso2 = []
lista_rnd_caso3 = []
lista_rnd_caso4 = []
lista_rnd_caso5 = []

# Dados de entrada
n = 0
tipoSort = None

# Medidas
start_time = 0.0
end_time = 0.0
ms = 0.0
current = 0.0
peak = 0.0
memory = 0.0

# Somatorios para media
soma_quant = 0
soma_ms = 0.0
soma_memory = 0.0
Media_ms = 0.0
Media_memory = 0.0


# Saidas
datahora = None
line = None


###############################################################
# Video: https://www.youtube.com/watch?v=S99XufEPCFQ
# Escolha de pivot do "Quick Sort"
###############################################################
# Pivo Inicial
def piv_ini(caso_pv, inip, fimp):
    # Pivo Inicial pior caso será o primeiro ZERO
    if caso_pv in "melhor":
        # aqui o pivo fica no centro da lista
        inp = (inip + fimp) // 2
    else:
        inp = int(randint(inip, (fimp-1))+1)
    return inp


################################################################
# Vídeo "Quick Sort": https://youtu.be/wx5juM9bbFo
################################################################
def quicksort(caso_qs, listaq, inicioq=0, fimq=None):
    if fimq is None:
        fimq = len(listaq)-1
    if inicioq < fimq:
        p = partition(caso_qs, listaq, inicioq, fimq)
        # recursivamente na sublista à esquerda (menores)
        quicksort(caso_qs, listaq, inicioq, p-1)
        # recursivamente na sublista à direita (maiores)
        quicksort(caso_qs, listaq, p+1, fimq)

def partition(caso_qp, listap, iniciop, fimp):
    # pivot = listap[fimp]
    ap = piv_ini(caso_qp, iniciop, fimp)
    pivot = listap[ap]
    ib = iniciop
    for jb in range(iniciop, fimp):
        # jb sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        if listap[jb] <= pivot:
            listap[jb], listap[ib] = listap[ib], listap[jb]
            # incrementa-se o limite dos elementos menores que o pivô
            ib = ib + 1
    listap[ib], listap[fimp] = listap[fimp], listap[ib]
    return ib



################################################################
# Vídeo "Merge Sort": https://youtu.be/S5no2qT8_xg
################################################################
def mergesort(listams, msinicio=0, msfim=None):
    if msfim is None:
        msfim = len(listams)
    if (msfim - msinicio) > 1:
        meio = (msfim + msinicio)//2
        mergesort(listams, msinicio, meio)
        mergesort(listams, meio, msfim)
        merge(listams, msinicio, meio, msfim)

def merge(mlista, minicio, meio, mfim):
    left = mlista[minicio:meio]
    right = mlista[meio:mfim]
    top_left, top_right = 0, 0
    for k in range(minicio, mfim):
        if top_left >= len(left):
            mlista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            mlista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            mlista[k] = left[top_left]
            top_left = top_left + 1
        else:
            mlista[k] = right[top_right]
            top_right = top_right + 1



################################################################
# Vídeo "Bubble Sort": https://youtu.be/GiNPe_678Ms
################################################################
def bubble_sort(blista):
    global n
    n = len(blista)
    for aj in range(n-1):
        for ai in range(n-1):
            if blista[ai] > blista[ai+1]:
                # troca de elementos nas posições i e i+1
                blista[ai], blista[ai+1] = blista[ai+1], blista[ai]
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)


################################################################
# Site: https://docs.python.org/3/library/tracemalloc.html
#################################################################
# Inicia o Tempo
#################################################################
def StartTime():
    global start_time
    tracemalloc.start()
    start_time = time.time()


#####################################################################
# site: https://docs.python.org/pt-br/3/library/time.html#module-time
#####################################################################
# Finaliza o Tempo
#####################################################################
def EndTime(tcaso):
    global end_time
    global ms
    global current
    global peak
    global memory
    global end_time

    global soma_quant
    global soma_ms
    global soma_memory
    global Media_ms
    global Media_memory

    end_time = time.time()
    # o tempo deve ser calculado em segundos
    ms = (end_time - start_time)
    # Obtenha o tamanho atual e o tamanho máximo dos blocos de memória
    # current = atual(int) peak = pico(int) usada com reset_peak()
    current, peak = tracemalloc.get_traced_memory()
    # Obtem o uso de memória em bytes e transforma em Mb
    memory = tracemalloc.get_tracemalloc_memory() / (1024 * 1024)
    tracemalloc.stop()

    if tcaso.lower() in "medio":
        soma_quant = soma_quant + 1
        soma_ms = soma_ms + ms
        soma_memory = soma_memory + memory


################################################################
# Grava Resultado
################################################################
def GravaResultado(gcaso):
    global end_time
    global ms
    global current
    global peak
    global memory
    global end_time
    global tipoSort

    global soma_quant
    global soma_ms
    global soma_memory
    global Media_ms
    global Media_memory
    global line

    print(
        '-------------------------------------------------------------------------------------------------------------')
    print("Numero de elementos :", n)
    print("Tipo Sort :", tipoSort)
    print("Caso: ", gcaso)
    print("start_time", start_time)
    print("end_time: ", end_time)
    print("Ms: ", ms)
    print("current: ", current)
    print("peak: ", peak)
    print("memory: ", memory)

    line = ""
    gf = open("saida.csv", "a")
    if gcaso.lower() in 'medio':
        print("Soma Quantidade: ", soma_quant)
        print("Soma Ms:", soma_ms)
        print("Soma Memoria", soma_memory)
        if soma_quant > 4:
            # Tira as medias
            Media_ms = soma_ms / soma_quant
            Media_memory = soma_memory / soma_quant

            print("Media Ms:", Media_ms)
            print("Media Memoria", Media_memory)

            gdatahora = time.strftime("%d/%m/%Y-%H:%M:%S")
            print(gcaso)
            line = str(gdatahora) + "," + tipoSort + "," + str(n) + "," + gcaso + "," + " " + str(Media_ms) + "," + str(
                Media_memory)
            gf.write(line + "\n")
            soma_quant = 0
            soma_ms = 0.0
            soma_memory = 0.0
            Media_ms = 0.0
            Media_memory = 0.0

    else:
        gdatahora = time.strftime("%d/%m/%Y-%H:%M:%S")
        line = str(gdatahora) + "," + tipoSort + "," + str(n) + "," + gcaso + "," + " " + str(ms) + "," + str(memory)
        gf.write(line + "\n")

    print(line)
    gf.close()


# Executa algoritmo Ordenação Bolha
def Executa_BubbleSort(listab, caso_b):
    StartTime()
    bubble_sort(listab)
    EndTime(caso_b)
    GravaResultado(caso_b)


# Executa algoritmo Mege Sort
def Executa_MergeSort(lista_m, caso_m):
    StartTime()
    mergesort(lista_m)
    EndTime(caso_m)
    GravaResultado(caso_m)


# Executa algoritmo Mege Sort
def Executa_QuickSort(listaq, caso_q):
    StartTime()
    quicksort(caso_q, listaq)
    EndTime(caso_q)
    GravaResultado(caso_q)


####################################################################
# Abrir Arquivo de entrada
####################################################################
option = "melhor"  # nenhuma, melhor, pior
f = open("entrada.txt", "r")
file = f.readlines()

# Lendo o arquivo
contLinha = 0
for linha in file:
    if contLinha < 1:
        n = int(linha)
    else:
        tipoSort = linha
    contLinha += 1
f.close()



#####################################################################
# Criar as listas 
#####################################################################
# Melhor caso lista já ordenada
for i in range(1, n+1):
    lista_caso_ordenado.append(i)

# Pior caso lista decrescente
lista_caso_decresc = sorted(lista_caso_ordenado, reverse=True)

# Caso Medio Rabdomico 5 listas
lista_rnd_caso1 = random.sample(range(1, n+1), n)
lista_rnd_caso2 = random.sample(range(1, n+1), n)
lista_rnd_caso3 = random.sample(range(1, n+1), n)
lista_rnd_caso4 = random.sample(range(1, n+1), n)
lista_rnd_caso5 = random.sample(range(1, n+1), n)



# Aplicar o algoritimo e ptoduzir resultados
#---------------------------------------------------------------------
if tipoSort.lower() in "merge":
    # Aplicar algoritmo Bubble Sort
    lista = lista_caso_ordenado
    Executa_MergeSort(lista, "melhor")

    lista = lista_caso_decresc
    Executa_MergeSort(lista, "pior")

    lista = lista_rnd_caso1
    Executa_MergeSort(lista, "medio")

    lista = lista_rnd_caso2
    Executa_MergeSort(lista, "medio")

    lista = lista_rnd_caso3
    Executa_MergeSort(lista, "medio")

    lista = lista_rnd_caso4
    Executa_MergeSort(lista, "medio")

    lista = lista_rnd_caso5
    Executa_MergeSort(lista, "medio")


if tipoSort.lower() in "bubble":

    lista = lista_caso_ordenado
    Executa_BubbleSort(lista, "melhor")

    lista = lista_caso_decresc
    Executa_BubbleSort(lista, "pior")

    lista = lista_rnd_caso1
    Executa_BubbleSort(lista, "medio")

    lista = lista_rnd_caso2
    Executa_BubbleSort(lista, "medio")

    lista = lista_rnd_caso3
    Executa_BubbleSort(lista, "medio")

    lista = lista_rnd_caso4
    Executa_BubbleSort(lista, "medio")

    lista = lista_rnd_caso5
    Executa_BubbleSort(lista, "medio")



if tipoSort.lower() in "quick":
    # Lista decrescente com pivo no centro
    lista = lista_caso_decresc
    Executa_QuickSort(lista, "melhor")
    # lista ordenada com pivo no ZERO
    lista = lista_caso_ordenado
    Executa_QuickSort(lista, "pior")

    lista = lista_rnd_caso1
    Executa_QuickSort(lista, "medio")

    lista = lista_rnd_caso2
    Executa_QuickSort(lista, "medio")

    lista = lista_rnd_caso3
    Executa_QuickSort(lista, "medio")

    lista = lista_rnd_caso4
    Executa_QuickSort(lista, "medio")

    lista = lista_rnd_caso5
    Executa_QuickSort(lista, "medio")