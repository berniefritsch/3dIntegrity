#!/usr/bin/env python
# coding: utf-8

import pymeshlab as ml
ms = ml.MeshSet()
#import pymeshlab
#ms = pymeshlab.MeshSet()

#import matplotlib

# Load 3D model
# Mesh
#ms.load_mesh('Mesh_Test.ply')

# Pointcloud

# Broken Mesh

# OBJ with texture
ms.load_mesh('Head of Buddha - 5K TRIS.obj')

print('Loaded successfully')

# Show 3D

# Name and number of Mesh

current = ms.current_mesh()
number = ms.number_meshes()
status = ms.print_status()

print(current)
print(number)
print(status)

# Number of vertices and faces
num_verts =  ms.current_mesh().vertex_number() 
num_face =  ms.current_mesh().face_number() 
print(num_face)
print(num_verts)

# Mesh or Pointcloud

if num_face > 0:
    print('Mesh')
if num_face == 0 and num_verts > 0:
    print('Pointcloud')


# Manifoldness

verbose = ms.set_versbosity(True)
print(verbose)
nmedges = ms.apply_filter('select_non_manifold_edges_')
nmvert = ms.apply_filter('select_non_manifold_vertices')
print(nmedges)
print(nmvert)

# Duplicated vertices
# Position
# Texture File
# Georef oder nicht


# Receipt (Export as PDF)
 
print('**Receipt:**')
print('Status:','Loades successfully')
print('Number of Meshes:', number)
print('Number of Faces:', num_face)
print('Number of Vertices:', num_verts)

