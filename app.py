import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Ortho Force Calculator",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for high-quality professional UI
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stAlert {
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf, #2e7bcf);
        color: white;
    }
    h1, h2, h3 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
col_head1, col_head2 = st.columns([1, 8])
with col_head1:
    st.image("https://img.icons8.com/fluency/96/tooth.png", width=80)
with col_head2:
    st.title("Ortho Force Calculator")
    st.markdown("*Advanced Biomechanical Simulation Engine by Dr. Ajay K. Kubavat*")

st.divider()

# --- SYNTHETIC DATA GENERATOR ---
def get_force_curve(material, size, max_deflection=4.0):
    deflection_points = np.linspace(0, max_deflection, 100)
    stiffness_factors = {
        "0.012": 0.5, "0.014": 0.8, "0.016": 1.2, "0.018": 1.8,
        "16x22": 2.5, "17x25": 3.0, "19x25": 4.5, "21x25": 6.0
    }
    factor = stiffness_factors.get(size, 1.0)
    
    # Material specific physics simulation
    if material == "Stainless Steel (SS)":
        forces = (160 * factor) * deflection_points
    elif material in ["NiTi", "CuNiTi"]:
        # Sigmoid function to simulate the superelastic plateau
        forces = (90 * factor) * (1 - np.exp(-2.2 * deflection_points))
    elif material == "TMA":
        forces = (110 * factor) * deflection_points
    else: # Default/Elgiloy/etc
        forces = (130 * factor) * deflection_points
        
    return pd.DataFrame({"Deflection_mm": deflection_points, "Force_g": forces})

# --- SIDEBAR: CONTROL CENTER ---
st.sidebar.image("https://img.icons8.com/fluency/48/settings.png", width=30)
st.sidebar.header("Biomechanical Settings")

slot_size = st.sidebar.radio("Slot Size (inches)", ["0.022", "0.018"], horizontal=True)
bracket_system = st.sidebar.selectbox("Bracket System", 
    ["Conventional (Elastic)", "Passive Self-Ligating (e.g., Damon)", "Active Self-Ligating"])

material = st.sidebar.selectbox("Wire Material", 
    ["NiTi", "Stainless Steel (SS)", "CuNiTi", "TMA", "Elgiloy", "Multi-strand Coaxial"])

cross_section = st.sidebar.radio("Cross-Section", ["Round", "Rectangular"], horizontal=True)

if cross_section == "Round":
    wire_sizes = ["0.010", "0.012", "0.014", "0.016", "0.018", "0.020"]
else:
    if slot_size == "0.018":
        wire_sizes = ["16x22", "17x25"]
    else:
        wire_sizes = ["16x22", "17x25", "18x25", "19x25", "21x25"]

size = st.sidebar.select_slider("Select Wire Size", options=wire_sizes)

st.sidebar.divider()
deflection_input = st.sidebar.slider("Current Deflection (mm)", 0.0, 4.0, 1.5, 0.1)

# --- CALCULATION ENGINE ---
df_curve = get_force_curve(material, size)
current_force = np.interp(deflection_input, df_curve["Deflection_mm"], df_curve["Force_g"])

# Friction & Binding Logic
binding_risk = "Low"
color_map = {"Low": "green", "Moderate": "orange", "High": "red"}

if slot_size == "0.022" and size in ["19x25", "21x25"]:
    binding_risk = "High"
elif slot_size == "0.018" and size == "17x25":
    binding_risk = "High"
elif cross_section == "Rectangular":
    binding_risk = "Moderate"

# --- MAIN DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Estimated Force", f"{int(current_force)} g", delta=None)
with col2:
    st.metric("Binding Risk", binding_risk, delta_color="inverse")
with col3:
    status = "Physiologic" if 50 <= current_force <= 150 else "Sub-optimal" if current_force < 50 else "Traumatic"
    st.metric("Force Status", status)

st.divider()

tab1, tab2, tab3 = st.tabs(["📊 Biomechanical Analytics", "⚙️ Technical Specs", "📜 Clinical Insights"])

with tab1:
    chart_col1, chart_col2 = st.columns([1, 1])
    
    with chart_col1:
        st.subheader("Active Force Gauge")
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = current_force,
            domain = {'x': [0, 1], 'y': [0, 1]},
            gauge = {
                'axis': {'range': [None, 600], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#1e3a8a"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': '#e5e7eb'},
                    {'range': [50, 150], 'color': '#86efac'}, # Optimal
                    {'range': [150, 250], 'color': '#fef08a'}, # Warning
                    {'range': [250, 600], 'color': '#fca5a5'}  # Danger
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 250
                }
            }
        ))
        fig_gauge.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with chart_col2:
        st.subheader("Load-Deflection Profile")
        fig_curve = go.Figure()
        
        # Plot the curve
        fig_curve.add_trace(go.Scatter(
            x=df_curve["Deflection_mm"], 
            y=df_curve["Force_g"],
            mode='lines',
            line=dict(color='#3b82f6', width=4),
            fill='tozeroy',
            fillcolor='rgba(59, 130, 246, 0.1)'
        ))
        
        # Plot current position
        fig_curve.add_trace(go.Scatter(
            x=[deflection_input], 
            y=[current_force],
            mode='markers+text',
            text=[f"{int(current_force)}g"],
            textposition="top center",
            marker=dict(color='#ef4444', size=15, symbol="diamond")
        ))
        
        fig_curve.update_layout(
            xaxis_title="Deflection (mm)",
            yaxis_title="Force (grams)",
            plot_bgcolor='white',
            margin=dict(l=20, r=20, t=50, b=20),
            height=350,
            showlegend=False
        )
        fig_curve.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f3f4f6')
        fig_curve.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f3f4f6')
        
        st.plotly_chart(fig_curve, use_container_width=True)

with tab2:
    st.subheader("Hardware Combination Analysis")
    specs_col1, specs_col2 = st.columns(2)
    with specs_col1:
        st.write(f"**Slot Clearance:** {0.022 - float(size.split('x')[0])/1000 if 'x' in size else 'N/A'}")
        st.write(f"**Material Modulus:** {'High' if material == 'Stainless Steel (SS)' else 'Low/Superelastic'}")
    with specs_col2:
        st.write(f"**Ligation Friction:** {'Minimal' if 'Self-Ligating' in bracket_system else 'High'}")
        st.write(f"**Critical Contact Angle:** {'Approaching' if binding_risk == 'High' else 'Optimal'}")

with tab3:
    st.info("💡 **Clinical Tip:** For initial leveling and aligning, aim for the green zone (50g - 150g). Excessive force can lead to root resorption and hyalinization.")
    if binding_risk == "High":
        st.error("⚠️ **Binding Alert:** This combination has high frictional resistance. Consider a smaller wire size or a passive self-ligating system to improve sliding efficiency.")
    elif material == "NiTi":
        st.success("✨ **Superelasticity:** This NiTi wire provides a nearly constant force over a wide range of deflection, ideal for early treatment phases.")

# --- FOOTER ---
st.divider()
st.caption(f"© 2026 Dr. Ajay K. Kubavat | Biomechanical Engineering & Orthodontics | All Rights Reserved")
