# Ailab + leNER-BR

Repository created to encapsule leNER-BR model for judicial portuguese texts with Ailab text classification effort.
To execute this repository it's necessary to trained the leNER-BR model and have the weights available.

## Instalation

```bash
pip3 install -r requirements.txt
pip3 install jupyterlab
```

Then move the already trained weights to inside assets/model_assets/model/prototype_revised/model.weights folder.

To run the code use:

```bash
python3 jupyter notebook
```

Then open main.ipynb