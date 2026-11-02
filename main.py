from src.calculator.calculator import SimpsonCalculator

# 536 pontos
ITERATIONS: int = 536

# x ao quadrado mas provavelmente deve ser mudada
def used_function(x: float):
    return x ** 2



if __name__ == '__main__':
    start_point = float(input("Insira o ponto inicial: \n"))
    end_point = float(input ("Insira o valor final: \n"))
    
    calculator = SimpsonCalculator(start_point,end_point,ITERATIONS, used_function)
    if calculator.output is not None:
       print(calculator.output)