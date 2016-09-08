ALLOWED_EXTENSIONS = set(['txt', "md"])

def allowed_file(filename):
    return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_allowed_extensions():
	return ALLOWED_EXTENSIONS