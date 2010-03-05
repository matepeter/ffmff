def raise_404(method):
	"""catch ObjectDoesNotExist and raise Http404"""

	def wrap(*args, **kwargs):
		from django.core.exceptions import ObjectDoesNotExist
		from django.http import Http404
		try:
			return method(*args, **kwargs)
		except ObjectDoesNotExist, ex:
			raise Http404(ex.message)

	return wrap
