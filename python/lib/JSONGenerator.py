from google.appengine.ext.db import Model
import json

def JSONList(lst):
	out = []
	for item in lst:
		if isinstance(item, Model):
			out.append(item.toJSON())			
		else:
			out.append(json.dumps(item))
	return "[%s]" % ",".join(out)
	
def JSONGenerator(obj):
	tempdict = dict([(p, unicode(getattr(obj, p))) for p in obj.properties()])
	tempdict['key'] = unicode(obj.key())
	tempdict['id'] = unicode(obj.key().id())
	jsonString = json.dumps(tempdict).replace('\"True\"', 'true').replace('\"False\"', 'false')
	return jsonString
