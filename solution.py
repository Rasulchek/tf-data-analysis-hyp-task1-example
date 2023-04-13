import pandas as pd
import numpy as np
from scipy.stats import *
chat_id = 680977959  # Ваш chat ID, не меняйте название переменной


def solution(x1: int,
             n1: int,
             x2: int,
             n2: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    u = norm.ppf(0.91)
    ev = (x1 + x2) / (n1 + n2)
    un = (x1 / n1 - x2 / n2) / np.sqrt(ev * (1 - ev) * (1 / n1 + 1 / n2))
    return un > u
