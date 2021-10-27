import pydicom
from matplotlib import pyplot


dicom_path = input('path')
file = pydicom.read_file(dicom_path)
pyplot.imshow(file.pixel_array, cmap=pyplot.cm.bone)
pyplot.show()