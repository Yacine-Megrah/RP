from os import path
import numpy as np
import cv2

class Piece:
    def __init__(self, color = 'WHITE', name = '', decal = None, scope = [], value = 0):
        self.color = color
        self.name = name
        self.decal = decal
        self.scope = scope
        self.value = value
class PieceMap:
    def __init__(self, path):
        self.path = path
        self.map = cv2.imread(path)
        self.HEIGHT = self.map.shape[0]
        self.WIDTH = self.map.shape[1]
        self.sqrSize = 60
        self.pieces = []
        pieces_names = [
            #(piece)
            ("B_Qn"), ("B_Kg"), ("B_Rk"), ("B_K8"), ("B_Bp"), ("B_Pn"),
            ("W_Qn"), ("W_Kg"), ("W_Rk"), ("W_K8"), ("W_Bp"), ("W_Pn")
        ]
        for y in range(0, 120, self.sqrSize):
            for x in range(0, 360, self.sqrSize):
                self.pieces.append((self.map[y : y + self.sqrSize-1 , x : x + self.sqrSize-1]))
        for piece in self.pieces:
            print(piece.shape[:2])

#

pcsMap = PieceMap(path.join('src','ChessPiecesArray.png'))
print(pcsMap.map.shape[0])
print(pcsMap.map.shape[1])
