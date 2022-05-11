import random
import math
from matplotlib import pyplot as plot
#0x00200
			
sampleCount = 255#number of randomly generated data
dataSet = []
clusterSet = []
color = ["red", "brown", "green", "black"]
k = 4 #number of k-clusters
cluster_size = int(((sampleCount * k) - k )/k) #number of data points calculated per cluster
centroid = []
init_Centroid = [] #initialize values

#calculate distance of point Y from centroid K
def euclidean_distance(k,y):
	temp = tuple(map(lambda i,j: round(i - j,2), centroid[k],dataSet[y])) #i = centroid (x,y) j = datapoint (x,y ); therefore temp= [(x1 - x2), (y1-y2)]
	temp2 = tuple(map(lambda i: round(i*i,2) , temp)) # [(x1-x2)^2 ,(y1-y2)^2]
	temp3 = sum(list(temp2)) #sum of the squares (x1-x2)^2 + (y1-y2)^2
	temp4 = round(math.sqrt(temp3),2) #euclidean distance sqrt((x1-x2)^2 + (y1-y2)^2)]
	return temp4
#generate random x and y values for dataset
def generate_dataset(): 
	for i in range(sampleCount):
		x_randomValue = float("{0:.2f}".format(random.uniform (1,100))) #generate a random value between 1 to 10 with two decimal places
		y_randomValue = float("{0:.2f}".format(random.uniform(1,100))) #generate a random value between 1 to 10 with two decimal places
		dataSet.append((x_randomValue,y_randomValue))
		
#k-initialization by assigning random centroid values
def create_centroids():
	for i in range(k):
		random_index = random.randint(0,sampleCount-1) #select a random data point
		init_Centroid.append(dataSet[random_index]) #store initialized centroid values for iteration
		centroid.append(dataSet[random_index]) #add to centroid array
		#print (centroid)
		plot.scatter(centroid[i][0],centroid[i][1],c=color[i],marker='+',s=200) #plot the centroids accordingly based on colors
#def update_centroids():

#check if the datapoint is a centroid
def is_centroid_point(y):
	isCentroid = False #assume datapoint isn't the centroid
	for x in range(k): #check centroids
		if centroid[x] == dataSet[y]: #skip centroids
			plot.scatter(centroid[x][0],centroid[x][1],c=color[x],marker='+',s=200) #plot the centroids accordingly based on colors
			isCentroid = True
			break
	return isCentroid
			
def main():
	
	generate_dataset()
	plot.scatter(*zip(*dataSet)) #plot all data points
	create_centroids() 
	old_centroidVal = tuple(map(lambda i: sum(i), centroid)) #get values of the initial centroid points for comparison
	
	plot.show() #show generated centroid and data points
	#compute euclidean distance between datapoints and centroid
	
	c = 0 #iteration counter
	
	while True:
		
		c+=1 #increase iteration count
		
		for y in range(sampleCount):
		
			x = 0 #reinitialize x
			closest = 0			
			if is_centroid_point(y) is False:
				while x < k: #calculate distance of datapoints from each centroid
					value = euclidean_distance(x,y)
					if x == 0 or value < closest: #get the closest centroid from a data point
						closest = value
						closest_k = x
					#print (closest)
					x+=1
					if x == k:
					#save closest centroid for the data point and add label
						clusterSet.append((dataSet[y],closest_k))
						plot.scatter(dataSet[y][0],dataSet[y][1],c=color[closest_k])
						
		plot.show() #show iteration results	
		centroid.clear() #clear the previous centroid values
				
		#get the means for new centroid value
		for x in range(k):
			counter = 0
			temp = (0,0)	
				
			if c == 1:
				temp = tuple(map(lambda i,j: round(i + j,2) , init_Centroid[x],temp)) #add the centroid point for mean calculation if iteration = 1
				counter+=1
			for y in range(sampleCount-k):
				if clusterSet[y][1] == x: #get the sum of the datapoints found in a cluster
					temp = tuple(map(lambda i,j: round(i + j,2) , clusterSet[y][0],temp))
					counter+=1
					#print (temp)
			numOfElements = (counter,counter) #number of elements tuple
			#print(numOfElements)
			temp2 = tuple(map(lambda i,j: round(i / j,2), temp,numOfElements)) #the mean value of the cluster aka new centroid point
			centroid.append(temp2)
			plot.scatter(centroid[x][0],centroid[x][1],c=color[x],marker='+',s=200) #plot new centroid points
		
		clusterSet.clear() # clear clustered data points
		
		cur_centroidVal = tuple(map(lambda i: sum(i), centroid))
		print (cur_centroidVal) #current centroid values
		print (old_centroidVal) #previous centroid values
		
		if(old_centroidVal == cur_centroidVal): #check if centroid values is no longer moving
			print("Done at Iteration:", c)
			break
		else:
			old_centroidVal = tuple(map(lambda i: sum(i), centroid)) #if there's a change update old centroid values
		#plot.show()			
		if c == 50: #maximum value for iterations if centroid keeps moving
			break
	

if __name__ == "__main__":
    main()
