import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA (ESTILO MOTION DESIGN)
st.set_page_config(page_title="Otto Calculator Pro", page_icon="📈", layout="centered")

# --- INJEÇÃO DE CSS AVANÇADO ---
st.markdown("""
<style>
    /* Estética de Motion Design e Glassmorphism */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #FFFFFF;
    }

    .stApp {
        background: radial-gradient(circle at top left, #0d1117 0%, #010409 100%);
    }

    /* Card Gigante do Título */
    .hero-card {
        background: linear-gradient(135deg, #EE4D2D 0%, #FF7337 100%);
        padding: 50px 20px;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(238, 77, 45, 0.3);
        margin-bottom: 30px;
        animation: fadeInDown 0.8s ease-out;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
        letter-spacing: -2px;
        text-transform: uppercase;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 400;
    }

    /* Títulos dos Inputs */
    .input-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 5px;
        color: #E2E8F0;
        animation: fadeInLeft 0.8s ease-out;
    }
    
    .money-highlight { color: #00FF88; }
    .tax-highlight { color: #FFD700; }
    .ads-highlight { color: #00E5FF; }

    /* Cards de Resultado */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 1s ease-out;
    }

    .result-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 255, 136, 0.3);
    }

    .price-value {
        font-size: 2.8rem;
        font-weight: 900;
        display: block;
        margin-top: 10px;
    }

    /* Animações */
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-50px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInLeft { from { opacity: 0; transform: translateX(-30px); } to { opacity: 1; transform: translateX(0); } }

    /* Customização dos Campos do Streamlit */
    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 2. CABEÇALHO HERO
st.markdown("""
<div class="hero-card">
    <h1 class="hero-title">CALCULADORA OTTO</h1>
    <p class="hero-subtitle">Preços exatos para máximo controle operacional da Shopee</p>
</div>
""", unsafe_allow_html=True)

# 3. ÁREA DE INPUTS (DESIGN LIMPO E GRANDES FONTES)
st.markdown('<p class="input-title money-highlight">💰 1. Custo Total do Produto (R$)</p>', unsafe_allow_html=True)
custo_produto = st.number_input("", min_value=0.0, step=1.0, format="%.2f", help="Soma do tecido, confecção e aviamentos", key="custo")

st.markdown('<p class="input-title tax-highlight">🏢 2. Regime Tributário (Receita Federal)</p>', unsafe
