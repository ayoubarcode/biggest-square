#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
from utils import PLATEAU


class Plateau:

    def __init__(self):
        self.line_nb = 0
        self.void_ch = "."
        self.obs_ch = "o"
        self.fill_ch = "x"

    def process_file(self, filename):
        line_nb = self.line_nb
        void_ch = self.void_ch
        obs_ch = self.obs_ch
        fill_ch = self.fill_ch

        self.process(line_nb, void_ch, obs_ch, fill_ch, filename)

    def process(self, line_nb, void_ch, obs_ch, fill_ch, filename):
        error = False
        for file in filename:
            first_line = True
            print('HELLO')

            # une erreur sur le 1er caractère, la solution que j'ai trouvée a été d'utiliser utf-8 comme encodage
            with open(file, "r", encoding="utf-8") as file_object:
                line = file_object.readline()
                if not (re.findall('\d+', line)) or not (line[0].isdigit()):
                    print("cart invalide 1")
                    self.processCartInvalid(
                        line_nb, void_ch, obs_ch, fill_ch, filename)
                else:
                    line_nb = int(re.findall('\d+', line)[0])
                    if len(line) != len(str(line_nb)) + 4 or line_nb <= 0:
                        #cela entraînera une "erreur de carte" si le nombre de lignes commence par un 0 (ex : 09)
                        print("cart invalide 2")
                        self.processCartInvalid(
                            line_nb, void_ch, obs_ch, fill_ch, filename)
                    else:
                        void_ch = line[len(str(line_nb))]
                        obs_ch = line[len(str(line_nb)) + 1]
                        fill_ch = line[len(str(line_nb)) + 2]
                        if not (self.check_plateau(line_nb, void_ch, obs_ch, fill_ch, file_object)):
                            print("cart invalide 3")
                            self.processCartInvalid(
                                line_nb, void_ch, obs_ch, fill_ch, filename)
                        else:
                            self.replace_vide_plein(
                                line_nb, void_ch, obs_ch, fill_ch, file_object)

    def isCartInvalid(self, filename):
        with open(filename[0], 'a+') as file_object:
            data = file_object.read()
            file_object.seek(0)
            file_object.write(re.sub(
                r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", data))
            file_object.truncate()
            file_object.writelines(PLATEAU)
            return [file_object.name]

    def processCartInvalid(self, line_nb, void_ch, obs_ch, fill_ch, filename):
        filename = self.isCartInvalid(filename)
        for file in filename:
            first_line = True

            # une erreur sur le 1er caractère, la solution que j'ai trouvée a été d'utiliser utf-8 comme encodage
            with open(file, "r", encoding="utf-8") as file_object:
                line = file_object.readline()
                if not (re.findall('\d+', line)) or not (line[0].isdigit()):
                    print("cart invalide 1")
                    self.isCartInvalid(
                        line_nb, void_ch, obs_ch, fill_ch, filename)
                else:
                    line_nb = int(re.findall('\d+', line)[0])
                    if len(line) != len(str(line_nb)) + 4 or line_nb <= 0:
                        #cela entraînera une "erreur de carte" si le nombre de lignes commence par un 0 (ex : 09)
                        print("cart invalide 2")
                        self.isCartInvalid(
                            line_nb, void_ch, obs_ch, fill_ch, filename)
                    else:
                        void_ch = line[len(str(line_nb))]
                        obs_ch = line[len(str(line_nb)) + 1]
                        fill_ch = line[len(str(line_nb)) + 2]
                        if not (self.check_plateau(line_nb, void_ch, obs_ch, fill_ch, file_object)):
                            print("cart invalide 3")
                            self.isCartInvalid(
                                line_nb, void_ch, obs_ch, fill_ch, filename)
                        else:
                            self.replace_vide_plein(
                                line_nb, void_ch, obs_ch, fill_ch, file_object)

    def replace_vide_plein(self, line_nb, void_ch, obs_ch, fill_ch, f):
        start_point, best_start_point = [0, 0], [0, 0]
        square_side, best_square_side = 0, 0
        x, y, xi, yi = 0, 0, 0, 0
        arr = []
        # en remplaçant le curseur au début du fichier
        f.seek(0)
        # sauter la première ligne
        f.readline()
        for line in f:
            arr.append(list(line))
        while yi < line_nb:
            while xi < len(arr[0]):
                start_point = [xi, yi]
                obs_found = False
                if arr[yi][xi] == void_ch:
                    x = xi
                    y = yi
                    if x < len(arr[0]) - 1 and y < line_nb - 1:
                        while (x < len(arr[0]) - 1 or y < line_nb - 1) and obs_found == False:
                            x += 1
                            y += 1
                            square_side += 1
                            if x >= len(arr[0]) or y >= line_nb:
                                obs_found = True
                            while x >= xi and obs_found == False:
                                if arr[y][x] == obs_ch:
                                    obs_found = True
                                x -= 1
                            x = xi + square_side
                            while y >= yi and obs_found == False and y < line_nb:
                                if arr[y][x] == obs_ch:
                                    obs_found = True
                                y -= 1
                            y = yi + square_side
                            if square_side > best_square_side:
                                best_square_side = square_side
                                best_start_point = start_point
                        x = 0
                        y = 0
                        square_side = 0
                xi += 1
            xi = 0
            yi += 1
        #Afficher la solution
        self.print_solution(
            best_square_side, best_start_point, line, fill_ch, f)

    def print_solution(self, best_square_side, best_start_point, line, fill_ch, f):
        f.seek(0)
        f.readline()
        square = ""
        while best_square_side > 0:
            square = square + fill_ch
            best_square_side -= 1
        for lidx, line in enumerate(f):
            if lidx >= best_start_point[1] and lidx < best_start_point[1] + len(square):
                print(line[:best_start_point[0]] + square +
                      line[best_start_point[0]+len(square):])
            else:
                print(line)
        f.close()

    def check_plateau(self, line_nb, void_ch, obs_ch, fill_ch, f):
        check_chars = [void_ch, obs_ch, fill_ch, "\n"]
        for line_idx, line in enumerate(f):
            for ch in line:
                if not ch in check_chars:
                    return False
            if line[-1] != "\n":
                return False
        if line_idx + 1 != int(line_nb):
            return False
        len_line = len(line)
        f.seek(0)
        f.readline()
        for line in f:
            if len(line) != len_line:
                return False
        return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Missing parameters.')
        exit()
    p = Plateau()
    p.process_file(sys.argv[1:])
