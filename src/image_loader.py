import rasterio 


def load_raster(uploaded_file):
    """Read the uploaded GeoTIFF file using Rasterio """
    with rasterio.MemoryFile(uploaded_file.read()) as memfile:
        with memfile.open() as dataset:
            image=dataset.read()
            metadata={
                "width":dataset.width,
                "height":dataset.height,
                "bands":dataset.count,
                "crs":str(dataset.crs),
                "dtype":str(dataset.dtypes[0]),
                "nodata":dataset.nodata
            }

    return image,metadata