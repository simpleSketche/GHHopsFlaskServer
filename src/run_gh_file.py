#tested with python3.7
from pathlib import Path
import rhinoinside
import clr
import json
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
import Rhino
from Grasshopper.Kernel import GH_Document
from GH_IO.Serialization import GH_Archive
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper.Kernel import IGH_Param


def gh_addition(input):
    '''
    do addition and get results from gh c# component
    '''
    # run and access GH document
    definition = GH_Document()
    archive = GH_Archive()
    archive.ReadFromFile("gh_files/rhinoinsideTestFIle.gh")
    archive.ExtractObject(definition, "Definition")

    for ob in definition.Objects:

        if(ob.NickName == "num1"):
            param = IGH_Param(ob)
            param.ClearData()
            param.AddVolatileData(GH_Path(0), 0, input)

        if(ob.NickName == "Result"):
            param = IGH_Param(ob)
            param.ClearData()
            param.CollectData()
            param.ComputeData()
            result = param.get_VolatileData()[0][0]
            output= result
            return output

            # the method below displays all properties / methods of IGH_Param
            # print(dir(param))
    return


def gh_make_sphere(radius):
    '''
    Make a shpere with the given radius and return results from gh c# component
    '''
    # run and access GH document
    definition = GH_Document()
    archive = GH_Archive()
    archive.ReadFromFile("gh_files/rhinoinsideTestFIle.gh")
    archive.ExtractObject(definition, "Definition")

    output = ""

    for ob in definition.Objects:

        if(ob.NickName == "radius"):
            inputParam = IGH_Param(ob)
            inputParam.ClearData()
            inputParam.AddVolatileData(GH_Path(0), 0, radius)

        if(ob.NickName == "ResultSphere"):
            testParam = IGH_Param(ob)
            testParam.ClearData()
            testParam.CollectData()
            testParam.ComputeData()
            test = testParam.get_VolatileData()[0][0]
            if(test != None):
                mesh = test.Value
                area = Rhino.Geometry.AreaMassProperties.Compute(mesh).Area
                print(area)
            
            

        if(ob.NickName == "outputString"):
            param = IGH_Param(ob)
            param.ClearData()
            param.CollectData()
            param.ComputeData()
            result = param.get_VolatileData()[0][0]
            meshJson = result.Value
            output= json.loads(meshJson)
            return output

            # the method below displays all properties / methods of IGH_Param
            # print(dir(param))
    return
