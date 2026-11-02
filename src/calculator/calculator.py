from scipy.integrate import simpson
from collections.abc import Callable
import numpy as np

class SimpsonCalculator:
    
    def __init__(self, start_point : int , end_point : int, subintervals : int, target_equation: Callable[[float], float]):
        self.start_point = start_point
        self.end_point = end_point
        if(self.end_point <= 0 or self.start_point <= 0 or self.end_point <= self.start_point):
            print("[ERRO] Insira um ponto inicial e um ponto final validos.")
            self.output = None
        elif subintervals % 2 != 0:
            print("Subintervalos devem ser par para a regra de 1/3 de Simpson.")
            self.output = None
        else:
            self.subintervals = subintervals
            self.current_point = start_point
            self.target_equation = target_equation
            self.step_size = (end_point - start_point) / subintervals
            self.outputs: list[int] = []
            self.output: float 
            self._get_y()
            self._integrate()
    
    def _integrate(self):
        self.output = simpson(y=self.outputs, dx=self.step_size)
    
    def _get_y(self):
        # linspace = linearly spaced
        # os resultados usando while loop nao eram corretos
        x_values = np.linspace(self.start_point, self.end_point, self.subintervals + 1)
        self.outputs = [self.target_equation(x) for x in x_values]