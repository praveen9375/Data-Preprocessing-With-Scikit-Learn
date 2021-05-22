#The coding exercise here uses PCA (imported in backend) to complete the pca_data function.
#The function will apply principal component analysis (PCA) to the input NumPy array, data.
def pca_data(data, n_components):
  pca_obj = PCA(n_components = (n_components))
  component_data = pca_obj.fit_transform(data)
  return component_data
