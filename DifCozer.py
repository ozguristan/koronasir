# coding=utf-8
import numpy as np
from tqdm import tqdm


class DifCozer:
    """
    Difrensiyal denklem çözücü

    İlerle metodunu implement etmeniz gerekiyor
    """

    def __init__(self, f):
        self.f = f

    def ilerle(self):
        raise NotImplementedError

    def baslangicKosullari(self, U0):
        if isinstance(U0, (int, float)):
            self.denklemSayisi = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.denklemSayisi = U0.size
        self.U0 = U0

    def coz(self, kacAralik):
        self.t = np.asarray(kacAralik)
        n = self.t.size
        self.u = np.zeros((n, self.denklemSayisi))

        self.u[0, :] = self.U0
        for i in tqdm(range(n - 1), ascii=True):
            self.i = i
            self.u[i + 1] = self.ilerle()
        return self.u[:i + 2], self.t[:i + 2]


class ForwardEuler(DifCozer):
    def ilerle(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i + 1] - t[i]
        s = u[i, :] + dt * f(u[i, :], t[i])
        print(s, "sssss")
        return u[i, :] + dt * f(u[i, :], t[i])
