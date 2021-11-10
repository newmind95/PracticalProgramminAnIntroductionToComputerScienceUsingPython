def read_molecule(reader):

    # If there isn't another line , we're at the end of the file
    line = reader.readline()
    if not line:
        return None

    # Name of the molecule: 'CMPND name'
    key, name = line.split()

    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = [name]
    line = reader.readline()

    # Parse all the atoms in the molecule
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        line = reader.readline()

    return molecule


def read_all_molecules(reader):

    # The list of molecule information
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:
            result.append(molecule)
        else:
            reading = False

    return result


if __name__ == '__main__':
    molecule_file = open("multimol.pdb", "r")
    molecules = read_all_molecules(molecule_file)
    print(molecules)
