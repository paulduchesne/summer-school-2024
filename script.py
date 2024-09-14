import pathlib
from clairmeta import DCP

dcp = DCP(pathlib.Path.cwd() / 'test_dcp' / 'TestDcp_SHR-1_F-178_XX-XX_MOS_2K_20240914_SMPTE_OV')
dcp.parse()
status, report = dcp.check()


    #   TestDcp_SHR-1_F-178_XX-XX_MOS_2K_20240914_SMPTE_OV/cpl_1c6ad489-fa93-4ddb-9cea-5a1ce6f71e0e.xml
