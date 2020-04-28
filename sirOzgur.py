# coding=utf-8
"""
            SIR modellemesi,
    differnsial denklemlerimiz:
dS/dt = - beta*S*I
dI/dt = beta*S*I- gamma*I
dR/dt = gamma*I
"""
import numpy as np
from DifCozer import ForwardEuler
from matplotlib import pyplot as plt


class sirOzgur:
    def __init__(self, beta, gamma, S0, I0, R0):
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        if isinstance(gamma, (float, int)):
            self.gamma = lambda t: gamma
        elif callable(gamma):
            self.gamma = gamma

        self.baslangicKosullari = [S0, I0, R0]

    def __call__(self, u, t):
        S, I, _ = u
        print("beta=", self.beta(t), "susceptibles= ", S,     "gamma=", self.gamma(t),"   infected=",I)
        return np.asarray(
            -self.beta(t) * S * I,
            self.beta(t) * S * I - self.gamma(t) * I,
            self.gamma(t) * I
        )


if __name__ == "__main__":
    sir = sirOzgur(0.0008, 0.1, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.baslangicKosullari(sir.baslangicKosullari)

    araliklar = np.linspace(0, 60, 10)
    u, t = solver.coz(araliklar)
    # print(u)
    plt.plot(t, u[:, 0], label=" Hasta Olmayanlar")  # susceptibles
    plt.plot(t, u[:, 1], label="Enfekte Olanlar")
    plt.plot(t, u[:, 2], label=" Iyilesenler")
    plt.legend()
    plt.show()
