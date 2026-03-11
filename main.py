import streamlit as st

st.title("Cientista Regressa à Escola")
st.write("Estremoz, 2006: if-else conditions")


tree_string = """Tem coluna vertebral?
├── Não
│   └── Invertebrado
│
└── Sim
    └── Tem pelo?
        ├── Sim
        │   └── Mamífero
        │
        └── Não
            └── Tem penas?
                ├── Sim
                │   └── Ave
                │
                └── Não
                    └── Pele húmida?
                        ├── Sim
                        │   └── Anfíbio
                        │
                        └── Não
                            ├── Tem escamas?
                            │   ├── Sim
                            │   │   └── Vive apenas na água?
                            │   │       ├── Sim
                            │   │       │   └── Peixe
                            │   │       │
                            │   │       └── Não
                            │   │           └── Réptil
                            │   │
                            │   └── Não
                            │       └── Outro
                            └── Não
                                └── (Outro)
"""

option_tree_diagram = st.selectbox(
    "Mostrar árvore de classificação?",
    ["Sim", "Não"],
    index=1
)

if option_tree_diagram == "Sim":
    st.code(tree_string)
    
    
    

tree_code="""
if tem_coluna_vertebral == "não":
    animal = "Invertebrado"

else:
    if tem_pelo == "sim":
        animal = "Mamífero"

    else:
        if tem_penas == "sim":
            animal="Ave"

        else:
            if tem_pele_humida == "sim":
                animal="Anfíbio"

            else:
                if tem_escamas == "sim":

                    if vive_apenas_na_agua == "sim":
                        animal="Peixe"

                    else:
                        animal="Réptil"

                else:
                    animal="Outro"
"""
    
option_code = st.selectbox(
    "Mostrar código",
    ["Sim", "Não"],
    index=1
)

if option_code == "Sim":
    st.code(tree_code)
    
        
        
st.divider()
st.subheader("Classificar um animal")

tem_coluna_vertebral = st.selectbox("Tem coluna vertebral?", ["sim", "não"])
tem_pelo = st.selectbox("Tem pelo?", ["sim", "não"])
tem_penas = st.selectbox("Tem penas?", ["sim", "não"])
tem_pele_humida = st.selectbox("Tem pele húmida?", ["sim", "não"])
tem_escamas = st.selectbox("Tem escamas?", ["sim", "não"])
vive_apenas_na_agua = st.selectbox("Vive apenas na água?", ["sim", "não"])


if st.button("Classificar animal"):

    if tem_coluna_vertebral == "não":
        animal = "Invertebrado"

    else:
        if tem_pelo == "sim":
            animal = "Mamífero"

        else:
            if tem_penas == "sim":
                animal="Ave"

            else:
                if tem_pele_humida == "sim":
                    animal="Anfíbio"

                else:
                    if tem_escamas == "sim":

                        if vive_apenas_na_agua == "sim":
                            animal="Peixe"

                        else:
                            animal="Réptil"

                    else:
                        animal="Outro"

    st.success(f"O animal é: **{animal}**")