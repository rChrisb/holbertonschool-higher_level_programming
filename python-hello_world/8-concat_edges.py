#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str[str.index("object"): str.index("language")] +
      str[str.index("with"): str.index("very")] +
      str[str.index("Py"): str.index("is")])
