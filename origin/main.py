from Algorithm import *
from Excel_Data import *
from File_operation import *
from Json_Data import *

if __name__ == '__main__':
    File_operation = File_operation()
    File_operation.Input()    #Input the file name and turn into the dataframe

    Excel_Data = Excel_Data(File_operation.File_name)
    Excel_Data.Run()

    Json_Data = Json_Data()

    Algorithm = Algorithm(Excel_Data, Json_Data)
    Algorithm.Run()
    
    File_operation.Output_File_Json(Json_Data.dict)