import streamlit as st
import tempfile
import os
from markitdown import MarkItDown

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="PDF → Markdown",
    page_icon="📄",
    layout="centered",
)

# ── Estilos personalizados ────────────────────────────────────────────────────
st.markdown("""
<style>
    .stApp { max-width: 760px; margin: auto; }
    .title  { font-size: 2.4rem; font-weight: 800; margin-bottom: 0; }
    .sub    { color: #888; margin-top: 0; margin-bottom: 2rem; }
    .badge  {
        display: inline-block;
        background: #f0f0f0;
        border-radius: 6px;
        padding: 2px 10px;
        font-size: 0.8rem;
        color: #555;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="title">📄 PDF → Markdown</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Sube un PDF y obtén Markdown listo para usar.</p>', unsafe_allow_html=True)

# ── Upload ────────────────────────────────────────────────────────────────────
uploaded = st.file_uploader(
    "Arrastra tu PDF aquí o haz clic para buscarlo",
    type=["pdf"],
    help="Solo archivos .pdf",
)

if uploaded:
    st.divider()
    
    # Guardar en archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded.read())
        tmp_path = tmp.name

    # Conversión
    with st.spinner("Convirtiendo..."):
        try:
            md_instance = MarkItDown()
            result = md_instance.convert(tmp_path)
            markdown_text = result.text_content
            success = True
        except Exception as e:
            st.error(f"❌ Error al convertir: {e}")
            success = False
        finally:
            os.unlink(tmp_path)  # Limpiar archivo temporal

    if success:
        # Métricas rápidas
        lines   = markdown_text.count("\n")
        words   = len(markdown_text.split())
        chars   = len(markdown_text)

        col1, col2, col3 = st.columns(3)
        col1.metric("Líneas",    f"{lines:,}")
        col2.metric("Palabras",  f"{words:,}")
        col3.metric("Caracteres",f"{chars:,}")

        st.divider()

        # Tabs: preview + raw
        tab_preview, tab_raw = st.tabs(["👁️ Vista previa", "📋 Markdown raw"])

        with tab_preview:
            st.markdown(markdown_text, unsafe_allow_html=False)

        with tab_raw:
            st.code(markdown_text, language="markdown")

        st.divider()

        # Botón de descarga
        nombre_salida = os.path.splitext(uploaded.name)[0] + ".md"
        st.download_button(
            label="⬇️ Descargar .md",
            data=markdown_text.encode("utf-8"),
            file_name=nombre_salida,
            mime="text/markdown",
            use_container_width=True,
            type="primary",
        )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Powered by [markitdown](https://github.com/microsoft/markitdown) · Deploy gratis en [Streamlit Cloud](https://streamlit.io/cloud)")
