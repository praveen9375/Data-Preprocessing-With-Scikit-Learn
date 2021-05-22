#The coding exercise here uses Normalizer (imported in backend) to complete the normalize_data function.
#The function will apply L2 normalization to the input NumPy array, data.
def normalize_data(data):
  normalizer = Normalizer()
  norm_data = normalizer.fit_transform(data)
  return norm_data
