@ stdcall -arch=i386 InterlockedDecrement(ptr) kernel32.InterlockedDecrement
@ stdcall -arch=i386 InterlockedCompareExchange(ptr long long) kernel32.InterlockedCompareExchange
@ stdcall -arch=i386 -ret64 InterlockedCompareExchange64(ptr double double)
@ stdcall -arch=i386 InterlockedExchange(ptr long) kernel32.InterlockedExchange
@ stdcall -arch=i386 InterlockedExchangeAdd(ptr long)
@ stdcall -arch=i386 InterlockedIncrement(ptr) kernel32.InterlockedIncrement
@ stdcall InitializeSListHead(ptr) ntdll.RtlInitializeSListHead
@ stdcall InterlockedFlushSList(ptr) ntdll.RtlInterlockedFlushSList
@ stdcall InterlockedPopEntrySList(ptr) ntdll.RtlInterlockedPopEntrySList
@ stdcall InterlockedPushEntrySList(ptr ptr) ntdll.RtlInterlockedPushEntrySList
@ stdcall InterlockedPushListSList(ptr ptr ptr long) ntdll.RtlInterlockedPushListSList
@ stdcall QueryDepthSList(ptr) ntdll.RtlQueryDepthSList