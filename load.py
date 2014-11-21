import os

_CUR_DIR = os.path.dirname(os.path.realpath(__file__))

def get_instances_from_directory(directory):
  """
  Get text instances that are put in a directory
  Arguments:
    - directory(str): the directory has a number of instances
    (each file is a different class)
  Returns:
    - X(list): text documents
    - y(list): labels as integers
    - label_names(list): label names as in the file name that has
    the instances
  """
  X = []
  y = []
  text_path = os.path.join(_CUR_DIR, directory)
  files = [ii for ii in os.listdir(text_path)] 
  label_names = [ii.split('.')[0] for ii in files]
  for ii, thefile in enumerate(files):
    input_path = os.path.join(directory, thefile)
    with open(input_path) as input_file:
      temp = input_file.readlines()
      temp = filter(lambda k: k.strip() != '' and k.strip(), temp)
      y += [ii] * len(temp) # Add labels with number of instances
      X += temp
  return X, y, label_names
