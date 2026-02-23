# 🦷 Ortho Force Calculator

## 📖 Overview
The **Ortho Force Calculator** is an interactive, data-driven web application designed to simulate and calculate biomechanical forces and frictional resistance in orthodontic mechanics. Traditional orthodontic force estimation relies heavily on clinical intuition. This application bridges the gap between materials science, classical physics, and clinical orthodontics. By inputting specific hardware variables (wire material, cross-section, slot size, and ligation type), the application dynamically calculates the active force delivered to the periodontal ligament (PDL) and flags potential binding or high-friction scenarios. Designed by an Orthodontist and AI expert, this tool serves as both a clinical reference utility and a robust educational framework for postgraduate and PhD orthodontic programs to visualize complex load-deflection characteristics.

## ✨ Key Features
* **Dynamic Force Estimation:** Calculates active force (in grams/centiNewtons) based on user-defined deflection and material stiffness.
* **Superelasticity Simulation:** Accurately models the non-linear, constant-force plateau (hysteresis) of NiTi and CuNiTi wires compared to the linear Hookean behavior of Stainless Steel and TMA.
* **Friction & Binding Alerts:** Evaluates the critical contact angle based on wire-to-slot clearance (e.g., 0.018 vs. 0.022 slots) and triggers warnings when heavy frictional binding is expected.
* **Ligation Degradation:** Accounts for force decay in conventional elastic modules versus passive/active self-ligating bracket systems.

## 💻 Tech Stack
* **Frontend:** Streamlit
* **Backend Logic:** Python 3
* **Data Processing & Visualization:** NumPy, Pandas, Plotly Graph Objects

## ⚠️ Clinical Disclaimer
This software is intended for educational, research, and informational purposes only. It is not a substitute for professional medical or dental judgment. The calculated forces are estimations based on ideal in-vitro conditions and may not perfectly reflect in-vivo biological responses. Always exercise clinical discretion.

---
**Copyright © 2026 Dr. Ajay K. Kubavat. All Rights Reserved.**
This repository is published for educational and academic viewing purposes only. No license is granted for the use, modification, reproduction, or distribution of this software or its underlying code.
