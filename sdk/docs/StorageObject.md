# StorageObject

An object representation of a drive file or folder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | File or folder identifier | 
**path** | **str** | Path of the folder or file | 
**name** | **str** | Name of the folder or file | 
**created_by** | **str** | Identifier of the user who created the file or folder | 
**created_on** | **datetime** | Date of file/folder creation | 
**updated_by** | **str** | Identifier of the last user to modify the file or folder | 
**updated_on** | **datetime** | Date of file/folder modification | 
**type** | **str** | Type of storage object (file or folder) | 
**size** | **int** | Size of the file in bytes | [optional] 
**status** | **str** | File status corresponding to virus scan status.  (Active, Available, Checking, MalwareDetected, Failed) | [optional] 
**status_detail** | **str** | Detailed description describing any negative terminal state of file | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


