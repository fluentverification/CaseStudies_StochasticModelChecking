# Stochastic Model Case Studies

Stochastic models are well-suited to studying systems in emerging fields such as nanotechnology, computational chemistry, and synthetic biology. However, the kinds of stochastic models which arise in these emerging fields tend to have infinite state space which cannot be analyzed by most existing tools. It is therefore prudent that tools be developed to verify infinite state space stochastic models. Likewise, there does not exist a collection of case studies for analyzing the performance of infinite state space stochastic model checking tools. Here, such a collection is developed and presented. The collection includes case studies from nanotechnology, computational chemistry, and synthetic biology which vary in complexity from toy models to practical designs encoded in the PRISM language. The models can be used in [PRISM](https://www.prismmodelchecker.org), [STORM](https://www.stormchecker.org), or [STAMINA](https://github.com/fluentverification/stamina-cplusplus) or any other tool that uses the PRISM language. The case-study repository presented here is intended to be a living document, so community contributions and recommendations are welcome.

## Repository structure

### Benchmarks

Benchmarks play a critical role in accessing various systems in computer engineering and science. They ensure a reliable, systematic test to evaluate a computer system's accuracy and performance. The benchmarks of this work includes two different sets of benchmarks.

### Chemical Reaction Networks

Chemical reaction networks are systems including some number of chemical species reacting through some number of defined reaction channels. Because chemical reaction networks underlie all biomolecular processes, their modeling, and analysis are relevant to the design and analysis of biological systems with applications to medicine, biomanufacturing, and biofuels. Stochastic model checking is particularly relevant in these systems because biochemical systems may have low molecule counts, so traditional chemical kinetics are insufficient. This section describes five such examples.

### Genetic Circuits

Genetic circuits are part of synthetic biology, a research field combining engineering principles with biology. Researchers build circuits out of defined biological parts adding desired functionalities to biological systems. Automation in the design process allows scientists to model and analyze their genetic circuits \emph{in silico} to test the system before implementation. Stochastic model checking has been used to analyze genetic circuits before, which have an infinite state space and therefore suit the case studies presented here.

## Running STAMINA/Storm via Docker on Apple Silicon Mac

This guide explains how to pull, configure, and run the `ifndefjosh/sstamina` tool using Docker on an Apple Silicon (M-series) Mac. It includes the specific configurations needed to bypass architecture mismatches, map local files, and call the exact internal binary path.

### Prerequisites

- [Docker Desktop](https://docker.com) installed and running on Mac.
- Model files (e.g., `.sm` and `.props`) saved together in a dedicated project directory.

---

### Step-by-Step Instructions

#### 1. Prepare Your Project Directory
Before starting, ensure the terminal is inside the folder containing the model files. Docker uses the active folder to share files with the container.

```bash
cd /path/to/your/StaminaDocker
```
*(Verify your files are visible in this directory by running `ls` before proceeding).*

#### 2. Download the Image
Pull the verified `v3.0_2025` build from Docker Hub:

```bash
docker pull ifndefjosh/sstamina:v3.0_2025
```

#### 3. Run the Model Verification Command
Because this container is built for Intel processors (`amd64`) and the internal tool path is not configured in the system `$PATH`, the tool must be executed using the absolute path while enabling Mac architecture emulation.

Run the following command directly from the terminal (replace `your_model.prism` and `your_properties.csl` with the actual filenames):

```bash
docker run --rm \
  --platform linux/amd64 \
  -v "\$(pwd)":/data \
  ifndefjosh/sstamina:v3.0_2025 \
  /opt/stamina-storm/build/sstamina /data/your_model.prism /data/your_properties.csl
```
## Windows Alternatives

If you are running the tool on Windows instead of macOS, you do not need the `--platform` flag, but you must adjust the folder mounting syntax depending on the shell environment:

### Windows (PowerShell):
```powershell
docker run --rm \
  -v "\${PWD}:/data" \
  ifndefjosh/sstamina:v3.0_2025 \
  /opt/stamina-storm/build/sstamina /data/your_model.prism /data/your_properties.csl
```

### Windows (Command Prompt - CMD):
```cmd
docker run --rm \
  -v "%cd%:/data" \
  ifndefjosh/sstamina:v3.0_2025 \
  /opt/stamina-storm/build/sstamina /data/your_model.prism /data/your_properties.csl
```

---

## Command Flag Breakdown

- `--rm`: Automatically deletes the temporary container instance as soon as the calculation finishes to keep your system clean.
- `--platform linux/amd64`: Forces the Apple Silicon Mac to use its internal translation layer (Rosetta/QEMU) to execute the Intel-based container code.
- `-v "$(pwd)":/data`: Creates a live link between the current Mac folder (`$(pwd)`) and a virtual folder named `/data` inside the container.
- `/opt/stamina-storm/build/sstamina`: Specifies the exact location of the compiled binary discovered inside this container version.
- `/data/...`: Directs the tool to read the files from the shared virtual directory.

---

## Troubleshooting & Verification

### Verifying File Sharing and Internal Paths
If the tool reports that it cannot find the files, an interactive terminal can be opened directly inside the container to inspect the directories:

```bash
docker run --rm -it --platform linux/amd64 -v "\$(pwd)":/data ifndefjosh/sstamina:v3.0_2025 bash
```

Once inside the container terminal, these diagnostic checks can be run:
- **Check files:** Type `ls /data` to confirm the Mac files are passing through successfully.
- **Check the binary:** Type `ls /opt/stamina-storm/build` to verify the `sstamina` compilation file exists.
- **Exit:** Type `exit` to return to the normal Mac terminal prompt.
