import streamlit as st

st.set_page_config(
    page_title="Eagle Eye",
    page_icon="E",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.write("""
         #            Eagle Eye
         ####         detection de numeros de matricule   
         """
         )


file = st.sidebar.file_uploader("Veuillez importer une image", type=["jpg", "png"])

        
        


if file is not None:

    image = Image.open(file)
    st.image(image, use_column_width=True)
    
    if (st.sidebar.button('extraire le numero')):
         
        
            st.write("""
            ##  DL8CAF5030
             """)
      
    
        
  


