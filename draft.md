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