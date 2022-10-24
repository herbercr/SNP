#!/usr/bin/env python3 
import requests, sys, io

def uniprot_query(ID):
	

	requestURL=f"https://alphafold.ebi.ac.uk/files/AF-{ID}-F1-model_v3.pdb"
	
	r=requests.get(requestURL)#,headers={"Accept":"application/json"})

	query=r.text

	query2=io.StringIO(query) #creates a string that acts like a file. can be passed to pdb_parser.
	return(query2)

#print(query)
if __name__=='__main__':
	ID=sys.argv[1]
	test_data='Q9N4D8'
	print(uniprot_query(ID))

