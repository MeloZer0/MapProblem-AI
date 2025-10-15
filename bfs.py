from mapProblem import MapProblem

class NoProcura:
    def __init__(self, estado: MapProblem, pai=None, acao=None, custo=0, nivel=0):
        self.estado = estado      # Estado do tipo MapProblem
        self.pai = pai            # Nó pai
        self.acao = acao          # Ação realizada (up, down, left, right)
        self.custo = custo        # Custo acumulado
        self.nivel = nivel        # Nível (profundidade)

def BFS(mapa_inicial: MapProblem):
    # Inicializa a fila com o nó inicial
    fila = []
    no_inicial = NoProcura(estado=mapa_inicial, custo=0, nivel=0)
    fila.append(no_inicial)

    # Lista para controlar estados já visitados (evitar ciclos)
    visitados = []

    while len(fila) > 0:
        no_atual = fila.pop(0)  # Retira da frente da fila (FIFO)

        if no_atual.estado.isFinal():
            # Encontrou solução, reconstruir caminho
            return reconstruir_caminho(no_atual)

        visitados.append(no_atual.estado)

        # Para cada sucessor gerado
        for (sucessor_estado, acao, custo) in no_atual.estado.succ():
            # Criar o novo nó
            novo_no = NoProcura(
                estado=sucessor_estado,
                pai=no_atual,
                acao=acao,
                custo=no_atual.custo + custo,
                nivel=no_atual.nivel + 1
            )
            # Verificar se o estado já foi visitado
            if not any(sucessor_estado.isEqual(v) for v in visitados):
                fila.append(novo_no)


    print("Visitados:", len(visitados))
    return None  # Não encontrou solução

def reconstruir_caminho(no_final):
    caminho = []
    atual = no_final
    while atual.pai is not None:
        caminho.append(atual.acao)
        atual = atual.pai
    caminho.reverse()  # Inverter para ordem correta
    return caminho
