import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA (ESTILO MOTION DESIGN)
st.set_page_config(page_title="Otto Calculator Pro", page_icon="📈", layout="centered")

# --- INJEÇÃO DE CSS AVANÇADO ---
st.markdown("""
<style>
    /* Estética de Motion Design e Glassmorphism */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #FFFFFF;
    }

    .stApp {
        background: radial-gradient(circle at top left, #0d1117 0%, #010409 100%);
    }

    /* Card Gigante do Título (Estilo Shopee Motion) */
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

    /* Labels Estilizadas */
    .money-label {
        color: #00FF88;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 20px;
        animation: fadeInLeft 1s ease-out;
    }

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

    /* Animações Keyframes */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Customização dos Inputs */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 2. CABEÇALHO HERO
st.markdown("""
<div class="hero-card">
    <h1 class="hero-title">CALCULADORA OTTO</h1>
    <p class="hero-subtitle">Preços exatos para máximo controle operacional</p>
</div>
""", unsafe_allow_html=True)

# 3. ÁREA DE INPUTS (DESIGN LIMPO)
st.markdown('<p class="money-label">💰 Custo Total do Produto</p>', unsafe_allow_html=True)
custo_produto = st.number_input("", min_value=0.0, step=1.0, format="%.2f", help="Insira o custo de tecido + oficina")

st.markdown('<p style="font-size: 1.2rem; font-weight: 700; margin-top:20px;">🏢 Classe de Impostos</p>', unsafe_allow_html=True)
classe_imposto = st.radio("", ["MEI (Isento por venda)", "Simples Nacional (4%)"], horizontal=True)

# Lógica de ADS
st.markdown('<p style="font-size: 1.2rem; font-weight: 700; margin-top:20px;">📢 Investimento em ADS (Marketing)</p>', unsafe_allow_html=True)
st.info("O sistema reserva automaticamente 5% do valor da venda para custo de anúncios.")

# 4. MOTOR DE CÁLCULO
if st.button("CALCULAR MARGENS BLINDADAS 🚀", use_container_width=True):
    if custo_produto > 0:
        with st.spinner("Processando algoritmo financeiro..."):
            time.sleep(0.8)
            
            # Definir alíquota de imposto
            aliquota_imposto = 0.04 if "Simples" in classe_imposto else 0.0
            ads_percent = 0.05 # 5% fixo de ADS conforme solicitado
            
            preco_teste = custo_produto
            preco_18 = preco_25 = preco_30 = 0

            # Loop de Precificação Inteligente
            while preco_30 == 0:
                # Lógica de Taxas Shopee
                if preco_teste < 80.00:
                    taxa_shopee = (preco_teste * 0.20) + 4.00
                elif preco_teste < 100.00:
                    taxa_shopee = (preco_teste * 0.14) + 16.00
                elif preco_teste < 200.00:
                    taxa_shopee = (preco_teste * 0.14) + 20.00
                else:
                    taxa_shopee = (preco_teste * 0.14) + 26.00
                
                imposto = preco_teste * aliquota_imposto
                custo_ads = preco_teste * ads_percent
                
                # Cálculo de Lucro Líquido Real
                lucro = preco_teste - custo_produto - taxa_shopee - imposto - custo_ads
                margem_atual = lucro / preco_teste if preco_teste > 0 else 0
                
                if margem_atual >= 0.18 and preco_18 == 0:
                    preco_18 = preco_teste
                if margem_atual >= 0.25 and preco_25 == 0:
                    preco_25 = preco_teste
                if margem_atual >= 0.30 and preco_30 == 0:
                    preco_30 = preco_teste
                
                preco_teste += 0.05 # Incremento fino para precisão

            # 5. EXIBIÇÃO DE RESULTADOS (COLUNAS)
            st.markdown("<br><hr><br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#FF4B2B; font-weight:700;">AGRESSIVO (18%)</span>
                    <span class="price-value" style="color:#FF4B2B;">R$ {preco_18:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#00FF88; font-weight:700;">EQUILIBRADO (25%)</span>
                    <span class="price-value" style="color:#00FF88;">R$ {preco_25:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="result-card">
                    <span style="color:#BD00FF; font-weight:700;">PREMIUM (30%)</span>
                    <span class="price-value" style="color:#BD00FF;">R$ {preco_30:.2f}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.success("Cálculo finalizado com sucesso! Margens seguras.")
            st.balloons()
    else:
        st.error("Por favor, insira o custo inicial do produto.")
