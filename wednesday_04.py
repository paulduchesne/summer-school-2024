
import pathlib
from clairmeta import DCP


dcp_path = pathlib.Path.cwd() / 'test_dcp'  / 'TestDcp_SHR-1_F-178_XX-XX_MOS_2K_20240925_SMPTE_OV'
print(dcp_path.exists())

dcp = DCP(str(dcp_path))
dcp.parse()
status, report = dcp.check()
