def delete_black_lines(text) -> str:
	resp = ''
	for w in text.split():
		resp += w + ' '

	return resp