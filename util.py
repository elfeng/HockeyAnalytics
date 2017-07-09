import entry.py


def mapEntry(entry, index):

	#set initiating_player
	player_name = originDataFrame.loc[index, 'player']
	entry.initiate_player(player_name);

	#track coordinates, determine when Entry ends by case
	if entry.style == 'drop':
		initialX = originDataFrame.loc[index, 'x_coord_ft']
		temp_list = []
		inZone = 0
		beenInZone = 0
		for i in range(index+1, numberOfEvents):
			currentXstr = str(originDataFrame.loc[i, 'x_coord_ft'])
			currentYstr = str(originDataFrame.loc[i, 'y_coord_ft'])
			currentX = int(currentXstr)
			currentY = int(currentYstr)
			#track coordinates
			temp_list.append([currentX, currentY])
			#check fail entry
			if currentX < initialX:
				#save tracked coordinates so far
				entry.coords = temp_list
				return i
			#puck exits zone
			if currentX < 125 and beenInZone == 1:
				#stop entry, save tracked coordinates
				entry.coords = temp_list
				endTime = originDataFrame.loc[i, 'clock']
				#update time for entry
				setTime(startTime, endTime, entry)
				#update entry success
				if entry.time_in_zone >= 10:
					entry.success = True
					return i
			#puck remains zone
			if currentX > 125 and inZone == 1:
				beenInZone = 1
				continue
			#puck enters zone
			if currentX > 125:
				inZone = 1
				startTime = originDataFrame.loc[i, 'clock']
