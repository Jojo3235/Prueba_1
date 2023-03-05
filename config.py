import sys

DATABASE_PATH = "coches.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/***"
elif "bicicleta" in sys.argv[0]:
    DATABASE_PATH = "bicicletas.csv"
