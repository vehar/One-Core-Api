@ stdcall AssocCreateForClasses(ptr long long ptr)
@ stdcall AssocGetDetailsOfPropKey(ptr ptr ptr ptr ptr)
@ stdcall SHBindToObject(ptr ptr ptr ptr ptr) 
@ stdcall SHBindToFolderIDListParent(ptr ptr ptr ptr ptr)
@ stdcall SHBindToFolderIDListParentEx(ptr ptr ptr long ptr ptr)
@ stdcall SHCreateItemFromIDList(ptr ptr ptr)
@ stdcall SHCreateItemFromParsingName(wstr ptr ptr ptr)
@ stdcall SHCreateItemFromRelativeName(ptr wstr ptr long ptr)
@ stdcall SHCreateItemWithParent(ptr ptr ptr long ptr)

@ stdcall SHCreateShellItemArray(ptr ptr long ptr ptr)
@ stdcall SHCreateShellItemArrayFromIDLists(long ptr ptr)

@ stdcall Shell_GetCachedImageIndexA(str ptr long) 
@ stdcall Shell_GetCachedImageIndexW(wstr ptr long) 

@ stdcall Shell_NotifyIcon(long ptr) Shell_NotifyIconA
@ stdcall Shell_NotifyIconA(long ptr) 
@ stdcall Shell_NotifyIconW(long ptr)

@ stdcall SHGetKnownFolderPath(ptr long ptr ptr)
@ stdcall SHCreateShellItemArrayFromShellItem(ptr ptr ptr)
@ stdcall SHCreateShellItemArrayFromDataObject(ptr ptr ptr)
@ stdcall SHGetPropertyStoreFromParsingName(wstr ptr long long ptr)

@ stdcall SHAssocEnumHandlers(wstr long ptr)
@ stdcall SHSetDefaultProperties(ptr ptr long ptr)
@ stdcall SHAddDefaultPropertiesByExt(wstr ptr)

@ stdcall SHChangeNotifyRegisterThread(long)

@ stdcall SHGetNameFromIDList(ptr long ptr)

@ stdcall SHGetIDListFromObject(ptr ptr)

@ stdcall SHCreateDefaultExtractIcon(ptr ptr)

@ stdcall SHSetTemporaryPropertyForItem(ptr ptr ptr)

@ stdcall SHGetPropertyStoreFromIDList(ptr long long ptr)

@ stdcall SHQueryUserNotificationState(ptr)

@ stdcall SHCreateDefaultContextMenu(ptr ptr ptr)

@ stdcall SHGetLocalizedName(wstr wstr long ptr)

@ stdcall ILLoadFromStreamEx(ptr ptr)

@ stdcall SHCreateItemInKnownFolder(ptr long wstr ptr ptr)

@ stdcall SHGetPathFromIDListEx(ptr wstr long long)

@ stdcall InitNetworkAddressControl()

@ stdcall SHCreateAssociationRegistration(long ptr)
@ stdcall SHRemoveLocalizedName(wstr)

@ stdcall SHGetDriveMedia(wstr ptr)

@ stdcall SHGetTemporaryPropertyForItem(ptr ptr ptr)

761 stdcall -noname SHChangeNotifyDeregisterWindow(ptr)

758 stdcall -noname SHCreateThreadUndoManager(ptr ptr)

759 stdcall -noname SHGetThreadUndoManager(ptr ptr)

@ stdcall SHEvaluateSystemCommandTemplate(wstr wstr wstr wstr)

@ stdcall SHCreateDataObject(ptr long ptr ptr ptr ptr)

850 stdcall -noname PathComparePaths(wstr wstr)