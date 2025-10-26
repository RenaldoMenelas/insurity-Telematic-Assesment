import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"
HEADERS = {"Content-Type": "application/json"}  # add {"x-api-key":"dev-key"} if you enabled the key

# ---------- Simple brand-ish styling ----------
st.set_page_config(page_title="Telematics Pricing Demo", page_icon="🚗", layout="centered")
st.markdown("""
<style>
/* gradient header bar */
.header-strip {
  background: linear-gradient(90deg, #FFE6F4 0%, #F3E8FF 100%);
  border-radius: 16px; padding: 18px 22px; margin-bottom: 14px;
  border: 1px solid rgba(255,79,162,0.25);
}

/* callout cards */
.card {
  background: white;
  border: 1px solid rgba(17,24,39,0.08);
  border-radius: 16px;
  padding: 18px 16px; margin: 8px 0 14px 0;
  box-shadow: 0 4px 18px rgba(17,24,39,0.06);
}

/* buttons & sliders to match pink */
.stButton>button {
  border-radius: 999px;
  padding: 10px 18px;
  border: 1px solid #FF4FA2;
  background: #FF4FA2;
  color: white; font-weight: 600;
}
.stButton>button:hover {
  filter: brightness(0.95);
}
.stSlider > div[data-baseweb="slider"] div[role="slider"] {
  box-shadow: 0 0 0 4px rgba(255,79,162,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="header-strip"><h2 style="margin:0;color:#111827;">Insurity-style Telematics Pricing</h2><p style="margin:6px 0 0 0;color:#6B7280;">Usage-based risk scoring → dynamic premium</p></div>', unsafe_allow_html=True)

# ---------- Inputs ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Driver inputs")
col1, col2 = st.columns(2)
with col1:
    avg_speed = st.slider("Average speed (mph)", 30, 100, 60, help="Typical cruising speed")
    harsh_brakes = st.slider("Harsh brakes (count)", 0, 15, 2, help="Detected abrupt decelerations")
with col2:
    night_drive = st.checkbox("Driving at night?", value=False, help="Counts more risk if enabled")
    distance_miles = st.slider("Distance (miles)", 0, 300, 100, help="Trip or period mileage")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Action ----------
if st.button("Calculate premium"):
    payload = {
        "avg_speed": avg_speed,
        "harsh_brakes": harsh_brakes,
        "night_drive": night_drive,        # boolean True/False
        "distance_miles": distance_miles
    }
    try:
        r = requests.post(API_URL, json=payload, headers=HEADERS, timeout=10)
        if r.ok:
            result = r.json()
            risk = result["risk_score"]
            prem = result["premium"]

            # result card
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Result")
            colA, colB = st.columns(2)
            with colA:
                st.metric(label="Risk score", value=f"{risk:.2f}")
            with colB:
                st.metric(label="Monthly premium", value=f"${prem:.2f}")
            # simple label
            label = "Safe Driver" if risk < 37 else ("Moderate" if risk < 90 else "High Risk")
            badge_color = "#10B981" if label=="Safe Driver" else ("#F59E0B" if label=="Moderate" else "#EF4444")
            st.markdown(f"<span style='background:{badge_color};color:white;padding:6px 10px;border-radius:999px;font-weight:600;'>{label}</span>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error(f"API error: {r.status_code} – {r.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Could not reach API at {API_URL}. Is FastAPI running? {e}")

# ---------- Footer ----------
st.caption("Prototype for demonstration only • Parameters and corridor caps are configurable")
