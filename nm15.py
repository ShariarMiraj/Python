# (NUMpy) Linear algebra
import numpy  as np 

a = np.array([[1,2] , [3,4]])
eigenvalues , eigenvectors = np.linalg.eig(a)
print(a)

print(eigenvalues)
print(eigenvectors)  #colum vector

# eigenvactor*eigenvalues = a * eigvector


b = eigenvectors[:,0] * eigenvalues[0]
print(b)

c = a @ eigenvectors[:,0]
print(c)

#  cheking to cerify b and c are right 
# print(b==c)
print(np.allclose(b,c))