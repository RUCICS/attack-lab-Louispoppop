## p1

|     func      |          |
| :-----------: | :------: |
|    retaddr    |          |
|               |  rbp+8   |
|  old rbp ()   |          |
|               | <-- %rbp |
|   buffer[8]   |          |
|               |  rbp-8   |
|               |  rbp-16  |
| char* content |          |
|               |  rbp-24  |

## p3

|     func      |                          |
| :-----------: | :----------------------: |
|    retaddr    |                          |
|               |          rbp+8           |
|  old rbp ()   |                          |
|               | <-- %rbp= 0x7fffffffd600 |
|     0x72      |           1row           |
|      0x0      |          3rows           |
|  buffer[32]   |                          |
|               |          rbp-32          |
| char* content |                          |
|               |          rbp-40          |