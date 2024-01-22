# SynthDoG 🐶: Synthetic Document Generator

SynthDoG is synthetic document generator for visual document understanding (VDU).

![image](../misc/sample_synthdog.png)

## Prerequisites

- python>=3.6
<!-- - [synthtiger](https://github.com/clovaai/synthtiger) (`pip install synthtiger`) -->
- forked synthtiger (`pip install -e .`)
     ```bash
     git clone https://github.com/BetterACS/synthtiger.git
     cd synthtiger
     pip install -e .
     ```

## Usage

```bash
# Set environment variable (for macOS)
$ export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

synthtiger -o ./outputs/SynthDoG_th -c 50 -w 4 -v template.py SynthDoG config_th.yaml

{'config': 'config_th.yaml',
 'count': 50,
 'name': 'SynthDoG',
 'output': './outputs/SynthDoG_th',
 'script': 'template.py',
 'verbose': True,
 'worker': 4}
{'aspect_ratio': [1, 2],
     .
     .
 'quality': [50, 95],
 'short_size': [720, 1024]}
Generated 1 data (task 3)
Generated 2 data (task 0)
Generated 3 data (task 1)
     .
     .
Generated 49 data (task 48)
Generated 50 data (task 49)
46.32 seconds elapsed
```

Some important arguments:

- `-o` : directory path to save data.
- `-c` : number of data to generate.
- `-w` : number of workers.
- `-s` : random seed.
- `-v` : print error messages.
