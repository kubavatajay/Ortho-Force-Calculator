import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ortho Force Calculator", layout="wide")

# --- SYNTHETIC DATA GENERATOR (Simulating Instron Data) ---
def get_force_curve(material, size, max_deflection=4.0):
    deflection_points = np.linspace(0, max_deflection, 100)
    stiffness_factors = {
        "0.012": 0.5, "0.014": 0.8, "0.016": 1.2, "0.018": 1.8,
        "16x22": 2.5, "17x25": 3.0, "19x25": 4.5, "21x25": 6.0
    }
    factor = stiffness_factors.get(size, 1.0)
    if material == "Stainless Steel (SS)":
        forces = (150 * factor) * deflection_points
    elif material in ["NiTi", "CuNiTi"]:
        forces = (80 * factor) * (1 - np.exp(-2.5 * deflection_points))
    else:
        forces = (100 * factor) * deflection_points
    return pd.DataFrame({"Deflection_mm": deflection_points, "Force_g": forces})

# --- UI: SIDEBAR CONTROL PANEL ---
st.sidebar.title("⚙️ Control Panel")
st.sidebar.markdown("Configure your biomechanical setup.")
slot_size = st.sidebar.selectbox("Slot Size", ["0.022", "0.018"])
bracket_type = st.sidebar.selectbox("Ligation / Bracket Type", ["Conventional (Elastic)", "Passive Self-Ligating", "Active Self-Ligating"])
material = st.sidebar.selectbox("Wire Material", ["NiTi", "Stainless Steel (SS)", "CuNiTi", "TMA"])
cross_section = st.sidebar.selectbox("Cross-Section", ["Round", "Rectangular"])

if cross_section == "Round":
    wire_sizes = ["0.012", "0.014", "0.016", "0.018"]
else:
    if slot_size == "0.018":
        wire_sizes = ["16x22", "17x25"]
    else:
        wire_sizes = ["16x22", "17x25", "19x25", "21x25"]
size = st.sidebar.selectbox("Wire Size", wire_sizes)
st.sidebar.divider()
deflection_input = st.sidebar.slider("Current Crowding / Deflection (mm)", min_value=0.0, max_value=4.0, value=1.5, step=0.1)

# --- BACKEND LOGIC ---
df_curve = get_force_curve(material, size)
current_force = np.interp(deflection_input, df_curve["Deflection_mm"], df_curve["Force_g"])
binding_warning = False
if slot_size == "0.022" and size in ["19x25", "21x25"]:
    binding_warning = True
elif slot_size == "0.018" and size == "17x25":
    binding_warning = True

# --- UI: MAIN DASHBOARD ---
st.title("🦷 Ortho Force Calculator")
st.markdown(f"**Setup:** {size} {material} in {slot_size} {bracket_type} bracket")
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Active Force Output")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_force,
        title = {'text': "Force on PDL (grams)"},
        gauge = {
            'axis': {'range': [None, 1000]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 150], 'color': "lightgreen"},
                {'range': [150, 250], 'color': "yellow"},
                {'range': [250, 1000], 'color': "red"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 250}
        }
    ))
    st.plotly_chart(fig_gauge, use_container_width=True)
    if binding_warning:
        st.error("⚠️ **High Binding Risk:** Wire cross-section is near slot capacity. The critical contact angle will be reached quickly.")
    elif bracket_type == "Conventional (Elastic)":
        st.warning("⏱️ **Friction Note:** Elastic modules add 50-150g of normal force initially, decaying by ~50% in 3 weeks.")
    else:
        st.success("✅ **Low Friction:** Setup allows for relatively unimpeded sliding mechanics.")

with col2:
    st.subheader("Load-Deflection Curve")
    fig_curve = go.Figure()
    fig_curve.add_trace(go.Scatter(x=df_curve["Deflection_mm"], y=df_curve["Force_g"], mode='lines', name=f'{size} {material}', line=dict(color='blue', width=3)))
    fig_curve.add_trace(go.Scatter(x=[deflection_input], y=[current_force], mode='markers', name='Current Deflection', marker=dict(color='red', size=12)))
    fig_curve.update_layout(xaxis_title="Deflection (mm)", yaxis_title="Force (grams)", showlegend=False, hovermode="x")
    st.plotly_chart(fig_curve, use_container_width=True)
