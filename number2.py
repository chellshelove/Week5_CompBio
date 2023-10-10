from pymsaviz import MsaViz, get_msa_testdata
msa_file = get_msa_testdata("HIGD2A.fa")
mv = MsaViz(msa_file, wrap_length=70, show_count=True)
mv.savefig("example1.png")

mv = MsaViz(msa_file, color_scheme="Taylor", wrap_length=80, show_grid=True, show_consensus=True)
mv.savefig("example2.png")