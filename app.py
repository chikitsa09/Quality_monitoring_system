import streamlit as st
from src.image_loader import load_raster
from src.preprocessing import normalize_image

st.set_page_config(
    page_title='Satellite Image Quality Monitoring',
    page_icon='🛰️',
    layout='wide'

)
st.title("Satellite Image Quality Monitoring System")
st.write("Upload a Satellite Image to analyze its Image quality")

uploaded_file=st.file_uploader(
    "upload satellite image",
    type=["tif","png","tiff","jpg","jpeg"]
)
if uploaded_file is not None:
    st.success(f"uploaded:{uploaded_file.name}")
    image,metadata=load_raster(uploaded_file)
    st.subheader("Image information")
    col1,col2,col3=st.columns(3)
    with col1:
        st.write("Width:",metadata['width'])
    with col2:
        st.write("height:",metadata['height'])
    with col3:
        st.write("bands:",metadata['bands'])
    st.write("CRS",metadata['crs'])
    st.write("data type",metadata['dtype'])
    st.write("nodata value",metadata["nodata"])

    display_image=normalize_image(image)
    st.subheader("satellite Image")
    if metadata['bands']>=3:
       rgb_image=display_image[:3]
       rgb_image=rgb_image.transpose(1,2,0)
       st.image(
        rgb_image,
        caption="uploaded Satellite Image",
        use_container_width=True
    )

    else:
       single_band=display_image[0]
       st.image(
        single_band,
        caption="uploaded satellite image",
        use_container_width=True
    )