#tested with python3.7
from pathlib import Path
from tokenize import String
import rhinoinside
import clr
import sys
sysdir = Path(r"C:\Program Files\Rhino 7\System")
plugdir = Path(sysdir, "..", "Plug-ins").resolve()
rhinoinside.load()

GrasshopperDll = f'{Path(plugdir, "Grasshopper", "Grasshopper.dll").resolve()}'
GH_IODll= f'{Path(plugdir, "Grasshopper", "GH_IO.dll")}'
GH_UtilDll= f'{Path(plugdir, "Grasshopper", "GH_Util.dll")}'

clr.AddReference(GrasshopperDll)
clr.AddReference(GH_IODll)
clr.AddReference(GH_UtilDll)
# Set up ready, now do the actual Rhino usage
import System
import Rhino
from Grasshopper.Kernel import GH_Document, GH_SolutionMode
from GH_IO.Serialization import GH_Archive
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper.Kernel.Types import GH_String
from Grasshopper.Kernel import IGH_Param

def run_gh_file(input):
    definition = GH_Document()

    archive = GH_Archive()

    archive.ReadFromFile("gh_files/addTwoNumebrsC#.gh")
    archive.ExtractObject(definition, "Definition")

    output = {
        "result":""
    }

    for ob in definition.Objects:

        if(ob.NickName == "num1"):
            param = IGH_Param(ob)
            param.ClearData
            param.AddVolatileData(GH_Path(0), 0, input)

        if(ob.NickName == "Result"):
            param = IGH_Param(ob)
            param.ClearData()
            param.CollectData()
            param.ComputeData()
            result = param.get_VolatileData()[0][0]
            output["result"] = result
            print(result)

            # the method below displays all properties / methods of IGH_Param
            # print(dir(param))
    return output["result"]