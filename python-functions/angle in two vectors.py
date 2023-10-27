python3
#finding the angle between two vectors
angle=lambda x,y,t;np. arccos((x@y)/(np.linalg.norm(x)*np.linalg.norm(y)))
angle(m_a,l_a)

#writting a method in python
det lincomb(coef,vectors)
n=len(vectors)
comb=np.zeros(n)
for i in range(n)
comb=comb+coef(i)*vectors(i)

#MATRICES
m1=np.array([[-3,1,0.3],[np.sqrt(2),sqrt(6)],[-5,0,-10]])