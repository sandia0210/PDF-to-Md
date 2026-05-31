# 📄 PDF → Markdown

Convierte cualquier PDF a Markdown con drag & drop. Deploy gratuito en Streamlit Cloud.

## 🚀 Deploy en 5 minutos (Streamlit Cloud)

1. **Sube este repo a GitHub**
   ```bash
   git init
   git add .
   git commit -m "first commit"
   git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
   git push -u origin main
   ```

2. **Ve a [share.streamlit.io](https://share.streamlit.io)**
   - Inicia sesión con tu cuenta de GitHub
   - Clic en **"New app"**
   - Selecciona tu repositorio y rama (`main`)
   - En **"Main file path"** escribe: `app.py`
   - Clic en **"Deploy!"**

3. **¡Listo!** En ~2 minutos tendrás una URL pública tipo:
   `https://tu-usuario-tu-repo-app-xxxx.streamlit.app`

## 🖥️ Correr en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Estructura

```
.
├── app.py           # App principal
├── requirements.txt # Dependencias
└── README.md
```

## ⚙️ Tecnologías

- [Streamlit](https://streamlit.io) — UI web en Python puro
- [markitdown](https://github.com/microsoft/markitdown) — Conversión PDF → Markdown (by Microsoft)
