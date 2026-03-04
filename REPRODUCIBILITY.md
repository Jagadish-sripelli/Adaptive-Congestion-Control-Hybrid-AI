
# Reproducibility Guide

This document explains how to reproduce the experiments presented in the paper:

"A Hybrid Bio-Inspired and Machine Learning Framework for Adaptive Congestion Control and QoS Optimization in Modern Networks"

The repository provides dataset samples and configuration details used in the experimental evaluation.

---

# 1. System Requirements

The experiments were conducted using the following environment:

Operating System:
Ubuntu 22.04 LTS

Hardware:
Intel Core i9 processor  
64 GB RAM  

Software:
Python 3.10  
NS-3 Network Simulator  
Mininet  
Ryu SDN Controller  

---

# 2. Repository Structure

The repository contains the following important components:

dataset/
    synthetic_ns3_dataset.csv

README.md
DATASET.md
REPRODUCIBILITY.md
requirements.txt

The dataset folder contains the sample dataset used for congestion prediction experiments.

---

# 3. Installing Dependencies

Install the required Python libraries:

pip install -r requirements.txt

Typical dependencies include:

- numpy
- pandas
- scikit-learn
- catboost
- matplotlib

---

# 4. Dataset Preparation

The dataset used for machine learning experiments is located in:

dataset/synthetic_ns3_dataset.csv

The dataset contains the following features:

- queue_length
- hop_count
- packet_drop_ratio
- round_trip_time
- bandwidth_utilization
- inter_arrival_time
- congestion_label

These features represent network traffic conditions used for congestion prediction.

---

# 5. Experiment Setup

Network simulations were conducted using the NS-3 simulator.

Simulation parameters include:

Number of nodes: 100–200  
Network topology: Grid, Random, Scale-Free  
Traffic model: CBR and Poisson traffic  
Packet size: 256–1024 bytes  
Mobility model: Random Waypoint  

These parameters emulate realistic network conditions.

---

# 6. Running Experiments

To reproduce the dataset-based analysis:

1. Load the dataset
2. Train the CatBoost congestion prediction model
3. Evaluate congestion classification performance
4. Use predictions to influence routing optimization decisions

Example workflow:

- Load dataset
- Train congestion prediction model
- Evaluate routing performance metrics

---

# 7. Performance Metrics

The following metrics were used to evaluate system performance:

- Throughput
- Packet Delivery Ratio (PDR)
- End-to-End Delay
- Packet Loss Rate
- Congestion Recovery Time

These metrics are commonly used in network congestion control research.

---

# 8. Reproducibility Notes

The dataset provided in this repository is a synthetic dataset generated using NS-3 simulations to illustrate the congestion prediction process.

Researchers can extend the experiments using larger datasets or real-world network traces such as CAIDA or MAWI.

---

# 9. Contact

For questions regarding experiment reproduction, please contact the repository author.
