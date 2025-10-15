from libskmaps import readSkMap, printSkMap, createWindow, drawSkMap, markPathSkMap
from mapProblem import MapProblem
from bfs import BFS

# Lê o mapa do ficheiro de texto
skmap = readSkMap("maze.txt")
print("Mapa lido:")
printSkMap(skmap)  # <---- ADICIONA ISTO
# Cria o problema inicial a partir do mapa
problem = MapProblem(skmap)

# Executa a busca em largura
solution = BFS(problem)
print("Posição inicial do jogador:", problem.player)
print("Posição do objetivo:", problem.goal)
print("isFinal inicial:", problem.isFinal())  # Deve ser False
if solution is None:
    print("Nenhuma solução encontrada.")
else:
    print("Solução encontrada:", solution)
    print("Número de passos (custo):", len(solution))
    
    # Mostra o caminho visualmente
    win = createWindow(400)
    marked_map = markPathSkMap(skmap, solution)
    print("Heurística final:", MapProblem(marked_map).heuristic())
    drawSkMap(marked_map, win)
    input("Pressiona ENTER para fechar a janela...")




