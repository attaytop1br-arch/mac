import streamlit as st

# Configura o visual da página
st.set_page_config(page_title="Motor de Precificação", page_icon="🛒")

st.title("Calculadora Otto - Shopee 🛒")
st.write("Insira os dados da sua produção para gerar os preços de venda ideais.")

# Troca o 'input' do terminal por uma caixa de digitação na tela
custo = st.number_input("Qual o custo total da peça? R$ ", min_value=0.0, step=1.0)

# Cria um botão na tela. O código abaixo só roda se o botão for clicado!
if st.button("Gerar Preços Inteligentes"):
    
    preco_teste = custo
    preco_18 = 0
    preco_25 = 0
    preco_30 = 0

    while preco_30 == 0:
        if preco_teste < 80.00:
            taxa = (preco_teste * 0.20) + 4.00
        elif preco_teste < 100.00:
            taxa = (preco_teste * 0.14) + 16.00
        elif preco_teste < 200.00:
            taxa = (preco_teste * 0.14) + 20.00
        else:
            taxa = (preco_teste * 0.14) + 26.00
            
        imposto = preco_teste * 0.06
        lucro = preco_teste - custo - taxa - imposto
        margem_atual = lucro / preco_teste if preco_teste > 0 else 0
        
        if margem_atual >= 0.18 and preco_18 == 0:
            preco_18 = preco_teste
        if margem_atual >= 0.25 and preco_25 == 0:
            preco_25 = preco_teste
        if margem_atual >= 0.30 and preco_30 == 0:
            preco_30 = preco_teste
            
        preco_teste += 0.10

    # Mostra os resultados em "cards" visuais bonitos (métricas)
    st.divider()
    st.subheader("Sugestões de Preço Final")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🔥 Agressivo (18%)", f"R$ {preco_18:.2f}")
    col2.metric("⚖️ Intermediário (25%)", f"R$ {preco_25:.2f}")
    col3.metric("💎 Premium (30%)", f"R$ {preco_30:.2f}")
