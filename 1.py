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

def transform(image):
    
        size = (224,224)    
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, size, interpolation=cv2.INTER_CUBIC))/255.
        img_reshape = img_resize[np.newaxis,...]        
        return img_reshape

        
        


if file is not None:

    image = Image.open(file)
    transform(image)
    st.image(image, use_column_width=True)
    
    if (st.sidebar.button('extraire le numero')):
         
        
            st.write("""
            ##  DL8CAF5030
             """)
      
    
        
  


