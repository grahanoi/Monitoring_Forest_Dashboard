import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import zipfile

# Extract the zip file
z = zipfile.ZipFile('images.zip')
# Extract all the contents of zip file in current directory to a new folder named 'data'
z.extractall('data')

# Load images
image_spring = mpimg.imread('data/median_ndvi_spring.jpg')
image_summer = mpimg.imread('data/median_ndvi_summer.jpg')
image_autumn = mpimg.imread('data/median_ndvi_autum.jpg')
image_winter = mpimg.imread('data/median_ndvi_winter.jpg')
image_mean = mpimg.imread('data/mean2023.jpg')

# Create a figure to hold the subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Set titles for the subplots
titles = ['Spring NDVI', 'Summer NDVI', 'Mean NDVI', 'Autumn NDVI', 'Winter NDVI', 'Mean NDVI']

# Plot each image in its corresponding subplot
axes[0, 0].imshow(image_spring)
axes[0, 0].set_title(titles[0])
axes[0, 0].axis('off')

axes[0, 1].imshow(image_summer)
axes[0, 1].set_title(titles[1])
axes[0, 1].axis('off')

axes[0, 2].imshow(image_mean)
axes[0, 2].set_title(titles[2])
axes[0, 2].axis('off')

axes[1, 0].imshow(image_autumn)
axes[1, 0].set_title(titles[3])
axes[1, 0].axis('off')

axes[1, 1].imshow(image_winter)
axes[1, 1].set_title(titles[4])
axes[1, 1].axis('off')

axes[1, 2].imshow(image_mean)
axes[1, 2].set_title(titles[5])
axes[1, 2].axis('off')

# Add a colorbar
fig.colorbar(axes[0, 0].imshow(image_spring), ax=axes, orientation='horizontal', fraction=0.05, pad=0.05, label='NDVI Value')

# Show the plot
plt.tight_layout()
plt.show()