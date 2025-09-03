# Energy Network Simulations (pandapower)

This project demonstrates a **simple 3-bus low-voltage power system simulation** using [pandapower](https://pandapower.readthedocs.io/).  
It models:
- A grid connection (external grid),
- A load (consumer bus),
- Two transmission lines,  
and runs a **power flow analysis** to calculate voltages, power flows, and line losses.

## Project Structure
- `Project.py` → Main Python script to build and run the simulation.
- `requirements.txt` → Python dependencies (pandapower).
- `README.md` → Documentation.

## How to run
1) Create a virtual env (optional)
   python -m venv .venv
   .venv\Scripts\activate

2) Install packages
   pip install -r requirements.txt

3) Run
   python Project.py

## Results

- [Bus Results (CSV)](results/bus_results.csv)
- [Line Results (CSV)](results/line_results.csv)
