class MapProblem:
    
    #   Func para saber se 2 mapas são iguais (tamanho, boneco e final)
    
    #   class-point.py (init)
    
    #   if __name__ == "__main__":
    
    """
    Methods:
    __init__ (map (file()))  # Construtor do file (Recebe a lista de listas)

    isFinal() -> bool
    heuristic() -> number   # Manhattan distance
    succ() -> list of (MapProblem, action, cost)    #custo de 1 para todos
    isEqual(MapProblem) -> bool
    
    """
    #   Cada succ cria um novo mapa atualizado

    def __init__(self, map):
        self.map = map
        self.player = None
        self.goal = None
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '@' or map[i][j] == '+':
                    self.player = [i, j]
                if map[i][j] == '.' or map[i][j] == '+':
                    self.goal = [i, j]
        
        if self.player is None or self.goal is None:
            raise ValueError("Mapa inválido: jogador ou objetivo não encontrados.")


    def isFinal(self):
        return self.player == self.goal


    def heuristic(self):
        # Distancia manhattan
        return abs(self.player[0] - self.goal[0]) + abs(self.player[1] - self.goal[1])

    def succ(self):
        moves = []
        directions = ["up", "down", "left", "right"]
        
        for direction in directions:
            new_map = [row[:] for row in self.map]
            new_player = self.player.copy()
            
            if self.try_move(new_map, new_player, direction):
                new_problem = MapProblem(new_map)
                moves.append((new_problem, direction, 1))
                
        return moves

    def isEqual(self, other):
        return self.player == other.player and self.goal == other.goal

    def try_move(self, map, player, direction):
        new_l = player[0]
        new_c = player[1]

        if direction == "up":
            new_l -= 1
        elif direction == "down":
            new_l += 1
        elif direction == "left":
            new_c -= 1
        elif direction == "right":
            new_c += 1
        else:
            return False

        if not (0 <= new_l < len(map) and 0 <= new_c < len(map[0])):
            return False

        if map[new_l][new_c] == '#':
            return False

        # Limpa a posição antiga do jogador
        if map[player[0]][player[1]] == '+':
            map[player[0]][player[1]] = '.'  # Estava sobre o objetivo
        else:
            map[player[0]][player[1]] = ' '

        # Atualiza a nova posição
        if map[new_l][new_c] == '.':
            map[new_l][new_c] = '+'  # Jogador chega ao objetivo
        else:
            map[new_l][new_c] = '@'  # Jogador em célula normal

        player[0] = new_l
        player[1] = new_c

        return True
