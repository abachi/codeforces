
n = int(input())
m = {
    'tetrahedron': 4,
    'cube': 6,
    'octahedron': 8,
    'dodecahedron': 12,
    'icosahedron': 20
}
faces = 0
for i in range(0, n):
    faces += m[input().lower()]

print(faces)