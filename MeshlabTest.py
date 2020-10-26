#!/usr/bin/env python
# coding: utf-8


import pymeshlab as ml
ms = ml.MeshSet()

# import matplotlib


# Lade 3D Modell

ms.load_mesh('Mesh_Test.ply')

# Test mit Punktwolke und kaputter Datei
#ms.load_mesh('PW_Test.ply')
#ms.load_mesh('3D_korrupt.ply')

print('Datei korrekt')


# Show 3D

# Anzahl Vertices und Faces
num_verts =  ms.current_mesh().vertex_number() 
num_face =  ms.current_mesh().face_number() 
print(num_face)
print(num_verts)


# Mesh oder Pointcloud

if num_face > 0:
    print('Mesh')
if num_face == 0 and num_verts > 0:
    print('Pointcloud')

# Manifoldness
#class meshlab.MeshSet
#__init__(self: meshlab.MeshSet, verbose: bool = False)

#ms.set_verbosity(True)
ms.apply_filter('select_non_manifold_edges_')
ms.apply_filter('select_non_manifold_vertices')

print('select_non_manifold_edges_')

# Duplicated vertices
# Position
# Texture File
# Georef oder nicht

# Receipt (Export als PDF)
 
print('**Receipt:**')
print('Status:','Datei korrekt')
print('Anzahl Faces:', num_face)
print('Anzahl Vertices:', num_verts)

