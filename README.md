# Stochastic Model Case Studies

It is always good to have a readme in your repository, so I have created one. I suggest you edit this Bryant to your liking.

Signed,
Josh

Within this repository are several case studies and scripts used to create and catalog models for various types of stochastic model checking. These models are mostly in the PRISM language and can be used in PRISM, STORM, or [STAMINA](https://github.com/fluentverification/stamina-cplusplus). Additionally, there are models for the IVy model checker as well as Python scripts used to generate such models. The models are organized into the following folders:

## `./SBML` folder

Models in the SBML format (a type of XML). Multiple toggle switches are placed here as well as some other example models. SBML can be converted to PRISM using STORM's SBML-to-PRISM conversion tool.

## `./crn` Folder

Mostly contains IVy files for one of the following two types of models:

### `./crn/DonovanYeastPolarization` subfolder

This folder contains several scripts to generate yeast polarization models in IVy, as well as some of those IVy files and their results. There is even a relevant PRISM file. *Yeast Polarization* occurs during yeast growth and is important in the budding process. These polarizations can be modelled using stochastic systems.

### `./crn/KuwaharaEnzyme` subfolder

Contains PRISM and IVy files, as well as a Python script relevant to, the reaction of the Kuwahara Enzyme. TODO: what is the Kuwahara Enzyme? Josh doesn't know because he doesn't work mainly on this project. Ask Landon, Bryant, or Lukas, or if all else fails, Chris Meyers.

## `./prism` folder

Various relevant PRISM models (mostly conversions of the SBML files in `./SBML`) that can be used to model certain properties of systems. Can be run in STORM, PRISM, or STAMINA.
