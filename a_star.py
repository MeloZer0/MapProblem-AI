import heapq

class NoProcura:
    def __init__(self, estado: MapProblem, pai=None, acao=None, custo=0, nivel=0):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo       # g(n)
        self.nivel = nivel

    def __lt__(self, other):
        # Usado pela fila de prioridade
        return (self.custo + self.estado.heuristic()) < (other.custo + other.estado.heuristic())


def A_Estrela(mapa_inicial: MapProblem):
    # Fila de prioridade
    fila = []
    no_inicial = NoProcura(estado=mapa_inicial, custo=0, nivel=0)
    heapq.heappush(fila, (no_inicial.custo + mapa_inicial.heuristic(), no_inicial))

    visitados = []

    while len(fila) > 0:
        _, no_atual = heapq.heappop(fila)

        if no_atual.estado.isFinal():
            return reconstruir_caminho(no_atual)

        visitados.append(no_atual.estado)

        for (sucessor_estado, acao, custo) in no_atual.estado.succ():
            novo_no = NoProcura(
                estado=sucessor_estado,
                pai=no_atual,
                acao=acao,
                custo=no_atual.custo + custo,
                nivel=no_atual.nivel + 1
            )
            if not any(sucessor_estado.isEqual(v) for v in visitados):
                prioridade = novo_no.custo + sucessor_estado.heuristic()
                heapq.heappush(fila, (prioridade, novo_no))

    return None


def reconstruir_caminho(no_final):
    caminho = []
    atual = no_final
    while atual.pai is not None:
        caminho.append(atual.acao)
        atual = atual.pai
    caminho.reverse()  # Inverter para ordem correta
    return caminho
