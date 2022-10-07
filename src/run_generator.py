#tested with python3.7
from pathlib import Path
import rhinoinside
import clr
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
from Grasshopper.Kernel import GH_Document
from GH_IO.Serialization import GH_Archive
from Grasshopper.Kernel import IGH_Param

# use your own path to the rhino file


def get_result():
    '''
    Get the generated result from the Minus_Design_Lab generator
    '''
    # run and access GH document
    definition = GH_Document()
    archive = GH_Archive()
    archive.ReadFromFile(gh_file_path)
    archive.ExtractObject(definition, "Definition")

    for ob in definition.Objects:
        if(ob.NickName == "OutputGeo"):
            param = IGH_Param(ob)
            param.CollectData()
            print(param)
            param.ComputeData()
            result = param.get_VolatileData()[0][0]
            output= result
            print(output)
            return str(output)

            # the method below displays all properties / methods of IGH_Param
            # print(dir(param))
    return "hello!"