import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Otto Calculator Pro", page_icon="📈", layout="centered")

# --- INJEÇÃO DE CSS AVANÇADO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; color: #FFFFFF; }
    .stApp { background: radial-gradient(circle at top left, #0d1117 0%, #010409 100%); }
    
    .hero-card { background: linear-gradient(135deg, #EE4D2D 0%, #FF7337 100%); padding: 40px 20px; border-radius: 30px; text-align: center; box-shadow: 0 20px 40px rgba(238, 77, 45, 0.3); margin-bottom: 30px; }
    .hero-title { font-size: 3rem; font-weight: 900; margin: 0; text-transform: uppercase; }
    
    .input-title { font-size: 1.2rem; font-weight: 700; margin-top: 20px; color: #E2E8F0; }
    .money-highlight { color: #00FF88; }
    .tax-highlight { color: #FFD700; }
    .ads-highlight { color: #00E5FF; }

    .result-card { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 25px; padding: 20px; text-align: center; }
    .price-value { font-size: 2.2rem; font-weight: 900; display: block; margin-top: 10px; }
    
    .roas-card { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border: 2px solid #FFD700; border-radius: 20px; padding: 25px; margin-top: 20px; text-align: center; }
    
    div[data-baseweb="input"] { background-color: rgba(255, 255, 255, 0.05) !important; border-radius: 15px !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; color: white !important; }
    #MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 2. CABEÇALHO
st.markdown('<div class="hero-card"><h1 class="hero-title">CALCULADORA OTTO</h1></div>', unsafe_allow_html=True)

# 3. INPUTS
st.markdown('<p class="input-title money-highlight">💰 1. Custo Total (R$)</p>', unsafe_allow_html=True)
custo_produto = st.number_input("", min_value=0.0, step=1.0, format="%.2f", key="custo")

st.markdown('<p class="input-title tax-highlight">🏢 2. Imposto (%)</p>', unsafe_allow_html=True)
imposto_input = st.number_input("", min_value=0.0, max_value=100.0, value=0.0, step=0.1, format="%.1f", key="imposto")
aliquota_imposto = imposto_input / 100.0

st.markdown('<p class="input-title ads-highlight">📢 3. Custo Fixo de ADS (R$)</p>', unsafe_allow_html=True)
custo_ads_fixo = st.number_input("", min_value=0.0, step=0.5, format="%.2f", key="ads")

# 4. CÁLCULO
if st.button("CALCULAR ESTRATÉGIA 🚀", use_container_width=True):
    if custo_produto > 0:
        with st.spinner("Analisando métricas..."):
            time.sleep(0.6)
            
            # Cálculo de Preço e Margem
            preco_teste = custo_produto + custo_ads_fixo
            preco_18 = preco_25 = preco_30 = 0
            
            while preco_30 == 0:
                taxa_shopee = preco_teste * 0.14 + 20.00 # Média simplificada para o cálculo
                lucro = preco_teste - custo_produto - taxa_shopee - (preco_teste * aliquota_imposto) - custo_ads_fixo
                margem = lucro / preco_teste if preco_teste > 0 else 0
                
                if margem >= 0.18 and preco_18 == 0: preco_18 = preco_teste
                if margem >= 0.25 and preco_25 == 0: preco_25 = preco_teste
                if margem >= 0.30 and preco_30 == 0: preco_30 = preco_teste
                preco_teste += 0.10

            # Cálculo do Break-Even ROAS (Zero a Zero)
            # Fórmula: 1 / Margem de Contribuição
            margem_contribuicao = 1 - (taxa_shopee/preco_25) - aliquota_imposto
            roas_break_even = 1 / margem_contribuicao

            # 5. RESULTADOS
            col1, col2, col3 = st.columns(3)
            with col1: st.markdown(f'<div class="result-card"><span style="color:#FF4B2B;">AGRESSIVO</span><span class="price-value">R$ {preco_18:.2f}</span></div>', unsafe_allow_html=True)
            with col2: st.markdown(f'<div class="result-card"><span style="color:#00FF88;">EQUILIBRADO</span><span class="price-value">R$ {preco_25:.2f}</span></div>', unsafe_allow_html=True)
            with col3: st.markdown(f'<div class="result-card"><span style="color:#BD00FF;">PREMIUM</span><span class="price-value">R$ {preco_30:.2f}</span></div>', unsafe_allow_html=True)
            
            # Card de ROAS
            st.markdown(f"""
            <div class="roas-card">
                <h3 style="color:#FFD700; margin:0;">🎯 BREAK-EVEN ROAS</h3>
                <p style="font-size: 1.5rem; margin:10px 0;">Para não ter prejuízo no ADS, seu ROAS mínimo deve ser:</p>
                <b style="font-size: 3rem;">{roas_break_even:.2f}x</b>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("Cálculo pronto!")
    else:
        st.error("Insira o custo do produto.")
