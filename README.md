Satellite Image Quality Monitoring System
Overview

Satellite imagery is widely used in remote sensing ,Earth observation,enviromental monitoring ,agricultural ,disaster management,space technology.
However,the usability of satellite imagery can be affected by factore such as cloud coverage,noise,blur,poor contrast,overexposure and invalid or missing pixels.

The Satellite Image Quality Monitoring System is Python-based project designed to access satellite image quality using multiple image-quality and raster paramters.
The system analyzes an input satellite image,calculate quality metrics,generates an overall quality assessment and identifies spatial variations in image quality.

The project combines Python,OpenCV,Rasterio,Streamlit and QGIS to provide both numerical quality assessment and geospatial visualization.

---Key Features----
1.Multi-Parameter Image Quality Assessment

Instead of evaluating an image using only one metric, the system considers multiple parameters:

Cloud Coverage
Image Sharpness
Contrast
Noise Level
Brightness
NoData / Invalid Pixels

These parameters provide a broader assessment of the usability of satellite imagery.

2.Overall Quality Score

The individual quality parameters are normalized and combined to calculate an overall image quality score.
The image is then classified into categories such as:

Good
Moderate
Poor

The classification provides a simple way to interpret the overall quality of an image.

Quality Parameters
1. NoData / Invalid Pixels

The system identifies pixels that contain NoData or invalid values.
This helps determine whether missing pixel regions could affect subsequent image analysis.

2. Image Sharpness

Sharpness is used to estimate the level of image detail.
Low sharpness can indicate blurred imagery, while higher sharpness generally indicates greater edge/detail information.

3. Contrast

Contrast measures the difference between darker and brighter regions of the image.
Poor contrast can make features difficult to distinguish during image interpretation.

4. Brightness

Brightness is analyzed to identify images or regions that may be unusually dark or bright.
This can help identify potential underexposure or overexposure conditions.

5. Noise

Noise analysis helps identify unwanted variations in pixel values that may affect image interpretation and subsequent processing.

6. Cloud Coverage

Cloud-affected regions can reduce the usability of optical satellite imagery.
The system analyzes cloud coverage as one of the image-quality parameters and incorporates it into the quality assessment.


Technology Stack

-Python	:Core development and processing
-OpenCV	:Image processing and quality metrics
-Rasterio:	Raster and geospatial data processing
-NumPy	:Numerical and pixel-level computation
-Pandas	:Data handling and analysis
-Streamlit	:Interactive application interface
-QGIS	:Geospatial visualization and spatial analysis
-Matplotlib:	Visualization and graphical analysis

Applications

The system can be useful as a preliminary quality-control and screening tool for satellite imagery used in:

-Remote sensing
-GIS analysis
-Earth observation
-Agricultural monitoring
-Environmental monitoring
-Disaster management
-Satellite image processing
-Geospatial data analysis
-Space technology applications

