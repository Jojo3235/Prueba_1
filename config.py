import sys


if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/***"
elif "bicicleta"  in sys.argv[0]:
    DATABASE_PATH = "bicicletas.csv"
elif "camioneta"  in sys.argv[0]:
    DATABASE_PATH = "camionetas.csv"
elif "formula1"  in sys.argv[0]:
    DATABASE_PATH = "formula1s.csv"
elif "quad"  in sys.argv[0]:
    DATABASE_PATH = "quads.csv"
elif "motocicleta" in sys.argv[0]:
    DATABASE_PATH = "motocicletas.csv"
elif "coche" in sys.argv[0]:
    DATABASE_PATH = "coches.csv"