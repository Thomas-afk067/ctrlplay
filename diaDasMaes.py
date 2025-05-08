import streamlit as st 

st.set_page_config(page_title="Dia das Mães", page_icon="👩🏻")
st.title("❤❤ feliz Dia das Mães ❤❤")
nome=st.text_input("Digite o nome da sua mãe:")

if st.button("mostrar mensagem"):
    if nome:
        st.success(f"Parabéns {nome} você é uma mãe incrivel")
        st.balloons()
    else:
        st.warning("Digite o nome da sua mãe")

st.image("https://s.calendarr.com/upload/90/a4/dia-das-maes-f.png",use_container_width=True)
