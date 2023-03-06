import sys


if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/***"
elif "bicicleta" or "menu_bici" in sys.argv[0]:
    DATABASE_PATH = "bicicletas.csv"
elif "camioneta" or "menu_camioneta" in sys.argv[0]:
    DATABASE_PATH = "camionetas.csv"
elif "formula1" or "menu_f1" in sys.argv[0]:
    DATABASE_PATH = "formula1s.csv"
elif "quad" or "menu_quad" in sys.argv[0]:
    DATABASE_PATH = "quads.csv"
elif "motocicleta" or "menu_moto" in sys.argv[0]:
    DATABASE_PATH = "motocicletas.csv"
elif "coche" or "menu_coche" in sys.argv[0]:
    DATABASE_PATH = "coches.csv"