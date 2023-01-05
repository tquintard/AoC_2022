class Blocks:
    def __init__(self, shape, offset_v = 0, offset_h = 0):
        self.shape = shape
        self.resting = False
        self.min_h, self.min_v  = offset_h, offset_v
        match shape:
            case '-':
                self.coords = [[offset_v, offset_h + i] for i in range(4)]
                self.max_h, self.max_v = offset_h + 3, offset_v
            case '+':
                self.coords = [[offset_v + i, offset_h + j] 
                               for i in range(3) for j in range(3)
                               if i == 1 or j == 1]
                self.max_h, self.max_v = offset_h + 2, offset_v + 2
            case 'L':
                self.coords =[]
                for i in range(3):
                    self.coords.append([offset_v, offset_h + i])
                for j in range(1, 3):
                    self.coords.append([offset_v + j, offset_h + 2])
                self.max_h, self.max_v = offset_h + 2, offset_v + 2
            case '|':
                self.coords = [[offset_v + i, offset_h] for i in range(4)]
                self.max_h, self.max_v = offset_h, offset_v + 3
            case 'O':
                self.coords = [[offset_v + i, offset_h + j] for i in range(2) for j in range(2)]
                self.max_h, self.max_v = offset_h + 1, offset_v + 1         
    
    def colision(self, next_pos, tiles_filled):
        for pos in next_pos:
            if pos in tiles_filled:
                return True
        return False

    def move_block(self, dir, tiles_filled):
        #move horizontally
        match dir:
            case '>': # move right
                if self.max_h < 6: #blocks is not adjacent to rigth wall
                    next_pos = list(map(lambda x: [x[0], x[1]+1], self.coords))
                    if not self.colision(next_pos, tiles_filled):
                        self.coords = next_pos
                        self.max_h, self.min_h = self.max_h + 1, self.min_h + 1
            case '<': # move left
                if self.min_h > 0: #blocks is not adjacent to left wall
                    next_pos = list(map(lambda x: [x[0], x[1]-1], self.coords))
                    if not self.colision(next_pos, tiles_filled):
                        self.coords = next_pos
                        self.max_h, self.min_h = self.max_h - 1, self.min_h - 1
        #move vertically (down)
        curr_pos = self.coords
        if self.min_v > 0: #blocks is not adjacent to bottom wall
            next_pos = list(map(lambda x: [x[0] - 1, x[1]], self.coords))
            if not self.colision(next_pos, tiles_filled):
                self.coords = next_pos
                self.max_v, self.min_v = self.max_v - 1, self.min_v - 1
        if curr_pos == self.coords: #block hasn't moved, thus is resting
            self.resting = True
