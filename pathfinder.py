#main script

import pandas



def do_work():
	
	map_df = pandas.read_csv('map.txt', sep = " ", header = None)
	start_node = 1
	end_node = 6

	print(map_df.head)


	#map_dict = convert_to_dict(map_df)
	#print(map_dict[65063])

	#just for testing 
	map_dict = {
        1: [(2, 1), (4,1)],
        2: [(1, 1), (4, 1), (3,2)],
        3: [(2,2), (4,1), (5,1), (6,1)],
        4: [(1, 1), (2, 1), (3,1), (5,2), (6,15)],
        5: [(3, 1), (4,2), (6,1)],
        6: [(3, 1), (4,15), (5,1)]
     }
	search(map_dict, start_node, end_node)

	


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
	visited_list = end_node * [0]

	predec_dict = {}

	pr_que[start_node] = 0

	distance_dict = {}
	
	curr_node = start_node

	

	while pr_que:
	
		#init_len = len(visited_list)
		curr_node = (next(iter(pr_que)))

		if end_node == curr_node:
			print(visited_list)
			print('Done')
			exit()
		
		neighbour_list = map_dict[curr_node]
		#print(f' \n --- Currently working on {curr_node} with following neighbours \n -- {neighbour_list}')
		for item in neighbour_list:
			nb_node = item[0]
			dist = item[1]
			if visited_list[nb_node] != 0:
				val_from_start = pr_que[curr_node]
				try:
					prev_dist_val = pr_que[nb_node]
					curr_dist_val = val_from_start + dist
					
					#Not dealing with condition having both equal values right now	
					if curr_dist_val < prev_dist_val:
						pr_que[nb_node] = curr_dist_val

				except KeyError:
					pr_que[nb_node] = val_from_start + dist


		visited_list[curr_node] = 1

		del pr_que[curr_node]	
	
		sorted_que = {k: v for k, v in sorted(pr_que.items(), key=lambda item: item[1])}
		

		pr_que = sorted_que


		


				
			


		
		
	
	


if __name__ == '__main__':
	do_work()
