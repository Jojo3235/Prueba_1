import sys

DATABASE_PATH = "coches.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/***"
elif "bicicleta" in sys.argv[0]:
    DATABASE_PATH = "bicicletas.csv"
elif "camioneta" in sys.argv[0]:
    DATABASE_PATH = "camionetas.csv"
elif "Formula1s" in sys.argv[0]:
    DATABASE_PATH = "Formula1s.csv"