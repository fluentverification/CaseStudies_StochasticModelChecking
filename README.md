# Stochastic Model Case Studies

Within this repository are several case studies and scripts used to create and catalog models for various types of stochastic model checking. These models are mostly in the PRISM language and can be used in PRISM, STORM, or [STAMINA](https://github.com/fluentverification/stamina-cplusplus). Additionally, there are models for the IVy model checker as well as Python scripts used to generate such models. The models are organized into the following folders:

## Repository structure

### `./SBML` folder

Case studies of genetic designs represented in the _Systems Biology Markup Language_ (SBML) are stored in this directory. SBML encodes mathmatical models of biological processes.

### `./crn` Folder

Mostly contains IVy files for one of the following two types of models:

#### `./crn/DonovanYeastPolarization` subfolder

This folder contains several scripts to generate yeast polarization models in IVy, as well as some of those IVy files and their results. There is even a relevant PRISM file. *Yeast Polarization* occurs during yeast growth and is important in the budding process. These polarizations can be modelled using stochastic systems.

#### `./crn/KuwaharaEnzyme` subfolder

Contains PRISM and IVy files for the reaction of the Kuwahara Enzyme.

### `./prism` folder

Various relevant PRISM models (mostly conversions of the SBML files in `./SBML`) that can be used to model certain properties of systems. Can be run in STORM, PRISM, or STAMINA.

