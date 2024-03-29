
class HyperGraph:
    """
    operations on hypergraphs:
    each has a set of vertices : vertices
    and a list of hyperedges  : hyedges
    """

    def __init__(self, c=set([]), l = []):
        "initialization; default: empty vertices, empty list of hyperedges"
        self.vertices = c.copy()
        self.hyedges = [ e.copy() for e in l ]

    def addel(self,elem):
        "add one element to all the hyperedges - did we EVER use this function?"
        self.vertices.add(elem)
        for e in self.hyedges:
            e.add(elem)

    def added(self,ed=set([])):
        "add one hyperedge ed, empty by default - ed must be a set"
        for el in ed:
            self.vertices .add(el)
        self.hyedges.append(ed)

    def addhg(self,another):
        "union of two hypergraphs into the first one - did we EVER use this function?"
        for e in another.hyedges:
            self.added(e)

    def remel(self,elem):
        "remove element from all hyperedges where it belongs"
        for e in self.hyedges:
            if elem in e:
                e.remove(elem)

    def remed(self,elem):
        "remove all hyperedges where the element appears"
        new = []
        for e in self.hyedges:
            if not elem in e:
                new.append(e)
        del self.hyedges
        self.hyedges = new

    def _xcopy(self,thecopy):
        "copy hypergraph onto existing one"
        thecopy.carrier = self.vertices.copy()
        thecopy.hyedges = [e.copy() for e in self.hyedges]

    def copy(self):
        "make fresh copy of hypergraph"
        thecopy = hypergraph()
        thecopy.vertices = self.vertices.copy()
        thecopy.hyedges = [e.copy() for e in self.hyedges]
        return thecopy

    def updatecarrier(self):
        "after deleting hyperedges, remove elems possibly left over in vertices"
        new = set([])
        for e in self.hyedges:
            for el in e:
                new.add(el)
        self.vertices = new

    def somempty(self):
        "check for an empty hyperedge"
        for e in self.hyedges:
            if len(e)==0:
                return True
        return False

    def simplify(self):
        """
        Obtain a simple hypergraph by removing nonminimal hyperedges
        But does not remove duplicates
        Careful: one of the calls might assume no reordering
        """
        sieve = self.hyedges
        for e in self.hyedges:
            sieve = [ e1 for e1 in sieve if not e<e1 ]
        self.hyedges = sieve

    def rmdups(self):
        "remove duplicate edges - sometimes they creep in - REALLY?"
        nodups = []
        for e in self.hyedges:
            if not e in nodups:
                nodups.append(e)
        self.hyedges = nodups

