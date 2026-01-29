# Learning from Delay Distributions: A New Representation for Delay-Aware Reinforcement Learning

Official implementation of **D²AC**

*Learning from Delay Distributions: A New Representation for Delay-Aware Reinforcement Learning* (AAMAS 2026)  

[Appendix](https://github.com/COOLAS-CS/D2AC/blob/main/Appendix.pdf)

## Installation

We recommend using **conda** to manage dependencies.

### 1. Clone the repository

```bash
git clone https://github.com/yourname/D2AC.git
cd D2AC
```
### 2. Setup the environment

```bash
conda env create -f environment.yml
conda activate D2AC
```
## Training
```bash
python d2ac_main.py --env_id Walker2d-v4 --obs_delay_dis gamma

```
