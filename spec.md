# Repository Specifications

## Minimum Information Required In the Annotation of Models [(MIRIAM)](https://en.wikipedia.org/wiki/Minimum_information_required_in_the_annotation_of_models)

- Model must have a name
- Must identify the author(s), including contact information
- Creation and last modified dates must be included
- Licensing information

## File Structure

```
.
├── README.md                           # Quick start information
├── spec.md                             # This file. Repository structure details
├── Tools
|   └── README.md                       # Tools user guide (required)
├── Scripts
|   ├── README.md                       # Scripts user guide (required)
|   ├── downloader.py                   # Download script
|   └── manager.py                      # Management script
├── <Model Category>
|   ├── README.md                       # Category description (required)
|   ├── <Model Name>
|   |   ├── README.md                   # Model details for all versions (required)
|   |   ├── meta.json                   # Model metadata for all versions (required)
|   |   └── <version>
|   |       ├── README.md               # Version specific model details (optional)
|   |       ├── meta.json               # Version specific model metadata (required)
|   |       ├── results.txt             # Pre-calculated, expected results (required)
|   |       ├── <Model Name>.<ext1>     # Model file (required)
|   |       ├── <Model Name>.<ext2>     # Model file in alternate format (optional)
|   |       └── ...
|   └── <Model Name>
|       └── ... 
└── <Model Category>                
    └── ...
```



## File/Directory Naming Conventions

- All **files** and **directories** shall contain only alphanumeric or underscore characters.
- All words shall be separated by an **underscore**.
- **Model categories** and **model names**
  - Shall use title case capitalization.
- **Version directories**
  - Shall be of the format `<version_tag>_v<version.number>`, e.g. `n100_m10_v1.1.3`.
  - Should be lowercase, unless there is reasoning otherwise.

## File Formats

### Readme

### meta.json

Example:
```json
{
    "model": {
        "authors": [
            "John Doe": {
                "email": "john.doe@example.com",
            },
        ],
        "created": "2022-12-01",
        "modified": "2023-01-12",
        "license": "GPLv3",
        "tags": [
            "contrived",
            "unbounded",
        ],
    },
}
```

### results.txt

## Specification Data
```json
{
    "spec": {
        "version": {
            "major": 0,
            "minor": 1,
            "patch": 0
        },
        "tags": {
            "contrived":    "Contrived",
            "unbounded":    "Unbounded Models/Massive Models",
            "bounded":      "Bounded Models",
            "challenging":  "Challenging Models",
            "low_prob":     "Low probability events",
        },
    }
}
```
