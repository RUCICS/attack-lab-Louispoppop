## p1

|               |          |
| :-----------: | :------: |
|    retaddr    |          |
|               |  rbp+8   |
|  old rbp ()   | （func)  |
|               | <-- %rbp |
|   buffer[8]   |          |
|               |  rbp-8   |
|               |  rbp-16  |
| char* content |          |
|               |  rbp-24  |