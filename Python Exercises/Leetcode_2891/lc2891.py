import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    sortedanimals = animals[["name","weight"]]
    heavyanimals = sortedanimals.query("weight > 100")
    heavyfilteredanimals = heavyanimals.sort_values("weight", ascending = False)
    return heavyfilteredanimals[["name"]]