def linearsearchproduct(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices
products = ["computer", "cpu", "computer", "memorycard", "computer"]
target ="computer"
result = linearsearchproduct(products, target)
print(result)