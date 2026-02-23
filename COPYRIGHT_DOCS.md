# Indian Copyright Application Materials

This document contains the formally drafted annexures for the Indian Copyright application for the "Ortho Force Calculator" software, as created by Dr. Ajay K. Kubavat.

## ANNEXURE I: SYNOPSIS & INTRODUCTION

**Title of the Work:** Ortho Force Calculator  
**Nature of Work:** Computer Programme (Literary Work)  
**Author & Applicant:** Dr. Ajay K. Kubavat

### 1. Introduction
The "Ortho Force Calculator" is an original, interactive, and data-driven proprietary software application designed to simulate, calculate, and visualize biomechanical forces and frictional resistance in orthodontic mechanics. Traditional force estimation in orthodontic treatment relies heavily on subjective clinical intuition. This software bridges the gap between materials science, classical physics, and clinical orthodontics by providing an objective, algorithmic framework to calculate active forces delivered to the periodontal ligament (PDL).

### 2. Purpose of the Software
The primary objective of this computer programme is to serve as both a predictive clinical utility and an advanced educational framework. It empowers postgraduate orthodontic residents, PhD scholars, and educators to visualize complex load-deflection characteristics and critical contact angles, thereby elevating the standard of orthodontic biomechanics education and clinical planning.

## ANNEXURE II: TECHNICAL DESCRIPTION

### 1. Software Architecture and Environment
* **Frontend Interface:** Developed using the Streamlit framework to provide a responsive, web-based graphical user interface (GUI).
* **Backend Logic & Algorithmic Engine:** Programmed in Python 3. The logic utilizes custom-defined mathematical models to simulate generalized material properties of orthodontic wires.
* **Data Processing:** Utilizes NumPy and Pandas libraries for rapid interpolation of user-defined variables against simulated 3-point bending test datasets.
* **Data Visualization:** Integrates Plotly Graph Objects to render real-time, dynamic load-deflection curves and active force gauges.

### 2. Core Algorithmic Functions
The proprietary logic of the Ortho Force Calculator executes the following biomechanical evaluations:
* **Dynamic Force Estimation:** Calculates the active force (measured in grams or centiNewtons) based on user-defined deflection inputs and material stiffness multipliers.
* **Superelasticity Simulation:** Differentiates between the linear Hookean behavior of rigid materials (e.g., Stainless Steel, TMA) and the non-linear, constant-force plateau (hysteresis) of superelastic materials (e.g., NiTi, CuNiTi) using exponential decay modeling.
* **Frictional Binding Evaluation:** Cross-references wire cross-sections with bracket slot dimensions (0.018-inch vs. 0.022-inch) to predict the critical contact angle, triggering algorithmic warnings when high frictional binding is expected.
* **Ligation Degradation Logic:** Adjusts expected force profiles based on the selected ligation method, accounting for the rapid decay of conventional elastic modules compared to passive self-ligating systems.

## ANNEXURE III: OPERATING INSTRUCTIONS (USER MANUAL)

### 1. Initialization
The application is deployed via a web browser interface. Upon launching the programme, the user is presented with a bipartite screen consisting of a "Control Panel" (Inputs) and a "Biomechanical Dashboard" (Outputs).

### 2. Step-by-Step Execution
* **Step 1: Define Bracket Parameters.** The user selects the desired bracket 'Slot Size' (0.018 or 0.022) and 'Ligation Type' from the respective drop-down menus.
* **Step 2: Select Wire Metallurgy.** The user selects the 'Wire Material' (e.g., Stainless Steel, NiTi) and the 'Cross-Section' (Round or Rectangular).
* **Step 3: Define Wire Dimensions.** Based on the prior selections, the software dynamically populates compatible 'Wire Sizes'. The user selects the required dimension.
* **Step 4: Input Clinical Deflection.** The user adjusts the 'Crowding/Deflection' slider (ranging from 0.0 mm to 4.0 mm) to simulate the required clinical tooth movement.

### 3. Output Interpretation
Upon inputting the variables, the algorithmic engine instantaneously updates the Biomechanical Dashboard:
* **Active Force Output:** Displays a gauge indicating the exact force on the PDL, color-coded for safety (Green for optimal physiologic force, Red for risk of hyalinization).
* **Load-Deflection Curve:** Plots a real-time line graph of the selected wire's mechanical behavior, plotting the current deflection point on the curve.
* **System Alerts:** Displays automated warnings regarding friction, binding risks, and force decay based on the hardware combination.

## ANNEXURE IV: AUTHORSHIP & PROPRIETARY CLAIM

This software, including its underlying logic, mathematical models, user interface design, and source code, is the sole intellectual property of Dr. Ajay K. Kubavat. As an Orthodontist, senior professor, program director for postgraduate and PhD programs, and an AI expert, the author synthesized specialized domain knowledge in clinical orthodontics, biomechanical engineering, and artificial intelligence to conceive and develop this original literary work.
