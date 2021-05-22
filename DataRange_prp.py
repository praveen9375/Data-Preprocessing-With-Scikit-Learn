#The exercise here uses MinMaxScaler (imported in backend) to complete the ranged_data function.
#The function will compress the input NumPy array, data, into the range given by value_range.
def ranged_data(data, value_range):
  min_max_scaler = MinMaxScaler(feature_range = value_range)
  scaled_data = min_max_scaler.fit_transform(data)
  return scaled_data
