from typing import Union

from fastapi import FastAPI
import uvicorn
import numpy as np
from rdkit import Chem
import os

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/mol/{SMILES}")
def read_mol(SMILES: str, q: Union[str, None] = None):
  mol = Chem.MolFromSmiles(SMILES)
  return {"num_atoms": mol.GetNumAtoms(), "q": q}

@app.get("/item/{rnd_size}")
def read_item(rnd_size: int, q: Union[str, None] = None):
  x = np.random.randint(rnd_size)
  return {"rnd_num": x, "q": q}

@app.get("/readfile")
def read_file():
  filepath = "./external.txt"

  if not os.path.isfile(filepath):
    return {"content": "file missing!"}

  with open(filepath, "r") as fp:
    for count, line in enumerate(fp):
      return {"content": line}
  return {"content": ""}

if __name__ == "__main__":
  uvicorn.run(app, port=8000, host="0.0.0.0")