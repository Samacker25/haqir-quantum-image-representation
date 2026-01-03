import streamlit as st
from classical_processing.preprocess import load_and_resize
from classical_processing.block_segmentation import split_blocks
from classical_processing.importance_score import importance_score
from qir_baselines.frqi import frqi_encode
from haqir.haqir_circuit import haqir_encode

st.set_page_config(page_title="HAQIR Demo", layout="centered")

st.title("HAQIR – Quantum Image Representation")
st.caption("NGO Internship Demo | Free Quantum Simulator")

uploaded = st.file_uploader("Upload a grayscale image", type=["jpg", "png", "jpeg"])

if uploaded:
    image = load_and_resize(uploaded)
    st.image(image, caption="Preprocessed Image (8×8)", width=200)

    blocks = split_blocks(image)
    scores = [importance_score(b) for b in blocks]

    method = st.selectbox("Choose Representation Method", ["FRQI", "HAQIR"])

    if st.button("Run Quantum Encoding"):
        if method == "FRQI":
            qc = frqi_encode(image)
        else:
            qc = haqir_encode(scores)

        st.subheader("Quantum Circuit")
        st.text(qc.draw())

        st.subheader("Encoding Metrics")
        st.write("Qubits Used:", qc.num_qubits)
        st.write("Circuit Depth:", qc.depth())
