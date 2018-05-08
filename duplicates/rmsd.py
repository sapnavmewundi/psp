import Bio.PDB
from Bio.PDB.PDBParser import PDBParser
import pandas as pd

fragment = pd.read_excel('fragment3.xlsx')
# writer = pd.ExcelWriter('fragment3.xlsx', engine='xlsxwriter')
rmsds = []

for index, row in fragment.iterrows():
    file_name_1 = row['ID_1'][0:4]
    file_name_2 = row['ID_2'][0:4]
    chain_name_1 = row['ID_1'][5:6]
    chain_name_2 = row['ID_2'][5:6]

    start_1 = int(row['Start_1'])
    start_2 = int(row['Start_2'])

    end_1 = int(row['End_1']) + 1
    end_2 = int(row['End_2']) + 1

    parser_1 = PDBParser()
    parser_2 = PDBParser()

    structure_1 = parser_1.get_structure("test1", file_name_1 + '.pdb')
    structure_2 = parser_2.get_structure("test2", file_name_2 + '.pdb')

    # chains = structure_1.get_chains()
    chain_1 = structure_1[0][chain_name_1]
    chain_2 = structure_2[0][chain_name_2]

    # print("Chains 1" + str(list(chain_1)))
    # print("Chains 2" + str(list(chain_2)))
    # print(list(chain_1))
    # for chain in chains:
    #     print(len(list(chain.get_atoms())))
    #     # print(list(chain.get_atoms()))

    # atoms_1 = structure_1.get_atoms()
    # atoms_2 = structure_2.get_atoms()

    residues_1 = list(chain_1)
    residues_2 = list(chain_2)

    temp_1 = residues_1[start_1:end_1]
    temp_2 = residues_2[start_2:end_2]

    print(temp_1)
    print(temp_2)

    atoms_1 = []
    atoms_2 = []

    for i in temp_1:
        # print(i.get_full_id()[3][1])
        # print(list(i.get_atoms()))
        atoms_1 = atoms_1 + list(i.get_atoms())

    for j in temp_2:
        # print(i.get_full_id()[3][1])
        # print(list(j.get_atoms()))    
        atoms_2 = atoms_2 + list(j.get_atoms())

    print("Start 1:  " + str(start_1), "End 1: " + str(end_1))
    print("Start 2:  " + str(start_2), "End 2: " + str(end_2))
    
    print("Atoms 1: " + str(len(atoms_1)))
    print("Atoms 1: " + str(list(atoms_1)))

    print("Atoms 2: " + str(len(atoms_2)))
    print("Atoms 2: " + str(list(atoms_2)))

    fixed = atoms_1
    moving = atoms_2

    sup = Bio.PDB.Superimposer()
    sup.set_atoms(fixed, moving)
    print(sup.rms)
    sup.apply(moving)
    # print(sup.rms) 
    rmsds.append(sup.rms)
    # break

print(rmsds)
fragment['RMSD'] = rmsds
print(fragment.columns)
# fragment.to_excel(writer)