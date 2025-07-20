import streamlit as st

st.set_page_config(page_title="Bit Switches", layout="centered")
st.title(" Flip the Bits!")

st.markdown("Toggle the bits below. Each one adds to the total based on place value.")

place_values = [128, 64, 32, 16, 8, 4, 2, 1]
bits = []

cols = st.columns(8)
for i, col in enumerate(cols):
    bit = col.checkbox(f"{place_values[i]}", key=i)
    bits.append(1 if bit else 0)

binary_str = ''.join(str(b) for b in bits)
decimal_value = sum([b * v for b, v in zip(bits, place_values)])

st.markdown(f"### Binary: `{binary_str}`")
st.markdown(f"### Decimal: **{decimal_value}**")
