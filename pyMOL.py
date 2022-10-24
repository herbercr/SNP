#!/usr/bin/env python3
import subprocess, sys
#begins the python part
snp_residues=[7,25,68]

def map_snp_to_structure(snp_residues,input_file,output_file=None):
	if output_file is None:
		output_file=input_file[:-4]+'.pml'
#open up a file to write to
	with open(output_file,'w') as output:
#these are the things it will tell it to do to the .pdb file. It will print them to std out
		output.write(f'load {input_file};\n')
		output.write(f'set ray_opaque_background,on;\n')
		output.write(f'show cartoon;\n') #this is the standard cartoon. Can be changed to different kinds
		output.write(f'color blue, ss H;\n') #I think that this makes helix blue
		output.write(f'color yellow, ss S;\n') #I think this makes sheets yellow
		for res_num in snp_residues:
 			output.write(f'color red, resi {res_num:d};\n') #trying to tell it that our snp is a loop, which does not need to be defined. 
	#output.write(f'color red, ss l+\n') #trying to get it to think our snp is a loop and color it red
#	output.write(f'rebuild;\n') #regenerate the cartoon
#	output.write(f'show cartoon;\n')
		output.write(f'ray 1500,1500;\n') #ray is the size of resulting image. larger can take longer to run
		output.write(f'png {output_file}.png;\n') # writes png file 
		output.write(f'quit;\n')

#pyMOL part
	subprocess.run(f'/Applications/PyMOL.app/Contents/bin/pymol -qxci {output_file}',shell=True)
if __name__=='__main__':
 input_file=sys.argv[1]
 output_file=sys.argv[2]
 test_data=[7,25,68]
 map_snp_to_structure(test_data,input_file,output_file)

