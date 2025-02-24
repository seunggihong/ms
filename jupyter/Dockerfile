FROM jupyter/base-notebook:python-3.10

WORKDIR /home/jovyan/work

RUN pip install --no-cache-dir \
    jupyterlab \
    numpy pandas matplotlib seaborn scikit-learn

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
