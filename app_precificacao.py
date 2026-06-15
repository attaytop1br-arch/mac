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

st.markdown('<p class="input-title tax-highlight">🏢 2. Regime Tributário (Receita Federal)</p>', unsafe_allow_html=True)
opcoes_imposto = {
    "MEI - Microempreendedor Individual (0% no faturamento)": 0.0,
    "Simples Nacional - Faixa 1 (Até R$ 180 mil/ano) ➔ 4.0%": 0.04,
    "Simples Nacional - Faixa 2 (De R$ 180 mil a R$ 360 mil) ➔ 7.3%": 0.073,
    "Simples Nacional - Faixa 3 (De R$ 360 mil a R$ 720 mil) ➔ 9.5%": 0.095,
    "Simples Nacional - Faixa 4 (De R$ 720 mil a R$ 1.8 milhão) ➔ 10.7%": 0.107,
    "Simples Nacional - Faixa 5 (De R$ 1.8 milhão a R$ 3.6 milhões) ➔ 14.3%": 0.143,
    "Simples Nacional - Faixa 6 (De R$ 3.6 milhões a R$ 4.8 milhões) ➔ 19.0%": 0.19
}
selecao_imposto = st.selectbox("", list(opcoes_imposto.keys()), key="imposto")
aliquota_imposto = opcoes_imposto[selecao_imposto]

st.markdown('<p class="input-title ads-highlight">📢 3. Investimento em ADS (%)</p>', unsafe_allow_html=True)
ads_input = st.number_input("", min_value=0.0, max_value=100.0, value=5.0, step=0.5, format="%.1f", help="Porcentagem do preço final destinada a anúncios (Ex: 5.0 para 5%)", key="ads")
ads_percent = ads_input / 100.0

st.markdown("<br>", unsafe_allow_html=True)

# 4. MOTOR DE CÁLCULO FINANCEIRO
if st.button("CALCULAR MARGENS BLINDADAS 🚀", use_container_width=True):
    if custo_produto > 0:
        with st.spinner("Sincronizando alíquotas e calculando taxas..."):
            time.sleep(0.8)
            
            preco_teste = custo_produto
            preco_18 = preco_25 = preco_30 = 0

            # Loop de Precificação Bruta
            while preco_30 == 0:
                # Lógica de Taxas Oficiais da Shopee
                if preco_teste < 80.00:
                    taxa_shopee = (preco_teste * 0.20) + 4.00
                elif preco_teste < 100.00:
                    taxa_shopee = (preco_teste * 0.14) + 16.00
                elif preco_teste < 200.00:
                    taxa_shopee = (preco_teste * 0.14) + 20.00
                else:
                    taxa_shopee = (preco_teste * 0.14) + 26.00
                
                # Descontos variáveis aplicados sobre o preço de venda
                imposto_total = preco_teste * aliquota_imposto
                custo_ads = preco_teste * ads_percent
                
                # O que sobra limpo no bolso
                lucro_liquido = preco_teste - custo_produto - taxa_shopee - imposto_total - custo_ads
                margem_atual = lucro_liquido / preco_teste if preco_teste > 0 else 0
                
                # Travamento das margens alvo
                if margem_atual >= 0.18 and preco_18 == 0:
                    preco_18 = preco_teste
                if margem_atual >= 0.25 and preco_25 == 0:
                    preco_25 = preco_teste
                if margem_atual >= 0.30 and preco_30 == 0:
                    preco_30 = preco_teste
                
                preco_teste += 0.05 # Incremento fino para arredondamento preciso

            # 5. RENDERIZAÇÃO DOS CARDS
            st.markdown("<hr>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#FF4B2B; font-weight:700; font-size:1.1rem;">AGRESSIVO (18%)</span>
                    <span class="price-value" style="color:#FF4B2B;">R$ {preco_18:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#00FF88; font-weight:700; font-size:1.1rem;">EQUILIBRADO (25%)</span>
                    <span class="price-value" style="color:#00FF88;">R$ {preco_25:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#BD00FF; font-weight:700; font-size:1.1rem;">PREMIUM (30%)</span>
                    <span class="price-value" style="color:#BD00FF;">R$ {preco_30:.2f}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.success("Matemática validada! Seu lucro, impostos e tráfego estão garantidos nesses valores.")
            st.balloons()
    else:
        st.error("Insira o custo do produto para iniciarmos o cálculo.")
