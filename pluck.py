def pluck(collection, key):
     '''
     extract x[key] for every item x in the collection
     '''

     plucked = []

     for x in collection:
        try:
            plucked.append(x[key])
        except KeyError:
            pass

     return plucked

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'pluck': pluck
        }