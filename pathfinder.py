
import pandas
import sys
from tqdm import tqdm
import timeit

def do_work():
	
	if len(sys.argv) < 4:
	
		note = \
		""" \nPlease provide the following input arguments in order - \n
	1. Start node 
	2. Destination node
	3. Input file name or path if in other directory

	Example - python pathfinder.py 1 200 map.txt

		"""
		print(note)
		exit()
			

	
	#Assigning input values to variables
	start_node = int(sys.argv[1])
	end_node =int(sys.argv[2])
	filename = sys.argv[3]

	

	#Reading text file
	map_df = pandas.read_csv(filename, sep = " ", header = None)
	
	#convert df to dict
	map_dict = convert_to_dict(map_df)
	
	#exit()
	
	search(map_dict, start_node, end_node)
	
	
	
	'''

	#Sample graph placed here for testing. I found it is easier to test on small graph and then scale
	map_dict = {
        1: [(2, 1), (4,1)],
        2: [(1, 1), (4, 1), (3,2)],
        3: [(2,2), (4,1), (5,1), (6,1)],
        4: [(1, 1), (2, 1), (3,1), (5,2), (6,15)],
        5: [(3, 1), (4,2), (6,1)],
        6: [(3, 1), (4,15), (5,1)]
     	}


	'''
	
	
	


def convert_to_dict(map_df):

	print(' \n ------ Running convert_to_dict() -> \n')

	pbar = tqdm(total = len(map_df.index))
	pbar.set_description('Processing ')

	map_dict = {}


	for index, row in map_df.iterrows():
		i1 = int(row[0])
		i2 = int(row[1])
		dist = int(row[2])		
		flag = str(row[3])
		
		#print(i1, i2, dist, flag)

		'''
		#Note - Each edge is only represented once. Therefore, to create a dict which will have all the nodes and all the
		edges, we should take both i1 and i2 and create a dict item for each of them
		'''
	
		#Check if enrty exists in dict for this item
		try:
			val = map_dict[i1]
			val.append((i2, dist, flag))
			map_dict[i1] = val 

		#If not then add
		except KeyError:
			
			map_dict[i1] = [(i2, dist,flag)]
	
			
		#Same as above just for the second node
		try:
			
			val1 = map_dict[i2]
			val1.append((i1, dist, flag))
			
			map_dict[i2] = val1

		except KeyError:
			map_dict[i2] = [(i1, dist,flag)]


	
		pbar.update(1)

	pbar.close()
		
	return map_dict



				

def search(map_dict, start_node, end_node):


	start_time = timeit.default_timer()

	print(' \n ------ Running search() -> \n')

	#Priority que
	pr_que = {}	

	#dict with latest distances from start node for each node 
	distance_dict = {}
		
	#for current implementation only, change it to take total number of nodes
	#visited_list = (end_node + 1) * [0]

	#Done - 
	visited_dict = {}

	#dict to store predecessors
	predec_dict = {}

	#Initializing priority que	
	pr_que[start_node] = 0

	#Initializing distance dict
	distance_dict[start_node] = 0
	
	#Name change
	curr_node = start_node

	

	while pr_que:
	
		#Next top node from priority que
		curr_node = (next(iter(pr_que)))

		
		#List of neighbours and their distances from the current node
		neighbour_list = map_dict[curr_node]

		#Kept this for dubugging purposes ->
		#print(f' \n --- Currently working on {curr_node} with following neighbours \n -- {neighbour_list}')
		
		

		for item in neighbour_list:
			nb_node = item[0]
			dist = item[1]

			try:
				val_node = visited_dict[nb_node] 
			except KeyError:
				visited_dict[nb_node] = 0

			try:

				if visited_dict[nb_node] == 0:
					val_from_start = distance_dict[curr_node]
					try:
						prev_dist_val = distance_dict[nb_node]
						curr_dist_val = val_from_start + dist
						
							
						if curr_dist_val < prev_dist_val:
							distance_dict[nb_node] = curr_dist_val
							pr_que[nb_node] = curr_dist_val
							predec_dict[nb_node] = curr_node

					except KeyError:
						distance_dict[nb_node] = val_from_start + dist
						pr_que[nb_node] = val_from_start + dist
						predec_dict[nb_node] = curr_node
						
			except IndexError:
				print(nb_node, len(visited_list))
				exit()

		#Marking current node as visited
		visited_dict[curr_node] = 1
		
		#If we reached destination node then exit
		if end_node == curr_node:
			path_list = [end_node]
			print(f'\n This is end node {end_node}')
			while start_node not in path_list:
				path_list.append(predec_dict[path_list[-1]])
			path_list.reverse()
			#print(path_list)
			#print('Done')
			
			print('\n -------- Shortest path is ---> \n')
			print(path_list)

			print('\n -------- Path distance is ----> \n')
			print(pr_que[curr_node])
			end_time = timeit.default_timer()
			
			print(f'\n -------- Execution Time ---> {end_time - start_time} seconds')

		
		
		#Deleting current node from priority que
		del pr_que[curr_node]	
	
		#Sorting the priority que according to the distance values
		sorted_que = {k: v for k, v in sorted(pr_que.items(), key=lambda item: item[1])}
		

		#Name change
		pr_que = sorted_que


				
			

	
	


if __name__ == '__main__':
	do_work()



