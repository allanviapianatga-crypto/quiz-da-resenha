import streamlit as st

st.title("🤣 QUIZ DA RESENHA 🔥")
st.write("Proibido ficar ofendidinho! KKKK")

nome = st.text_input("Qual é o seu nome?")

if nome.strip():
    st.success("Bem-vindo ao Quiz da Resenha, " + nome + "! 😂")

    st.header("PERGUNTA 1")
    st.write("Quem é o maior enrolador da turma?")

    resposta1 = st.radio(
        "Escolha uma alternativa:",
        [
            "A - O que diz que já está chegando",
            "B - O que nunca paga o churrasco",
            "C - O que só aparece quando tem comida",
            "D - Todos os anteriores KKKK"
        ],
        index=None,
        key="pergunta1"
    )

    st.header("PERGUNTA 2")
    st.write("Quem é o maior caloteiro do churrasco?")

    resposta2 = st.radio(
        "Escolha uma alternativa:",
        [
            "A - O que esqueceu o PIX",
            "B - O que só leva fome",
            "C - O que promete pagar depois",
            "D - O que come e desaparece"
        ],
        index=None,
        key="pergunta2"
    )

    st.header("PERGUNTA 3")
    st.write("Qual a frase mais dita no rolê?")

    resposta3 = st.radio(
        "Escolha uma alternativa:",
        [
            "A - Hoje eu vou de leve, amanhã tenho que acordar cedo",
            "B - Onde vai ser o esquenta?",
            "C - Manda a localização",
            "D - Ó, se eu quisesse?"
        ],
        index=None,
        key="pergunta3"
    )

    if st.button("🔥 VER RESULTADO DA RESENHA"):
        if resposta1 is None or resposta2 is None or resposta3 is None:
            st.warning("KKKK! Responde as três perguntas, figura!")
        else:
            pontos = 0

            if resposta1.startswith("A"):
                pontos += 10
                st.write("KKKK! Esse ainda está tomando banho!")
            elif resposta1.startswith("B"):
                pontos += 20
                st.write("Esse tem alergia a abrir a carteira!")
            elif resposta1.startswith("C"):
                pontos += 30
                st.write("Sentiu cheiro de churrasco e apareceu!")
            elif resposta1.startswith("D"):
                pontos += 40
                st.write("KKKK! Essa turma precisa de tratamento!")

            if resposta2.startswith("A"):
                pontos += 10
                st.write("KKKK! O PIX dele vive de férias!")
            elif resposta2.startswith("B"):
                pontos += 20
                st.write("Esse leva fome e volta com marmita!")
            elif resposta2.startswith("C"):
                pontos += 30
                st.write("Esse deve até para o calendário!")
            elif resposta2.startswith("D"):
                pontos += 40
                st.write("KKKK! Comeu, sumiu e bloqueou o grupo!")

            if resposta3.startswith("A"):
                pontos += 10
                st.write("KKKK! Sempre assim!")
            elif resposta3.startswith("B"):
                pontos += 20
                st.write("Na casa do Willian!")
            elif resposta3.startswith("C"):
                pontos += 30
                st.write("Dados não funcionam aqui!")
            elif resposta3.startswith("D"):
                pontos += 40
                st.write("KKKK! Tô confuso!")

            st.divider()
            st.header("🏆 RESULTADO FINAL DA RESENHA")
            st.write("Jogador:", nome)
            st.write("Pontuação final:", pontos)

            if pontos >= 70:
                st.success(nome + " - REI SUPREMO DA RESENHA! 🔥")
                st.write("Você não tem limites! KKKK")
            elif pontos >= 40:
                st.success(nome + " - REI DO DEBOCHE! 😂")
                st.write("Sua resenha já está dando trabalho!")
            else:
                st.success(nome + " - APRENDIZ DA ZOEIRA!")
                st.write("Precisa treinar mais no grupo! KKKK")
