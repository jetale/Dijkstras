
import pandas
import sys


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
	end_node = (sys.argv[2])
	filename = sys.argv[3]

	exit()

	map_df = pandas.read_csv(filename, sep = " ", header = None)
	

	print(map_df.head)
	
	sample_list = [1, 3359, 353, 2442, 12069, 9895, 7792, 16719, 26455, 27755, 34859, 42866, 50647, 57116, 62625, 69542, 76169, 85974, 92421, 96581, 106346, 101683, 111126, 117312, 120653, 129906, 135893, 137329, 146596, 152272, 158541, 162867, 157869, 163689, 168252, 172934, 179850, 189245, 198995, 193567, 196052, 189987, 196868, 190655, 200000]

	
	
	
	map_dict = convert_to_dict(map_df)
	#print(map_dict[1])
	
	

	see_if(map_dict, sample_list)

	"""
	'''

	#just for testing 
	map_dict = {
        1: [(2, 1), (4,1)],
        2: [(1, 1), (4, 1), (3,2)],
        3: [(2,2), (4,1), (5,1), (6,1)],
        4: [(1, 1), (2, 1), (3,1), (5,2), (6,15)],
        5: [(3, 1), (4,2), (6,1)],
        6: [(3, 1), (4,15), (5,1)]
     }
	'''
	search(map_dict, start_node, end_node)
	"""
	

def see_if(map_dict, sample_list):


	flag_list = []

	for i in range(1,len(sample_list) - 1):
		j = i +  1
	
		node1 = sample_list[i]
		node2 = sample_list[j]

		val_list = map_dict[node1]
	
		for item in val_list:
			
			if int(item[0]) == node2:
				flag_list.append(str(item[2]))
				print(node1,node2, item[2])

		print(''.join(flag_list))


#To be completed after basic implementation is complete. Currently has a error which has no reason to be there
#Fixed the issue. It was my mistake. I forgor list.append(x) does not return anything
def convert_to_dict(map_df):

	map_dict = {}

	for index, row in map_df.iterrows():
		i1 = int(row[0])
		i2 = int(row[1])
		dist = int(row[2])		
		flag = str(row[3])

		#print(i1, i2, dist, flag)

		'''
		#Note - Each edge is only represented once. Therefore, to create a dict which will have all the nodes and all the
		#edges we should take both i1 and i2 and create a dict item for each of them
		'''
	
		try:
			val = map_dict[i1]
			val.append((i2, dist, flag))
			map_dict[i1] = val 

		except KeyError:
			
			map_dict[i1] = [(i2, dist,flag)]
	
			

		try:
			
			val1 = map_dict[i2]
			val1.append((i1, dist, flag))
			
			map_dict[i2] = val1

		except KeyError:
			map_dict[i2] = [(i1, dist,flag)]

		
	return map_dict



				

def search(map_dict, start_node, end_node):

	pr_que = {}	
		
	#for current implementation only, change it to take total number of nodes
	visited_list = (end_node + 1) * [0]

	predec_dict = {}

	pr_que[start_node] = 0

	distance_dict = {}
	distance_dict[start_node] = 0
	
	curr_node = start_node

	print(distance_dict[curr_node])

	while pr_que:
	
		#init_len = len(visited_list)
		curr_node = (next(iter(pr_que)))

		
		neighbour_list = map_dict[curr_node]
		#print(f' \n --- Currently working on {curr_node} with following neighbours \n -- {neighbour_list}')
		for item in neighbour_list:
			nb_node = item[0]
			dist = item[1]
			try:

				if visited_list[nb_node] == 0:
					val_from_start = distance_dict[curr_node]
					try:
						prev_dist_val = distance_dict[nb_node]
						curr_dist_val = val_from_start + dist
						
						#Not dealing with condition having both equal values right now	
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

		visited_list[curr_node] = 1
		

		del pr_que[curr_node]	
	
		sorted_que = {k: v for k, v in sorted(pr_que.items(), key=lambda item: item[1])}
		

		pr_que = sorted_que

	
		if end_node == curr_node:
			path_list = [end_node]
			while start_node not in path_list:
				path_list.append(predec_dict[path_list[-1]])
			path_list.reverse()
			print(path_list)
			print('Done')
			exit()
		


		


				
			


		
		
	
	


if __name__ == '__main__':
	do_work()
