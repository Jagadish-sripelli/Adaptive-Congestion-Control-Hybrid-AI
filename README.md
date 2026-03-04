# Adaptive-Congestion-Control-Hybrid-AI
Research implementation of a hybrid AI-based congestion control framework integrating bio-inspired optimization and machine learning for scalable QoS optimization in SDN, IoT, and 5G networks.
# Hybrid AI Framework for Adaptive Congestion Control

This repository contains the implementation, datasets, and experimental setup for the research paper:

**"A Hybrid Bio-Inspired and Machine Learning Framework for Adaptive Congestion Control and QoS Optimization in Modern Networks"**

The proposed system integrates bio-inspired optimization algorithms with machine learning to improve network congestion control and Quality of Service (QoS) in dynamic and heterogeneous environments.

---

## Overview

Modern networks face increasing congestion due to the growth of IoT devices, cloud computing, and real-time applications. Traditional congestion control mechanisms struggle to adapt to highly dynamic traffic conditions.

This project proposes a **hybrid intelligent framework** combining:

- Genetic Algorithm (GA)
- Ant Colony Optimization (ACO)
- CatBoost Machine Learning
- Q-learning Reinforcement Learning

to dynamically optimize routing and network resource allocation.

---

## System Architecture

The framework consists of four main modules:

1. **Bio-Inspired Optimization Layer**
   - Genetic Algorithm (GA)
   - Ant Colony Optimization (ACO)

2. **Machine Learning Prediction Layer**
   - CatBoost model for congestion prediction

3. **Reinforcement Learning Layer**
   - Q-learning agents for adaptive routing decisions

4. **Hybrid Decision Engine**
   - Combines outputs from optimization and learning modules.

---

## Repository Structure


Hybrid-AI-Congestion-Control
│
├── dataset
│ ├── synthetic_traffic.csv
│ ├── caida_trace.csv
│ └── mawi_trace.csv
│
├── models
│ ├── catboost_model.json
│ └── qlearning_model.pkl
│
├── src
│ ├── ga_optimizer.py
│ ├── aco_routing.py
│ ├── congestion_predictor.py
│ ├── q_learning_agent.py
│ └── hybrid_engine.py
│
├── experiments
│ ├── run_grid_topology.sh
│ ├── run_random_topology.sh
│ └── run_scale_free.sh
│
├── results
│ ├── throughput_results.csv
│ ├── latency_results.csv
│ └── figures
│
└── README.md


---

## Dataset

The dataset used for congestion prediction includes features such as:

- Queue length
- Hop count
- Packet drop ratio
- Round-trip time
- Bandwidth utilization
- Congestion label

Datasets were generated using **NS-3 simulations** and enhanced using real network traffic traces from:

- CAIDA
- MAWI

---

## Installation

Clone the repository:
