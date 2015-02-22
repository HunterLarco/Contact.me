from google.appengine.ext import ndb


class Shake(ndb.Model):
  peaks = ndb.PickleProperty(indexed=False)


def receive(peaks):
  pass