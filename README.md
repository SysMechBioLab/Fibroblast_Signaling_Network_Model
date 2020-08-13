# Fibroblast_Signaling_Network_Model

This is the repository for our lab's network model of cardiac fibroblast signal transduction. Includes reaction topology, ODE model, and accompanying analysis scripts.

- **Reaction topology**: located in `cytoscape/snm_1_1_rev4.cys` as a Cytoscape Session File (requires Cytoscape 3.1.0 or later)
- **ODE Model**: located in `data/snm_1_1_rev4.xlsx`, and can be directly used in Netflux package for MATLAB
- **Analysis Scripts**: located in `utils/` folder
  - *ModelValidation*: qualitative validation against independent literature set
  - *MCInteractionAnalysis*: analysis of mechano-chemo interactions based on biochemical dose-response behavior
  - *PerturbationAnalysis*: analysis of node sensitivity/influence with knockdowns under multiple tension contexts
  - *DrugCaseStudies*: comparison of model-predicted responses to drug treatments with experimental studies
  - *DrugScreen*: comprehensive screening of drug treatments for mechano-adaptive behavior

Required software: MATLAB 2017a or later (Parallel Computing Toolbox required for select analyses)
