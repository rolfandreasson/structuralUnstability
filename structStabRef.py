
import sys
from sage.all import *


n = 3

print("Structurally stable, semistable and unstable reflexive polytopes")
print("Ambient dimension: ", end="")
print(n)
print()

nbr_of_reflexive = 0
if n==2:
    nbr_of_reflexive = 16
elif n==3:
    nbr_of_reflexive = 4319

nbr_of_stable = 0
nbr_of_strictly_semistable = 0
nbr_of_unstable = 0



for index in range(0, nbr_of_reflexive):

    print("Index: ", end="")
    print(index)

    # Some explicit test cases
    #P = LatticePolytope([[1, 0], [1, -1], [-1, -1], [-1, 0], [0, 1]])
    #P = LatticePolytope([
    #                    [0, 0, 1], [1, -1, 0], [-1, 1, 0],
    #                    [1, 1, 0], [-1, -1, 0], [1, -1, -1],
    #                    [-1, 1, -1], [1, 1, -1], [-1, -1, -1]
    #                    ])
    #n = P.dim()

    P = ReflexivePolytope(n, index)

    P_h = Polyhedron(vertices = P.vertices(), backend = 'normaliz')
    volume_P = P_h.volume(measure='induced_lattice')


    P_polar = P.polar()
    P_polar_h = Polyhedron(vertices = P_polar.vertices(), backend = 'normaliz')
    volume_polar_P = P_polar_h.volume(measure='induced_lattice')


    #Check if P correspond to non-singular variety
    non_singular = 0
    if P_polar_h.is_simplicial():
        non_singular = 1


    #Set up variables counting stability
    nbr_of_strictly_semistable_facets = 0
    nbr_of_unstable_facets = 0

    # Loop over facets in the dual (=source) and compute their volume,
    # then find the vertices of the facet, and find their dual facets in the
    # primary (=target)
    for facet in P_polar.facets():


        # Compute facet volume in dual
        facet_h = Polyhedron(vertices = facet.vertices(), backend = 'normaliz')
        facet_volume = facet_h.volume(measure='induced_lattice')
        if non_singular == 1:
            if facet_volume != 1:
                non_singular = 0

        # Find vertices of the face and compute volume of the dual
        # facet in the primary and add them to the volume of the star
        star_volume = 0
        for vertex in facet.faces(0):
            star_facet = vertex.dual()
            star_facet_h = Polyhedron(vertices = star_facet.vertices(), backend = 'normaliz')
            star_volume += star_facet_h.volume(measure='induced_lattice')

        # Compute relative volumes
        # but instead of dividing by the total volume
        # we multiply by the total dual volume to avoid floating point numbers.
        # Thus the name relative might be confusing
        relative_facet_volume = facet_volume*volume_P
        relative_star_volume = star_volume*volume_polar_P


        # Check the stability
        if relative_facet_volume > relative_star_volume: #and P.nvertices() == n+1 and P.nfacets() == n+1:
            nbr_of_unstable_facets += 1
        elif relative_facet_volume == relative_star_volume:
            nbr_of_strictly_semistable_facets +=1

    #Do the same but the dual condition
    for facet in P.facets():
        # Compute facet volume in dual
        facet_h = Polyhedron(vertices = facet.vertices(), backend = 'normaliz')
        facet_volume = facet_h.volume(measure='induced_lattice')

        # Find vertices of the face and compute volume of the dual
        # facet in the primary and add them to the volume of the star
        star_volume = 0
        for vertex in facet.faces(0):
            star_facet = vertex.dual()
            star_facet_h = Polyhedron(vertices = star_facet.vertices(), backend = 'normaliz')
            star_volume += star_facet_h.volume(measure='induced_lattice')

        # Compute relative volumes
        # but instead of dividing by the total volume
        # we multiply by the total dual volume to avoid floating point numbers.
        # Thus the name relative might be confusing
        relative_facet_volume = facet_volume*volume_polar_P
        relative_star_volume = star_volume*volume_P

        # Check the stability
        if relative_facet_volume > relative_star_volume: #and P.nvertices() == n+1 and P.nfacets() == n+1:
            nbr_of_unstable_facets += 1
        elif relative_facet_volume == relative_star_volume:
            nbr_of_strictly_semistable_facets +=1



    if nbr_of_unstable_facets > 0:
        print("Unstable with ", end="")
        print(nbr_of_unstable_facets)
        print("unstable facets.")
        nbr_of_unstable += 1
    elif nbr_of_strictly_semistable_facets > 0:
        print("Strictly semistable with ", end="")
        print(nbr_of_strictly_semistable_facets)
        print("semistable facets.")
        nbr_of_strictly_semistable += 1
    else:
        print("Stable")
        nbr_of_stable += 1

    if non_singular == 1:
        print('Non-singular')

    print()

print("In total there are ", end="")
print(nbr_of_reflexive, end="")
print(" reflexive polytopes in the given dimension")
print(" of which there are")
print("Structurally stable: ",end="")
print(nbr_of_stable)
print("Structurally strictly semistable: ", end="")
print(nbr_of_strictly_semistable)
print("Structurally unstable: ", end="")
print(nbr_of_unstable)



    #
