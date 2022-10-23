#!/bin/bash
# render-pymol.sh
if [ $# -eq 0 ]
  then
    echo "Usage: plot-pdb.sh <PDB ID>"
    exit
fi
o=$(basename $1 .pdb);
#Create the rasmol script
echo "load $1;" > $o.pml
echo "set ray_opaque_background, on;" >> $o.pml
echo "show cartoon;" >> $o.pml
echo "color purple, ss h;" >> $o.pml
echo "color yellow, ss s;" >> $o.pml
echo "ray 1500,1500;" >> $o.pml
echo "png $1.png;" >> $o.pml
echo "quit;" >> $o.pml
#Execute PyMol
/Applications/PyMOL.app/Contents/bin/pymol -qxci $o.pml
#Remove temporary files
rm -rf $o.pml
