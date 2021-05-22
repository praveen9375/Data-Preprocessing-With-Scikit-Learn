#The coding exercise here uses RobustScaler (imported in backend) to complete the robust_scaling function.
#The function will apply outlier-independent scaling to the input NumPy array, data.
def robust_scaling(data):
  robust_scaler = RobustScaler()
  scaled_data = robust_scaler.fit_transform(data)
  return scaled_data
