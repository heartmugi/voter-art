import numpy as np
import matplotlib.pyplot as plt
from copy import copy

# 使用するクラス
class VoterArt:
    def __init__(self, size, init_num=None, r=0.3):
        '''
        size: int
            モデルの一辺のサイズ。全体はsize^2となる。10以上とする。
        init_num: int
            初期状態の"1"の数。Noneの場合割合(r)を適用する。
        r: float
            初期状態の"1"の数の割合。init_numが指定されているときは適用されない。
        '''
        if size < 10:
            print('error: "size" must be bigger than 10.')
            exit(1)
        self.size = size
        self.init_num = int((size**2)*r) if init_num==None else init_num
        model = np.zeros(size**2)
        ones_idx = np.random.randint(0, size**2, self.init_num)
        model[ones_idx] = 1
        self.model = model.reshape([size, size])
        self.d = [[i,j] for i in range(-1,2) for j in range(-1,2)]

    def mutate(self):
        '''
        モデルの変異を行う関数。
        各セルは周辺によって"0"または"1"となる。
        '''
        model = copy(self.model)
        for i in range(self.size):
            for j in range(self.size):
                sum = num = 0
                for di, dj in self.d:
                    num += 1
                    if i + di >= 0 and i + di < self.size and j + dj >= 0 and j + dj < self.size:
                        sum += self.model[i+di, j+dj]
                p = sum / num
                model[i, j] = 1 if np.random.rand() < p else 0
        self.model = model

    def save_plot(self, i):
        '''
        モデルの描写を保存する。

        i: int
            現在のiteration
        '''
        plt.imshow(self.model)
        plt.title(f'iteration: {str(i)}')
        plt.savefig(f'results/{str(i)}.png')
        plt.close()

    def show_plot(self, i):
        '''
        モデルの描写を表示する。

        i: int
            現在のiteration
        '''
        plt.imshow(self.model)
        plt.title(f'iteration: {str(i)}')
        plt.show(block=False)
        plt.pause(0.1)
        plt.close()

    def run(self, iterations=None, show=True, save=False):
        '''
        モデルの変異と描写の表示/保存を連続で行う。

        iterations: int
            変異と描写の回数の指定。
            Noneの場合は全てが"0"または"1"になったとき終了する。
        show: bool
            モデルの描写を表示するかの指定。Trueなら表示。
        save; bool
            モデルの描写を保存するかの指定。Trueなら保存。
        '''
        # 変異がなくなるまで
        if iterations == None:
            i = 0
            while(np.sum(self.model) != 0 or np.sum(self.model) != self.size**2 ):
                self.mutate()
                if show:
                    self.show_plot(i)
                if save:
                    self.save_plot(i)
                i += 1
        # 指定回数分
        else:
            if show:
                    self.show_plot(0)
            if save:
                    self.save_plot(0)
            for i in range(1, iterations+1):
                self.mutate()
                if show:
                    self.show_plot(i)
                if save:
                    self.save_plot(i)

if __name__ == '__main__':
    VA = VoterArt(100)
    VA.run(100, show=False, save=True)