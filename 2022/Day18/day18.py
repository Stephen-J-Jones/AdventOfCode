from shared import read_lines, SAMPLE, find_all_numbers_in_string, PUZZLE


def read_data():
    for line in read_lines(SAMPLE):
        yield find_all_numbers_in_string(line)


def get_drop_faces(x, y, z):
    left = ((x, y, z), (x, y + 1, z), (x, y + 1, z + 1), (x, y, z + 1))
    right = ((x + 1, y, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x + 1, y, z + 1))
    bottom = ((x, y, z), (x + 1, y, z), (x + 1, y, z + 1), (x, y, z + 1))
    top = ((x, y + 1, z), (x + 1, y + 1, z), (x + 1, y + 1, z + 1), (x, y + 1, z + 1))
    back = ((x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z))
    front = ((x, y, z + 1), (x + 1, y, z + 1), (x + 1, y + 1, z + 1), (x, y + 1, z + 1))
    return {left, right, bottom, top, back, front}


def build_blob():
    blob_faces = set()
    for x, y, z in read_data():
        drop_faces = get_drop_faces(x, y, z)
        blob_faces.symmetric_difference_update(drop_faces)
    return blob_faces


def find_internals(faces):
    internal_faces = set()
    for face in faces:
        faces_to_check = get_drop_faces(face[0][0], face[0][1], face[0][2])
        if faces_to_check.issubset(faces):
            internal_faces |= faces_to_check
    return faces-internal_faces


if __name__ == "__main__":
    faces = build_blob()
    print(len(faces))
    print(len(find_internals(faces)))
