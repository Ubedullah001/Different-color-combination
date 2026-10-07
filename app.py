import streamlit as st

st.set_page_config(
    page_title="Textile Color App",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Textile Color Combination & LAB Color App")
st.write("Explore RGB colors, color combinations, and LAB colors.")

# ---------- Functions ----------

def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(
        int(r), int(g), int(b)
    )


def rgb_to_lab(r, g, b):
    # RGB to LAB conversion
    r = r / 255
    g = g / 255
    b = b / 255

    def linear(c):
        if c > 0.04045:
            return ((c + 0.055) / 1.055) ** 2.4
        return c / 12.92

    r = linear(r)
    g = linear(g)
    b = linear(b)

    x = (r * 0.4124564 + g * 0.3575761 + b * 0.1804375) / 0.95047
    y = (r * 0.2126729 + g * 0.7151522 + b * 0.0721750)
    z = (r * 0.0193339 + g * 0.1191920 + b * 0.9503041) / 1.08883

    def f(t):
        if t > (6 / 29) ** 3:
            return t ** (1 / 3)
        return t / (3 * (6 / 29) ** 2) + 4 / 29

    fx = f(x)
    fy = f(y)
    fz = f(z)

    L = 116 * fy - 16
    a = 500 * (fx - fy)
    lab_b = 200 * (fy - fz)

    return L, a, lab_b


def lab_to_rgb(L, a, b):
    # LAB to RGB conversion

    fy = (L + 16) / 116
    fx = fy + a / 500
    fz = fy - b / 200

    delta = 6 / 29

    def inverse_f(t):
        if t > delta:
            return t ** 3
        return 3 * delta ** 2 * (t - 4 / 29)

    x = 0.95047 * inverse_f(fx)
    y = inverse_f(fy)
    z = 1.08883 * inverse_f(fz)

    r = (
        x * 3.2404542
        + y * -1.5371385
        + z * -0.4985314
    )

    g = (
        x * -0.9692660
        + y * 1.8760108
        + z * 0.0415560
    )

    blue = (
        x * 0.0556434
        + y * -0.2040259
        + z * 1.0572252
    )

    def gamma(c):
        if c > 0.0031308:
            return 1.055 * (max(c, 0) ** (1 / 2.4)) - 0.055
        return 12.
